def palindrome(number):
    reversed_number=number[::-1]
    if(reversed_number==number):
        return "palindrome"
    else:
        return "not palindrome"
number=input("enter a number:")
print(palindrome(number))