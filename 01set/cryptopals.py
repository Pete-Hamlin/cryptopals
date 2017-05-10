import base64
import string

class Crypto:
    letters = string.ascii_lowercase + ' '
    score = {
                'e': 12.702, 't': 9.056, 'o': 7.507, 'a': 8.167, 'i': 6.966,
                'n': 6.749, 's': 6.327, 'h': 6.094, 'r': 5.987, 'd': 4.253,
                'l': 4.025, 'c': 2.782, 'u': 2.758, 'm': 2.406, 'w': 2.360,
                'f': 2.228, 'g': 2.015, 'y': 1.974, 'p': 1.929, 'b': 1.492,
                'v': 0.978, 'k': 0.772, 'j': 0.153, 'x': 0.150, 'q': 0.095,
                'z':0.074, ' ': 15.000
             }
    def to_64(x):
        a = bytearray.fromhex(x)
        a = base64.b64encode(a)
        return a
    def xor(x, y):
        if len(x) != len(y):
            print("Buffers do not match!")
        else:
            a = bytearray.fromhex(x)
            b = bytearray.fromhex(y)
            for i in range(len(a)):
                b[i] ^= a[i]
            return b
    def single_xor(self, x, y):
        a = bytearray.fromhex(x)
        b = ord(y)
        # b.extend(map(ord, self.letters))
        for i in range(len(a)):
            a[i] ^= b
        # print(chr(b) + ": " + a.decode("utf-8"))
        return a.decode("utf-8")    # Debug
    def scorer(self, s):
        string_score = 0
        for i in range(len(self.letters)):
            count = s.count(self.letters[i])
            string_score += self.score[self.letters[i].lower()]*count
        # print(string_score)
        return string_score
