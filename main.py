from imsurance import insurance

volba = 0

while volba != 4:
    print("  vyberte si akci ")
    print("1 přídejte nového pojišteného")
    print("2 vypsat všechny pojištěné")
    print("3 vyhledat pojištěného podle jmena a příjmení")
    print("4 konec")
    volba = int(input())
    if volba == 1:
        print("ma 1")
        for j in range(1, 4, 1):

            insurance.create_insured(j)

    elif volba == 2:
        print("ma 2")
    elif volba == 3:
        print("ma 3")
    elif volba == 4:
        print("ma 4")
    elif volba == 5:
        print("ma 5")
    else:
        pass
