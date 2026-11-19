
optiune = ""
teme = []

while optiune != "4":
    print("\n========== UNITRACK ==========")
    print("1. Adauga o tema")
    print("2. Afiseaza temele")
    print("3. Marcheaza o tema ca finalizata")
    print("4. Iesire")
    print("==============================")

    optiune = input("Alege o optiune: ")

    if optiune == "1":
        nume = input("Numele temei: ")

        if nume.strip() != "":
            teme.append(nume)
            print("Tema a fost adaugata!")
        else:
            print("Numele temei nu poate fi gol!")

    elif optiune == "2":
        if len(teme) == 0:
            print("Nu a fost adaugata nicio tema.")
        else:
            print("\n========== TEMELE TALE ==========")
            for i, tema in enumerate(teme, start=1):
                print(f"{i}. {tema}")

    elif optiune == "3":
        if len(teme) == 0:
            print("Nu ai nicio tema de finalizat.")
        else:
            for i, tema in enumerate(teme, start=1):
                print(f"{i}. {tema}")

            nr = input("Introdu numarul temei finalizate: ")

            if nr.isdigit():
                nr = int(nr)

                if 1 <= nr <= len(teme):
                    if not teme[nr - 1].startswith("[FINALIZATA] "):
                        teme[nr - 1] = "[FINALIZATA] " + teme[nr - 1]
                        print("Tema a fost finalizata!")
                    else:
                        print("Tema este deja finalizata!")
                else:
                    print("Numar invalid!")
            else:
                print("Introdu un numar valid!")

    elif optiune == "4":
        print("La revedere!")

    else:
        print("Optiune invalida!")
