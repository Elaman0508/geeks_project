import random
from decouple import config
import os

def casino_game():
    starting_money = int(os.getenv('MY_MONEY', 1000))
    available_slots = list(range(1, 11))
    play_again = True

    while play_again:
        print(f"ваш баланс{starting_money}.")

        # Вопрос о ставке
        bet = int(input("Сделайте свою ставку:"))
        selected_slot = int(input("Выберите слот (1-10): "))

        # Рандомный выбор выигрышной слоты
        winning_slot = random.choice(available_slots)

        # Проверка выигрыша или проигрыша
        if selected_slot == winning_slot:
            starting_money += bet * 2
            print(f"Поздравляю! Ты победил ${bet * 2}.")
        else:
            starting_money -= bet
            print(f"Извините, вы проиграли ${bet}.")

        # Проверка наличия денег для продолжения игры
        if starting_money <= 0:
            print("У вас закончились деньги. Игра окончена!")
            play_again = False
        else:
            choice = input("Хочешь поиграть еще? (да/нет): ")
            if choice.lower() != 'да':
                play_again = False

    print(f"Ваш окончательный баланс составляет ${starting_money}.")

  