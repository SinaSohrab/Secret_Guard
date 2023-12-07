number = int(input("input your number: "))
taghsim = number
baghimande = number
javab_list=[]

while True:
    javab_taghsim = taghsim // 2
    javab_baghimande = baghimande % 2

    taghsim = javab_taghsim
    baghimande = javab_taghsim
    javab_list.append(javab_baghimande)

    if taghsim == 0:
        break

javab = list(map(str, javab_list))
javab = "".join(javab)

print(javab)