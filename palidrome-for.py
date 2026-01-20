value = input("your word: ").lower().strip()

def get_palindrom(word):
    reversed_value=""
    for i in range(len(word)-1,-1,-1):
        reversed_value+=word[i]
    return reversed_value
    
reversed_value = get_palindrom(value)

if reversed_value == value:
    print("palindrome")
else:
    print("not palindrome")
