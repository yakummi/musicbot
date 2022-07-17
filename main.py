# face of nwork лицо работы
#task :
#parsing text from sites
# сделать для каждого саундтрека свой файл в котором хранится file.txt с текстом
# импорт нестандартных бибилиотек
# ВЫБОР ПОЛЬЗОВАТЕЛЯ
# весь процесс производить в функциях чтобы облегчить процесс работы.
from list1 import list1
from list2 import list2
from list3 import list3
from list4 import list4
from list5 import list5
from func_close import func_close
from func_start import func_start
def main():
    func_start()
    choice = int(input('Введите число: '))
    if choice == 1:
        list1()
    elif choice == 2:
        list2()
    elif choice == 3:
        list3()
    elif choice == 4:
        list4()
    elif choice == 5:
        list5()
    else:
        func_close()
if __name__ == '__main__':
    main()

