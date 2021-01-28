if __name__ == '__main__':
    with open('task1.txt', 'w', encoding='utf-8') as file:
        while True:
            string = input()
            if string == '':
                break
            file.write(string + '\n')
