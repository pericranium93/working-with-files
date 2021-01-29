if __name__ == '__main__':
    with open('task3.txt', encoding='utf-8') as file:
        elem = 0
        employee = {}
        for line in file.readlines():
            line = line.strip().split()
            employee[line[0]] = line[1]

        inv_employee = {}
        low_paying = []
        for key, val in employee.items():
            inv_employee[float(val)] = inv_employee.get(val, '') + key

        for key in inv_employee.keys():
            if key < 20000:
                low_paying.append(inv_employee.get(key))
        low_paying_text = (', '.join(low_paying))

        average = sum(inv_employee.keys()) / len(inv_employee.keys())
        print(
          f'Список сотрудников, чья з/п ниже 20000р.: {low_paying_text}.\nСредняя з/п в организации = {average: .2f}р.')
