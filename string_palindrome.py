def is_palindrome(text):
    left = 0
    right = len(text) - 1

    # Compare characters from both ends
    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


text = input("Enter a string: ")

if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")