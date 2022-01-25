
with open("data/FB.csv", newline='') as file:
    file_reader = file.readlines()
    data = []
    for line in file_reader:
        line_split = line.split(',')
        data.append(line_split)
    for row in data:
        row.append((float(row[4])-float(row[1]))/float(row[1]))

    print(data)
