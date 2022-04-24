""""
1st Question.
You decide to create a substitution cipher. The cipher alphabet is based on a key shared amongst those of your friends who don't mind spoilers.
Suppose the key is:
"The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!".
We use only the unique letters in this key to set the order of the characters in the substitution table.
T H E Q U I C K O N Y X G B L R A S W D J M P V Z F
(spaces added for readability)
We then align it with the regular alphabet:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T H E Q U I C K O N Y X G B L R A S W D J M P V Z F
Which gives us the substitution mapping: A becomes T, B becomes H, C becomes E, etc.
Write a function that takes a key and a string and encrypts the string with the key.
Example:
key = "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!"
encrypt("It was all a dream.", key) -> "Od ptw txx t qsutg."
encrypt("Would you kindly?", key) -> "Pljxq zlj yobqxz?"
Complexity analysis:
m: The length of the message
k: The length of the key

"""


class SubstitutionCipher:
    def __init__(self,
                 encode="The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!",
                 encryptWord=None):
        self.convertString = encode
        self.uniqueList = []
        self.alignHash = {}
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.encryptWord = encryptWord

    def convert_unique_string(self) -> list:
        for index in range(len(self.convertString)):
            if self.convertString[index].isalpha():
                temp = self.convertString[index].lower()
                if temp not in self.uniqueList:
                    self.uniqueList.append(self.convertString[index].lower())
        return self.uniqueList

    def align_unique_string(self) -> dict:
        for index in range(len(self.uniqueList)):
            self.alignHash[self.alphabet[index].lower()] = self.uniqueList[index]
        return self.alignHash

    def decode_any_string(self) -> str:
        res = []
        for char in self.encryptWord:
            if char.isupper():
                temp = self.alignHash[char.lower()]
                res.append(temp.upper())
            elif char.isalpha():
                res.append(self.alignHash[char])
            else:
                res.append(char)
        return "".join(res)


decodeSentences = ["It was all a dream.", "Would you kindly?"]
for eachSentence in decodeSentences:
    decodeString = SubstitutionCipher(encryptWord=eachSentence)
    decodeString.convert_unique_string()
    decodeString.align_unique_string()
    print(decodeString.decode_any_string())
