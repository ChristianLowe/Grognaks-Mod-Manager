# This was very loosly based on...
#
# Get image info using pure Python code
#   http://markasread.net/post/17551554979/get-image-size-info-using-pure-python-code
#
# PyPNG 0.0.14
#   https://pypi.python.org/pypi/pypng


import struct
import sys


# The PNG signature.
#   http://www.w3.org/TR/PNG/#5PNG-file-signature
png_signature = struct.pack('8B', 137, 80, 78, 71, 13, 10, 26, 10)


def read_metadata(f):
    """Returns a dict of PNG image metadata from a file-like object."""

    if (f.read(8) != png_signature):
        raise ValueError("PNG file has an invalid signature.")

    (chunk_length, chunk_type) = struct.unpack("!I4s", f.read(8))
    chunk_type = chunk_type.decode("ascii")

    if (chunk_length > 2**31-1):
        raise ValueError("Chunk %s is too large: %d." % (chunk_type, chunk_length))

    if (chunk_type != "IHDR"):
        raise ValueError("PNG file didn't start with an IHDR chunk.")

    chunk_data = f.read(chunk_length)
    if (len(chunk_data) != chunk_length):
        raise Exception("PNG chunk %s too short for required %i octets."
            % (chunk_type, chunk_length))
    chunk_checksum = f.read(4)

    # http://www.w3.org/TR/PNG/#11IHDR
    (header_width, header_height, header_bitdepth, header_color_type,
     header_compression, header_filter,
     header_interlace) = struct.unpack("!2I5B", chunk_data)

    # Derived values
    #   http://www.w3.org/TR/PNG/#6Colour-values
    colormap =  bool(header_color_type & 1)
    greyscale = not (header_color_type & 2)
    alpha = bool(header_color_type & 4)
    color_planes = (3,1)[greyscale or colormap]
    planes = color_planes + alpha

    result = {}
    result["width"] = header_width
    result["height"] = header_height
    result["bitdepth"] = header_bitdepth
    result["color_type"] = header_color_type
    result["compression"] = header_compression
    result["filter"] = header_filter
    result["interlace"] = header_interlace

    result["colormap"] = colormap
    result["greyscale"] = greyscale
    result["alpha"] = alpha
    result["color_planes"] = color_planes
    result["planes"] = planes

    return result
