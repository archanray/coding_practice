"""
This code base implements an autocomplete function using python
Notably, it saves prior searches and uses them when querying new
phrases/words/subwords
"""

class TrieNode():
    def __init__(self):
        # initialize single node for trie
        self.children = {}
        self.last = False

class Trie():
    def __init__(self):
        # initialize trie structure
        self.root = TrieNode()

    def formTrie(self, keys):
        # forms a trie structure with given set of strings
        for key in keys:
            self.insert(key)

    def insert(self, key):
        # insert key into a trie if it doesn't already exit
        # if key is a prefix of a trie node, marks it as a 
        # leaf node
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def suggestsRec(self, node, word):
        # method to recursively traverse the trie and return
        # the whole word
        if node.last:
            print(word)

        for a, n in node.children.items():
            self.suggestsRec(n, word+a)

    def printAutoSuggestions(self, key):
        # returns all the workds in the trie whose common prefix
        # is the given key and thus lists all suggestions for 
        # autocomplete
        node = self.root

        for a in key:
            # no string in the Trie has this prefix
            if not node.children.get(a):
                return 0
            node = node.children[a]

        # if prefix is present as a word, but no subtree
        # below the last matching node
        if not node.children:
            return -1

        self.suggestsRec(node, key)
        return 1

class dataStructure():
    def initializeTrie(self):
        # keys to form the trie structure.
        keys = ["hello", "dog", "hell", "cat", "a",
            "hel", "help", "helps", "helping"]  
        # creating trie object
        t = Trie()
         
        # creating the trie structure with the
        # given set of strings.
        t.formTrie(keys)
        # store the trie in self
        self.t = t

    def searchKey(self, key):
        # autocompleting the given key using
        # our trie structure.
        comp = self.t.printAutoSuggestions(key)
         
        if comp == -1:
            print("String matches exactly, nothing else to show")
        elif comp == 0:
            self.t.insert(key)
            print("String doesn't appear in the dict, adding to dict") 
        return


def main():
    # main driver code
    queryModel = dataStructure()
    queryModel.initializeTrie()

    # first key for autocomplete suggestions.
    key = "b"
    queryModel.searchKey(key)
    print("----------------")

    key = "a"
    queryModel.searchKey(key)
    print("----------------")

    key = ""
    queryModel.searchKey(key)
    print("----------------")

    key = "hell"
    queryModel.searchKey(key)
    print("----------------")

    key = "b"
    queryModel.searchKey(key)
    print("----------------")

    key = "ba"
    queryModel.searchKey(key)
    print("----------------")    

    key = "baba"
    queryModel.searchKey(key)
    print("----------------")

    key = "b"
    queryModel.searchKey(key)
    print("----------------")

    key = "ba"
    queryModel.searchKey(key)
    print("----------------")


    return

if __name__ == "__main__":
    main()
     
