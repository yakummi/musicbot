def list3():
    with open('list3.txt', encoding='UTF-8') as file:
        reader = file.read()
    print(reader)
