import random

def hangman():
    words = ['python', 'programlama', 'bilgisayar', 'oyun', 'kodlama']
    word = random.choice(words).upper()
    word_letters = set(word)
    guessed_letters = set()
    lives = 6

    hangman_pics = [
        """
        ------
        |    |
             |
             |
             |
             |
        ==========""",
        """
        ------
        |    |
        O    |
             |
             |
             |
        ==========""",
        """
        ------
        |    |
        O    |
        |    |
             |
             |
        ==========""",
        """
        ------
        |    |
        O    |
       /|    |
             |
             |
        ==========""",
        """
        ------
        |    |
        O    |
       /|\\   |
             |
             |
        ==========""",
        """
        ------
        |    |
        O    |
       /|\\   |
       /     |
             |
        ==========""",
        """
        ------
        |    |
        O    |
       /|\\   |
       / \\   |
             |
        =========="""
    ]

    while lives > 0 and word_letters != guessed_letters:
        print(hangman_pics[6 - lives])
        print(f"Kalan can: {lives}")
        print("Kullanılan harfler: ", " ".join(sorted(guessed_letters)))
        display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Kelime: ", " ".join(display))

        guess = input("Bir harf girin: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Lütfen tek bir harf girin!")
            continue

        if guess in guessed_letters:
            print("Bu harfi zaten kullandın!")
            continue

        guessed_letters.add(guess)
        if guess in word_letters:
            print("Doğru tahmin!")
        else:
            lives -= 1
            print("Yanlış tahmin!")

    if word_letters == guessed_letters:
        print(hangman_pics[6 - lives])
        print(f"Tebrikler! Kelime: {word}. Kazandın!")
    else:
        print(hangman_pics[6])
        print(f"Kaybettin! Kelime: {word} idi.")

if __name__ == "__main__":
    print("Adam Asmaca Oyununa Hoş Geldiniz!")
    hangman()
    while input("Tekrar oynamak ister misiniz? (e/h): ").lower() == 'e':
        hangman()