import random

def guess_car_brand():
    car_brands = ["volvo", "saab", "audi", "ford", "bmw", "kia", "tesla", "fiat", "ferrari", "lamborghini", "mercedes"]
    car = random.choice(car_brands)
    attempts = 0
    print("Välkommen till Gissa Bilmärket-spelet!")
    print("Jag tänker på ett bilmärke. Kan du gissa vilket?")
    
    while True:
        guess = input("Din gissning: ").strip().lower()
        attempts += 1
        
        if guess == car:
            print(f"Grattis! Du gissade rätt på {attempts} försök.")
            break
        else:
            print("Fel! Försök igen.")

if __name__ == "__main__":
    guess_car_brand()