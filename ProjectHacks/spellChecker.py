def ReadDb():
    word_list = []
    word_db = open("words.txt", "r")
    for i in word_db:
        x = i.strip('\n')
        word_list.append(x)
    word_db.close()
    print("{} words have been loaded".format(len(word_list)))
    return word_list


def checkerror(num):
    word_list = ReadDb()
    for i in num:
        if i in word_list:
            print(i,end = " ")
        else:
            print(i+"(wrong word)", end=" ")


def main():

    search_string = input("Enter a sentence: ")
    search_list = search_string.split(" ")
    checkerror(search_list)


if __name__ == '__main__':
    main()
