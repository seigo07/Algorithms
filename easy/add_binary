# 2つの二進数文字列 a と b を、右端から桁ごとに加算し、結果を二進数文字列で返す
# 時間空間計算量：O(n) n = max(len(a), len(b))
def add_binary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1   # a、bの現在位置（右端から開始）
    carry = 0                       # 次の桁への繰り上がり
    result = []                     # 計算結果を下位桁から格納

    while i >= 0 or j >= 0 or carry:
        # 文字列の範囲外になった側は0として加算
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        total = digit_a + digit_b + carry
        result.append(str(total % 2))  # 現在の桁
        carry = total // 2             # 次の桁への繰り上がり

        i -= 1
        j -= 1

    # 下位桁から格納したため、逆順にして返す
    return "".join(reversed(result))


# テスト
print(add_binary("11", "1"))      # 100
print(add_binary("1010", "1011")) # 10101