from cryptopals import *

KEY='ICE'
string0="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
crypt = Crypto()

crypt.repeat_key(string0, KEY)
