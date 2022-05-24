def randomNumber(x):
    if len(x)<3 :
        return
        
    if x == "100":
        print("Correct")
        return 1000
    else :
        print("Incorrect")
        return 0


money=randomNumber("100")
print("Price = ",money)