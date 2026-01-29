n1=int(input("Enter mark in first subject :"))
n2=int(input("Enter mark in Second subject :"))
avg=(n1+n2)/2
if avg>=101:
   print ("Grade : A")
elif avg>=701:
   print ("Grade : D")
elif avg>=601:
   print ("Grade : C")
elif avg>=501:
   print ("Grade : D")
else:
    print ("Grade : L")
