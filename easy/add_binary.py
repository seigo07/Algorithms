
# 2つの2進数文字列 a と b を加算して、結果を2進数の文字列として返す


def add_binary(a: str, b: str) -> str:
    # 目的：2進数文字列 a, b を加算して2進数文字列を返す
    
    result = []  # 加算結果を格納するリスト
    carry = 0    # 繰り上がり用の変数
    
    i, j = len(a) - 1, len(b) - 1  # 各文字列の末尾（最下位ビット）からスタート
    
    # どちらかのビットが残っているか、繰り上がりがあれば続行
    while i >= 0 or j >= 0 or carry:
        # 各ビットと繰り上がりを合計
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        
        # 結果に現在のビットを追加（total % 2で現在のビット値）
        result.append(str(total % 2))
        
        # 繰り上がりを更新（total // 2）
        carry = total // 2
    
    # ビット列を反転して文字列に変換
    return ''.join(reversed(result))


# 実行例
a = "1010"
b = "1011"
print(add_binary(a, b))  # 出力: "10101"
