import random
import time

def sayi_tahmin_oyunu():
    print("Hey! Are You Ready to Guess? 🎮")
    print("I kept a number between 1 and 100. Let's see if you can guess it!")
    
    gizli_sayi = random.randint(1, 100)  # 1-100 arasında rastgele bir sayı
    tahmin_hakki = 10  # Kullanıcının 10 hakkı var
    oyuncu_adi = input("What's your name? ")
    
    print(f"\nGood luck, {oyuncu_adi}! You have {tahmin_hakki} attempts to guess the number.")
    time.sleep(1)  # 1 saniyelik bekleme

    while tahmin_hakki > 0:
        print(f"\nRemaining Attempts: {tahmin_hakki}")
        tahmin = input("Enter Your Guess: ")
        
        # Kullanıcıdan doğru formatta giriş alınmasını sağlama
        if not tahmin.isdigit():
            print("Please enter a valid number!")
            continue

        tahmin = int(tahmin)
        
        if tahmin == gizli_sayi:
            print(f"Congratulations, {oyuncu_adi}! Correct Guess! 🎉")
            break
        elif tahmin < gizli_sayi:
            print("Guess a Bigger Number! 🔼")
        else:
            print("Guess a Smaller Number! 🔽")
        
        tahmin_hakki -= 1
    
    if tahmin_hakki == 0:
        print(f"\nSorry, you're out of guesses, {oyuncu_adi}. The correct number was {gizli_sayi}. 😞")

sayi_tahmin_oyunu()
