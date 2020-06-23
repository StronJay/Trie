test = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"]
]
strings = [
    "this",
    "is",
    "not",
    "a",
    "simple",
    "boggle",
    "board",
    "test",
    "REPEATED",
    "NOTRE-PEATED"
]


def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    wordsInTheBoard = {}
    visited = [[False for char in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            searchForWordsIn(board, i, j, trie.root, visited, wordsInTheBoard)
    print(wordsInTheBoard)
    return list(wordsInTheBoard.keys())


def searchForWordsIn(board, i, j, node, visited, wordsInTheBoard):
    if visited[i][j]:
        return
    char = board[i][j]
    if char not in node:
        return
    visited[i][j] = True
    node = node[char]
    if "*" in node:
        wordsInTheBoard[node["*"]] = True
    surroundingCharacters = getSurroundingCharacters(i, j, board)
    for surroundingCharacter in surroundingCharacters:
        searchForWordsIn(
            board, surroundingCharacter[0], surroundingCharacter[1], node, visited, wordsInTheBoard)
    visited[i][j] = False


def getSurroundingCharacters(i, j, board):
    surroundingCharacters = []
    if i > 0:
        surroundingCharacters.append([i - 1, j])
    if i < len(board) - 1:
        surroundingCharacters.append([i + 1, j])
    if j > 0:
        surroundingCharacters.append([i, j - 1])
    if j < len(board[0]) - 1:
        surroundingCharacters.append([i, j + 1])
    if i > 0 and j > 0:
        surroundingCharacters.append([i - 1, j - 1])
    if i > 0 and j < len(board[0]) - 1:
        surroundingCharacters.append([i - 1, j + 1])
    if i < len(board) - 1 and j > 0:
        surroundingCharacters.append([i + 1, j - 1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        surroundingCharacters.append([i + 1, j + 1])
    return surroundingCharacters


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.endSymbol] = word


print(boggleBoard(test, strings))
