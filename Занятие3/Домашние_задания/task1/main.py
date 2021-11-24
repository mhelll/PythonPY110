file_1 = open("FILE_1.txt", "r", encoding="utf8")

list_1 = ["abcd\n", "123456\n", "qwerty123456\n"]
file_1.write(list_1)

file_1.close()

with open("FILE_2.txt", "w") as file_2:
    file_2.write("qwerty")
    file_2.close()

if __name__ == "__main__":
    # Write your solution here
    pass
