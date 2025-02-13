num = input("Enter a number: ")

reverse_number = ""
for digit in num:
    reverse_number = digit + reverse_number
    
if num == reverse_number:
    print("Palindrome")
else:
    print("Not a Palindrome")