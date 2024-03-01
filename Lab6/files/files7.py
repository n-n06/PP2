#wordk with text7_1.txt and text7_2.txt
with open("text7_1.txt", "r") as f1, open("text7_2.txt", "a") as f2:
    for line in f1:
        f2.write(line)

# alternative
# import shutil
# f2 = shutil.copyfile(src="text7_1.txt", dst="text7_2.txt")