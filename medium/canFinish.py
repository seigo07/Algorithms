# 各コースをノードとし、prerequisitesをエッジとして考えると、すべてのコースを終了できるかどうかを判断する問題は、有向グラフに循環（サイクル）が存在しないかどうかを判断する
class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        # グラフを構築
        for course, pre in prerequisites:
            graph[course].append(pre)

        def dfs(course):
            if visited[course] == -1:  # 循環が検出された場合
                return False
            if visited[course] == 1:  # 既に訪問され、サイクルがないことが確認された場合
                return True
            visited[course] = -1  # 探索中のノードをマーク
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited[course] = 1  # すべての隣接ノードを訪問した後、訪問済みとしてマーク
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


# インスタンスの作成
solution = Solution()

# 使用例
numCourses = 2
prerequisites = [[1,0]]
print(solution.canFinish(numCourses, prerequisites))  # True
