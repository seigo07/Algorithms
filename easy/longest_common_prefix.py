
'''
与えられた複数の文字列において、先頭から見て全ての文字列に共通する最長の文字列（prefix）を見つけ出す。
共通部分が存在しない場合は空文字列 "" を返す。
'''


def longest_common_prefix(strs):
    # 文字列リストが空の場合は空文字を返す
    if not strs:
        return ""
    
    # 最初の文字列を基準とする
    prefix = strs[0]
    
    # 残りの文字列と1つずつ比較していく
    for s in strs[1:]:
        # 現在のprefixが、次の文字列の先頭と一致する範囲を見つける
        while not s.startswith(prefix):
            # 一致しない場合は、prefixの末尾から1文字ずつ削る
            prefix = prefix[:-1]
            # 共通部分がなくなったら空文字を返す
            if not prefix:
                return ""
    
    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))  # 出力: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))     # 出力: ""
