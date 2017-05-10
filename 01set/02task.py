from cryptopals import *

string1="1c0111001f010100061a024b53535009181c" # b'hit the bull\'s eye
string2="686974207468652062756c6c277320657965"

print(Crypto.xor(string1, string2)) # b'the kid don\'t play
