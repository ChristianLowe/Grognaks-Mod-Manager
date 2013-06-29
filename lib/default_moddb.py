# -*- coding: ascii -*-
# ^ Ascii chars are the norm in Python 2.x source code.
# This'll make a 3.x interpreter panic when any unicode sneaks in.

from lib import moddb


def populate_catalog(mod_db):
    mod_info = moddb.ModInfo()
    mod_info.set_title( "A Strange New Galaxy" )
    mod_info.set_author( "Metzelmax" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14896" )
    mod_info.put_version( "59a741e873b67efe38411d1c83424432", "0.2d Standard WIP" )
    mod_info.put_version( "926f3fbab11d1aeb61d58e94b49c93af", "0.2d WOO WIP" )
    mod_info.put_version( "a714b38157d5d665b54be419ed741790", "0.2b Standard WIP" )
    mod_info.put_version( "65468b6991b6988d929bc9b51170aba5", "0.2b WOO WIP" )
    mod_info.set_thread_hash( "af1588d408a42c78fcc9d8fa098d3336" )

    mod_info.set_desc(r"""This Mod contains the ships, weapons, and drones from my other 3 Mods. Check there for a detailed overview of ships and weaponry:
- The Anterian Terminator-Ships
- The Treel
- The Uz'ran Tribes

There are two versions of this mod:
- Standard - Includes everything.
- WOO - No custom player ships.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Advanced Weapons and Shields" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11058" )
    mod_info.put_version( "1368ecb746bea1fab261d8a5eb8c23f1", "1.2" )
    mod_info.set_thread_hash( "dbb90b01a5931e59a6e2cf5e6b3054f6" )

    mod_info.set_desc(r"""Discontinued. See: "Advanced Battle Systems".

Get five shields and power your advanced weaponry! Thanks to a breakthrough by Engi scientists, ships are now able to have five shields and level twelve weapons. The Engi Advanced Technology Development Division has released this technology to the Federation, in hopes that they can beat the rebels. You can pick it up today, at your local Zoltan Trade Hub or on this post!

Known Bugs:
A bug in FTL causes asteroid storms to be abnormally fast when you have five shields. This mod removes asteroids from events to compensate.
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
    mod_info.set_title( "Descent into Darkness" )
    mod_info.set_author( "DryEagle" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=12203" )
    mod_info.put_version( "31d113bd974ff7a85ced03aed790cd6f", "2013-05-23" )
    mod_info.put_version( "5abed01b50c41b7a208ac29bdbdbdcc9", "1.1" )
    mod_info.put_version( "c734abda7e230523f883a5ec92c28045", "1.0" )
    mod_info.set_thread_hash( "45ccb2dcecc62d4fafa48335ab32c30f" )

    mod_info.set_desc(r"""Descent into Darkness is a complete overhaul modification for FTL.
You do not start with a single ship loadout and play the game regularly.
Instead, you are given a barebones ship hull and pick your starting gear, crew, augments, everything.
There are 72 possible starting combinations - 4x more than the number of default ships in vanilla FTL!

Mod compatibility
- This mod is not intended to be compatible with a lot of other things.
- Anything with events is probably out of the question.
- Background system/planet images should be ok.
- Weapon graphic mods might work. Other stuff probably won't.
- If you insist on running it alongisde other mods, make SURE you load this LAST in the list! Any part of this mod's content being overwritten will likely mess up the whole thing.
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
    mod_info.set_title( "Enemy Diversity Pack" )
    mod_info.set_author( "kartoFlane" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=14408" )
    mod_info.put_version( "8fc6831574187d8d49ceb1c4bcaddcf3", "1.0 EDP-only" )
    mod_info.put_version( "9bd1296b4694e7802035c2d248ae0562", "1.0 Vanilla" )
    mod_info.set_thread_hash( "83e1de456fce0059afe0b1abe6b581b5" )

    mod_info.set_desc(r"""Ever got tired of killing the same enemies over and over again? Ever wanted some challenge, other than a new ship?

Here is a simple mod that strives to accomplish this - the Enemy Diversity Pack, which expands the enemy fleets by adding a layout B to almost every enemy ship in the game - tougher and better equipped than your ordinary foes!

There are two versions of this mod:
- EDP-only - All enemies have been replaced with their layout B counterparts, you won't encounter default ones anymore.
- Vanilla - Includes default (vanilla) enemy layouts, as well as EDP layout B ships.
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
    mod_info.set_title( "Faster Than Sound" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=12168" )
    mod_info.put_version( "2f8bca0a4e60fd9393aa0e563698d920", "0.1 Alpha WIP" )
    mod_info.set_thread_hash( "6e21416e7b96e68043ab05e864eb81a0" )

    mod_info.set_desc(r"""A new Total Conversion to bring the modern day into FTL.

Features
- F-22 Raptor
- F-35 Lightning
- The title screen background has been changed.
- Sector names changed (except for the first).
- Music for some sectors have been replaced with the national anthem of their respective sectors.
- Beginning sector events have been changed.

Replaces the Kestrel-A ship.
Replaces the Kestrel-B ship.
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

Replaces the Kestrel-A ship.
Replaces the Stealth-A ship.
Replaces the Federation Cruiser-A ship.
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
    mod_info.set_title( "Infinite Space" )
    mod_info.set_author( "DrkTemplar" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=3542" )
    mod_info.put_version( "5bad4d1ec8fcc188142ce2861f8650bb", "0.4.4 Hi-res Bkgs" )
    mod_info.put_version( "de440631df2c0b8274a0f37ccff79206", "0.4.4 Original Bkgs" )
    mod_info.put_version( "9de0823d7d8b33cf27ac2807e085cd45", "0.4.3" )
    mod_info.put_version( "516e20d80b9c6c878b0730c3e7978576", "0.4.1" )
    mod_info.set_thread_hash( "735b342724c077dd769a97dd32c71984" )

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
    mod_info.set_title( "Insane Difficulty" )
    mod_info.set_author( "brothershogo" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14101" )
    mod_info.put_version( "709cdd2e5a948fc2f8cec03ef1f7595e", "1.0" )
    mod_info.set_thread_hash( "c541978190439dff46171f6e1f682532" )

    mod_info.set_desc(r"""This mod rebalances all enemy NPC ships. Its a mod meant to be played with OP/God/Advanced/Powerful ships. Do you love OP ships but find it boring to play with them against vanilla enemies? Then try this mod and put your skillz to the test.

Features
- +10 hp to all ships
- All ships have at least level two shields
- All ships have max reactor power
- All ship systems leveled up to maximum
- All ships have max drone/weapon slots
- All ships have maximum number of crew
- You will encounter bomber/assault class vessels early in the game
- New cruiser class enemies including my Tsunami Class Battlecruiser and Tengu Stealth Cruiser
- Harder boss (increased hp and buffed weapons.)
- Two new OP weapons you will have to face. The Gatling Laser, which fires 8 shots, and the Advanced Burst Ion - Cannon which fires 3 shots every 6 seconds.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Mass Effect Total Coversion" )
    mod_info.set_author( "Captain_Brian" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=8936" )
    mod_info.put_version( "278414a9d1385dc2ec2676590afb3da3", "0.013" )
    mod_info.set_thread_hash( "e1ff5a7d2b0b51b7414d302792aea4b0" )

    mod_info.set_desc(r"""Backstory
Cerberus has found a way to control the reapers. The reaper war has been raging on since the failure of the Crucible Project, and the whereabouts of the Normandy and its crew are unknown.

Data mined from the Cerberus network suggests a tachyon pulse emanating from The Illusive Man's command ship has "erased" the reaper collective consciousness, and replaced it with a rudimentary command recognition structure that Cerberus can send commands to. The data also suggests that the Illusive Man's command ship is the only ship capable of sending commands to reaper forces, and that eliminating it will permanently disable the reapers.

Unfortunately, Cerberus have completely disabled galactic communications, which leaves it up to you to deliver this data to Alliance Command. Reaper forces are preoccupied with decimating planetary infrastructure, but the Cerberus fleet has only one target...

YOU.

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "New Enemy Classes" )
    mod_info.set_author( "Sleeper Service" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14503" )
    mod_info.put_version( "584e026f94c85645bc31c3a8a853a2bf", "0.95 A WIP" )
    mod_info.put_version( "9934631f0e382128da2f5d61fdc13c4b", "0.95 B WIP" )
    mod_info.set_thread_hash( "55a8d7a2e0a4267e375ce3e406e0fd6a" )

    mod_info.set_desc(r"""A subset of the "FTL Captains Edition" mod.

The new enemies use distinct tactics against you and are designed to add new challenges, opportunity and thrills to your FTL experience.

These alternate room-layouts are designed to fit seemingly into vanilla. Hopefully well balanced and lore-friendly.

There are two versions of this mod:
- A - Mixed with vanilla.
- B - Replaces all vanilla enemy layouts.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Omicron Dynasty" )
    mod_info.set_author( "speedoflight" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14577" )
    mod_info.put_version( "d49d1868d8c5d9af67e29f4516399742", "0.8 WIP" )
    mod_info.put_version( "", "0.7 WIP" )
    mod_info.put_version( "654970533e12c68e11ea48ceccc39b72", "0.6 WIP" )
    mod_info.set_thread_hash( "677655c04e2bb5c746a3c55f8aaa61d5" )

    mod_info.set_desc(r"""The Omicron Dynasty was born in the deepest quadrant of the Galaxy, the origins of this Society is almost unknown, but some rumors along the entire galaxy tell that they were a really advanced civilization eons ago, but the giant sun of their system started to collapse. Then some of them abandoned their system searching a new planet to colonize.

Features
- Replaces all player ships.
- New weapons.
- New drones.
- New events.

This mod is for experienced players or people who really want a little challenge.
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

On the aesthetic side, the rebel fleet has been replaced with the Federation military, dark green ships that seek to destroy or arrest you. You pilot a "liberated" model of one of these Federation ships, the "The Black Spot." The mod also rewrites all tooltips into "Pirate-Speak," a much more suitable dialect of English for those of you who are swashbuckling corsairs. All NPC crew-members will now have pirate names, including favorites such "Peg-leg" and "Patchy." In addition, the first of many new weapons has been added, the Cast-Iron Ship's Cannon, masterfully nailed to the side of your ship with wooden planks, and accompanied by a hearty quantity of lead cannonballs for you to launch through the depths of space.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Somewhat Faster Than Light" )
    mod_info.set_author( "blaeron" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2603" )
    mod_info.put_version( "e7558768ce75524079d9e58d521f54dd", "1.1" )
    mod_info.set_thread_hash( "10ffac10ee66440ecc8e1fcea6dd4c1a" )

    mod_info.set_desc(r"""Features
- Burst Laser Mark IID
- Voulge beam
- Plasma Beam
- Beam Drone Mark II
- New Pegasus and Aristea missile sprites.
- Improved drone speeds and fire rates.
- Added Elite Rigger.
- Changed the playable Rockman ships somewhat.
- New nebula and background sprites, and new warnings.
- New solar flare and ion storm sounds.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Sonata Total Conversion" )
    mod_info.set_author( "thashepherd" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=6517" )
    mod_info.put_version( "48e5693219f0fa501b9aa354118e2713", "7a" )
    mod_info.put_version( "b13de0c782576c9c20f0ef6d0fe317c5", "7" )
    mod_info.set_thread_hash( "e54da9b7c56aaca547fc1b6d963575f5" )

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
    mod_info.set_title( "Star Trek Universe" )
    mod_info.set_author( "speedoflight" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11844" )
    mod_info.put_version( "c60abdd47746b7233250fe1ae7272d38", "1.1" )
    mod_info.put_version( "ff4c15c3926827c4170c462369e2b0ce", "1.0" )
    mod_info.put_version( "ab77b5a3c53b21c7c7d0d55c688ce508", "0.7 Beta WIP" )
    mod_info.put_version( "b8b68c6906752235a0d3100ce143c94b", "0.6 Beta WIP" )
    mod_info.put_version( "77e25d8a9acc738970f0cd1c88269556", "0.5 Beta WIP" )
    mod_info.put_version( "0443f8504ad6823a1ea875127a87273b", "0.3 Beta WIP" )
    mod_info.put_version( "cddbb53e53745b8b1ac7cac7073e14e0", "0.2 Beta 2013-03-02 WIP" )
    mod_info.put_version( "c6880fd3e9423affe5ff9dc733580cad", "0.2 Beta WIP" )
    mod_info.put_version( "098dc2eb3865b701697e6a73420f57c6", "0.1 Beta WIP" )
    mod_info.set_thread_hash( "970abbe8864db06e2695f5c280e174bb" )

    mod_info.set_desc(r"""Eventually this will replace all 18 default ships in the game with vessels from Star Trek: Federation, Klingon, Species 8472, Romulan, Borg, Cardassian, Jem Haddar, Krenim, Hirogen, etc.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Turning the Tide" )
    mod_info.set_author( "Kieve" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=3056" )
    mod_info.put_version( "a5a73f329fb153dc445eca672b51114b", "1.0" )
    mod_info.set_thread_hash( "6d18802d42bb9de3b8c420f9aa4cec8a" )

    mod_info.set_desc(r"""This mod alters your encounters with the Rebel Fleet to increase the risk / reward factor, giving you the option to bring their advance in a sector to a screeching halt - or die horribly in the face of overwhelming odds!
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Twinge's Balance Mod" )
    mod_info.set_author( "Twinge" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14766" )
    mod_info.put_version( "6568f9abfb133a49d0a95baeb1cce2a4", "0.5.3 for FTL 1.03.3" )
    mod_info.set_thread_hash( "0a5ff027e923fa43016b7d4b76d2086e" )

    mod_info.set_desc(r"""This mod makes more equipment in the game worth using and increases the quantity of interesting decisions. This mod doesn't add large amounts of additional content - instead it focuses on improving the usefulness of existing content and making the base game a better overall experience.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Warhammer 40k - Battlefleet Gothic Mod" )
    mod_info.set_author( "DauntlessK" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=11604" )
    mod_info.put_version( "???", "N/A WIP" )
    mod_info.set_thread_hash( "45d4c8a847a945382311da3105cd07d3" )

    mod_info.set_desc(r"""This mod is meant to give you the feeling that you're a captain in the dark and twisted universe that is Warhammer 40,000. It is starting off as a ship+weapon mod, but will continue to grow into something even bigger.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Anterian Terminators" )
    mod_info.set_author( "Metzelmax" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=12652" )
    mod_info.put_version( "1da09a8b91c0043d87223fae29a073ff", "1.6" )
    mod_info.put_version( "43bdef53b4f612da111e8a7ab49cc174", "1.2 WIP" )
    mod_info.put_version( "2abbf46cdf98db0a02ed65734757370d", "1.0 WIP" )
    mod_info.set_thread_hash( "79c7e80030033423ab40b1eb11aea02b" )

    mod_info.set_desc(r"""Background
Back when my friend and me were 14, we got soon bored by the standard species in the Star Trek universe and began to develop our own.

The Anterian are small, blue scaled Humanoids with a lifespan of about 25. Their home planet is surounded by a huge nebula, which consists mainly out of metal. The Anterian have specialized in A.I., robotics and Computers. Most of their work is done by androids, which are not sentient but intelligent enough to work without surveillance.

Replaces the Engi-A ship.
Replaces the Engi-B ship.
Replaces the Rock-A ship.
Replaces the Rock-B ship.
Replaces the Kestrel-A ship.
Replaces the Kestrel-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Amber Shard" )
    mod_info.set_author( "DryEagle" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11703" )
    mod_info.put_version( "8a5a336510ac21b1e5b24e0657287b5d", "2.0" )
    mod_info.put_version( "8a5a336510ac21b1e5b24e0657287b5d", "1.0" )
    mod_info.set_thread_hash( "db2b990bc454e5d5e9fe4264a8a0393d" )

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
    mod_info.set_title( "Arwing" )
    mod_info.set_author( "VanguardOfValor" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15646" )
    mod_info.put_version( "7474299587c81e49240a11aae175db3b", "Arwing II 1.0" )
    mod_info.put_version( "c59674791a6faeef2b2751f44d3b0333", "Arwing I 1.0" )
    mod_info.set_thread_hash( "c792d6654155511431050ecc53221b09" )

    mod_info.set_desc(r"""The Arwing from StarFox 64.

If you're finding Arwing I too difficult, you may want to try the Arwing II instead, which has it's starting weaponry buffed and is quite a bit easier to get going with!

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Asteroid" )
    mod_info.set_author( "5thHorseman" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=16215" )
    mod_info.put_version( "fd266a27e4a32e82c345b87f4a5ecb88", "1.0" )
    mod_info.set_thread_hash( "c04ff19431fa0655922f34d0f7f85f72" )

    mod_info.set_desc(r"""Who's crazy enough to go toe-to-toe with the Rebel Flagship in a hollowed out asteroid?

The Asteroid is my attempt at a ship with a 4-person teleporter and a 4-person medbay. I love the 2x2 teleporter rooms but it's a pain to shuffle your away team around when you want to heal everybody up. No longer! Just run your whole team into the nearby medbay, heal 'em up, and send 'em back into the fray!

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Banana" )
    mod_info.set_author( "corporat" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=16567&p=50491#p50491" )
    mod_info.put_version( "5dcb1aa7e1dc985bb82b19874edeee7c", "0.999" )
    mod_info.set_thread_hash( "7783ac7281c6adaadb0fa66e395e47cd" )

    mod_info.set_desc(r"""A "space banana".

Why, you ask? I've been following the FTL mod community for a while now, and I've found it lacks something. Potassium. You guys have a serious deficiency. It's a problem.

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Battlefleet Gothic - Cobra Class Destroyer" )
    mod_info.set_author( "Harnisfechten" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=10431" )
    mod_info.put_version( "3d50785d23090ecb0aa0ede535b0c24b", "1.0 WIP" )
    mod_info.set_thread_hash( "6264da50ab73f21b95e04a874255df1b" )

    mod_info.set_desc(r"""The Cobra Class Destroyer is a ship from the Warhammer 40k Universe. It is known as the smallest independent Imperial ship (i.e., it can patrol alone, and is not a fighter or bomber based on another ship).

Due to difficulty in finding an overhead image of the ship of suitable quality, I decided to try something different and make the ship from a side view. Sure, the crew and rooms are all top view, but I actually think it looks pretty good.

The Cobra is armed with a dorsal weapons battery (a Burst Laser Mk II in the game) and prow-mounted torpedoes (2 Hull Missiles in the game). Note that the crew are not to-scale with the ship, as the ship is approximately 1.5km long (yeah, 40k ships are big). I like to think that instead of individual characters, each crew member represents a team of people, so the pilot is not just one pilot, it is the entire command staff on the bridge of the ship, and the weapons guy is not one guy, it is a large number of gun crew, the ratings that load the weapons, the engineers that serve them, etc.

Replaces the Rock-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Battlestars" )
    mod_info.set_author( "FrostWyrmWraith" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11940" )
    mod_info.put_version( "544a96a8c4af93c0099a55d10563e8fd", "1.0 2013-03-06" )
    mod_info.put_version( "4b2d7e5f6d80b475a9b4e9d0d740ff41", "1.0" )
    mod_info.set_thread_hash( "49de32110c905eb33e5ef07f888afbfd" )

    mod_info.set_desc(r"""A pair of new ships.

The Galactica begins with a missile launcher and two Vipers as a homage to what it fought like in the series.

Replaces the Engi-A ship.

With the Pegasus I didn't want to make the ship too overpowered so I gave it two KEW batteries and a single Viper, though starting it with more and giving it more drone slots would have been more accurate. I wanted it to play a bit differently, so it focuses more on weapons than fighters. In the game you can find the Viper Mk VII, as well, so keep your eyes peeled!

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Blazing Cruiser" )
    mod_info.set_author( "Zaffre" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=3133" )
    mod_info.put_version( "162e44fa11491c37046e7386b87834a6", "1.6" )
    mod_info.put_version( "eb5484304b45b3be8ff043aa78c0defc", "1.5" )
    mod_info.put_version( "af34777f9b70769828ea27f24b5b298a", "1.4" )
    mod_info.put_version( "c522d5da78aebbd55a6f68cc6e98162d", "1.3" )
    mod_info.put_version( "17b671da29f071521e8e54f77cb6c325", "1.2" )
    mod_info.put_version( "141f70d3643d275504c04993fdaab110", "1.1" )
    mod_info.put_version( "a23e32a6591af658e4ce9ab92403c4aa", "1.0" )
    mod_info.set_thread_hash( "3775b3b55c91460232f0abd11ce1a055" )

    mod_info.set_desc(r"""This cruiser uses fire weaponry. It starts with two extended fire beams, one laser weapon that starts fires, and a missile that starts fires. It starts with no shields or cloaking. To give the ship a chance, it has a unique drone upon start. The crew is composed of three Rock. The sprites are modified versions of the Kestrel B layout.

Replaces the Kestrel-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "BSG Colonial Fleet" )
    mod_info.set_author( "TheEzdev" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15799" )
    mod_info.put_version( "969e1c9ea59a13bca0db6d36caf23519", "1.1" )
    mod_info.set_thread_hash( "8444f0c4ef993e6695b4855b7fef612c" )

    mod_info.set_desc(r"""Ships from Battlestar Galactica.

Replaces the Kestrel-A ship.
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

    mod_info.set_desc(r"""This is the C-1092. It is made for teleportation combat. You get in, then out as quick as possible. I made this because I could not find any ships of this type.

Replaces the Stealth-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Capital Cruiser" )
    mod_info.set_author( "slowriderxcorps" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15761" )
    mod_info.put_version( "e488d5d8822f4748c8016cda3057a97d", "1.1" )
    mod_info.set_thread_hash( "ab480cec02bb380a6b046de2dad5a4d3" )

    mod_info.set_desc(r"""The Capital Cruiser (Type A) - The Imposter

She comes equipped with a wide variety of weaponry to pick off any foe that stands in your way. However, regardless of its blast doors, the lack of starting crew and any form of venting will make dealing with damage particularly challenging.

Replaces the Crystal-A ship.

The Capital Cruiser (Type B) - The Paradox

It starts with every single system already installed. Naturally it has its own issues, namely the lack of any form of direct damage, with the only form of offensive capability coming from a two-man teleporter and a quartet of hapless Humans. The other weaknesses to mention include a reactor that'll struggle to keep everything running from the get-go, as well as the (again) lack of any venting and additional lack of blast doors.

Replaces the Crystal-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Corellian Transport" )
    mod_info.set_author( "LarsenB" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=12201" )
    mod_info.put_version( "0e27c9756990306c581d3e175ee8b499", "1.0" )
    mod_info.set_thread_hash( "0d6c99e43d5c45f5c678a42974165347" )

    mod_info.set_desc(r"""A fairly straightforward ship based on Star Wars.

Features
- Good engines and FTL drive, for you smugglers out there.
- Ion and laser weapons
- Average sensors

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Crusher's Type C Annihilator" )
    mod_info.set_author( "Crusher" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14457" )
    mod_info.put_version( "8d44f882fcb48248307cab879d38466f", "1.0" )
    mod_info.set_thread_hash( "91107ed15071128e442e2a3d1bca69c5" )

    mod_info.set_desc(r"""Part of the "Crusher's Type C(hallenge) Ships" collection.

The Annihilator has used an experimental Zoltan weapon, the phase beam, to extract key information about a Rebel attack planned against the Federation capital. Escaping from Rebel fighters, The Annihilator rushed into its FTL jump, overloading and ultimately destroying its reactor. The Annihilator comes with 4 Zoltan crew, the only source of power at the start of the game, but you are able to buy power bars like normal (thematically repairing the reactor).

Replaces the Zoltan-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Crusher's Type C Krakatoa" )
    mod_info.set_author( "Crusher" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14457" )
    mod_info.put_version( "7dbc2e6e2f68526c76bc650e648690ba", "1.0" )
    mod_info.set_thread_hash( "91107ed15071128e442e2a3d1bca69c5" )

    mod_info.set_desc(r"""Part of the "Crusher's Type C(hallenge) Ships" collection.

Krakatoa is a non-military ship manned by a Rock religious sect, the Fire Monks. Krakatoa comes with a pyrogenic missile, the Vulcan Missile that does only 1 damage but is highly likely to start a fire. It also has an artillery weapon, the Prometheus Ray, that continuously attempts to ignite fires at random on the opposing ship. Since it is not a military ship, it does not come with shields, but it does have heavily reinforced armor (triple rock armor).

Replaces the Rock-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Crusher's Type C Sarcosuchus" )
    mod_info.set_author( "Crusher" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14457" )
    mod_info.put_version( "4d2f515ed73ca57eeb77fa2325a6a9d2", "1.0" )
    mod_info.set_thread_hash( "91107ed15071128e442e2a3d1bca69c5" )

    mod_info.set_desc(r"""Part of the "Crusher's Type C(hallenge) Ships" collection.

While extracting information from the Rebels, your ship sustained heavy damage, lowering shields to one bar and destroying sensors, doors and most importantly the life support (O2). Most of the crew has also died leaving you with just 1 Mantis and 1 Crystal. I suggest self-enforcing a 5-crew limit.

Though lacking several standard issue systems, it has many amenities to compensate: cloaking, drone control (system repair and antipersonel), a 4-crew teleporter, a 5-crew medbay, and level 2 piloting.

Replaces the Mantis-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Crusher's Type C Singularity" )
    mod_info.set_author( "Crusher" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14457" )
    mod_info.put_version( "ac9c260b2e3907d8f210609baa753b31", "1.0" )
    mod_info.set_thread_hash( "91107ed15071128e442e2a3d1bca69c5" )

    mod_info.set_desc(r"""Part of the "Crusher's Type C(hallenge) Ships" collection.

Cornered by the Rebels, the Engi have brought back their fearsome boarding drones and radiation weapons, which were (and still are) banned by a galactic protocol. Boarding drones never seemed like a viable primary strategy in FTL, so I wanted to make a ship that could (and must) do it. At some point you will probably have to transition into traditional weapons, but you should have several sectors of boarding drone fun.

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Dark Knight Cruiser" )
    mod_info.set_author( "Gunman698" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=13991" )
    mod_info.put_version( "0d12efc80148b6feb3e8769b63edc6d0", "1.0 WIP" )
    mod_info.set_thread_hash( "e9fb98dd4935939da884605fefd7d52e" )

    mod_info.set_desc(r"""To all of you who have a keen eye, yes I did just get some AI ships and gibs and glue them together for the ship design.

The ship is designed mostly for ion and drone damage, hence why it is an engi ship. It has 4 crew (2 Human, 2 Engi), all subsystems level 1 and basic systems.

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Duality Cruiser and Merchant Cruiser" )
    mod_info.set_author( "zaratustra" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2729" )
    mod_info.put_version( "4d68f90233698b7db9c792ae3573e2fe", "1.0" )
    mod_info.set_thread_hash( "158f664b69f336be816be618902437ba" )

    mod_info.set_desc(r"""The Duality is divided into two sections.

Replaces the Kestrel-A ship.
Replaces the Kestrel-B ship.
Replaces the Engi-A ship.
Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Escort Duty" )
    mod_info.set_author( "DryEagle" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11531" )
    mod_info.put_version( "bed7f8c867bb728ce852f4fcccf923e8", "1.0" )
    mod_info.set_thread_hash( "6435f1e566e92347458a8e21806037db" )

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

Intro
The Lockheed Martin/Boeing F-22 Raptor is a single-seat, twin-engine fifth-generation supermaneuverable fighter aircraft that uses stealth technology. It was designed primarily as an air superiority fighter, but has additional capabilities that include ground attack, electronic warfare, and signals intelligence roles.

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Falcon" )
    mod_info.set_author( "Thunderr" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15536" )
    mod_info.put_version( "d2bc64492240b52d29a04325ef2e2159", "1.1" )
    mod_info.put_version( "c8ed28c1aaf5a53ee97e7842715dda65", "1.0" )
    mod_info.set_thread_hash( "a1208693b636f160d6704e6dbdb67444" )

    mod_info.set_desc(r"""The Falcon is a high class Federation ship designed for speeding through enemy lines in a barrel roll. Designed by the Federation's best engineers, this ship uses state of the art engine technology, but is relatively low on other systems. It comes with an Artemis missile and Dual Lasers that take a while to charge, but when they do, they pack quite a punch.

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Fion Cruiser" )
    mod_info.set_author( "Yuurg" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15603" )
    mod_info.put_version( "b195375faad81206d4646a8b68bdf86d", "1.2" )
    mod_info.set_thread_hash( "9c7809ffd63ae6b1585d5adcf64c6890" )

    mod_info.set_desc(r"""The Fion Cruiser is a ship built around Fire and Ion. Its hull is half red, half blue and half Rock, half Kestrel. This ship is pretty powerful, perhaps even overpowered, but with no damaging weapons you'll have a hard time dealing with Rock ships and Automated ships.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Firestarter" )
    mod_info.set_author( "arcuspilot" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=14014" )
    mod_info.put_version( "7074ea05763ced5d65a4a9f55954308b", "1.0 WIP" )
    mod_info.set_thread_hash( "46b8185a6a035766fc272ea66e61bc4c" )

    mod_info.set_desc(r"""The starting crew, a human and an engi find that there are no sleeping quarters and have put their bedrolls in the sensor and pilot room.

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Goa'uld Hatak" )
    mod_info.set_author( "Zanoko" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=13846" )
    mod_info.put_version( "9c8f89d7489a197fbfd3a427757b233b", "1.1" )
    mod_info.set_thread_hash( "1bd6e84261edce85248ba92ab9452f41" )

    mod_info.set_desc(r"""A Hatak from Stargate.

Replaces the Mantis-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Gotterdammerung" )
    mod_info.set_author( "Koobi" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=13496" )
    mod_info.put_version( "4442f71848fd1e6f6491c70919491c0b", "2.0" )
    mod_info.set_thread_hash( "abed3b00b059e58def61a29ccf8f297e" )

    mod_info.set_desc(r"""This will add the mighty Gotterdammerung to your game, the strongest force in the galaxy. It is so dense that each square meter weighs 200 tons. It is so massive, it has its own gravitational field. The large gyro on top keeps it from attracting to other objects. It would take the combined force of 20 tsar bombs to breach its armor, so it doesn't need a shield.

Features
- New weapons
- New sounds and music
- New drones
- FTL fuel is now called helium

Replaces the Slug-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Halo 4 - Broadsword Ship" )
    mod_info.set_author( "Revenant721" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11620" )
    mod_info.put_version( "3f17e969074ad365d4d3e850d51fdca1", "1.1" )
    mod_info.set_thread_hash( "c4ed37f4842eb68bb5e7599a54cacdef" )

    mod_info.set_desc(r"""Greetings FTL and Halo fans!

Replaces the Kestrel-B ship.
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
    mod_info.set_title( "Hardcase" )
    mod_info.set_author( "sandtrooper956" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=12041" )
    mod_info.put_version( "6c3ee488fc3cc03ce2b4c33cc9678e80", "1.0 2013-03-06" )
    mod_info.put_version( "60b7591a6cbc4ade08b83b5c544ccfcb", "1.0" )
    mod_info.set_thread_hash( "6b118795dc49e0782797a676fa285ef1" )

    mod_info.set_desc(r"""An edit of the Rock-B ship.

It has 200 hp but it its systems are these:
- Level 3 Engines
- Level 4 Weapons
- Level 1 Oxygen
- Level 1 Piloting

They are very limited; no way to heal crew until you get a medbay, which could take a while.

Starting crew: just 2 rockmen.

It only has 2 Weapon slots, starting with:
- Heavy Laser II
- Ion Blast

Replaces the Rock-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Hayabusa Class Battlecruiser" )
    mod_info.set_author( "brothershogo" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14341" )
    mod_info.put_version( "c9df0114a78b0724dff94ad9e39b7795", "1.2 2013-05-17" )
    mod_info.put_version( "0c41fee94a55b1aa0933e6ca5c0232ce", "1.1 2013-05-14" )
    mod_info.put_version( "22c643accb0ebd09bfafa641b0eb7dbd", "1.0" )
    mod_info.set_thread_hash( "d1d9229e746e7d624f385a2e87d1c2df" )

    mod_info.set_desc(r"""A Drone Battlecruiser, using Engi, Mantis, and Federation technology, the Hayabusa is the pinnacle of drone warfare technology, designed to swarm entire ships with its advanced assault drones.

Features
- Advanced drone system can be upgraded to level 12
- Ship equipped with Drone Recovery Arm, Drone Reactor Booster, and FTL Jammer
- Ship balanced to play with my Insane Difficulty Mod

In terms of difficulty, this ship is OP because of its advanced drone system and assault drones. Haven't fully play tested it yet, so still working out the balancing.

Replaces the Mantis-A ship.
Replaces the Mantis-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Hunter" )
    mod_info.set_author( "Starfire" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15892" )
    mod_info.put_version( "38282cb1da8ea862bc5304c1e9a45975", "1.0" )
    mod_info.set_thread_hash( "5ea80a4120f948cfde358915711ce87f" )

    mod_info.set_desc(r"""Right after the Rebels started to form, These ships were made to stop them, however the Federation underestimated the Rebellion and these ships were blown to shreds. You now have the last ship, your ship is better then the rest, you refitted it yourself giving it a prototype cloak and impressive weaponry, Will you make it?

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Incursor Cruiser" )
    mod_info.set_author( "Kieve" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=10361" )
    mod_info.put_version( "fd357ea6465756e45e393feffb986f5f", "0.9c Beta WIP" )
    mod_info.set_thread_hash( "fff726ec5dcd965aaab3aadf62193040" )

    mod_info.set_desc(r"""DISCLAIMER - This mod is still in "beta" status and requires testing. Some weapons may feel imbalanced or overpowered, others underpowered or useless. Please leave detailed, constructive feedback.

Features
- Arc Beam - Antipersonnel particle beam. Damages systems and crew, starts fires.
- Aurora Mass Cannon - Anti-ship cannon that pierces all shielding.
- Bolide Ion Rocket - Deals no hull damage, but very effective at disabling shields and systems.
- Sunfury Rotary Autocanon - Rapid-fire burst weapon. Fast reload but will suck your ammo dry.
- Crew: 2 Zoltan

Also includes the Incursor Theme, replacing the default title music.

The Incursor "Archon" was designed to strike fast and hard, weakening the enemy for their larger capital ships. The Archon's weapon array is devastating indeed, but heavy reliance on limited ammunition makes it a poor choice for extended mission assignments.

Replaces the Zoltan-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Jeff's Boarding Ship" )
    mod_info.set_author( "JeffTheBoardingDrone" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14967" )
    mod_info.put_version( "7e98b705c1e7d47b0d7541b181ca8f21", "1.0" )
    mod_info.set_thread_hash( "5781644555e8e202f9be23ff342efcc7" )

    mod_info.set_desc(r"""This ship is made to board and destroy. Launch in a small army of 4 boarding drones and 2 crystal crewmembers, and make that enemy regret choosing to fire at your ship.

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Junkyard" )
    mod_info.set_author( "JeffTheBoardingDrone" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14808" )
    mod_info.put_version( "3cb09af52070a055154c54d0931bf3e8", "1.0" )
    mod_info.set_thread_hash( "51731e769e5d11236ec9d825a077e070" )

    mod_info.set_desc(r"""The Junkyard is an Engi cruiser replacement, manufactured as a home project by a small group of Engis and a group of old junkyard owners. Not the most efficient example of the Engi technology, but it still has its upsides - like a rusty, outdated magnet arm and an improvised oxygen filter made out of cardboard boxes and duct-tape.

It can't be that dangerous just ripping out random needles from a medivac for the medbay, right? But I think that the rocking stereo system makes up for it.

Replaces the Engi-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Kingfisher" )
    mod_info.set_author( "BadgersCanSpace" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=11522" )
    mod_info.put_version( "b6e4d637e2cf1ce18b8d29e07038f37c", "1.1" )
    mod_info.set_thread_hash( "a2dec688e77a0d5bcb4b6c5982e856b2" )

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

    mod_info.set_desc(r"""A Klingon K'vort-class Bird-of-Prey, "PIvlob Do" (klingonese: Warp Factor Speed).

Replaces the Mantis-A ship.

A Vor'cha-Class Klingon Battle Cruiser, "IKS QeylIS BetleH" (klingonese: The Sword of Kahless).

Replaces the Mantis-B ship.
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
    mod_info.set_thread_hash( "7a8105b7665fa01ad9e42bbea07a42c4" )

    mod_info.set_desc(r"""Marauder ships are characterised by powerful weapon systems that seem to require massive power to operate, even at the expense of all other systems. While not refined, the weapons are effective. Usually disableing and stripping ships clean to provide resources required for the vessel to reach it's full potential. Even though their origins and source of technology are a mystery, the ships are crewed by common races though it's hard to say if they joined up willingly or are slaves.

Fair warning to those eager to play, these ships will not be easy. My guess is that difficulty will be between NORMAL and EXTREME, depending on which ship you pick.

This mod was made without regard for compatibility with other mods. However, it will work with visual, events, and weapon mods, but will almost certainly break system mods. Whether or not it works with other ship mods is unpredictable. I recommend that you install this as a single mod.

Replaces the Stealth-A ship.
Replaces the Stealth-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Marauders - Standalone Weapons" )
    mod_info.set_author( "UltraMantis" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11501" )
    mod_info.put_version( "33556a1a9389047a76c0bd2f3aa685c1", "1.0 2013-03-05" )
    mod_info.set_thread_hash( "1bee67b405215442610bfefccea184dd" )

    mod_info.set_desc(r"""This weapons pack makes stores sell new weapons although they are quite rare so you wont see them all the time.

- Magma Cannon: High fire chance, bypasses shields, immune to defense drones. Pretty fast recycle.
- High-Energy Laser: Modified Fire Beam, pierces 2 shields, medium recycle and high power demand.
- Impact Cannon: Huge power demand. Each shot deals 1pt system damage and ion damage (can damage the shield system just by hitting the shield bubble, and of course ion it as well). Medium recycle.

You are not supposed to use this together with the Marauders mod, since the weapons are not meant to be sold in stores for that. "Not supposed to" doesn't mean you can't, if that's the way you like it.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Medi Cruiser" )
    mod_info.set_author( "jonny_AB" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15508" )
    mod_info.put_version( "25fd96768a367597a3412d72514a2e18", "0.2_1 WIP" )
    mod_info.put_version( "6549abd125069ad10e0a682a2a3ea0ba", "0.2b WIP" )
    mod_info.set_thread_hash( "00e3fbfce2c8895aa79c01f4a6952cf5" )

    mod_info.set_desc(r"""Originally used as a medevac, this ship has gone through multiple refittings and is now the fastest cruiser this side of the Milky Way.

Replaces the Federation Cruiser-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Medi Cruiser (Type-B)" )
    mod_info.set_author( "Thunderr" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15508" )
    mod_info.put_version( "1d097d174d652317d8de9592d64fb7d7", "0.2_1 WIP" )
    mod_info.set_thread_hash( "27e3927ed6be267dd438247da74110e2" )

    mod_info.set_desc(r"""Originally used as a medevac, this ship has gone through multiple refittings and is now the fastest cruiser this side of the Milky Way.

This is an alternate layout version of jonny_AB's "Medi Cruiser".

Replaces the Federation Cruiser-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Mercenary Stealth Cruiser" )
    mod_info.set_author( "JeffTheBoardingDrone" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14692" )
    mod_info.put_version( "b206ed166df303f9fa547a278ad12256", "1.0" )
    mod_info.set_thread_hash( "25a9fbbfa77ade18b692a2ac5f6557fb" )

    mod_info.set_desc(r"""It is armed with a Hull Crusher Laser and Old Dual Lasers. It has similar power levels to the original Stealth Cruiser, and a modified layout from the Stealth Cruiser B.

It is simply a side project that I made while working on a conversion mod.

Replaces the Stealth-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Merlin Fighter" )
    mod_info.set_author( "BadgersCanSpace" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14117" )
    mod_info.put_version( "28293685c270b2aac29e8ae676072f51", "1.0 Original" )
    mod_info.put_version( "8d307297a901d28ba940ac1da35005e1", "1.0 Balance by speedoflight" )
    mod_info.put_version( "8542a19818f86d0b531beda921c281b2", "1.0 Balance by BrenTenkage" )
    mod_info.put_version( "2ed00a6867a9bca85b9c9804b64a72e1", "1.0 Balance by Badgers" )
    mod_info.put_version( "b6bddf23cb366f0ffd3d7431091cb6bb", "1.0 Silly by Gausss" )
    mod_info.set_thread_hash( "a413e3f720f8dd0a4e22facee63310d0" )

    mod_info.set_desc(r"""Designed to be as small as possible, the Merlin Fighter only has room for a cloaking system.

Its custom guns (Talon Lasers) fire very quickly but require a lot of power to run. Shots can be staggered to create a continuous barrage preventing shields coming back online, so getting the timing right is interesting.

This mod comes in several flavors:
- Original
- speedoflight's balance rejig (4 second cooldown)
- BrenTenkage's balance rejig (single gun)
- BadgersCanSpace's balance rejig (cloak at start instead of shields)
- Gausss's "Well Now You're Just Being Silly" Mod (4 guns, everything unlocked)

Replaces the Rock-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Mor-Saxum" )
    mod_info.set_author( "HalfDemon23" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11514" )
    mod_info.put_version( "e50d7504123fab5224248c8704a5bc12", "0.6" )
    mod_info.set_thread_hash( "09e54784dbf67a2d92a395f28570e039" )

    mod_info.set_desc(r"""A gigantic Rock Dreadnought that was intended to blockade the entire Rebel Fleet; however the Rebels attacked the construction base before it was completed, resulting in the Prototype limping out of the attack. While it lacks secondary systems, the Mor-Saxum has an impressive armament and unrivalled hull strength, now TRIPLE of a standard Rock Cruiser - if its systems were brought up to full strength... not even a Rebel Fleet could stand in its way.

Replaces the Rock-A ship.
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
    mod_info.set_title( "Oblivion Bubbleship" )
    mod_info.set_author( "rck_mtn_climber" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15112" )
    mod_info.put_version( "01eed2ae1686071f96258b5609fa2e43", "1.0 WIP" )
    mod_info.set_thread_hash( "6071f7df6c5bc38e80913f3a04fb013b" )

    mod_info.set_desc(r"""The bubbleship from the Oblivion movie! It is an offensive powerhouse with very good starting burst lasers and anti-ship drones (because in the movie it uses lasers and the main character repairs drones), but without the capability to use cloaking or teleporting.

Note: I am trying to work out how to limit crew members, as this ship was intended to have a small crew as its weakness; however, if there is no way to limit it then remember that this ship is intended to use its 3 starting crew so dismiss accordingly! (if you want a challenge)

Replaces the Federation Cruiser-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Obsidian Cruiser" )
    mod_info.set_author( "Kieve" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2574" )
    mod_info.put_version( "e1bcbe57235fc41546ac1470f9bd7b29", "1.2.2" )
    mod_info.set_thread_hash( "f9664bda06067dcfd72023ce4fdeb7d9" )

    mod_info.set_desc(r"""'Weapon Systems: Offline. Drone Control: Offline. Engines: Offline. Shields: twenty-five percent power. Hull breaches detected in Medical and Oxygen rooms. Fires detected in...'

The lidless green eye of a lone Engi winked out, the mechanized equivalent of a wince. The Vortex was dying around him, clouds of debris surrounding the hull where the Rebel fighter's missiles had blasted it. Streams of precious oxygen vented into empty space, giving the ship a slight spin that the damaged engines could no longer compensate for. And without its precious repair drones active, The Vortex had no hope of recovering. One Engi was no match for the destruction surrounding him. Hot air escaped his vents in something very much like a sigh, his overtaxed processors reaching one last viable option: a gray finger stabbed down, activating the ship's distress beacon. Code willing, there'd be a Federation ship out there that could at least deliver some small measure of retribution for the loss of The Vortex...

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Planet Express Ship" )
    mod_info.set_author( "Yuurg" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15595" )
    mod_info.put_version( "7d169f783afe8658d2e99cdaf04c3ab5", "1.0" )
    mod_info.set_thread_hash( "d86bb46fa2fa2c2269753ccc6116bfa2" )

    mod_info.set_desc(r"""The Planet Express ship from Futurama.

You start off with 1 Engi (Bender) and 2 Humans (Leela and Fry).

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Playable Rebel Flagship" )
    mod_info.set_author( "Baldwebby360" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=10108" )
    mod_info.put_version( "9643c9a6af40bfd7710157dd49f00390", "1.0 Rebel WIP" )
    mod_info.put_version( "0a7890230e067e260d1e617a5e92871b", "1.0 Fed WIP" )
    mod_info.set_thread_hash( "a299a691648b3e787cf7b700a669a263" )

    mod_info.set_desc(r"""A playable rebel flagship.

Replaces the Slug-A ship.
Replaces the Slug-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Potential" )
    mod_info.set_author( "5thHorseman" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15581" )
    mod_info.put_version( "726f4c222fe513d97f4d3e30ce11bf8d", "2.0" )
    mod_info.set_thread_hash( "c8418f1d4b7e28d439890d3df63aa2ee" )

    mod_info.set_desc(r"""The Potential is not not-overpowered, but an overly powered ship. It comes with 80 power to start with. How, then, is it not overpowered? Well, it doesn't come with much else.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Praying Mantis" )
    mod_info.set_author( "arcuspilot" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=13051" )
    mod_info.put_version( "12543d2a574a5431997d154a7c00d9c5", "1.1" )
    mod_info.put_version( "12543d2a574a5431997d154a7c00d9c5", "1.0" )
    mod_info.set_thread_hash( "2ec28e69a7fa32a47936c26b096a73db" )

    mod_info.set_desc(r"""It's a modified Mantis bomber. The crew are a human, an engi, and the mantis who brought the ship to the feds.

Features
- More ergonomic room layout
- Level 2 sensors
- Custom paint job
- Basic cloaking system
- Drone system
- Cool placement of weapon mounts

Replaces the Kestrel-A ship.
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
    mod_info.set_title( "The Pyro" )
    mod_info.set_author( "5thHorseman" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14597" )
    mod_info.put_version( "26449f76e88f2fb16901e3a035aa1b03", "2.0" )
    mod_info.put_version( "26449f76e88f2fb16901e3a035aa1b03", "1.0" )
    mod_info.set_thread_hash( "e0bfeed6c3498efd5657a8b5f782e663" )

    mod_info.set_desc(r"""The Pyro is my attempt at a fire/teleport combo that is not overpowered (though it packs quite a punch). However, it has almost nothing else going for it. I upped the engines because I found the beginning sectors pretty hard without them. Even so, you'll be taking a lot of damage while your boarders and fire - the only ways you can do damage - slowly take apart the enemy ship and crew. It - like the default ships - has one less power bar to start than you need for every system.

It has no (decent) way to destroy automated ships, and it is VERY susceptible to missiles. You will need to solve those problems if you want to make it to the flagship, though I HAVE successfully (and quite handily) made it to and beaten the flagship without a cloak OR drones.

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Raven Stealth Cruiser" )
    mod_info.set_author( "Thunderr" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15517" )
    mod_info.put_version( "d225d5561ce6c35ed1e14aede8196aa4", "1.0" )
    mod_info.set_thread_hash( "f2a337aadb0578a8c23267b72b836978" )

    mod_info.set_desc(r"""The Raven is a stealth ship that relies on its fast engines to get it out of tricky situations. It has level three cloak and engines, but the rest is at a bare minimum. The Raven does not include a medbay, so it's ideal to keep boarders away.

Replaces the Stealth-A ship.
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
    mod_info.set_title( "Rebel Light Cruiser" )
    mod_info.set_author( "JeffTheBoardingDrone" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14520" )
    mod_info.put_version( "d40539f455f351013819c599fbcf7171", "1.0.1" )
    mod_info.set_thread_hash( "1e0a7b6d40dc424a96cf9dc9934ef663" )

    mod_info.set_desc(r"""The ship the Federation got the secret plans from - at least, will get from. It is armed with a Hull Beam and Dual laser, along with an FTL jammer.

Replaces the Kestrel-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Replica" )
    mod_info.set_author( "TheNewbie" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14449" )
    mod_info.put_version( "f6ec6fbba0e468f27d09eda0a1e78416", "1.0" )
    mod_info.set_thread_hash( "eddd70f55612284070cc7a13259ee489" )

    mod_info.set_desc(r"""A federation fighter prototype, which basically is a reskined rebel fighter with more rooms and vital systems.

Replaces the Engi-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Revenant" )
    mod_info.set_author( "Excelious" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=16536" )
    mod_info.put_version( "f2ef91890f00e646c75cf672e6790ae4", "1.0" )
    mod_info.set_thread_hash( "88375a0ae5095ff5a761957e87342921" )

    mod_info.set_desc(r"""The Revenant is a modified Rock assault cruiser. Used as the flagship of the small paramilitary, Excelsior, the Revenant has been through many fierce battles and contains much advanced technology.

Replaces the Kestrel-A ship.
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
    mod_info.set_title( "Science Vessels" )
    mod_info.set_author( "Teodor" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15717" )
    mod_info.put_version( "53659cd7824dd4c805dfe5edb8aa0c02", "A 1.0" )
    mod_info.put_version( "dfa905e94828e2472d39f6b57458f9fd", "B 1.0" )
    mod_info.set_thread_hash( "7ccf023e02b2a5a229f2cabe0b73efcb" )

    mod_info.set_desc(r"""Science Vessel Type-A
The Needle is made for exploring unknown planetary objects.

Replaces the Kestrel-A ship.

Science Vessel Type-B
Scarecrow was heavily damaged during a pirate attack. All but one crew died and the remaining engi now only has the company of a mindless system repair drone. Because of the damage the ship has NO possibility for stealth.

Note: Don't waste your scrap trying to buy a cloak for Scarecrow!

Replaces the Kestrel-B ship.

Since FTL doesn't fully support 1x1 size rooms I recommend using 5thHorseman's "Low O2 Icons" for a better visual experience.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Space Zeppelin" )
    mod_info.set_author( "Koobi" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14040" )
    mod_info.put_version( "0d430e810f3269c463a3ac1d2d4879a9", "1.0" )
    mod_info.set_thread_hash( "b9127af5cbe9ff8c011c7b8469982a2e" )

    mod_info.set_desc(r"""This will add the iron sky space zeppelin. These ships where large ship carriers. In the movie they where towing asteroids to bombard the planet.

Replaces the Federation Cruiser-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "SR-71 Blackbird" )
    mod_info.set_author( "Ferox9" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15664" )
    mod_info.put_version( "24d588d57e0ab5083e994798b6a6421f", "1.0 WIP" )
    mod_info.set_thread_hash( "772b81e2685f87e769272d4873d225ba" )

    mod_info.set_desc(r"""The Federation has recently stumbled upon ancient USAF blueprints from a time when humans solely lived on Earth. With these blueprints, Federation scientists have recreated the SR-71 Blackbird. It has been fitted with what some might say are the most powerful engines the galaxy has ever seen, as well as an incredibly tough titanium shell. The ship needs its engines and casing because it doesn't have the power necessary to run a shield system. To help counter this large hole in its defenses, The Federation also outfitted the ship with a cloaking system. Can you handle what just might be the fastest ship in the galaxy?

Replaces the Stealth-A ship.
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

    mod_info.set_desc(r"""The primary feature of this mod is: new ships to play! All your favourite air units from Starcraft 1 and 2, ported into FTL!

The Ship mod and the UI mod are designed to be used together, but if you find the Starcrafty icons confusing you could just use the SC2Ships with the default icons.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Starcraft Terran Battlecruiser" )
    mod_info.set_author( "tokepoke" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15643" )
    mod_info.put_version( "ff3a2165c6a8ce738675764b161e6b65", "1.1" )
    mod_info.set_thread_hash( "9b44e109a300bdef4a55a44fa74c7077" )

    mod_info.set_desc(r"""The Behemoth-Class Battlecruiser is a virtual flying fortress, built to keep peace and dominance within the koprulu sector. Ship image based on the Hyperion model used in Starcraft 2's cinematics.

Replaces the Federation Cruiser-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Tengu Stealth Cruiser" )
    mod_info.set_author( "brothershogo" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=13094" )
    mod_info.put_version( "f244b440445c90181ae9a12b9a2238dc", "1.2" )
    mod_info.put_version( "f244b440445c90181ae9a12b9a2238dc", "1.1" )
    mod_info.set_thread_hash( "bcc8de20f8ae4a1ff711be2d057df902" )

    mod_info.set_desc(r"""A prototype armored stealth assault vessel, using Engi and Rockmen technology, the Tengu was designed to ambush ships with its advanced cloak and impressive barrage of lasers. It lacks shields, drones, and maneuverability, however, these systems can be bought and upgraded(except drones).

Features
- Lacks a drone system (Do not buy the drone system at the store, waste of scrap)
- Cloak can be upgraded to level 4
- 5 weapon slots
- 4 dual lasers to start
- Reinforced armor plating

Replaces the Stealth-A ship.
Replaces the Stealth-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Thanatos" )
    mod_info.set_author( "OrangeBottle and kartoFlane" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=2373" )
    mod_info.put_version( "92ab09489c224940e0fa8c566ad79e3a", "2.1" )
    mod_info.put_version( "2fb96f6e697576947e7ff443e361ae01", "2.0" )
    mod_info.set_thread_hash( "31cc4aa05d0f38697afdff2210f8f5ee" )

    mod_info.set_desc(r"""If there's anything I've had a problem with in the game, it's the Nisos. The damn thing's ugly as sin. So, this mod completely reworks the Nisos and turns it into it's brother, the Thanatos.

Features
- Starts without the Artillery Beam subsystem. (available in stores)
- Starts with a single-shield-piercing, fire-causing, personnel-damaging, 1-damage, unique beam weapon.
- Starts with two human and two engi crewmembers.
- Starts with Engi Med-bot Dispersal and Titanium Casing augments.
- It's fairly vulnerable to internal fires.

Replaces the Federation Cruiser-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Treel" )
    mod_info.set_author( "Metzelmax" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14532" )
    mod_info.put_version( "38073f6b5e4e5d6167713f8c3db49cda", "0.5a WIP" )
    mod_info.set_thread_hash( "3ae9bacd08609ff571dd46faca6b3112" )

    mod_info.set_desc(r"""These are ships from the "A Strange New Galaxy" mod.

As with my last Mod (Anterian Terminators), this is one of the several Species I made up when I was a child. The Treel were a minor species, only there as some kind of underdog enemy to give the other species someone to beat on. But this ends here. Now its their time to shine!

The Treel are fanatics who see themselves still as the freedom fighters they once were and every soldier would give happily his life for the greater good of the Treel.

Replaces the Federation Cruiser-A ship.
Replaces the Federation Cruiser-B ship.
Replaces the Zoltan-A ship.
Replaces the Zoltan-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Tsunami Class Battlecruiser" )
    mod_info.set_author( "brothershogo" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=13508" )
    mod_info.put_version( "50cab257009ddadfa94a94da6ebff263", "1.1" )
    mod_info.set_thread_hash( "d318dbc787b44255064a1603a781b424" )

    mod_info.set_desc(r"""A Ion Battlecruiser, using Zoltan, Slug, and Federation technology, the Tsunami is the pinnacle of electronic warfare technology, designed to disable entire ships with its advanced ion beam. It lacks shields, cloak, and maneuverability, however, these systems can be bought and upgraded.

Notes
- May conflict with my Tengu Type-1 mod, which disables buy-able drone system
- May conflict with any mod that modifies the Vindicator Beam
- Advanced Ion Beam replaces the Vindicator Beam
- Advanced Ion Beam can be upgraded to level 5
- Tsunami Type-1 was designed to disable ships then finish them off with lasers
- Tsunami Type-2 was designed to disable ships and then board
- Both ships equipped with Ion Shielding and Titanium System Casing augments

Replaces the Federation Cruiser-A ship.
Replaces the Federation Cruiser-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "turbonutter's Custom Ships" )
    mod_info.set_author( "turbonutter" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=3520" )
    mod_info.put_version( "569b13f51f63e2fdce5da9749a79fa46", "0.6 Beta" )
    mod_info.set_thread_hash( "4d5b7a80c3721ffd597ee0eef050424b" )

    mod_info.set_desc(r"""Replaces all the standard versions of the ships, the only loadout changed is the Millenium Falcon.

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
    mod_info.set_title( "The Vega" )
    mod_info.set_author( "TheSwiftTiger" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14929" )
    mod_info.put_version( "5e4780350488c3d4155b3814c78b376e", "1.0 WIP" )
    mod_info.set_thread_hash( "c29901040527be9101e553500b528959" )

    mod_info.set_desc(r"""...

Replaces the Kestrel-B ship.
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
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Vulture" )
    mod_info.set_author( "Thunderr" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15600" )
    mod_info.put_version( "d2c312da6b70d2f703827e0b806c0f29", "1.0" )
    mod_info.set_thread_hash( "9518c5fb3181554b9cc894e1fc98357d" )

    mod_info.set_desc(r"""The Vulture is a Runner class Federation ship stolen and customized by mercenaries to fit their needs and tastes. It starts off with most systems and good weapons, although its low reactor power partially balances this. It is meant for the "Insane Difficulty" mod, but it could be played in vanilla if you want.

Replaces the Kestrel-B ship.
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
    mod_info.set_title( "The Uz'ran Tribes" )
    mod_info.set_author( "Metzelmax" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15103" )
    mod_info.put_version( "295b5d0e09bab25c8f469943b3b72bb1", "0.2a WIP" )
    mod_info.set_thread_hash( "9511687a8443fd71139270620b568c17" )

    mod_info.set_desc(r"""These are ships from the "A Strange New Galaxy" mod.

The Uz'ran are a transdimensional species which is divided into several small tribes. The tribes fight constantly one another for the leader ship of their dimension. The losing tribes are forced to leave their own systems - even their own dimension -- in search of a new place to live.

Their ships are organic and alive with a mind of their own. Since they are originated in another dimension, they can not survive within our space... but the Uz'ran found ways to pass that border. They upgraded their ships with mechanical parts - Technology the stole from ships they attacked in our universe - in order to be able to travel in this space. They also created genetically engineered warriors with increased combat capabilities but their Telepathy suffered, compared to the abilities of their creators.

But even though the Uz'ran learned a lot from our Technology they could not adapt everything. Shields for instance.

Replaces the Slug-A ship.
Replaces the Slug-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The Xoa" )
    mod_info.set_author( "TheSwiftTiger" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15511" )
    mod_info.put_version( "f2ed4de1404ff6ee3a0f84f9fb3b89e6", "1.0" )
    mod_info.set_thread_hash( "5a57d3af96eb04fe6e1b272a0a001db0" )

    mod_info.set_desc(r"""The Xoa has a new weapon, a missile launcher called the Armageddon, and an Engi drone.

Replaces the Engi-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "The YAS-62" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11124" )
    mod_info.put_version( "ebefad606e6a66dd9e3ec4f9908e5d60", "1.1" )
    mod_info.set_thread_hash( "3760572bd40ed02cb709f83ebfaa64b1" )

    mod_info.set_desc(r"""The Federation had a whole bunch of these Kestrel Cruisers lying around, so they decided to make use of them. This new mod comes with a different room arrangement, new augmentations, and new ship graphics.

Replaces the Kestrel-A ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "YT-2000 Correlian Freighter" )
    mod_info.set_author( "Kiloku" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=15618" )
    mod_info.put_version( "07725ebbe3b531d504c3d9a3f5b60f4d", "1.0" )
    mod_info.set_thread_hash( "c60d4448b024521199e0469d4cc3edbf" )

    mod_info.set_desc(r"""The YT-2000 Light Freighter is recognized as the best of Corellian Engineering Corporation's YT Series Vessel. Its extremely powerful Hyperdrive allows it to outrun its competitors easily. The ship is easily modifiable, making it a favorite of customizers. The reactor, though, has been the main complaint from many pilots, as it never has enough juice to power everything at once.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "YTR-1335 Burnout" )
    mod_info.set_author( "nataryeahbuddy" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11321" )
    mod_info.put_version( "4616d96003fda87b39d1541873fb111d", "1.1" )
    mod_info.set_thread_hash( "33cd8b79bb658db22bcc97805cf006b7" )

    mod_info.set_desc(r"""Developed by NATAR Weapons Development Division for the sole purpose of burning out enemy crews.

Replaces the Engi-B ship.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "Balanced Arsenal Mod" )
    mod_info.set_author( "Sleeper Service" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=13920" )
    mod_info.put_version( "d18d3879fdc1ef519c689f640df2f99e", "Player Ships Addon 1.2" )
    mod_info.put_version( "0b7fcb7ab1ff32c97979d0c063ab2fe7", "Player Ships Addon 1.0" )
    mod_info.put_version( "5938cc2edc515be1d20d912764cdf978", "1.12b" )
    mod_info.put_version( "654bf376137ab0616a3d21bd77ebd834", "1.12" )
    mod_info.set_thread_hash( "bb1a53c775580ef7713304b860f16c9a" )

    mod_info.set_desc(r"""Balanced Arsenal currently adds dozens of new weapons, all of them with custom models and animations. Among them are beams, missile launchers (mostly multishot variations), bomb launchers, lasers and ion weapons (some of them electronic warfare devices that work quite differently).

The aim here was to create stuff that fits into vanilla, both visually as well as from the side of balance.

Note: "Balanced Arsenal X.XXb" Contains some weapon related custom events (might conflict with other event mods).

The "New Enemy Classes" mod will work with this if it's loaded before Balanced Arsenal.

A related mod, "Player Ships Addon", equips all player ships with BA weapons (must be loaded after Balanced Arsenal).
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
    mod_info.set_title( "Extended Ion" )
    mod_info.set_author( "Zaffre" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?p=17749" )
    mod_info.put_version( "03831481149b1c1f1de100178ff5e7d9", "1.0" )
    mod_info.set_thread_hash( "1fdc0a91ac0e0b3ac7ad7c14516a7705" )

    mod_info.set_desc(r"""Discontinued.

Extended Ion aims to add more to the arsenal of ion weapons by adding things like ion drones and lasers, and also upgraded ion blast weapons. The Engi ship starts out with some of these ion weapons and drones for a preview.

Replaces the Engi-A ship.
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
    mod_info.set_title( "Low O2 Icons" )
    mod_info.set_author( "5thHorseman" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14243" )
    mod_info.put_version( "5a61fa3e8ce46061c2c3895c82b13414", "1.0" )
    mod_info.set_thread_hash( "1a51502ae8a7aa79ce8bfcf775dd891c" )

    mod_info.set_desc(r"""This is a very small mod to address a very particular issue:
Rooms that are not 1x2, 2x1, or 2x2 don't look right when your ship runs out of air.

This mod changes the 3 graphics for "out of air" to a single icon in the upper-left corner of the room.
""")
    mod_db.add_mod(mod_info)


    mod_info = moddb.ModInfo()
    mod_info.set_title( "New Game Booster" )
    mod_info.set_author( "Bonnie Lass" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14518" )
    mod_info.put_version( "b50fa68652b04e362cfb22d079bf0730", "1.0" )
    mod_info.set_thread_hash( "c9eea596983cd64b8193a25ef3aa41fd" )

    mod_info.set_desc(r"""There are a lot of ship designs that require a bit of luck during the beginning of the game to really shine. It can really get frustrating...

When the game starts, you have the option of getting 50 scrap as a lump sum, getting a human crew member + 10 scrap, getting long ranged sensors + 20 scrap, or getting a Burst Laser Mark I.

Note: This will conflict with any mod that alters the start of the game event, and it may conflict with mods that alter Federation Space (i.e. the first sector). So if you have doubts, just put the Booster up high in your load order. If it still works, then there's no conflict.
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
    mod_info.set_title( "The Vindicator Artillery Beam" )
    mod_info.set_author( "slowriderxcorps" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14513" )
    mod_info.put_version( "15885023a319f7ce3b0dd8aed08bb5f4", "1.0" )
    mod_info.set_thread_hash( "4b26434bf2562f22702723a28b571547" )

    mod_info.set_desc(r"""Ever wondered what the Artillery Beam was going to look like initially? Well thanks to files that were left in the standard game after being scrapped, you can. This mod takes two unused files and makes a couple of minor graphical and textual tweaks in order to animate the nose of the Federation Cruiser to reflect the charge status of the Artillery Beam.
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

    mod_info.set_desc(r"""This mod replaces all of the existing planets and backgrounds and adds a lot more.
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
    mod_info.set_title( "Corpses" )
    mod_info.set_author( "harpuea" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=12367" )
    mod_info.put_version( "0e72f5a6b10c10f60d7ed9f7f1dab837", "1.0" )
    mod_info.set_thread_hash( "618e543e0f4a4c254e9348a114e95e14" )

    mod_info.set_desc(r"""This is a very small mod that adds corpses when the enemy ship explodes. You may miss it if you don't look for it at the brief moment. When an enemy ship explodes, you may see the enemy crew get sucked into the vacuum of space. The corpses are also race specific. Rebel ships will have human corpses, mantis will have mantis corpses, and so forth. Nonetheless, adds that extra little satisfaction when killing your enemies after a bitter battle.

Should be compatible with all mods, unless the mod changes enemy gibs like this one.
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

    mod_info.set_desc(r"""This mod aims to create a greater diversity in mostly graphics and some parameters of FTL.
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
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=3365" )
    mod_info.put_version( "404bc800a8fd9febfe67475454e2c9c3", "2012-10-04" )
    mod_info.set_thread_hash( "ce41a9a2d288f459d80843b4a46ff8e2" )

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
    mod_info.set_title( "Spanish GUI" )
    mod_info.set_author( "tonxabar" )
    mod_info.set_url( "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=14476" )
    mod_info.put_version( "08c1c247d13f4688a76b3863276eb405", "Final for 1.03.1" )
    mod_info.set_thread_hash( "8cad816eebe04d2f305bab090ae4b597" )

    mod_info.set_desc(r"""A Spanish localization for FTL.
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


