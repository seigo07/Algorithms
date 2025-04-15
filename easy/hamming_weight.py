
'''

正の整数 n に対して、その2進数表現中に含まれる 1 の数（= ビットが立っている数）をカウントする

1.bin(n) を使って n を2進数文字列に変換（例: bin(5) → '0b101'）
2.count('1') を使って '1' の個数（ハミング重み）をカウント
3.結果を返す。例: n = 5 (0b101) → 結果は2

'''


def hamming_weight(n):
    return bin(n).count('1')

# テストケース
test_values = [5, 7, 8, 15, 1023]
for n in test_values:
    print(f"{n} のハミング重み（1の個数）: {hamming_weight(n)}")
