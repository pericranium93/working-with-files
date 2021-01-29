if __name__ == '__main__':
    with open('task6.txt', encoding='utf-8') as file:
        hours = []
        subjects = {}

        for line in file.readlines():
            line = line.split()
            for el in line[1:]:
                search = el.find('(')
                if search == -1:
                    continue
                else:
                    hours.append(int(el[:search]))

            subjects[line[0][:-1]] = sum(hours)
            hours = []
        print(subjects)
