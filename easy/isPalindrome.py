def isPalindrome(s):
    s = "".join(ch for ch in s.lower() if ch.isalnum())
    return s == s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))  # Returns True
print(isPalindrome("race car"))  # Returns True
print(isPalindrome("Hello, world"))  # Returns False

