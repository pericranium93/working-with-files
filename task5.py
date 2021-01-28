if __name__ == '__main__':
    with open('task5.txt', 'w', encoding='utf-8') as file:
        my_line = input('Введите числа через пробел')
        my_line = " ".join([el for el in my_line.split(' ') if el.strip()])
        result = sum(map(int, my_line.split()))
        file.write(f'Вы ввели числа {my_line}\nИх сумма равна {result}')

