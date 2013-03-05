# -*- coding: ascii -*-
# ^ Ascii chars are the norm in Python 2.x source code.
# This'll make a 3.x interpreter panic when any unicode sneaks in.

from lib import moddb


def populate_catalog(mod_db):
    mod_info = moddb.ModInfo()
    mod_info.set_title( "Advanced Weapons and Shields" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11058" )
    mod_info.put_version( "1368ecb746bea1fab261d8a5eb8c23f1", "1.2" )
    mod_info.set_thread_hash( "dbb90b01a5931e59a6e2cf5e6b3054f6" )

    mod_info.set_desc(r"""Discontinued. See: "Advanced Battle Systems".

Get five shields and power your advanced weaponry! Thanks to a breakthrough by Engi scientists, ships are now able to have five shields and level twelve weapons. The Engi Advanced Technology Development Division has released this technology to the Federation, in hopes that they can beat the rebels. You can pick it up today, at your local Zoltan Trade Hub or on this post!

Known Bugs:
Asteroid Fields are messed up and you die... unknown cause, code seems to be fine.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Advanced Battle Systems" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11469" )
    mod_info.put_version( "4b88a7f3664f96d54de0fe83fd17f2ed", "1.2" )
    mod_info.put_version( "b45b9610ef83386da780a88c8e29d027", "1.1" )
    mod_info.set_thread_hash( "6bd30a167155e7650ae3fee2c8e84ce1" )

    mod_info.set_desc(r"""Features
- Max power of teleporter increased to 4.
  - Level 4 is instant cooldown, but costs 150 scrap.
- Max power of cloaking is increased to 8.
  - Level 8 is 40 seconds cloak.
- Max power of weapons increased to 12 (from Advanced Weapons and Shields).
  - Level 12 Weapons=12 weapon energy bars.
- Max power of shields increased to 10 (from Advanced Weapons and Shields).
  - That's 5 shield bars!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Disable Fleet" )
    mod_info.set_author( "aedyr" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2593" )
    mod_info.put_version( "26e599dff4f8c622a53948caba4d9100", "1.0" )
    mod_info.set_thread_hash( "2e6b44eb9c2d6db24fc9e683466720ae" )

    mod_info.set_desc(r"""This is a simple mod that disables fleet pursuit and adds a bit of flavor text at game start.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Faster Than Hard Light" )
    mod_info.set_author( "blaeron" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2939" )
    mod_info.put_version( "72e45464194aa306397aa1e8223b3cf6", "Demo WIP" )
    mod_info.set_thread_hash( "3d73f835ab5a206f97b88c8533c6e5bf" )

    mod_info.set_desc(r"""Faster Than Hard Light is a total conversion, aimed at bringing the FreeSpace 2 universe into the FTL engine.

I currently don't have much to show for Faster Than Hard Light (okay sorry), but I do have a few pretty pictures and a general outline.

Anyway, here's what FTHL will include if I ever release this:

Most smaller enemy ships become corvettes or frigates, with ships that approach the size of a playable ship being Destroyers. Playable ships also become different types of destroyers, with one exception, the Arpyia Frigate. Drones becomes a fighterbay. Also, Rockmen become Vasudans, Mantis become Shivans, sekkrit race becomes Ancients, and the Rebels also become the Shivans.

Oh yes, a demo, a demo! Not much, and most of the stuff is horribly unbalanced, broken, or not implemented (Only a single new ship, GTD Orion, and only a few weapons were added, and the new beams that pierce all shields are horribly unbalanced), but it is at least slightly functional. The Orion even has gibs and proper weapon placement!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Foundation of the Federation" )
    mod_info.set_author( "Whale Cancer" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2947" )
    mod_info.put_version( "???", "N/A WIP" )
    mod_info.set_thread_hash( "c0876479b4618f539815c6abd1240fd3" )

    mod_info.set_desc(r"""This mod is supposed to present the foundation of the federation, rather than its fall. The Engi and Zoltan are presented as allies while the Mantis, Rock, and Slugs as aggressors; the final battle is a unifying battle in which the Engi, Zoltan, and Humanity stand against the Rock, Slugs, and Mantis (I'm thinking of casting the slugs as the manipulators of this 'axis'). The old playable ships associated with those races are mini-bosses at the end of quest chains and, of course, they will be used in the final battle as well.

The plan is also to rewrite a whole bunch of events, as I intend the mod to be event focused.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Ghost Stories" )
    mod_info.set_author( "Morat48" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10793" )
    mod_info.put_version( "9887fca7eff56923ab3fb712e95066a0", "2013-01-19" )
    mod_info.set_thread_hash( "4352c6900ef78495489eb9ac75bf4a48" )

    mod_info.set_desc(r"""Part of the "Ghost Ships and New Items" collection.

This mod creates two ghost ships, crewed by ghosts and equipped with unique weapons. One of these ships is a variant of the starting Kestrel, and the other is an alternate version of Stealth A. Since ghosts do not require air, the ships lack oxygen systems. This mod also adds a few ghost-related events, as well as some blue text options for ghosts. The Federation cruiser type A exchanges its human crew member for a ghost, but retains its other normal crew and still has an oxygen system.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Remove O2 Warning" )
    mod_info.set_author( "Morat48" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10793" )
    mod_info.put_version( "7759c317d925f3a7e4cb300bace6a754", "2013-01-16" )
    mod_info.set_thread_hash( "4352c6900ef78495489eb9ac75bf4a48" )

    mod_info.set_desc(r"""Part of the "Ghost Ships and New Items" collection.

This mod removes the big flashing "low oxygen" warning, which can be annoying on a ghost ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Equipment EX" )
    mod_info.set_author( "Morat48" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10793" )
    mod_info.put_version( "3db44e4835e96a7147bab3717905a13f", "2013-01-19" )
    mod_info.set_thread_hash( "4352c6900ef78495489eb9ac75bf4a48" )

    mod_info.set_desc(r"""Part of the "Ghost Ships and New Items" collection.

This mod expands the selection of equipment, adding new drones and weapons, and allowing cloak and teleporter systems to be upgraded by one additional level. Rather than spoil the experience of discovering all the new items, I'll just say that the new equipment includes a variety of plasma weapons that deal damage and cause fires, a torpedo weapon that acts as a slow moving missile, and the deadly anti-bio terminator drone, among many others.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Sci-Fi Names" )
    mod_info.set_author( "Morat48" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10793" )
    mod_info.put_version( "8913e54d19ec7f218ac2d1e1c91e3959", "Clobber 2013-01-16" )
    mod_info.put_version( "fdae4fd6402b41226c6d429c0b48812f", "Append 2013-01-16" )
    mod_info.set_thread_hash( "4352c6900ef78495489eb9ac75bf4a48" )

    mod_info.set_desc(r"""Part of the "Ghost Ships and New Items" collection.

A list of names taken from a number of sci-fi sources, including Star Trek, Star Wars, Firefly, Red Dwarf and many others. The mod comes has two versions: One which will replace any existing names, and another to append to an existing list (allowing you to use these names along with the default list, or any other modded name list).
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Manual Ship Unlocker" )
    mod_info.set_author( "Morat48" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10793" )
    mod_info.put_version( "c6204da7af84a959d4c075e6c99393aa", "2013-01-16" )
    mod_info.set_thread_hash( "4352c6900ef78495489eb9ac75bf4a48" )

    mod_info.set_desc(r"""Part of the "Ghost Ships and New Items" collection.

This is a useful utility mod for those who want to unlock certain ships without going through the unlock quests. With this installed, click on the tutorial, and you'll be given an option to immediately unlock a ship. This works for A type ships, achievements will still be needed to unlock B types. The tutorial can still be used normally while the mod is installed.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Halo" )
    mod_info.set_author( "Lord0fHam" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=11475" )
    mod_info.put_version( "1e381090dec2bca663a709d770eb0940", "1.0.1 WIP" )
    mod_info.set_thread_hash( "7c43fe82d068dd7085dc9a22ed76d8fd" )

    mod_info.set_desc(r"""I have decided to make a total conversion of the game to make it Halo themed. I'm going to add new weapons, ships, sectors, events, etc. I have some ideas, but I need more. I am going to make all new sectors after all so I need many new events. If there are any Halo fans (or not) out there that would like to suggest any new events, weapons, etc. or help out with art for new things, please post below. I hope to make this mod a total conversion, ending with the replacement of the final boss with some super powerful Covenant Cruiser to stop Truth from firing the Halos.

This mod is not compatible with other mods that change the Kestrel A Layout! In the future there may be other mods it won't be compatible with.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Incursion" )
    mod_info.set_author( "Kieve" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10361" )
    mod_info.put_version( "fd357ea6465756e45e393feffb986f5f", "0.9c Beta WIP" )
    mod_info.set_thread_hash( "3acaa80e3d2cecae869436ed0835a35f" )

    mod_info.set_desc(r"""DISCLAIMER - This mod is still in "beta" status and requires testing. Some weapons may feel imbalanced or overpowered, others underpowered or useless. Please leave detailed, constructive feedback.

Replaces the Zoltan-B ship.

Features
- Arc Beam - Antipersonnel particle beam. Damages systems and crew, starts fires.
- Aurora Mass Cannon - Anti-ship cannon that pierces all shielding.
- Bolide Ion Rocket - Deals no hull damage, but very effective at disabling shields and systems.
- Sunfury Rotary Autocanon - Rapid-fire burst weapon. Fast reload but will suck your ammo dry.
- Crew: 2 Zoltan

Also includes the Incursor Theme, replacing the default title music.

The Incursor "Archon" was designed to strike fast and hard, weakening the enemy for their larger capital ships. The Archon's weapon array is devastating indeed, but heavy reliance on limited ammunition makes it a poor choice for extended mission assignments.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Infinite Space" )
    mod_info.set_author( "DrkTemplar" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=3542" )
    mod_info.put_version( "5bad4d1ec8fcc188142ce2861f8650bb", "0.4.4 Hi-res Bkgs" )
    mod_info.put_version( "de440631df2c0b8274a0f37ccff79206", "0.4.4 Original Bkgs" )
    mod_info.put_version( "9de0823d7d8b33cf27ac2807e085cd45", "0.4.3" )
    mod_info.put_version( "516e20d80b9c6c878b0730c3e7978576", "0.4.1" )
    mod_info.set_thread_hash( "b8fb37954083fce4a872708eeb168238" )

    mod_info.set_desc(r"""What is FTL Infinite Space?
The universe is vast. With FTL Infinite Space you can explore the universe to your hearts content, or till you blow your ship to bits. Infinite Space will jump you from sector to sector, while you search for ancient powerful artifacts, and advanced technology to enhance your ships capabilities. Learn when to fight, and when to run. Dominate or be destroyed.

Features
- No Rebel Fleet, No Rebel Boss, No hard stop end of game.
- Redesign of Sectors, and Enemy ships.
- Sector "mini bosses" (Player Cruisers images).
- New custom weapons.
- New custom drones.
- New events
- A different gaming experience than vanilla.
- High-res background graphics mod by Splette!
- DronesPlus mod by karmos!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Mass Effect Total Coversion" )
    mod_info.set_author( "Captain_Brian" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=8936" )
    mod_info.put_version( "278414a9d1385dc2ec2676590afb3da3", "0.013" )
    mod_info.set_thread_hash( "e1ff5a7d2b0b51b7414d302792aea4b0" )

    mod_info.set_desc(r"""Backstory:
Cerberus has found a way to control the reapers. The reaper war has been raging on since the failure of the Crucible Project, and the whereabouts of the Normandy and its crew are unknown.

Data mined from the Cerberus network suggests a tachyon pulse emanating from The Illusive Man's command ship has "erased" the reaper collective consciousness, and replaced it with a rudimentary command recognition structure that Cerberus can send commands to. The data also suggests that the Illusive Man's command ship is the only ship capable of sending commands to reaper forces, and that eliminating it will permanently disable the reapers.

Unfortunately, Cerberus have completely disabled galactic communications, which leaves it up to you to deliver this data to Alliance Command. Reaper forces are preoccupied with decimating planetary infrastructure, but the Cerberus fleet has only one target...

YOU.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Pirates!" )
    mod_info.set_author( "RichText" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=3273" )
    mod_info.put_version( "1d34784e28007aa92cbb05086d0d583e", "2.2" )
    mod_info.put_version( "fb6f3e5c282906bdd79b2b294777cf1c", "2.1" )
    mod_info.put_version( "1de167d54d84556341ffcbc572e0a2d3", "2.0" )
    mod_info.put_version( "561460bacb6e83677334b6bb957f5344", "1.0" )
    mod_info.set_thread_hash( "fdbdaf6589ca2af263fb6641760b042a" )

    mod_info.set_desc(r"""Avast, thar be a pirate mod now!

"Pirates!" has rewritten events, changing the reactions and choices you can make, as well as altering the storylines. Pirate chasing civilian? You can aid the civilian OR the pirate. Caveman stuck on a moon? Sure, you can risk letting him join your crew... or you could throw him in the composter and turn him into fuel. Use your pirate charm to talk your way out of tricky situations or barter for more plunder, and flash the jolly roger to turn other pirates to your alliegance!

The overall plotline of the game is being changed as well. Already, the universe has shifted back in time to pre-rebellion times, when the Federation Military Police patrolled the spaceways, hunting pirates such as you. As a notorious pirate, you will have them at your tail at all times as you try to escape to the planet of Deadman's Port, the legendary pirate haven on the other side of the galaxy. And there is another story you've heard... of a wondrous place called... "Treasure Planet."

On the aesthetic side, the rebel fleet has been replaced with the Federation military, dark green ships that seek to destroy or arrest you. You pilot a "liberated" model of one of these Federation ships, the "The Black Spot." The mod also rewrites all tooltips into "Pirate-Speak," a much more suitable dialect of English for those of you who are swashbuckling corsairs. All NPC crew-members will now have pirate names, including favorites such "Peg-leg" and "Patchy." In addition, the first of many new weapons has been added, the Cast-Iron Ship's Cannon, masterfully nailed to the side of your ship with wooden planks, and accompanied by a hearty quantity of lead cannonballs for you to launch through the depths of space.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Somewhat Faster Than Light" )
    mod_info.set_author( "blaeron" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2603" )
    mod_info.put_version( "e7558768ce75524079d9e58d521f54dd", "1.1" )
    mod_info.set_thread_hash( "10ffac10ee66440ecc8e1fcea6dd4c1a" )

    mod_info.set_desc(r"""Includes:
- Burst Laser Mark IID
- New Pegasus and Aristea missile sprites
- Voulge beam
- Plasma Beam
- Beam Drone Mark II
- Improved drone speeds and fire rates
- Added Elite Rigger
- Changed the playable Rockman ships somewhat
- New nebula and background sprites, and new warnings.
- New solar flare and ion storm sounds.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Sonata Total Conversion" )
    mod_info.set_author( "thashepherd" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=6517" )
    mod_info.put_version( "b13de0c782576c9c20f0ef6d0fe317c5", "7" )
    mod_info.set_thread_hash( "3e0d8f09ba612d167e80368e4bd79e3d" )

    mod_info.set_desc(r"""With cries of "Sic Semper Tyrannis", nearly a quarter of the United Empire's worlds have seceded to form their own nation. They call themselves the "Pilgrims". The Empire's legislature interpreted this secession as treason, and the overwhelming might of the loyalist fleet has fallen on the Pilgrims. Although the situation is militarily hopeless, your family and friends have all joined the resistance - and so you shall.

Sonata is a total conversion mod for FTL based on the storyline of Endless Space by Amplitude Studios, with modifications. It aims to create a gritty, realishtic, and morally ambiguous story on the FTL engine where politics, motivations, and the nature of humanity itself affect your journey.

Features
- All-new soundtrack
- All-new backgrounds
- All-new story and events
- All-new UI
- Custom player ships
- Custom enemies
- All-new weapons
- Custom weapon graphics, and animations
- New sound effects
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Turning The Tide" )
    mod_info.set_author( "Kieve" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=3056" )
    mod_info.put_version( "a5a73f329fb153dc445eca672b51114b", "1.0" )
    mod_info.set_thread_hash( "08f7767e979f2228c474deb2fdcdde24" )

    mod_info.set_desc(r"""This mod alters your encounters with the Rebel Fleet to increase the risk / reward factor, giving you the option to bring their advance in a sector to a screeching halt - or die horribly in the face of overwhelming odds!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Warhammer 40k - Battlefleet Gothic Mod" )
    mod_info.set_author( "DauntlessK" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=11604" )
    mod_info.put_version( "???", "N/A WIP" )
    mod_info.set_thread_hash( "45d4c8a847a945382311da3105cd07d3" )

    mod_info.set_desc(r"""This mod is meant to give you the feeling that you're a captain in the dark and twisted universe that is Warhammer 40,000. It is starting off as a ship, weapon mod, but will continue to grow into something even bigger.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Amber Shard" )
    mod_info.set_author( "DryEagle" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11703" )
    mod_info.put_version( "8a5a336510ac21b1e5b24e0657287b5d", "1.0" )
    mod_info.set_thread_hash( "c4de807ba790239c6d44f9de89bc700b" )

    mod_info.set_desc(r"""Features
- Custom graphics for pretty much everything
- Customised ship hull
- Customised crew sprites, shield graphic, room interiors
- Gibs with proper layering etc
- Unique weapons
- Heavy, heavy focus on killing ship crews. Lots of boarding drones, weapons that lock down rooms and cause breaches to suffocate the crew without causing direct damage...
- No oxygen system. Specially adapted version of the nanobot augment which heals crew at exactly the rate that they would take suffocation. Only works on crytals, others will still die unless stuck in the medbay.
- Custom pricing (and in some cases levels) for almost all ship upgrades.
- Included tutorial pointing out some important details about no-oxygen system.

Note: There are no low-oxygen stripes (the floor will still turn pink however). Because this ship has no O2 system, I chose to remove them for visual pleasantness. Bear this in mind when attacking enemy ships.

Replaces the Kestrel-A ship.

I am not including any custom events, so that this remains compatible with as many mods as possible.

- All modified files are renamed to be specific to this ship, except for crystal crew sprites and lockdown effect, and oxygen stuff. Basically, load it last and it will be compatible with anything.
- If you wish just rename the relevant line in blueprints file to have it replace another ship instead.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Battlefleet Gothic: Cobra Class Destroyer" )
    mod_info.set_author( "Harnisfechten" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=10431" )
    mod_info.put_version( "3d50785d23090ecb0aa0ede535b0c24b", "1.0 WIP" )
    mod_info.set_thread_hash( "6264da50ab73f21b95e04a874255df1b" )

    mod_info.set_desc(r"""The Cobra Class Destroyer is a ship from the Warhammer 40k Universe. It is known as the smallest independent Imperial ship (ie it can patrol alone, and is not a fighter or bomber based on another ship).

Due to difficulty in finding an overhead image of the ship of suitable quality, I decided to try something different and make the ship from a side view. Sure, the crew and rooms are all top view, but I actually think it looks pretty good.

The Cobra is armed with a dorsal weapons battery (a Burst Laser Mk II in the game) and prow-mounted torpedoes (2 Hull Missiles in the game). Note that the crew are not to-scale with the ship, as the ship is approximately 1.5km long (yeah, 40k ships are big). I like to think that instead of individual characters, each crew member represents a team of people, so the pilot is not just one pilot, it is the entire command staff on the bridge of the ship, and the weapons guy is not one guy, it is a large number of gun crew, the ratings that load the weapons, the engineers that serve them, etc.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Battlestars" )
    mod_info.set_author( "FrostWyrmWraith" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11940" )
    mod_info.put_version( "4b2d7e5f6d80b475a9b4e9d0d740ff41", "1.0" )
    mod_info.set_thread_hash( "49de32110c905eb33e5ef07f888afbfd" )

    mod_info.set_desc(r"""Here we have a pair of ships in one file-the Galactica and the Pegasus.

The Galactica begins with a missile launcher and two Vipers as a homage to what it fought like in the series.

With the Pegasus I didn't want to make the ship too overpowered so I gave it two KEW batteries and a single Viper, though starting it with more and giving it more drone slots would have been more accurate. I wanted it to play a bit differently, so it focuses more on weapons than fighters. In the game you can find the Viper Mk VII, as well, so keep your eyes peeled!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Blazing Cruiser" )
    mod_info.set_author( "Zaffre" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=3133" )
    mod_info.put_version( "141f70d3643d275504c04993fdaab110", "1.1" )
    mod_info.put_version( "af34777f9b70769828ea27f24b5b298a", "1.4" )
    mod_info.put_version( "eb5484304b45b3be8ff043aa78c0defc", "1.5" )
    mod_info.put_version( "c522d5da78aebbd55a6f68cc6e98162d", "1.3" )
    mod_info.put_version( "a23e32a6591af658e4ce9ab92403c4aa", "1.0" )
    mod_info.put_version( "17b671da29f071521e8e54f77cb6c325", "1.2" )
    mod_info.set_thread_hash( "0872231554efba1a11bec2271f17d0d1" )

    mod_info.set_desc(r"""This cruiser uses fire weaponry. It starts with two extended fire beams, one laser weapon that starts fires, and a missile that starts fires. It starts with no shields or cloaking. To give the ship a chance, it has a unique drone upon start. The crew is composed of three Rock. The sprites are modified versions of the Kestrel B layout.

Replaces the Kestrel-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Buffalo" )
    mod_info.set_author( "EchoesofOld" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11327" )
    mod_info.put_version( "642c121e47964c6e825c4b89da7a7e7e", "1.1" )
    mod_info.set_thread_hash( "d8ecd11fad226a01436e233f08ba822f" )

    mod_info.set_desc(r"""This ship is an unarmed vessel that relies on its cloak to survive.

Replaces the Engi-A ship.

Please Note:
I have discovered that you can NOT load my ships simultaneously. I dont know WHAT causes this, but im looking into it.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "C-1092" )
    mod_info.set_author( "MeGusta" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11434" )
    mod_info.put_version( "848d44e196b16fec980862432d82fa1f", "1.1 No Human" )
    mod_info.set_thread_hash( "04ef703bdcb3dcf80859040a2928e490" )

    mod_info.set_desc(r"""This is the C-1092. It is made for teleportation combat. You get in, then out as quick as possible. I made this because I could not find any ships of this type. It looks the same as the Type B stealth fighter.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Duality Cruiser & Merchant Cruiser" )
    mod_info.set_author( "zaratustra" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2729" )
    mod_info.put_version( "4d68f90233698b7db9c792ae3573e2fe", "1.0" )
    mod_info.set_thread_hash( "158f664b69f336be816be618902437ba" )

    mod_info.set_desc(r"""The Duality is divided into two sections.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Escort Duty" )
    mod_info.set_author( "DryEagle" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11531" )
    mod_info.put_version( "bed7f8c867bb728ce852f4fcccf923e8", "1.0" )
    mod_info.set_thread_hash( "0493e82769c2067b4a8e0704c986aec8" )

    mod_info.set_desc(r"""The story:
You have been comissioned to help escort some freighters which carry intel and technology vital to the federation. Unfortunately weaponry is in short supply so you had to salvage what you could:
- A prototype ion pulse weapon
- A defective burst laser (no secondary effects e.g. no fires, no crew damage)
- An unstable nanite repair bomb (may overload systems it repairs, starting a fire. 10% chance)
Fortunately you were given a top-of-the-line point defence drone to help protect the unshielded freighters.
The freighters also have ample space to install cloaking and a large industrial-sized teleporter, should you manage to come across vendors willing to provide the hardware necessary for the upgrade.

A shielded frigate escorting unshielded freighters.
The odds are stacked against you.
Will you survive and defeat the rebel fleet?

Replaces the Kestrel-A ship.

Mod data:
- The replaced ship can be changed in blueprints append. There are no dependencies.
- Sll names in internal files are unique to this mod so it should be entirely compatible with everything.
- No events, this is just a ship. so you can use it with more or less everything, just load it last.
- Gibs, cloaking graphics, menu graphics - the works.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "F-22A Raptor" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11537" )
    mod_info.put_version( "7981bcf4ae27eeb3551ea46adedfe779", "1.2" )
    mod_info.set_thread_hash( "d5fd366a25b7a9a7e8fb22f480406336" )

    mod_info.set_desc(r"""Lockheed-Martin/Boeing F-22A Raptor for FTL
Part of a "Present-Time" Total Conversion that MAY be coming soon! (I'm working on an F-35)

Intro:
The Lockheed Martin/Boeing F-22 Raptor is a single-seat, twin-engine fifth-generation supermaneuverable fighter aircraft that uses stealth technology. It was designed primarily as an air superiority fighter, but has additional capabilities that include ground attack, electronic warfare, and signals intelligence roles.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Halo 4 : Broadsword ship" )
    mod_info.set_author( "Revenant721" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11620" )
    mod_info.put_version( "3f17e969074ad365d4d3e850d51fdca1", "1.1" )
    mod_info.set_thread_hash( "c4ed37f4842eb68bb5e7599a54cacdef" )

    mod_info.set_desc(r"""Greetings FTL and Halo fans!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Halo: CCS-Class Battlecruiser" )
    mod_info.set_author( "FrostWyrmWraith" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11938" )
    mod_info.put_version( "21fc1a22707e4b30e806b1a2e9f66674", "1.0" )
    mod_info.set_thread_hash( "a925d0ba5d43b6d90def7bfe732da653" )

    mod_info.set_desc(r"""The Covenant battlecruiser featured heavily in the Halo series! It starts with a slug and two engi. It also adds the plasma torpedo to the game. It requires two power and has a fairly long charge up, but does two damage and is pretty much guaranteed to cause fires.

Replaces the Slug-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Kingfisher" )
    mod_info.set_author( "BadgersCanSpace" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=11522" )
    mod_info.put_version( "b6e4d637e2cf1ce18b8d29e07038f37c", "1.1" )
    mod_info.set_thread_hash( "b95b288bec588ef8fd84d4c036e2d236" )

    mod_info.set_desc(r""""By modern standards, the Federation Spaceworks Kingfisher-class Field Hospital and Medical Supply Vessel is outdated. Older even than the venerable Kestrel-class, they fell into an uncomfortable balance of being too poorly equipped for military use, but overpowered and overpriced for the civilian market. Their shields are weak by modern standards and their lack of armament prevented any private usage other than freight haul. However, due to their relatively easy modification and powerful engines, they remain a firm favourite with playboys and pirates." - Jane's Military Spacecraft Edition XXVIII

Replaces the Engi-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Klingon Bird-of-Prey" )
    mod_info.set_author( "Wiseworm" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11086" )
    mod_info.put_version( "ee02457c0d7f3dc1217d8fb217ada74a", "2.0" )
    mod_info.set_thread_hash( "46a9a5f464e67eb9f63b7497692f0e30" )

    mod_info.set_desc(r"""It's a Klingon K'vort-class Bird-of-Prey (replacing Mantis cruiser B) named PIvlob Do (klingonese for Warp Factor Speed).

After a little busy time I got my hand again on this to present you a new ship!
The Vor'cha-Class Klingon Battle Cruiser "IKS QeylIS BetleH" (klingonese: The Sword of Kahless).
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Lost Hunter" )
    mod_info.set_author( "TheDarkdu42" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10873" )
    mod_info.put_version( "7308cdebfc8b62ec1d80d5e8e0d837cc", "1.0" )
    mod_info.set_thread_hash( "28dabe5edb77f69b92802c893dc05d75" )

    mod_info.set_desc(r"""So, The Lost Hunter is a ship in the original game but it is improved and overpowered now!
You can destroy the rebel ships Faster than Light!

It has got 99 hull points, unlimited energy, all systems upgraded to the max.

Replaces the Stealth-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Marauders" )
    mod_info.set_author( "UltraMantis" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11501" )
    mod_info.put_version( "ef5cdc4b6413f4013959271155ef84be", "1.0 2013-03-04" )
    mod_info.put_version( "3851b27cd288083356b433436eda6195", "1.0" )
    mod_info.set_thread_hash( "6d71975f90004484da6788e1f5c3acb5" )

    mod_info.set_desc(r"""Marauder ships are characterised by powerful weapon systems that seem to require massive power to operate, even at the expense of all other systems. While not refined, the weapons are effective. Usually disableing and stripping ships clean to provide resources required for the vessel to reach it's full potential. Even though their origins and source of technology are a mystery, the ships are crewed by common races though it's hard to say if they joined up willingly or are slaves.

Fair warning to those eager to play, these ships will not be easy. My guess is that difficulty will be between NORMAL and EXTREME, depending on which ship you pick.

This mod was made without regard for compatibility with other mods. However, it will work with visual, events, and weapon mods, but will almost certainly break system mods. Whether or not it works with other ship mods is unpredictable. I recommend that you install this as a single mod.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Mor-Saxum (Rock Cruiser)" )
    mod_info.set_author( "HalfDemon23" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11514" )
    mod_info.put_version( "e50d7504123fab5224248c8704a5bc12", "0.6" )
    mod_info.set_thread_hash( "09e54784dbf67a2d92a395f28570e039" )

    mod_info.set_desc(r"""A gigantic Rock Dreadnought that was intended to blockade the entire Rebel Fleet; however the Rebels attacked the construction base before it was completed, resulting in the Prototype limping out of the attack. While it lacks secondary systems, the Mor-Saxum has an impressive armament and unrivalled hull strength, now TRIPLE of a standard Rock Cruiser - if its systems were brought up to full strength... not even a Rebel Fleet could stand in its way.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The NightHawk" )
    mod_info.set_author( "EchoesofOld" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11330" )
    mod_info.put_version( "6bf83f50fcdf3b13d366ad745745f911", "1.0" )
    mod_info.set_thread_hash( "d011f5f173faa113fadeb8aed0ce1a11" )

    mod_info.set_desc(r"""The NightHawk is a cheap suicide fighter, meant for quick hit and run fights. It normally operates in packs, but you dont really have that option, do you?

I designed this ship with the intention of being a total jerk (Much like Vechs and his Minecraft Super Hostile maps.) If you people like it enough, I'll re-balance it to be more fair.

Replaces the Slug-A ship.

PLEASE NOTE: I have discovered that you can NOT load my ships simultaneously. I dont know WHAT causes this, but im looking into it.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Obsidian Cruiser" )
    mod_info.set_author( "Kieve" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2574" )
    mod_info.put_version( "e1bcbe57235fc41546ac1470f9bd7b29", "1.2.2" )
    mod_info.set_thread_hash( "f81da5b68fc54068c4701958610f8d87" )

    mod_info.set_desc(r"""'Weapon Systems: Offline. Drone Control: Offline. Engines: Offline. Shields: twenty-five percent power. Hull breaches detected in Medical and Oxygen rooms. Fires detected in...'

The lidless green eye of a lone Engi winked out, the mechanized equivalent of a wince. The Vortex was dying around him, clouds of debris surrounding the hull where the Rebel fighter's missiles had blasted it. Streams of precious oxygen vented into empty space, giving the ship a slight spin that the damaged engines could no longer compensate for. And without its precious repair drones active, The Vortex had no hope of recovering. One Engi was no match for the destruction surrounding him. Hot air escaped his vents in something very much like a sigh, his overtaxed processors reaching one last viable option: a gray finger stabbed down, activating the ship's distress beacon. Code willing, there'd be a Federation ship out there that could at least deliver some small measure of retribution for the loss of The Vortex...

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Playable rebel flagship" )
    mod_info.set_author( "Baldwebby360" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=10108" )
    mod_info.put_version( "9643c9a6af40bfd7710157dd49f00390", "1.0 Rebel WIP" )
    mod_info.put_version( "0a7890230e067e260d1e617a5e92871b", "1.0 Fed WIP" )
    mod_info.set_thread_hash( "a299a691648b3e787cf7b700a669a263" )

    mod_info.set_desc(r"""A playable rebel flagship.

Replaces the Slug-A and Slug-B ships.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Predator" )
    mod_info.set_author( "Dark Spartan" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11474" )
    mod_info.put_version( "cd9ed7b2a4e04cbeb3d06e7031009766", "1.1 WIP" )
    mod_info.set_thread_hash( "7a57ff0cadd8591af860ee703446e72b" )

    mod_info.set_desc(r"""The Predator is a heavily-armed cruiser that relies on its ability to swiftly damage and destroy systems to make up for its lack of defenses. Its only defensive measures from the start are a rank 2 cloaking device and a few drones. Shields, door control, and teleporters must be purchased. However, with any cunning, you should be able to kill them before they kill you.

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Rebel Flagship Prototype" )
    mod_info.set_author( "Ginger Dragon" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10845" )
    mod_info.put_version( "3a8365874d541aa0412d6afd7b7d78e5", "1.2 BBF" )
    mod_info.put_version( "2a11e8c23fb9845b570fddabbd3c8a3a", "1.3" )
    mod_info.put_version( "b689a69cca46ab99c9af83a9dbe2c63c", "1.0" )
    mod_info.put_version( "bada632225d8a11fdde87c279681b176", "1.2" )
    mod_info.set_thread_hash( "08d2783a425129268a1af3260ba2e2bc" )

    mod_info.set_desc(r"""A prototype of the Rebel Flagship discovered by Federation scouts that was scrapped and spaced by the Rebels due to its key weakness. Its high-power weaponry makes it more unstable than most ships.

Replaces the Kestrel-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Robotic Cruiser" )
    mod_info.set_author( "Jonfon" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10839" )
    mod_info.put_version( "b44022f5918cab6b8674ccc87e13a6d3", "0.4 WIP" )
    mod_info.set_thread_hash( "6aff1d0ea1fe8860fb43e6a17400c07f" )

    mod_info.set_desc(r"""The Nexus Robotic Salvage Cruiser
An Engi ship designed to work without a crew. It is a originally a repair, refitting and salvage vessel which has been sent on a desperate mission by its creators.

Replaces the Engi-B ship.

Slug Bomber
Uses an array of new bombs and a small Disruptor.

Replaces the Slug-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Scarab" )
    mod_info.set_author( "DryEagle" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10942" )
    mod_info.put_version( "ca9d59bb3f605f31949f0e9b631bd8e0", "1.0" )
    mod_info.set_thread_hash( "5117eff894eea92772bf0d6827db91fb" )

    mod_info.set_desc(r"""A prototype diplomatic vessel, the Scarab was not designed with heavy fighting in mind - however it is more dangerous than it first appears.

Replaces the Kestrel-A ship.

All files/graphics which have been edited use custom names specific to this mod; to make it replace a different ship besides the kestrel, simply change one line in the blueprints append file and everything will still work.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "StarBug - Red Dwarf" )
    mod_info.set_author( "Heathen" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11448" )
    mod_info.put_version( "3f040bafc307237180f79e4dfdf290c7", "1.0" )
    mod_info.set_thread_hash( "8c8186bf576a8a95d9b56eaa84a29ea0" )

    mod_info.set_desc(r"""StarBug is is one of the old class-2 ship-to-surface vessels - the very model, in fact, that was withdrawn due to major flight design flaws.

Replaces the Stealth-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Starcraft Conversion" )
    mod_info.set_author( "alextfish" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=5238" )
    mod_info.put_version( "43dd7ced0e1f930604b5bce5e917fa9b", "0.5 UI" )
    mod_info.put_version( "958fba168d38361cce4f9ad280e83e99", "0.5 Ships" )
    mod_info.set_thread_hash( "0f04d41207487b4870ca57bd4c6c3484" )

    mod_info.set_desc(r"""The primary feature of this mod is: 18 new ships to play! All your favourite air units from Starcraft 1 and 2, ported into FTL!

The Ship mod and the UI mod are designed to be used together, but if you find the Starcrafty icons confusing you could just use the SC2Ships with the default icons.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Star Trek Universe" )
    mod_info.set_author( "speedoflight" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11844" )
    mod_info.put_version( "cddbb53e53745b8b1ac7cac7073e14e0", "0.2 2013-03-02 WIP" )
    mod_info.put_version( "c6880fd3e9423affe5ff9dc733580cad", "0.2 Beta WIP" )
    mod_info.put_version( "098dc2eb3865b701697e6a73420f57c6", "0.1 Beta WIP" )
    mod_info.set_thread_hash( "4344e1d170bd33dbc01daf7de467cf3c" )

    mod_info.set_desc(r"""For now, this is in alpha state.

The Defiant is a ship designed for assault purposes, there is no space for exploration equipment, colonial investigation or whatever. Its main purpose is to provide high reactor power to feed the weapons and the engines. Like the tv show, the Defiant has a cloaking system, installed by the romulans when they needed to defeat the Dominion. The Hull is reduced to 26 points to compensate a bit.

Replaces the Kestrel-A ship.

Various new weapons are added, too.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "turbonutter's Custom Ships" )
    mod_info.set_author( "turbonutter" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=3520" )
    mod_info.put_version( "569b13f51f63e2fdce5da9749a79fa46", "0.6 Beta" )
    mod_info.set_thread_hash( "4d5b7a80c3721ffd597ee0eef050424b" )

    mod_info.set_desc(r"""Replaces all the standard versions of the ships, the only loadout changed is the millenium falcon.

Ship Replacements
- Starbug = Fed A
- Fed Shuttle = Zoltan A
- Star Destroyer = Stealth A
- Romulan = Rock A
- Millennium Falcon = Kestrel A
- Death Star = Slug A
- Klingon D7 = Engi A
- Klingon BOP = Mantis A
- Big Fed ship = Crystal A
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Viper" )
    mod_info.set_author( "DryEagle" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10439" )
    mod_info.put_version( "502bbffee3198fc03178bdf9bff85050", "1.0" )
    mod_info.set_thread_hash( "3153bdfc380e6c9741138c94270c7b8d" )

    mod_info.set_desc(r"""The Viper is an assault-class cruiser. Strong offensive potential and level 2 shields right off the bat, at the cost of weak secondary systems.

Replaces the Kestrel-A ship.
You can just change which ship it overwrites in the blueprints file - all of the files the ship requires have unique names so it will work in any slot.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "USS Defiant" )
    mod_info.set_author( "y0sho" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=11022" )
    mod_info.put_version( "164b884b9565eab150b0ef5a843f87c8", "0.63" )
    mod_info.set_thread_hash( "6c54f0326a65451643374f9f9993cbbd" )

    mod_info.set_desc(r"""The layout is to as close to the actual ship as I could get it.

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "THE YAS-62" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11124" )
    mod_info.put_version( "ebefad606e6a66dd9e3ec4f9908e5d60", "1.1" )
    mod_info.set_thread_hash( "601e5da614262d4db26e034639055af6" )

    mod_info.set_desc(r"""The Federation had a whole bunch of these Kestrel Cruisers lying around, so they decided to make use of them. This new mod comes with a different room arrangement, new augmentations, and new ship graphics.

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "YTR-1335 Burnout" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11321" )
    mod_info.put_version( "4616d96003fda87b39d1541873fb111d", "1.1" )
    mod_info.set_thread_hash( "33cd8b79bb658db22bcc97805cf006b7" )

    mod_info.set_desc(r"""Developed by NATAR Weapons Development Division for the sole purpose of burning out enemy crews.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "DronesPlus" )
    mod_info.set_author( "karmos" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10813" )
    mod_info.put_version( "20c0a6edfcd157d28c45f6edc41f6715", "0.7.7" )
    mod_info.set_thread_hash( "1d3f9f461d2d2eac83cef9801b6637fc" )

    mod_info.set_desc(r"""DronesPlus adds new drones to FTL.

Beam II
Deals one damage per room like the Beam I drone with 25% longer beam and a higher firing rate. 4 Power.

Ion I
Shoots ion blasts. 2 Power.

Ion II
Shoots ion blasts faster. 4 Power.

Missile I
Shoots missiles. Pretty slow. 2 Power.

Missile II
Shoots missiles. Less slow. 4 Power.

Fire
A drone equipped with a beam that causes fires. 2 Power.

Crystal
Shoots shield-piercing crystal shards. Only obtainable in the Crystal Sector. 3 Power.

The mod may (i.e. will probably) conflict with other mods that add drones. It is likely that we modders have used the same blueprint and weapon names at least once.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Law's Arsenal - Ion Beam" )
    mod_info.set_author( "Law" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2297" )
    mod_info.put_version( "358fb657d823b1ffdb99ba46acaf4927", "0.3" )
    mod_info.set_thread_hash( "0742a7685928621da16ab70f016d29d1" )

    mod_info.set_desc(r"""Part of the "Law's Arsenal" collection.

This beam hooks into the Federation Cruiser's artillery system, which instead of firing a piercing regular beam, causes ion damage instead. It's very good for disabling systems temporarily, though it is seen to be moderately overpowered.

A note about these weapons:
Any mods that replace the artillery system won't work together, so when you're selecting the mods to use, select only ONE of the mods. Any breakage of the game, I hold no responsibility if you haven't installed the mod correctly.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Law's Arsenal - Splint Bombs" )
    mod_info.set_author( "Law" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2297" )
    mod_info.put_version( "967e1365dfda1446ed5520629ce6517f", "0.1" )
    mod_info.set_thread_hash( "0742a7685928621da16ab70f016d29d1" )

    mod_info.set_desc(r"""Part of the "Law's Arsenal" collection.

This mod teleports 5 bombs into the enemy ship where possible, and causes hull breaches when successful. Like the Ion Beam, this replaces the default artillery that comes with the Federation Cruiser.

A note about these weapons:
Any mods that replace the artillery system won't work together, so when you're selecting the mods to use, select only ONE of the mods. Any breakage of the game, I hold no responsibility if you haven't installed the mod correctly.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Law's Arsenal - Rapid Missiles" )
    mod_info.set_author( "Law" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2297" )
    mod_info.put_version( "43ba9c8cca009994fe059283242387b5", "0.1" )
    mod_info.put_version( "8de20e49020d05b22685b05de40cbcb8", "0.5" )
    mod_info.set_thread_hash( "0742a7685928621da16ab70f016d29d1" )

    mod_info.set_desc(r"""Part of the "Law's Arsenal" collection.

This is a standard weapon mod (so it's very much compatible with the Ion Beam and the Splint Bombs), which simply increases the firing rate of missiles. Does 2 damage per shot, pierces shields, has a 4 second charge time, but requires 4 energy to operate and yes, your missile supply will drop quite quickly.

Version 0.1 replaced the Kestrel A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Law's Arsenal - Athena Missile Launcher" )
    mod_info.set_author( "Law" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2297" )
    mod_info.put_version( "1bb19a2bbbb71416d2f495cec085f904", "0.1" )
    mod_info.set_thread_hash( "0742a7685928621da16ab70f016d29d1" )

    mod_info.set_desc(r"""Part of the "Law's Arsenal" collection.

The Athena is a missile launcher that doesn't use missiles. Instead, it is built over time, fueled by your reactor. There's nothing too special about this weapon (though the same could be said for a lot of the weapons here), but if you ever find yourself out of missiles and needing to get past a shield, this is a good choice.

Replaces the Kestrel-A ship.
Using Rapid Missiles in conjunction? Check your mod order.

A note about these weapons:
Any mods that replace the artillery system won't work together, so when you're selecting the mods to use, select only ONE of the mods. Any breakage of the game, I hold no responsibility if you haven't installed the mod correctly.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Overclocked Weapons" )
    mod_info.set_author( "HausHFG" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11468" )
    mod_info.put_version( "445f00599032a0d6be4551df06204300", "0.5 WIP" )
    mod_info.set_thread_hash( "ddba41960966ec48c84a5ecea4123ea9" )

    mod_info.set_desc(r"""So, I just wanted to make overclocked weapons to add more variety to the game, so far, it seems to have worked. As on February 9th 2013, there are 4 new weapons, based off their original counterparts, after all, overclocking makes the weapon more powerful, not a different model.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Weaponanza" )
    mod_info.set_author( "buzzyrecky" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2691" )
    mod_info.put_version( "d94a4fd0a94c4299999ae365d8acb4c5", "1.1" )
    mod_info.put_version( "c680700f88e314235d0efb3e204d794a", "1.0" )
    mod_info.set_thread_hash( "32c8c068af95b9284dd9ee3600750d9c" )

    mod_info.set_desc(r"""This is Weaponanza, a mod focused on bring you unique weapons without losing the FTL feel of the game. As of Sept 20th, there are 16 weapons added, and I plan on continually adding more as time goes on.

Note: Panacea is bugged, and there really isn't a way to fix it with the current way modding works. If you're going to use it for it's healing properties, avoid using it on rooms with systems in them, and you should be good.

Features
- NEW weapons (and counting) with custom textures
- Improved weapons (do not replace originals)
- Plenty of new events (for the weapons, of course)
- Creeper Bombs (who doesn't want creepers?)
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Better Planets and Backgrounds" )
    mod_info.set_author( "sanmonku" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=9241" )
    mod_info.put_version( "f40d9d8d3b82c8c487018beae83ebbbf", "1.2" )
    mod_info.put_version( "dcabfc921456dc2fa19e7f7d3659764a", "1.3" )
    mod_info.put_version( "8fb8c81074ef80f91ab9fa9a27b1c480", "1.0" )
    mod_info.set_thread_hash( "c1da7f250cb71a9f5c23d89d93f112f6" )

    mod_info.set_desc(r"""This mod replaces all of the existing planets and backgrounds and adds a lot more. Only 3 of the backgrounds are taken from Hubble, rest were done by me.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Better Asteroids" )
    mod_info.set_author( "sanmonku" )
    mod_info.set_url( "http://www.moddb.com/mods/better-planets-and-backgrounds/downloads/better-asteroids" )
    mod_info.put_version( "96a78e1850d8796a78a7cbda7da5676b", "1.0" )
    mod_info.set_thread_hash( "???" )

    mod_info.set_desc(r"""This Mod replaces the Textures for the Asteroids and the ion storm lightning.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "diversityMod" )
    mod_info.set_author( "liakad" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=3363" )
    mod_info.put_version( "2534e515b635e15a9af90dacc376f900", "0.3" )
    mod_info.put_version( "ce799c0f1f698b855e6170025c6cbba5", "0.2" )
    mod_info.put_version( "179857cc78d0b8be747c20358e3fbb90", "0.1" )
    mod_info.set_thread_hash( "bacae38d34c3ad9eaf06d4d244d747cc" )

    mod_info.set_desc(r"""This Mod aims to create a greater diversity in mostly graphics and some parameters of FTL.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "High-res Background Graphics" )
    mod_info.set_author( "splette" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=3107" )
    mod_info.put_version( "f4c3f9b954c855677df8df856f6a0767", "1.0" )
    mod_info.set_thread_hash( "6c87d36c03578dc98b843a4fcd1288b7" )

    mod_info.set_desc(r"""I love FTL and I do like retro and pixel graphic. But I'm not a huge fan of the background graphic of FTL. They seem low res (especially the nebula animations). Some of the planets and galaxies look like they were painted over with an impressionist brush in Photoshop. So, I decided to replace the planets and backgrounds with higher quality versions, trying to stay as close as possible to the original subjects - and add a couple of new ones.

The only thing this mod does is replace the background graphics. That is planets, sun, stars, galaxies and the nebula. No other textures (ships etc) are being modified.

Please note: For the added backgrounds and planet, I had to modify the file events_imageList.xml (append is not possible in this case). Keep this in mind if you use any other mods that altered that file.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Beginning Scrap Advantage" )
    mod_info.set_author( "Grognak" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2464" )
    mod_info.put_version( "b5a9fad1abec0018ea3d5b332bb6dce5", "1.0" )
    mod_info.set_thread_hash( "???" )

    mod_info.set_desc(r"""Beginning Scrap Advantage is a simple example mod. All it does is give you some extra scrap when you first start a game.

Rename .ftl to .zip and extract it in order to study it further.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Beginning Scrap Mod" )
    mod_info.set_author( "Tails" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11094" )
    mod_info.put_version( "eac9c093b8e400eba73868c8253a6e91", "2.1" )
    mod_info.set_thread_hash( "380a872c1ad35c81ce039e95efb3af85" )

    mod_info.set_desc(r"""This is a slight upgrade to the Scrap Advantage mod that comes with Grognak's Mod Manager.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Additional Events and Texts" )
    mod_info.set_author( "Collaboration" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11094" )
    mod_info.put_version( "404bc800a8fd9febfe67475454e2c9c3", "2012-10-04" )
    mod_info.set_thread_hash( "???" )

    mod_info.set_desc(r"""The goal of this mod is to add new content in form of events and random texts, this will ensure that you are unlucky if you experience the same event twice in a row. It will add extra random texts to already existing events, like when you get to a beacon with nothing, you don't want to see the same text here. All events should be balanced, you won't get a lot of scrap for nothing, at least not more than you could if you played vanilla.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "OliMods - Better Mercenaries " )
    mod_info.set_author( "Catalyst78" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11338" )
    mod_info.put_version( "91ee0a6f71d37c24ca02c1b52a430e76", "1.3" )
    mod_info.set_thread_hash( "daf2f98ce1225cc55781f581c23c033d" )

    mod_info.set_desc(r"""Tired of slaughtering every mercenary that darer fly your path of destruction? Want some of those neat little blue options to spice up your mercenary encounter? Well look no further!

With the intention of making mercenary encounters a little more interesting I have tripled the amount of code in the mercenary encounter event!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Crystal Quest Tweak" )
    mod_info.set_author( "Stickman" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=3483" )
    mod_info.put_version( "7b26f95c8b1147030683d0ea1f84a676", "1.0" )
    mod_info.put_version( "db63e6d4f5a5fb0bfbc6ecc42c43afc6", "1.0 Start Boost" )
    mod_info.set_thread_hash( "37f6ffaccd9406637645c521085a3288" )

    mod_info.set_desc(r"""This simple mod tweaks the secret ship unlock quest line to make it slightly less frustrating.

Specifics (with some potential spoilers):

**Spoilers!**
Once you've opened the stasis pod, entering the required homeworld sector with the secret crew member will put a quest marker at a secret sector wormhole location. This should alleviate the frustration of opening the pod, finding the correct homeworld, but missing the wormhole event.
**End Spoilers**

Alternate version with increased quest start probability:

I've also created a second version (Crystal Quest - Start Boost) which makes the pod event a guaranteed node in Engi space and a possible node in Zoltan space. If you try this version, let me know if you run in to too many pods!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Extra Names Mod" )
    mod_info.set_author( "IcarusTyler" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=3293" )
    mod_info.put_version( "be28ee23c37bfb0aec2f7f684c8779cc", "1.1" )
    mod_info.set_thread_hash( "d3a98eeaa6ccd4259424b2707294e760" )

    mod_info.set_desc(r"""Have you been playing FTL for 30+ hours already? Are you seeing the same names appear over and over again? Are you tired of having the same old crewmen re-join your ship during your journey?

The Extra Names Mod adds over 400 new, unique and hand-picked names to FTL.

140 female first names, like
- Annika
- Hannah
- Selene

138 male first names, including
- Harvey
- Douglas
- Miles

And 129 unisex last Names, in the style of
- Freeman
- Jensen
- Collins
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Ghosts" )
    mod_info.set_author( "Attackid" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=3453" )
    mod_info.put_version( "5623c3ed75ae42ae0a2b86db3d8cb67c", "0.2 Ghosts Only" )
    mod_info.put_version( "6057fe3c431567787f6998a5d71fc3b8", "0.2 Toggle" )
    mod_info.set_thread_hash( "a4273294427aba035ba56158fe0d6922" )

    mod_info.set_desc(r"""Ghosts appear in FTL as an AI race that currently cannot join your crew, which is something I thought should be changed.

Features
- 50 health (can't be changed)
- 50% visible
- Can survive with NO oxygen

This mod has 2 varieies.

Version 1
This version replaces all starting human crew on all ships with ghosts

Version 2
This version replaces all starting human crew on all ships with ghosts
However you can enable this mod and still play as humans.
Once you reselect a ship in the hanger the ghosts will turn back into humans. Just go back to the main menu (ESC) to turn them back into ghosts. So you can have this mod always enabled!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Gruesome" )
    mod_info.set_author( "DryEagle" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11183" )
    mod_info.put_version( "0a6a4ef02a8c316e11f22b0ac4bae0db", "1.0" )
    mod_info.set_thread_hash( "1b68447189c0030a75f563830ecc1150" )

    mod_info.set_desc(r"""I present to you a very small, minor and incredibly compatible-with-everything mod which changes some of the event text.

Any time you lose a crew member to an event, this will in some way be caused by (usually eaten by) a grue.

If you are running any other mods which edit events, load this first so that it won't conflict with them, though that is very unlikely as it only edits very specific parts of text and not any event names etc.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "UnlockedAugmentations" )
    mod_info.set_author( "karmos" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10997" )
    mod_info.put_version( "09613c51e19c8139e6f3867ecd61ae1c", "1.1" )
    mod_info.set_thread_hash( "e31ecbbdf3da62a873298a818f02bab2" )

    mod_info.set_desc(r"""UnlockedAugmentations is a small mod that makes Vanilla ship-specific augmentations (Engi Med-bot Dispersal, Drone Reactor Booster, Mantis Pheromones, Rock Plating, Slug Repair Gel, Titanium System Casing, Zoltan Shield) findable in events and shops in their respective racial sectors.

Engi Med-bot Dispersal - Engi Controlled and Engi Home Sectors
Drone Reactor Booster - Nebula Sectors
Mantis Pheromones - Mantis Controlled and Mantis Home Sectors
Rock Plating - Rock Controlled and Rock Home Sectors
Slug Repair Gel - Slug Controlled and Slug Home Nebula Sectors
Titanium System Casing - Pirate Sectors
Zoltan Shield - Zoltan Controlled and Zoltan Home Sectors

Each augmentation is as rare as the Weapons Pre-Igniter in their sectors, meaning each is ultimately rarer than other augments in Vanilla due to their sector specificity. Titanium Systems Casing and Drone Reactor Boosters are as rare as Repair Arms, Stealth Weapons, Advanced FTL Navigation, and FTL Jammers in their respective sectors. Augmentation costs have been modified to reflect accurate sale values and may be adjusted in later versions of the mod.

This mod shouldn't conflict with other mods unless augmentations are being tweaked. If you are using a ship or weapons mod in conjunction with UnlockedAugmentations and want to preserve the changes made to augmentations in those mods, simply place UnlockedAugmentations above the other mods in GMM.
""")
    mod_db.add_mod(mod_info)


