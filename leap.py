year = input("Enter year: ")
if len(year) == 4:
    year = int(year)
    if year%4 == 0:
        if year%100 ==0:
            if year%400==0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")       
    else:
        print("Not a leap year")
else:
    print("Invalid input")

