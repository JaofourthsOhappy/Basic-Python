import random

ATM_PASSWORD="ko6"
result="" 

while result!=ATM_PASSWORD :
      result="" 
      for letter in range(len(ATM_PASSWORD)):
          list_number=random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
          result="".join(list_number)+str(result)
          print("SEARCH = ",result)
print("The password is ", result)