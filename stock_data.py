import os
from urllib.request import urlopen

url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'

local_path = os.path.join('data', 'GOOG.csv')
with urlopen(url) as file, open(local_path, 'wb') as f:
    f.write(file.read())

url = 'https://query1.finance.yahoo.com/v7/finance/download/AMZN?period1=1611675026&period2=1643211026&interval=1d&events=history&includeAdjustedClose=true'

local_path = os.path.join('data', 'AMZN.csv')
with urlopen(url) as file, open(local_path, 'wb') as f:
    f.write(file.read())

url = 'https://query1.finance.yahoo.com/v7/finance/download/FB?period1=1611675102&period2=1643211102&interval=1d&events=history&includeAdjustedClose=true'

local_path = os.path.join('data', 'FB.csv')
with urlopen(url) as file, open(local_path, 'wb') as f:
    f.write(file.read())


def calculate_change(file_path):
    with open(file_path) as file:
        file_reader = file.readlines()
        data = []
        for line in file_reader:
            line_replace = line.replace('\n', "")
            line_split = line_replace.split(",")
            data.append(line_split)
        for row in data:
            if row == data[0]:
                row.append("Change")
            else:
                row.append(round((float(row[4]) - float(row[1])) / float(row[1])*100, 2))

    with open(file_path, 'w') as new_file:
        for line in data:
            new_file.write(str(line).replace('\'', '').replace('[','').replace(']', '').replace(' ',''))
            new_file.write('\n')


calculate_change('data/GOOG.csv')
calculate_change('data/FB.csv')
calculate_change('data/AMZN.csv')


