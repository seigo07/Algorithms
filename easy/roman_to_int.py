# ローマ数字の文字列を整数に変換
# 現在の数字より次の数字が大きい場合は引き算、それ以外は足し算
# 時間計算量：O(n) 空間計算量：O(1)
def roman_to_int(s: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    # 文字列を左から順番に確認する
    for i, char in enumerate(s):
        current = values[char]  # 現在のローマ数字の値
        # 次の値のほうが大きい場合は、現在の値を引く（ex. IVの場合、I = 1 の次に V = 5 があり、1 < 5）
        if i + 1 < len(s) and current < values[s[i + 1]]:
            total -= current
        else:
            total += current

    return total


print(roman_to_int("III"))      # 3
print(roman_to_int("LVIII"))    # 58
print(roman_to_int("MCMXCIV"))  # 1994