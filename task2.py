if __name__ == '__main__':
    with open('task2.txt', encoding='utf-8') as file:
        lines = file.readlines()
        print('Количество строк:', len(lines))
        words = 0
        for num, line in enumerate(lines, 1):
            words = len(line.split())
            a = words % 10
            b = words % 100
            if a == 1 and b != 11:
                c = 'о'
            elif 1 < a < 5 and not 11 < b < 15:
                c = 'а'
            else:
                c = ''
            print(f'В строчке № {num} {words} слов{c}')

