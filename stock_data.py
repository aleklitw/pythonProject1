
with open("data/FB.csv") as file:
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
            row.append((float(row[4]) - float(row[1])) / float(row[1]))
    #print(data)

with open("data/new_FB.csv", "w") as new_file:
   for line in data:
       new_file.write(str(line).replace('\'', '').replace('[','').replace(']', ''))
       new_file.write("\n")
