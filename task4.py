if __name__ == '__main__':
    with open('task4.txt', encoding='utf-8') as file:
        diction = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        new_text = []
        for line in file.readlines():
            line = line.strip()
            for key in diction:
                line = line.replace(key, diction.get(key))
            new_text.append(line + '\n')

    with open('task4upd.txt', 'w', encoding='utf-8') as new_file:
        new_file.writelines(new_text)




