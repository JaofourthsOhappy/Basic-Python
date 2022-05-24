while True:
    try:
        name=input("Enter name :")
        if name == "fourth":
            raise Exception("Have name in system")
        
        number1=int(input("Enter no 1 :"))
        number2=int(input("Enter no 2 :"))
        if number1 == 0 and number2 == 0:
            break
        if number1<0 or number2<0:
            raise Exception("Cannot enter positive number")

        result=number1/number2
        print(result)
    except Exception as e:
        print(e)
