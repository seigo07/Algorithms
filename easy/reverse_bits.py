
'''
与えられた32ビットの整数の各ビットを逆順に並べ替えて、新しい整数として返す
'''


def reverse_bits(n):
    result = 0  # 結果用の空の整数を初期化
    for _ in range(32): # 32ビットすべてに対して処理
        # resultを左に1ビットシフトして空きビットを作る
        result <<= 1
        # nの最下位ビットを取り出してresultに加える
        result |= n & 1
        # nを右に1ビットシフトして次のビットに進む
        n >>= 1
    return result

# 実行例（例：43261596 -> 964176192）
input_num = 43261596
output = reverse_bits(input_num)
print(f"Input: {input_num}, Output: {output}")
