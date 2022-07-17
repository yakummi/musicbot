def list5():
    with open('list5.txt', encoding='UTF-8') as file:
        reader = file.read()
    print(reader)