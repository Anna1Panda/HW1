from operator import is_
import numpy as np


def game_core_v2(number: int = 1) -> int:
    """[summary]

    Args:
        number (int, optional): [description]. Defaults to 1.

    Returns:
        int: [description]
    """

    left = 1
    right = 100
    count = 0
    is_right = np.random.randint(1, 101)


    while True:
        
        count += 1
        current = (left + right) // 2
        
        if count == 21:
            break
        
        if is_right == current:
            break
        elif is_right > current:
            left = current
        else:
            right = current
            
    return count


def score_game(game_core_v2) -> int: 
    """[summary]

    Args:
        game_core_v2 ([type]): [description]

    Returns:
        int: [description]
    """
    
    count_ls = [] 
    random_array = np.random.randint(1,101, size=1000) 
    
    for number in random_array:
        count_ls.append(game_core_v2(number)) 
    
    score = int(np.mean(count_ls)) 

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    
    return(score)


if __name__ == '__main__':
    score_game(game_core_v2)