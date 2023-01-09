import random                                                               #импорт библиотеки random
digits = '23456789'                                                         #объявляем переменные
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ban_simbol = 'il1Lo0O'
pas = []
chars = ''
j = 1
flag_digit, flag_lowercase_letters, flag_uppercase_letters, \
    flag_punctuation, flag_ban_simbol = False, False, False, False, False,  #создаем флаги

num = int(input('Сколько паролей вам нужно? '))                             #Узнаем сколько пароль нужно и какой они длины
length = int(input('Какой длины требуется пароль? Минимум 4. '))
if length < 4:                                                              #проверка на длину пароля
    while length < 4:
        print('Пароль слишком короткий, повторите пожалуйста')
        length = int(input())

def generate(var):                                                          #функция проверки и доваление в пароль необходимых символов
    global pas, chars, varible_length
    pas += random.choice(var)
    varible_length -= 1

if input('Пароль должен включать цифры?').lower() in ['да', 'yes', 'y']:    #Узнаем требования к паролям и создаем библиотеку для генерации пароля
    flag_digit = True
    chars += digits
if input('Пароль должен включать прописные буквы?').lower() in ['да', 'yes', 'y']:
    flag_lowercase_letters = True
    chars += lowercase_letters
if input('Пароль должен включать строчные буквы?').lower() in ['да', 'yes', 'y']:
    flag_uppercase_letters = True
    chars += uppercase_letters
if input('Пароль должен включать символы?').lower() in ['да', 'yes', 'y']:
    flag_punctuation = True
    chars += punctuation
if input('Оставить неоднозначные символы "il1Lo0O?"').lower() in ['да', 'yes', 'y']:
    flag_ban_simbol = True
    chars += ban_simbol

while j <= num:                                                             #создаем пароли и выводим их
    varible_length = length
    pas = []
    if flag_digit:                                                          #проверяем требования к паролю
        generate(digits)
    if flag_lowercase_letters:
        generate(lowercase_letters)
    if flag_uppercase_letters:
        generate(uppercase_letters)
    if flag_punctuation:
        generate(punctuation)
    while varible_length > 0:                                               #создаем пароль нужной длины
        pas += random.choice(chars)
        varible_length -= 1
    random.shuffle(pas)                                                     #перемешиваем символы в пароле
    print('Ваш', j, 'пароль: ', end='')                                     #выводим пароль
    for i in pas:
        print(i, end='')
    print('')
    j += 1