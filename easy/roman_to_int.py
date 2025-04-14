
'''

ローマ数字（例: "IX", "LVIII", "MCMXCIV"）を整数に変換する

処理の流れ（簡潔に）
1.各ローマ字の値を辞書に登録
2.左から順に文字を走査し、現在の値が次の文字の値より小さい場合は引き算、それ以外は足し算
3.合計値を返す

'''


def roman_to_int(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

print(roman_to_int("III"))      # 3
print(roman_to_int("IV"))       # 4
print(roman_to_int("IX"))       # 9
print(roman_to_int("LVIII"))    # 58
print(roman_to_int("MCMXCIV"))  # 1994
