
# 逆ポーランド記法で書かれた数式を評価する
# tokens = ["2", "1", "+", "3", "*"] → (2 + 1) * 3 = 9

# 1. 空の stack を作る。
# 2. tokens を先頭から順に処理する。
# 3. 数字なら stack に追加（append）。
# 4. 演算子なら2つ取り出す（pop）→計算→結果を追加。
# 5. 最後に残った値を返す。

# 時間空間計算量 O(n)

def eval_RPN(tokens):
    stack = []

    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            b, a = stack.pop(), stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if a * b < 0 and a % b != 0:
                    stack.append(a // b + 1)
                else:
                    stack.append(a // b)
        else:
            stack.append(int(token))

    return stack[0]


# 使用例1
tokens1 = ["2", "1", "+", "3", "*"]
print(eval_RPN(tokens1))  # 出力: 9  (つまり、(2 + 1) * 3 = 9)

# 使用例2
tokens2 = ["4", "13", "5", "/", "+"]
print(eval_RPN(tokens2))  # 出力: 6  (つまり、4 + (13 / 5) = 4 + 2 = 6)

# 使用例3
tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(eval_RPN(tokens3))  # 出力: 22
