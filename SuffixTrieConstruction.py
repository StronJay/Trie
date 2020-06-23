class SuffixTree:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "$"
        self.populateSuffixTrieFrom(string)


    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            dictionary = self.root
            for j in range(i, len(string)):
                key = string[j]
                if key not in dictionary:
                    dictionary[key] = {}
                dictionary = dictionary[key]
            dictionary[self.endSymbol] = True #Can be changed

    def contains(self, string):
        dictionary = self.root
        for key in string:
            if key not in dictionary:
                return False
            dictionary = dictionary[key]
        return self.endSymbol in dictionary

test = SuffixTree("ThisIsATest")
print(test.root)