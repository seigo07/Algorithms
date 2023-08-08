# トライ (「トライ」と発音) またはプレフィックス ツリーは、文字列のデータセット内のキーを効率的に格納および取得するために使用されるツリー データ構造です。
# このデータ構造には、オートコンプリートやスペルチェッカーなど、さまざまな用途があります
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# 使用例
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app"))     # True
