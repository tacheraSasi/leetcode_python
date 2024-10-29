def isPalindrome(x :int)-> bool:
    if x < 0:
        return False
    
    output = str(x) == str(x)[::-1]
    return output

num = 111
print(f"The number {num} is {'a' if isPalindrome(num) else 'not'} a palindrome")
#give out some sort of output