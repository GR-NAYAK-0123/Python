
def isPalindrome(value):
    for i in range(0,(len(value)//2)):
        if value[i] != value[len(value)-i-1]:
            print("It is not palindrome number")
            break
    else:
        print("It is a palindrome number")


isPalindrome("Radha")
isPalindrome("Krishna")
isPalindrome("naman")