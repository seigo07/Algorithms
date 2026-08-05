# 整数nを2進数で表したときに、1になっているビットの個数（Hamming Weight） を返す
# 時間計算量：O(log n) ビット数（約32回）だけループ
# ex. n = 11の場合、右シフト毎に 1011 (11) → 0101 (5) → 0010 (2) → 0001 (1) → 0000 (0)
# 空間計算量：O(1)

def hamming_weight(n: int) -> int:
    count = 0

    while n:
        count += n & 1   # 最下位ビットが1なら加算
        n >>= 1          # 1ビット右へシフト

    return count


print(hamming_weight(11))         # 3
print(hamming_weight(128))        # 1
print(hamming_weight(2147483645)) # 30