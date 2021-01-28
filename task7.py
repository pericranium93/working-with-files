import json

if __name__ == '__main__':
    with open('task7.txt', encoding='utf-8') as file:
        profit_list = []
        firms_profit = {}
        profit_dict = {}
        total_list = [firms_profit, profit_dict]
        for line in file.readlines():
            line = line.split()
            profit = float(line[2]) - float(line[3])
            if profit > 0:
                profit_list.append(profit)
            firms_profit[line[0]] = profit
        average_profit = sum(profit_list) / len(profit_list)
        profit_dict['Average profit'] = average_profit

    with open('task7.json', 'w', encoding='utf-8') as f_json:
        json.dump(total_list, f_json, ensure_ascii=False)




