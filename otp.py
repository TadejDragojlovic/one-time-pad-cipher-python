from secrets import choice # Used to to generate truly random values
from string import ascii_lowercase # Lowercase alphabet

class OTP:
    def __init__(self, message):
        self.message = message
        self.pad = "".join([choice(ascii_lowercase) for x in range(len(message))])
        self.whitespace_positions = []
        self.capitalized_positions = []
        self.has_whitespace = False
        self.message = self.message.lower()

        if self.message.find(" ")>0:
            self.has_whitespace = True
            for i, char in enumerate(self.message):
                if char == " ":
                    self.message = self.message.replace(" ", "") # Delete the spaces if there are any

        # /////// ADD AN ERROR IF LENGTH ISN'T EQUAL //////////

    def encrypt(self):
        ciphertext = ""
        for i, char in enumerate(self.message):
            curr = (ord(char)-97)+(ord(self.pad[i])-96)
            if curr > 26:
                curr %= 26
            ciphertext += chr(curr+96)

        return ciphertext

    def decrypt(self):
        decipheredtext = ""
        for i, char in enumerate(self.encrypt()):
            curr = (ord(char)-96)-(ord(self.pad[i])-96)
            if curr > 26 or curr < 0:
                curr %= 26
            curr += 1
            decipheredtext += chr(curr+96)
        return decipheredtext

if __name__ == "__main__":
    otp = OTP('This is a test')

    print("\n")
    print(f"THIS IS THE SECRET PAD {otp.pad}")
    print(otp.encrypt())
    print(otp.decrypt())
    print("\n")
