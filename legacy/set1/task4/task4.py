#!/usr/bin/python

file = open('4.txt')
line_count = 0

lines = file.readlines() 

#hex_data = 0x4554414f494e20534852444c55
for line in lines:
	hex_data = int(line, 16)
	dat = hex(hex_data).replace("0x", "").replace("L", "").zfill(60)
	print str(line_count)+": "+str(dat)
	line_count += 1

# Split into 8-bit ASCII
	x = 0
	y = 2
	in_arr = []
	while x < len(dat)-2: 
		dec = int(dat[x:y], 16)
		in_arr.append(dec)
#		print chr(dec)
		x += 2
		y += 2

#	print in_arr

# Run through each XOR char key
	for i in range(255):		#Actual ascii characters likely to be used
		temp = ''
		out_arr = []
		for j in range(0, len(in_arr)):
			code = in_arr[j]^i
			out_arr.append(code)	
			temp += chr(code)
		if all(y in (range(32, 126)) for y in out_arr):
			print chr(i)+': '+temp

# Line 170 single XOR encrypted with 5
