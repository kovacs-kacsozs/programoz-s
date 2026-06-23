input = int(input("Add meg az első számot: "))
input2 = int(input("Add meg a második számot: "))

if input > input2:
    print("Az első szám nagyobb.")
elif input2 > input:
    print("A második szám nagyobb.")
else:
    print("A két szám egyenlő.")