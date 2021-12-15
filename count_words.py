txt = open('text.txt', 'r')
d = dict()

for line in txt:
    b = ".,?()!\"\'["
    for char in b:
        line = line.replace(char, "")
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])