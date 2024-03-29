# Header Swap GB

## Description

This is a series of scripts designed to take any normal GameBoy ROM, and modify its header in order to make it playable in Pokémon Stadium's "GB Tower". While normally GB Tower cannot load anything outside of Pokémon games, it's possible to get it to load something else by modifying the header of the ROM itself. For it in action, be sure to check out [my video here](https://www.youtube.com/watch?v=jcn5XGW1on8)

## Requirements

- Python 3.x
- Clean Pokémon Blue (UE) ROM (MD5: 50927E843568814F7ED45EC4F944BD8B)
- Pokémon Stadium (U)
- Rewritable GameBoy cartridge

## Usage

- Place a clean ROM of Pokemon Blue in the same folder as the Python scripts
- Rename the Pokemon ROM to "source.gb"
- Open the folder in Command Prompt
 -Type either: 
py make_new_gb.py "(your rom here).gb"
or
make_new_gb.py "(your rom here).gb"
- Write "output.gb" to your cartridge

## Issues

- GameBoy Color games DO NOT work
- Games cannot save as the header also contains code that dictates how games save, that gets overwritten
- Pocket Monsters Stadium and Pokémon Stadium 2 do not work with this, only Stadium 1 (international)

## Credits

[Angrevol](https://twitter.com/Angrevol) for helping with the code  
[Mezmorize](https://www.youtube.com/channel/UCgX4JmHxh49Sk9yr-QJdZvw) for first making this public  
[Stop Skeletons from Fighting](https://www.youtube.com/channel/UC5Xeb9-FhZXgvw340n7PsCQ) for being the reason why I began looking into this
