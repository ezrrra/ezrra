
def normalize(text):
    result = ""
    for ch in text:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
            result += ch.lower()
    return result


def is_palindrome(text, left, right):
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


text = input()
clean_text = normalize(text)

if is_palindrome(clean_text, 0, len(clean_text) - 1):
    print("YES")
else:
    print("NO")
