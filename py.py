vowels = 'aeiouAEIOU'
vowel = input("Enter character: ")

if len(vowel) ==1:
    if vowel in vowels:
        print("True")
        if vowel == 'a':
            print("a is in vowels")
        elif vowel == 'e':
            print("e is in vowels")
        else:
            print("Other vowel")
    else:
        print("False")
else:
    print("More than one character entered. Invalid")



