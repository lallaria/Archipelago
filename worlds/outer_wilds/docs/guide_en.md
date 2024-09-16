# Outer Wilds Setup Guide

Prerequisites
Make sure you have Outer Wilds installed
Install the Outer Wilds Mod Manager
Install the core Archipelago tools (at least version 0.4.4)
Go to the Releases page of this repository and look at the latest release. There should be three files: A .zip, an .apworld and a .yaml. Download the .apworld and the .yaml.
Archipelago tools setup
Go to your Archipelago installation folder. Typically that will be C:\ProgramData\Archipelago.
Put the outer_wilds.apworld file in Archipelago\lib\worlds\.
Put the Outer.Wilds.yaml file in Archipelago\Players. You may leave the .yaml unchanged to play on default settings, or use your favorite text editor to read and change the settings in it.
I've never used Archipelago before. How do I generate a multiworld?
Let's create a randomized "multiworld" with only a single Outer Wilds world in it.

Make sure Outer.Wilds.yaml is the only file in Archipelago\Players (subfolders here are fine).
Double-click on Archipelago\ArchipelagoGenerate.exe. You should see a console window appear and then disappear after a few seconds.
In Archipelago\output\ there should now be a file with a name like AP_95887452552422108902.zip.
Open https://archipelago.gg/uploads in your favorite web browser, and upload the output .zip you just generated. Click "Create New Room".
The room page should give you a hostname and port number to connect to, e.g. "archipelago.gg:12345".
For a more complex multiworld, you'd put one .yaml file in the \Players folder for each world you want to generate. You can have multiple worlds of the same game (each with different settings), as well as several different games, as long as each .yaml file has a unique player/slot name. It also doesn't matter who plays which game; it's common for one human player to play more than one game in a multiworld.

Modding and Running Outer Wilds
In the Outer Wilds Mod Manager, click on "Get Mods", search for "Archipelago Randomizer", and once you see this mod listed, click the install button to the right of it (if you were wondering about the .zip file we didn't download earlier, that's what the Mod Manager is installing).
(Optional: Other Mods) Some other mods that I personally like to play with, and that this randomizer is compatible with, include: "Clock" (exactly what it sounds like), "Cheat and Debug Menu" (for its fast-forward button), and "Suit Log" (access the ship log from your suit).
Now click the big green Run Game button. Note that you must launch Outer Wilds through the Mod Manager in order for the mods to be applied; launching from Steam won't work.
Once you're at the main menu of Outer Wilds itself, click "New Random Expedition", and you will be asked for connection info such as the hostname and port number. Unless you edited Outer.Wilds.yaml (or used multiple .yamls), your slot/player name will be "Hearthian1". And by default, archipelago.gg rooms have no password.
