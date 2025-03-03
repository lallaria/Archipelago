# Super Mario 64 Hacks Setup Guide

First, create a json file using [this website](https://dnvic.com/ArchipelagoGenerator/index.html), using a .jsml file. You can get a .jsml file for a hack by loading up a hack in PJ64/Mupen64/Retroarch, opening stardisplay (or the [stardisplay client](https://github.com/DNVIC/Archipelago-StarDisplay)), and finding the layout folder in the same folder the exe file is in. You can also get premade json files here

Then, get the .jsml file from the layout folder located where the stardisplay .exe is.

Input the jsml file into the website, and fill out the requirements for everything in the hack, by clicking on the stars, cannons, caps/keys, or courses. Most hacks only really have star and key requirements, and maybe per-star cap requirements, but some hacks have more complicated requirements. If a cannon exists, select it, hit the exists checkbox, add requirements, and hit save. Same with keys/caps. Conditional requirements are a bit more confusing, but are necessary if for example you can get to a level with either the vanish cap or key 2. You'd create one conditional requirement for the vanish cap, and one for key 2, and that'll make it so only one is required.

Click on the victory text at the bottom, and put whatever is required to achieve "Victory" in the hack. As it is, this will not be automatically be achieved in the rando when you get it, since its impossible to know what constitutes victory for an arbitrary hack, but its still important since the rando makes sure that victory is possible.

Export the .json file, and put it in the same folder as the archipelago .exe (or generate.py)

Copy the template.yaml, change json_file to be the json file you just made (and if you want keys to be progressive, enable that as well), and place it in the worlds folder.

Once your world is generated, open the hack you want to play, and delete/move file 2 (this is important)

Open the rom in PJ64/Mupen/Retroarch, open the [stardisplay client](https://github.com/DNVIC/Archipelago-StarDisplay), right click -> archipelago, log in, and you should be ready to go!
