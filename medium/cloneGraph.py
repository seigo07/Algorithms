# このプログラムは、与えられた連結無向グラフを深いコピーとしてクローンする目的で作成されています。
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(node):
            if node.val in visited:
                return visited[node.val]

            clone = Node(node.val)
            visited[node.val] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


# インスタンスの作成
solution = Solution()

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
cloned_node1 = solution.cloneGraph(node1)

# クローンの内容を表示
print(cloned_node1.val)  # 1
for neighbor in cloned_node1.neighbors:
    print(neighbor.val)  # 2 と 4
