best = "ndbajwhfawkjljkfaopwdlaawjk dawkj awjkawkfjhkawk ahjwkjad jadfljawd"
sest = ["abc", "akwbc", "awbc", "abafac", "ajjfbc", "abac", "jadfl"]


# def obnsTimeandO1Space(bigString, smallStringsArray):
#     return [isInBigString(bigString, string) for string in smallStringsArray]


# def isInBigString(bigString, string):
#     for i in range(len(bigString)):
#         if i + len(string) > len(bigString):
#             break
#         if isInBigStringHelper(bigString, string, i):
#             return True
#     return False


# def isInBigStringHelper(bigString, string, currentIdx):
#     leftBigStringIdx = currentIdx
#     rightBigStringIdx = currentIdx + len(string) - 1
#     leftStringIdx = 0
#     rightStringIdx = len(string) - 1
#     while leftBigStringIdx <= rightBigStringIdx:
#         if bigString[leftBigStringIdx] != string[leftStringIdx] or bigString[rightBigStringIdx] != string[rightStringIdx]:
#             return False
#         leftBigStringIdx += 1
#         rightBigStringIdx -= 1
#         leftStringIdx += 1
#         rightStringIdx -= 1
#     return True


# def obSquaredPlusnsTimeAndObSquaredPlusn(bigString, smallStringsArray):
#     modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
#     # print(modifiedSuffixTrie.root)  # Now that's a trie
#     return [modifiedSuffixTrie.contains(string) for string in smallStringsArray]


# class ModifiedSuffixTrie:
#     def __init__(self, string):
#         self.root = {}
#         self.populateSuffixTrie(string)

#     def populateSuffixTrie(self, string):
#         for i in range(len(string)):
#             node = self.root
#             for j in range(i, len(string)):
#                 letter = string[j]
#                 if letter not in node:
#                     node[letter] = {}
#                 node = node[letter]

#     def contains(self, string):
#         node = self.root
#         for letter in string:
#             if letter not in node:
#                 return False
#             node = node[letter]
#         return True
best1 = "this is a big string"
sest1 = ["this", "yo", "is", "a", "bigger", "string", "sappa"]

def multiStringSearch(bigString, smallStringsArray):
    trie = Trie()
    for string in smallStringsArray:
        trie.insert(string)
        print(string, trie.root)
    containedStrings = {}
    for i in range(len(bigString)):
        node = trie.root
        print("RIGHT HERE!!!!!!!!!!!",i, node)
        for j in range(i, len(bigString)):
            letter = bigString[j]
            if letter not in node:
                print("BROKE",i, j)
                break
            node = node[letter]
            if trie.endSymbol in node:
                print("BUT NOT ACTUALLY:", i, j)
                containedStrings[node[trie.endSymbol]] = True
                print(containedStrings)
    print(containedStrings, smallStringsArray)
    return [string in containedStrings for string in smallStringsArray]


# def findSmallStringsIn(string, i, trie, containedStrings):
        


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "$"

    def insert(self, string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = string # this is important now!!!!


print(multiStringSearch(best1, sest1))
