print("\033[36m\033[1mПідтвердження особистості")
print("="*42,"\033[0m\n")
#while ans=="1":
    #age=int(input("how old are you:"))
    for kol in range (3):
    print("\033[36m\033[1m")
    if age >=0 and age <14:
        print("Свідоцво про народження")
    elif 14<=age<=35:
        print("id картка")
    elif 35<age<=110:
        print("паспорт старого зразку")
    else:
        print("помилке при введеня віку")
    print("\033[0m")
    ans=input("продовжити:(1-так,2-ні)")
print("Програма закінчилась")
