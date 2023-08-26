# -*- coding: utf-8 -*-
import sys, json, os
from struct import unpack, pack

values = {
	"CGB":{
		"128": "Game supports CGB functions, but works on old gameboys also.",
		"192": "Game works on CGB only (physically the same as 80h).",
		"0": "No CGB Flag."
	},
	"SGB":{
		"0": "No SGB functions (Normal Gameboy or CGB only game)",
		"3": "Game supports SGB functions"
	},
	"cart_type":{
		"0": "ROM ONLY",
		"1": "MBC1",
		"2": "MBC1+RAM",
		"3": "MBC1+RAM+BATTERY",
		"5": "MBC2",
		"6": "MBC2+BATTERY",
		"8": "ROM+RAM",
		"9": "ROM+RAM+BATTERY",
		"11": "MMM01",
		"12": "MMM01+RAM",
		"13": "MMM01+RAM+BATTERY",
		"15": "MBC3+TIMER+BATTERY",
		"16": "MBC3+TIMER+RAM+BATTERY",
		"17": "MBC3",
		"18": "MBC3+RAM",
		"19": "MBC3+RAM+BATTERY",
		"21": "MBC4",
		"22": "MBC4+RAM",
		"23": "MBC4+RAM+BATTERY",
		"25": "MBC5",
		"26": "MBC5+RAM",
		"27": "MBC5+RAM+BATTERY",
		"28": "MBC5+RUMBLE",
		"29": "MBC5+RUMBLE+RAM",
		"30": "MBC5+RUMBLE+RAM+BATTERY",
		"252": "POCKET CAMERA",
		"253": "BANDAI TAMA5",
		"254": "HuC3",
		"255": "HuC1+RAM+BATTERY"
	},
	"ROM":{
		"0": "32KByte (no ROM banking)",
		"1": "64KByte (4 banks)",
		"2": "128KByte (8 banks)",
		"3": "256KByte (16 banks)",
		"4": "512KByte (32 banks)",
		"5": "1MByte (64 banks)- only 63 banks used by MBC1",
		"6": "2MByte (128 banks) - only 125 banks used by MBC1",
		"7": "4MByte (256 banks)",
		"82": "1.1MByte (72 banks)",
		"83": "1.2MByte (80 banks)",
		"84": "1.5MByte (96 banks)"
	},
	"RAM":{
		"0": "None",
		"1": "2 KBytes",
		"2": "8 Kbytes",
		"3": "32 KBytes (4 banks of 8KBytes each)"
	},
	"dest":{
		"0": "Japanese",
		"1": "Non-Japanese"
	}
}



def r(f, mode="<i", size=4):
	return unpack(mode, f.read(size))[0]

av = sys.argv
if len(av) < 2:
	print("usage: %s <filename>" % av[0].split("/")[-1])
	exit()

f = open(av[1], "rb")

f.seek(0x100)

entry_point = "%.8X" % r(f, ">i")

nin_logo = ""
for i in range(0x134 - 0x104):
	nin_logo += "%X" % abs(r(f, "B", 1))

title_raw = []
for i in range(0x144 - 0x134):
	title_raw.append(r(f, "B", 1))
title = "".join([chr(i) for i in title_raw])

manuf_code = title_raw[11:-1]
cgb_flag = title_raw[-1]
new_license_code = b"".join([r(f, "c", 1) for i in range(2)])
sgb_flag = r(f, "B", 1)
cart_type = r(f, "B", 1)
rom_size = r(f, "B", 1)
ram_size = r(f, "B", 1)
dest = r(f, "B", 1)
old_license_code = r(f, "B", 1)
version = r(f, "B", 1)

f.seek(0x134)

x = 0
for i in range(25):
	x -= r(f, "B", 1) + 1
x &= 255
h_check = x
# f.seek(0x14D)
h_sum = r(f, "B", 1)

f_sum = r(f, ">H", 2)

f.seek(0, os.SEEK_END)
j = f.tell()
fsize = j
f_check = 0
f.seek(0)
for i in range(j):
	if not i in [0x14E, 0x14F]:
		f_check += r(f, "B", 1)
	else:
		r(f, "B", 1)
f_check &= 0xFFFF


print("Entry Point:", entry_point)
print("Logo:", nin_logo)
# print title_raw
print("Title:", title)
print("Manufacturer Code:", "".join([chr(i) for i in manuf_code]))
print("CGB Flag:", "%X -" % cgb_flag, values["CGB"][str(cgb_flag)] if str(cgb_flag) in values["CGB"] else "Unknown")
print("New License Code:", new_license_code)
print("SGB Flag:", "%X -" % sgb_flag, values["SGB"][str(sgb_flag)] if str(cgb_flag) in values["SGB"] else "Unknown")
print("Cartridge Type:", "%X -" % cart_type, values["cart_type"][str(cart_type)] if str(cart_type) in values["cart_type"] else "Unknown")
print("ROM Size:", "%X -" % rom_size, values["ROM"][str(rom_size)] if str(rom_size) in values["ROM"] else "Unknown")
print("RAM Size:", "%X -" % ram_size, values["RAM"][str(ram_size)] if str(ram_size) in values["RAM"] else "Unknown")
print("Destination:", "%X -" % dest, values["dest"][str(dest)] if str(dest) in values["dest"] else "Unknown")
print("Old License Code: %X" % old_license_code)
print("Version:", version)
print("Calculated Header Checksum:", "%X" % h_check)
print("File Header Checksum:", "%X" % h_sum)
print("Calculate Global Checksum:", "%X" % f_check)
print("File Global Checksum:", "%X" % f_sum)
