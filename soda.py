print("Welcome to Soda Vending Machine")
while True:
    num_of_soda=int(input("How many soda's do you need (max 5)"))
    if num_of_soda>5:
        print("Please enter number of soda's less than 5")
    else:
        print("You have entered", num_of_soda, "soda's")
        print("Each soda cost Rs.3")
        b = 3 * num_of_soda
        print("Therefore the cost for", num_of_soda, "soda's is", b, "Rs")
        a=int(input("press 1 to continue"))
        if a==1:
            print("Please insert the coins(the coins must be in 2 rupee or 1 rupee only ")
            while (True):
                c=int(input("Please tell how many two rupee coins you are inserting"))
                d=int(input("Please tell how many one rupee coins you are inserting"))
                total=(c*2)+(d*1)
                if total<b:
                    print("Please enter required amount")

                else:
                    print("You have inserted",total,"rupees")
                    change=total-b
                    print("You will get change of",change,"rupees")
                    print("Thank you for using Vending Machine")
                    break
        break