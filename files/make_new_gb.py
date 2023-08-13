# -*- coding: utf-8 -*-
import sys, json, os
from struct import unpack, pack

def r(f, mode="<i", size=4):
	return unpack(mode, f.read(size))[0]

# Write from chosen rom to new file
def wfc(b):
	f.seek(b)
	nf.write(bytes([r(f, "B", 1)]))

# Write from pokemon rom to new file
def wfo(b):
	of.seek(b)
	nf.write(bytes([r(of, "B", 1)]))

def calc_header_chksum(f):
	f.seek(0x134)
	x = 0
	for i in range(25):
		x -= r(f, "B", 1) + 1
	x &= 255
	return x

def calc_global_chksum(f):
	f.seek(0, os.SEEK_END)
	f_end = f.tell()
	f.seek(0)
	x = 0
	for i in range(j):
		if not i in [0x14E, 0x14F]:
			x += r(f, "B", 1)
		else:
			r(f, "B", 1)
	x &= 0xFFFF
	return x

av = sys.argv
if len(av) < 2:
	print("usage: %s <filename>" % av[0].split("/")[-1])
	exit()

f = open(av[1], "rb")

f.seek(0, os.SEEK_END)
j = f.tell()
fsize = j

of = open("source.gb", "rb") # Pokemon ROM
nf = open("output.gb" , "w+b") # Output ROM

# Making the new rom but keeping the pokemon rom header
h = 0
for i in range(fsize):
	if i in range(0x100, 0x14D):
		wfo(i)
	else:
		wfc(i)

of.close()
f.close()

f = nf

# ROM Size to 1MB
f.seek(0x148)
f.write(bytes([5]))

# Destination type to non-japanese
f.seek(0x14A)
f.write(bytes([1]))

# Checksums fix
x = calc_header_chksum(f)
f.seek(0x14D)
f.write(bytes([x]))
x = calc_global_chksum(f)
f.seek(0x14E)
f.write(bytes([x>>8]))
f.write(bytes([x&0xFF]))

# Padding
f.seek(0, os.SEEK_END)
j = f.tell()
f.write(bytes([0]*((1024**2)-j)))
