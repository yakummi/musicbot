def list1():
    with open('list1.txt', encoding='UTF-8') as file:
        read = file.read()
    print(read)
