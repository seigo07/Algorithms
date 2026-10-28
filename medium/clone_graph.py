
# 元のノードと同じ値と接続関係を持つ新しいノードを作る

# DFS + Hash Map
# 1. 現在のノードをコピーする。
# 2. Hash Mapに {元ノード: コピーノード} を保存する。
# 3. 隣接ノードをDFSで再帰的にコピーする。
# 4. コピーした隣接ノードを接続する。
# 5. すでにコピー済みなら辞書から取得する（無限ループ防止）。

# 計算量: ノード数を V、接続数（辺数）を E とする
# 時間計算量：O(V + E)
# 空間計算量：O(V)


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    if not node:
        return None

    visited = {}

    def dfs(node):
        if node.val in visited:
            return visited[node.val]

        copy = Node(node.val)
        visited[node.val] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)


# 使用例
# グラフの作成
#   1--2
#   |  |
#   4--3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# グラフのクローンを作成
cloned_node1 = clone_graph(node1)

# クローンの内容を表示
print(cloned_node1.val)  # 1
for neighbor in cloned_node1.neighbors:
    print(neighbor.val)  # 2 と 4
