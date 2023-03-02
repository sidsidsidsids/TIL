test_case = int(input())
for tc in range(test_case):
    word = str(input())
    word_numeric = len(word)
    if word_numeric == 1:
        print('..#..')
        print('.#.#.')
        print(f'#.{word}.#')
        print('.#.#.')
        print('..#..')
    else:
        print('..#..',end='')
        for i in range(word_numeric):
            if i == word_numeric - 2:
                print('.#..')
                break
            else:
                print('.#..',end='')
        print('.#.#.',end='')
        for i in range(word_numeric):
            if i == word_numeric - 2:
                print('#.#.')
                break
            else:
                print('#.#.',end='')
        print(f'#.{word[0]}.#',end='')
        for i in range(word_numeric):
            if i == word_numeric - 2:
                print(f'.{word[i+1]}.#')
                break
            else:
                print(f'.{word[i+1]}.#',end='')

        print('.#.#.', end='')
        for i in range(word_numeric):
            if i == word_numeric - 2:
                print('#.#.')
                break
            else:
                print('#.#.', end='')
        print('..#..', end='')
        for i in range(word_numeric):
            if i == word_numeric - 2:
                print('.#..')
                break
            else:
                print('.#..', end='')