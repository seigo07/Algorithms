# 配列内で、要素数の半分より多く出現する「多数派要素」を返す
# 時間計算量：O(n) 空間計算量：O(1)

# Boyer–Moore多数決アルゴリズムを使用
# 1.countが0なら、現在の要素を新しい候補にする。
# 2.現在の要素が候補と同じならcountを増やす。
# 3.異なるならcountを減らし、候補と異なる要素を相殺する。
# 4.最後まで残った候補が多数派要素になる。

def majority_element(nums):
    candidate = None  # 過半数要素の候補
    count = 0         # 候補と他の要素を相殺した残数

    for num in nums:
        # 残数が0なら、現在の要素を新しい候補にする
        if count == 0:
            candidate = num

        # 候補と同じなら加算、異なるなら相殺
        count += 1 if num == candidate else -1

    return candidate


# テストコード
print(majority_element([3, 2, 3]))           # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2