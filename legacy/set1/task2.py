#!/usr/bin/python

inp = 0x1c0111001f010100061a024b53535009181c
cipher = 0x686974207468652062756c6c277320657965

output = inp ^ cipher
print hex(output)
