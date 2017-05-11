from cryptopals import *

crypt = Crypto()
attempts = string.ascii_letters+string.digits+string.punctuation
high_score = 0
high_letter = ''
high_string = ''
high_line = 0

with open("04.txt", "r") as file:
    for line in file.readlines():
        # print(line.rstrip()) #Debug
        for i in range(len(attempts)):
            f = crypt.single_xor(line.rstrip(), attempts[i])
            if all(c in string.printable for c in f):
                # print(crypt.scorer(f))
                if (crypt.scorer(f) > high_score):
                    high_score = crypt.scorer(f)
                    high_letter = attempts[i]
                    high_string = f.rstrip()
                    high_line = line

print(high_letter)
print(high_string)
print(high_score)
print("Line: "+line)
