table = []
new_table = []
count = []
co = 0
con = 0
cont = 0
with open('text.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        if line[len(line) - 1:len(line)] == '\n':
            line = line.replace(line[len(line) - 1:len(line)], "")
        table.append(line)
        line = open_file.readline()
for i in table:
    if i not in new_table:
        new_table.append(i)
for i in table:
    if i == new_table[0]:
        co += 1
for i in table:
    if i == new_table[1]:
        con += 1
for i in table:
    if i == new_table[2]:
        cont += 1
dictionary = {
    new_table[0]: co,
    new_table[1]: con,
    new_table[2]: cont
}
print(dictionary)
