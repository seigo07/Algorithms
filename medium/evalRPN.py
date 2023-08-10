# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.

# このプログラムは逆ポーランド記法で書かれた数式を評価します。
class Solution(object):
    def evalRPN(self, tokens):
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


# インスタンスの作成
solution = Solution()

# 使用例1
tokens1 = ["2", "1", "+", "3", "*"]
print(solution.evalRPN(tokens1))  # 出力: 9  (つまり、(2 + 1) * 3 = 9)

# 使用例2
tokens2 = ["4", "13", "5", "/", "+"]
print(solution.evalRPN(tokens2))  # 出力: 6  (つまり、4 + (13 / 5) = 4 + 2 = 6)

# 使用例3
tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(solution.evalRPN(tokens3))  # 出力: 22
