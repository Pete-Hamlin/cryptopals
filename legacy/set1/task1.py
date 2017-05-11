#!/usr/bin/python

#Task 1

# Encoder lookup table
lut = [
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z', '0', '1', '2', '3', 
'4', '5', '6', '7', '8', '9', '+', '/'
]

hexi = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d		#Insert hex hexi here
print 'Hex: ' + str(hex(hexi))
output = ''

BASE = 64		# Encoder base value
while (hexi > 0):
	temp = hexi % BASE
	hexi = (hexi-temp)/BASE
	code = lut[temp]
	#print code
	output = code + output
print 'Output: ' + output
