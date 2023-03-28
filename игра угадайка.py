import random, math
print('Ну, привет! Давно мы не виделись.')
print('Предлагаю сыграть тебе со мной в одну игру.')
input()
print('Я загадаю натуральное число, а ты попробуешь его угадать.')
input()


def is_valid(s, num_last):
    return s.isdigit() and 0 < int(s) <= num_last

def game_run():
    while True:
        num_last = input('Напиши число больше 1: ')
        if num_last.isdigit() == False or int(num_last) < 2:
            print('Дружище, давай играть по правилам Я сказал загадать натуральное число больше 1!')
            print()
        else:
            print()
            print(f'Ок, я загадаю число от 1 до {num_last}.')
            print()
            break

    attempt = math.log2(int(num_last))
    attempt = math.ceil(attempt)

    print(f'Что бы было интереснее, я гарантиирую, что угадать число можно с {attempt} попытки.')
    print()

    num_last = int(num_last)
    num = random.randint(1, num_last)
    count = 0
    while True:
        count += 1
        n = input('Напиши число, которое я загадал: ')
        if is_valid(n, num_last) == False:
            print()
            print('Нууу... Старичок, я же сказал ЦЕЛОЕ ЧИСЛО от 0 до 100!')
            print()
            continue
        else:
            print()
            n = int(n)


        if n < num:
            print('Не угадал!')
            print()
            print('Но.. так уж и быть.. Дам тебе подсказку...')
            print('Твое число меньше моего.')
            print()

        elif n > num:
            print('Не угадал!')
            print()
            print('Но.. так уж и быть.. Дам тебе подсказку...')
            print('Твое число больше моего.')
            print()

        else:
            print(f'Отлично! Я загадал {num} и ты угадал c {count} попытки.')
            print()
            print()
            break

game_run()
print('Хочешь сыграть еще разок?')
if input('д - да, н - нет   ') == 'д':
    print()
    print('Без проблем. Погнали!')
    game_run()
else:
    print('Спасибо за игру!')