# #をバックスペースとみなし、文字を削除した後の2つの文字列が同じか判定
# 時間・空間計算量：O(N + M)
def backspace_compare(s: str, t: str) -> bool:
    # 文字列を後ろから1文字ずつ返すジェネレータ
    def valid_chars(text):
        skip = 0  # 消すべき文字数

        # 後ろから走査
        for c in reversed(text):
            if c == "#":
                skip += 1          # '#'なら次の文字を消す
            elif skip:
                skip -= 1          # 消される文字なのでスキップ
            else:
                yield c            # 有効な文字だけ返す

    # 両方の有効文字列が一致するか比較
    return list(valid_chars(s)) == list(valid_chars(t))


print(backspace_compare("ab#c", "ad#c"))   # True
print(backspace_compare("ab##", "c#d#"))   # True
print(backspace_compare("a#c", "b"))       # False