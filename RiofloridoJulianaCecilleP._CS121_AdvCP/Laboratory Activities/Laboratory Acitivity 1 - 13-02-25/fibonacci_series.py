num = int(input("Enter a number: "))

first_num = 0
second_num = 1

if num <=0:
    print("Enter a positive integer")
elif num ==1:
    print("Fibonacci sequence up to 1 term: ")
    print(first_num)
    
else:
    print("Fibonacci sequence:")
    for _ in range(num):
        print(first_num, end=" ")
        next_term = first_num + second_num
        first_num = second_num
        second_num = next_term
    print()