
# 文字列を保存し、次の3つの操作を実現する
# 基本アルゴリズム：Trie（木構造）＋ Hash Map（辞書）

# - insert(word)：単語を登録
# - search(word)：単語が完全一致するか確認
# - startsWith(prefix)：指定した文字列で始まる単語が存在するか確認

# 時間計算量: L = 入力文字数 O(L)
# 空間計算量: insert O(L) search, startsWith O(1)


class Trie:
    def __init__(self):
        self.root = {}  # Trieの起点

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}  # 文字がなければ追加
            node = node[char]    # 次の階層へ移動

        node["#"] = True  # 単語の終端を記録

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node:
                return False
            node = node[char]

        return "#" in node  # 単語の終端か確認

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True  # prefixがすべて存在


# Example 1
trie = Trie()
trie.insert("apple")

print(trie.search("apple"))      # True
print(trie.search("app"))        # False
print(trie.startsWith("app"))    # True

trie.insert("app")
print(trie.search("app"))        # True
