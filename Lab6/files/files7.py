with open("text7.txt", "r") as f1, open("text7_2.txt", "a") as f2:
    for line in f1:
        f2.write(line)
