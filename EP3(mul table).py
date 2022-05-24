start=int(input("Start = ")) # 1
stop=int(input("Stop = ")) # 4

for x in range(start,stop+1):
    print("At = ",x)
    for y in range(1,13):
        print(x,'x',y ," = ",(x*y))