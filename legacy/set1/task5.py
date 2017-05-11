#!/usr/bin/python

key = 'ICE'

#hex_data = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
hex_data = int("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode("hex"), 16)
dat = hex(hex_data).replace("0x", "").replace("L", "")
#print dat

# Split into 8-bit ASCII
x = 0
y = 2
arr =[]
while x < len(dat)-1: 
	dec = int(dat[x:y], 16)
	arr.append(dec)
#	print chr(dec)
	x += 2
	y += 2

#print arr
i = 0
j = 0
crypt = ''
# Run through each XOR char key
while i <len(arr):
	temp = chr(arr[i]^ord(key[j]))
	crypt += temp
	i += 1
	j += 1 if j < (len(key) - 1) else -2
#	print j
print crypt.encode("hex")
