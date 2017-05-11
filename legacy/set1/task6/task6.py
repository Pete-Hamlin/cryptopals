#!/usr/bin/python

KEYSIZE = 2
KEYLEN = KEYSIZE*8
KEYS = 2

with open('6.txt') as f:           #Decode from base64
    #input = base64.b64decode(f.read()).encode("bin")
    input = f.read().decode('base64')

#print input

while KEYSIZE <= 40:
    count = 0
    l = [[]for x in range(KEYS)]
    for i in range(KEYSIZE):
        for key in range(KEYS):
            l[key].append(input[count+(KEYSIZE*key)])
        count += 1
    #print l[0][40]
    for i in range(KEYS-1):
        for j in range(KEYSIZE):
            diff = 0
            x = bin(ord(l[i][j])).replace('0b', '').zfill(8)
            y = bin(ord(l[i+1][j])).replace('0b', '').zfill(8)
            print x+" "+y
            for b in range(KEYLEN-1):
                if x[b] != y[b]:
                    diff += 1  
            out[KEYSIZE] = diff
        print ""


    KEYSIZE += 1
