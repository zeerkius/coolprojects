def count_letter_cases(vro):
    capital = 0
    lowercase = 0
    for i in range(len(vro)):
        if (ord(vro[i]) >= 65) and (ord(vro[i]) <= 90):
            capital += 1
        if (ord(vro[i]) >= 97) and (ord(vro[i]) <= 122):
            lowercase += 1
    print(capital)
    print(lowercase)

    
count_letter_cases("JollyRancher")
count_letter_cases("Hello")
count_letter_cases("ZIyad")


def is_palindrome(glo):
    count = 0
    if len(glo) == 2:
        print("This is a palindrome")
    if glo[0] == glo[len(glo)-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


is_palindrome("racecar")
is_palindrome("ab")
is_palindrome("hello")


    


