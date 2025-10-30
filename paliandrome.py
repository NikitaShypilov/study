def is_palindrome(text):
    text = text.lower()
    clean_text = ''.join(ch for ch in text if ch.isalnum())
    return clean_text == clean_text[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
