# 文字列の配列から、すべての文字列に共通する最長の先頭部分（共通接頭辞）を返す
# 時間計算量：O(n × m)
# 空間計算量：O(m + n) 戻り値のprefixが最大m文字 比較用のcharsとsetが最大n要素
def longest_common_prefix(strs):
    prefix = ""

    # 各文字列の同じindexにある1文字をチェック ex. fff, lll, ooi
    for chars in zip(*strs):
        if len(set(chars)) != 1:  # 文字が一致しなければ終了 ex. fff = 1, ooi = 2
            break
        prefix += chars[0]

    return prefix


# 実行例
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # fl