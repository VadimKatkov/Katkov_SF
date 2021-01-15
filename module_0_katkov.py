import numpy as np

def game_core(number):
    '''Сначала устанавливаем любое random число
    Механизм поиска - каждый раз уменьшаем диапазон поиска в два раза
    Для этого определяем нижний (min_predict) и верхний (max_predict) предел диапазона поиска
    Загаданное число сравниваем с верхним пределом
    '''

    min_predict = 1
    max_predict = 50
    count = 1

    while number != max_predict:
        count += 1
        if number > max_predict:
            min_predict = max_predict
            max_predict = min_predict + min_predict // 2
        elif number < min_predict + (max_predict - min_predict) // 2:
            max_predict = min_predict + (max_predict - min_predict) // 2 - 1
        else:
            max_predict = min_predict + (max_predict - min_predict) // 2
    print("загаданное число", number, "угаданное число", max_predict, "попыток", count)
    return(count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

score_game(game_core)
