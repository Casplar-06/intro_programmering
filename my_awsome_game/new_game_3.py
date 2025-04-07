import random

def skapa_spelplan():
    return [["O"] * 5 for _ in range(5)]

def skriv_ut_spelplan(spelplan):
    for row in spelplan:
        print(" ".join(row))

def placera_skepp(spelplan):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    spelplan[x][y] = "S"
    return x, y

def spela():
    print("Välkommen till Battleship!")
    
    spelplan_dator = skapa_spelplan()
    spelplan_spelare = skapa_spelplan()
    
    x_skepp, y_skepp = placera_skepp(spelplan_dator)
    
    gissningar = 0
    träffar = 0
    
    while träffar < 1:
        print("\nDin spelplan:")
        skriv_ut_spelplan(spelplan_spelare)
        
        gissning_x = int(input("\nAnge rad (0-4): "))
        gissning_y = int(input("Ange kolumn (0-4): "))
        
        gissningar += 1
        
        if spelplan_dator[gissning_x][gissning_y] == "S":
            print("Grattis! Du träffade skeppet!")
            spelplan_spelare[gissning_x][gissning_y] = "X"
            träffar += 1
        else:
            print("Du missade!")
            spelplan_spelare[gissning_x][gissning_y] = "M"
        
    print(f"\nDu sänkte skeppet på {gissningar} gissningar!")
    skriv_ut_spelplan(spelplan_spelare)

spela()