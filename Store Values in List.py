a=int(input("Enter Your many values you want to store in list"))
b=[]
for i in range(0,a):
    c=int(input("Enter Values"))
    b.append(c)
print("\n\n PRINTING DATA")
time.sleep(3)
print(b)
d=sorted(b)
print(d)
