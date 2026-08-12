# 32ビット整数のビットを左右反転し、反転後の整数を返す
# 時間計算量：O(32)、32ビット固定なので実質 O(1) 空間計算量：O(1)

def reverse_bits(n: int) -> int:
    n &= 0xFFFFFFFF  # nを32ビットとして扱う
    result = 0       # 反転後のビットを格納する

    for _ in range(32):
        bit = n & 1                  # nの一番右のビットを取得
        result = (result << 1) | bit # 左へ1ビットずらし、一番右にbitを追加
        n >>= 1                      # 右に1ビットずらす

    return result


# 実行例
print(reverse_bits(43261596))  # 964176192