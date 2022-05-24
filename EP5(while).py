start , stop = 1,3
sum ,avg =0,0
while (start<=stop):
    number=int(input("Enter number :"))
    sum+=number # บวกเลขที่ป้อนแต่ละรอบ
    start+=1

avg=sum/stop
print("Summation = ", sum)
print("Avg  = ", avg)