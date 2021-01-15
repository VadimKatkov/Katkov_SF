import numpy as np

def guess_try(number, min_predict, max_predict):
    '''
    Trying just to guess number in range
    This reduces tries for 1 step
    '''
    lucky_guess = np.random.randint(min_predict, max_predict + 1)
    if number == lucky_guess:
        return lucky_guess
    else:
        return max_predict

def game_core(number):
    '''
    Set random number
    Overall approach - reducing current range twice
    Setting up floor (min_predict) and ceiling (max_predict) for range
    Comparing number with ceiling
    At every step just trying to guess number (def guess_try) in range
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
    '''Launch game 1000 times, to find out as soon we could guess number'''

    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    count_try = list(map(lambda num: game_core(num), random_array))
    score = int(np.mean(count_try))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
