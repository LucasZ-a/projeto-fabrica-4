boi1 = input("digite o nome do boi ")
peso1 =float(input(f"digite o peso do boi {boi1} "))
boi2 = input("digite o nome do boi ")
peso2 =float(input(f"digite o peso do boi {boi2} "))
boi3 = input("digite o nome do boi ")
peso3 =float(input(f"digite o peso do boi {boi3} "))

if peso1 > peso2 and peso1 > peso3:
    if peso2 > peso3:
        print("o placar de bois ficará :", boi1, boi2, boi3)
    else:
        print("o placar de bois ficará :", boi1, boi3, boi2)
elif peso2 > peso1 and peso2 > peso3:
    if peso1 > peso3:
        print("o placar de bois ficará :", boi2, boi1, boi3)
    else:
        print("o placar de bois ficará :", boi2, boi3, boi1)
elif peso3 > peso2 and peso3 > peso1:
    if peso2 > peso1:
        print("o placar de bois ficará :", boi3, boi2, boi1)
    else:
        print("o placar de bois ficará :", boi3, boi1, boi2)
else:
    print("!!!erro!!!")