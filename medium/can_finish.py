
# 前提科目に循環（ループ）があるかを調べ、全科目を履修できるか判定(トポロジカルソート + BFS（Kahn法）)
# [a, b] → 「bを先に受けないとaを受けられない」 ループがあると不可能

# - graph：各コースの次に履修できるコース ex. 0の場合次に履修できるのは1 [[1], []]
# - indegree：各コースに必要な前提科目の数 ex. 0の前提条件は0個 1の前提条件は1個 [0, 1]
# - queue：履修可能なコース（前提条件が0になったコース） ex. deque([0])
# - count：履修完了したコース数 ex. 0 → 1 → 2

# 1. prerequisites から graph と indegree を作成
# 2. indegree == 0 のコースを queue に追加
# 3. BFSでコースを取り出し、次のコースの indegree を減らす
# 4. indegree == 0 になったコースを queue に追加
# 5. count == numCourses なら True

# 時間・空間計算量: O(V + E) V = numCourses、E = prerequisitesの数

from collections import deque

def can_finish(num_courses, prerequisites):

    # 1. グラフと入次数を初期化
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    # 2. グラフと入次数を作成
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    # 3. 入次数0のコースをキューに追加
    queue = deque( i for i in range(num_courses) if indegree[i] == 0 )
    finished = 0    # 履修済み数

    # 4. BFSで履修 → 次の科目の indegree を減らす
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
