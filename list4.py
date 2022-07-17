def list4():
    with open('list4.txt', encoding='UTF-8') as file:
        file_reader = file.read()
    print(file_reader)
