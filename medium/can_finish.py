# 前提科目に循環（ループ）があるかを調べ、全科目を履修できるか判定(トポロジカルソート BFS)
# [a, b] → 「bを先に受けないとaを受けられない」 ループがあると不可能
# 時間・空間計算量: O(V + E) V = numCourses、E = prerequisitesの数

from collections import deque

def can_finish(num_courses, prerequisites):

    graph = [[] for _ in range(num_courses)] # 履修した後に行けるコース ex. graph[[1], []] → [1]: 科目0 → 科目1、[]: 科目1 → なし
    indegree = [0] * num_courses # その科目を履修する前に終える必要がある科目数 ex. indegree = [0, 1] → 科目0は前提科目なし 科目1は前提科目が1つ（科目0）

    # pre → course のグラフを構築
    for course, pre in prerequisites:
        graph[pre].append(course)   # pre → course  [[1], [2], [3], []]
        indegree[course] += 1       # 入次数(まだ終わっていないprerequisiteの数)+1  [0, 1, 1, 1]

    # 前提科目がないindegree == 0 の科目を queue に入れる
    queue = deque( i for i in range(num_courses) if indegree[i] == 0 )
    finished = 0    # 履修済み数

    # BFS → 履修するたび、次の科目の indegree を減らす
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

    # 全科目を処理できれば True 循環があると途中で進めなくなるため False
    return finished == num_courses


num_courses = 4
prerequisites = [
    [1, 0],
    [2, 1],
    [3, 2]
]
print(can_finish(num_courses, prerequisites))  # True
