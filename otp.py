from secrets import choice # Used to to generate truly random values

class OTP:
    def __init__(self, message, pad):
        self.message = message
        self.pad = pad
        self.whitespace_positions = []
        self.capitalized_positions = []

        "Hello World"
        "ABCDE FGHIJ"


        for i, char in enumerate(self.message): # Save positions of capital letters for later
            if char.isupper():
                self.capitalized_positions.append(i)

        self.message = self.message.lower()
        self.pad = self.pad.lower()

        if self.message.find(" ")>0:
            for i, char in enumerate(self.message):
                if char == " ":
                    self.whitespace_positions.append(i)
                    # Used to save space positions, so that later when decrypting the message, spaces can be added back
                    self.message = self.message.replace(" ", "") # Delete the spaces

        print(self.message)
        # /////// ADD LATER IF NEW TRIMMED MESSAGE IS NOT EQUAL TO PAD IN LENGTH, THROW AN ERROR //////////

    def encrypt(self):
        ciphertext = ""

        for i, char in enumerate(self.message):
            curr = (ord(char)-96)+(ord(self.pad[i])-96)
            if curr > 26:
                curr %= 26
            curr -= 1
            ciphertext += chr(curr+96)

        return ciphertext

    def decrypt(self):
        pass

if __name__ == "__main__":
    otp = OTP('Hello World', 'ABCDEFGHIJ')

    ciphertext = otp.encrypt()
    print(ciphertext)
    # print(otp.decrypt())
