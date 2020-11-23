# Header Swap GB

## Description

This is a series of scripts designed to take any normal GameBoy ROM, and modify it's header in order to make it playable in Pokémon Stadium's "GB Tower". While normally GB Tower cannot load anything outside of Pokémon games, it's possible to get it to load something else by modifying the header of the ROM itself. 

## Requirements

- Python 2.x
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
