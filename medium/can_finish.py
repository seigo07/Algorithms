
from collections import deque

# 授業の依存関係から全コースを最後まで履修できるか判定(トポロジカルソート BFS)
# [a, b] → 「bを先に受けないとaを受けられない」 ループがあると不可能
# 時間・空間計算量: O(コース数 + prerequisite数)　各ノードと辺を1回ずつ見る
def can_finish(num_courses, prerequisites):

    graph = [[] for _ in range(num_courses)] # 次に行けるコース(各コースの次のコース一覧)
    indegree = [0] * num_courses # prerequisite数

    # グラフ構築
    for course, pre in prerequisites:
        graph[pre].append(course)   # pre → course  [[1], [2], [3], []]
        indegree[course] += 1       # 入次数(まだ終わっていないprerequisiteの数)+1  [0, 1, 1, 1]

    queue = deque() # 今すぐ履修可能(prerequisiteが0のコースを入れる)   [0]
    for i in range(num_courses):
        if indegree[i] == 0:
            queue.append(i)
    
    finished = 0    # 履修済み数

    # BFS → prerequisiteを減らしていく
    while queue:

        # 先頭コースを履修
        cur = queue.popleft()
        finished += 1

        # 次のコースを見る
        for next_course in graph[cur]:

            # prerequisiteを1減らす
            indegree[next_course] -= 1

            # prerequisiteが0なら履修可能
            if indegree[next_course] == 0:
                queue.append(next_course)

    # 全部履修できたか判定
    return finished == num_courses


num_courses = 4
prerequisites = [
    [1, 0],
    [2, 1],
    [3, 2]
]
print(can_finish(num_courses, prerequisites))  # True
