value = input("enter your word: ").lower().strip()
reversed_value=""
def is_palindrome(word="unknown"):
   reversed_value=word[-1::-1]
   return reversed_value

reversed_value = is_palindrome(value)
print(reversed_value)
if reversed_value == value:
  print("This is palindrome")
else:
  print("This is not palindrome")
