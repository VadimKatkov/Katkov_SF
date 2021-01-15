import numpy as np

def guess_try(number, min_predict, max_predict):
    ''' в этой функции попытка угадать число в диапазоне
    этот шаг уменьшает количество попыток на 1
    '''
    lucky_guess = np.random.randint(min_predict, max_predict + 1)
    if number == lucky_guess:
        return lucky_guess
    else:
        return max_predict

def game_core(number):
    '''Сначала устанавливаем любое random число
    Механизм поиска - каждый раз уменьшаем диапазон поиска в два раза
    Для этого определяем нижний (min_predict) и верхний (max_predict) предел диапазона поиска
    Загаданное число сравниваем с верхним пределом
    Ну и еще просто каждый раз пробуем угадать число  (def guess_try) в проверяемом диапазоне ))
    '''

    min_predict = 1
    max_predict = 50
    count = 1

    while number != max_predict:
        count += 1

        if number > max_predict:
            min_predict = max_predict
            max_predict = min_predict + (101 - min_predict) // 2
            max_predict = guess_try(number, min_predict, max_predict)

        elif number < min_predict + (max_predict - min_predict) // 2:
            max_predict = min_predict + (max_predict - min_predict) // 2 - 1
            max_predict = guess_try(number, min_predict, max_predict)
        else:
            max_predict = min_predict + (max_predict - min_predict) // 2
            max_predict = guess_try(number, min_predict, max_predict)

    return count  # выход из цикла, если угадали


def score_game(core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    count_ls = list(map(lambda num: game_core(num), random_array))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
