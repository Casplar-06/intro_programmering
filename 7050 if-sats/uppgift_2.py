text = input("Ange din näst sista siffra i ditt personnummer: ")
tal = int(text)
if tal % 2 != 0:
    print('Du är kille')
else:
    print('Du är tjej')
