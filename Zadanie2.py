def count_info():
    try:
        with open('test_1.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            print(f"Количество строк в файле {len(my_list)}")
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f' В {i + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'
count_info()


