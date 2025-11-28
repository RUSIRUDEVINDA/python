word = input("Enter a word: ")
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
