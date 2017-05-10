from cryptopals import *

string0="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# Crypto.single_xor(string0) # Returns every a-zA-Z XOR
# Key is X: b'Cooking MC's like a pound of bacon'

crypt = Crypto()
attempts = string.ascii_letters
high_score = 0
high_letter = ''
high_string = ''

# Run through the alphabet and try a-zA-Z as the key, sequentially replacing the high score each time if it is beaten
for i in range(len(attempts)):
    f = crypt.single_xor(string0, attempts[i])
    if (crypt.scorer(f) > high_score):
        high_score = crypt.scorer(f)
        high_letter = attempts[i]
        high_string = f

# Print out letter with highest score, along with phase and total score
print(high_letter)
print(high_string)
print(high_score)
