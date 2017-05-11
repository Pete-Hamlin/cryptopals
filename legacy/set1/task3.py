#!/usr/bin/python

hex_data = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
#hex_data = int("ETAOIN SHRDLU".encode("hex"), 16)
dat = hex(hex_data)
print dat

# Split into 8-bit ASCII
x = 2
y = 4
arr =[]
while x < len(dat)-1: 
	dec = int(dat[x:y], 16)
	arr.append(dec)
#	print chr(dec)
	x += 2
	y += 2

print arr

# Run through each XOR char key
for i in range(255):
	temp = ''
	for j in range(0, len(arr)):	
	#	temp = ''
		temp += chr(arr[j]^i)
	print chr(i)+': '+temp

# Encoding key is X
