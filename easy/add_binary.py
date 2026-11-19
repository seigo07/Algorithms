
# 2つの2進数文字列 a, b を加算し、結果を2進数文字列で返す

# 1. aを2進数として整数に変換
# 2. bを2進数として整数に変換
# 3. 2つの整数を加算
# 4. 結果を2進数文字列に変換
# 5. 先頭の0bを除去して返す

# 時間計算量: O(n + m) n = len(a)、m = len(b)
# 空間計算量: O(n + m)


def add_binary(a: str, b: str) -> str:
    num_a = int(a, 2)
    num_b = int(b, 2)
    total = num_a + num_b
    result = bin(total)
    return result[2:]


# テスト
print(add_binary("11", "1"))      # 100
print(add_binary("1010", "1011")) # 10101