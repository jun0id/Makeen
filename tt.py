input_file = open("test.txt", "r")
for line in input_file:
    line= line.split(" ")
    if (int(line[1]) >= 70):
        print(line[0], 'mark is :', line[1])