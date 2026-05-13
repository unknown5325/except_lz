import csv

def main():
    class Error:
        def __init__(self, coll_1, coll_2):
            self.coll_1  = coll_1
            self.coll_2 = coll_2

        @property
        def check(self):
            try:
                with open('var7.csv', 'r') as file:
                    types_a = []
                    types_b = []
                    err_type = []
                    err = []
                    with open(self.coll_1, 'r', encoding='utf-8-sig') as file_1, open(self.coll_2, 'r', encoding='utf-8' ) as file_2:
                        csv_str1 = csv.reader(file_1)
                        csv_str2 = csv.reader(file_2)
                        first_str1 = next(csv_str1, None)
                        first_str2 = next(csv_str2, None)
                        if first_str1 != first_str2:
                            err = ['Структура датафрейма НЕ соответствует ожидаемой:', 'Названия столбцов не совпадают.']
                            err.append(f'Ождиаемые {first_str1}')
                            err.append(f'Фактические: {first_str2}')

                        second_str1 = next(csv_str1, None)
                        second_str2 = next(csv_str2, None)

                        for i in second_str1:
                            try:
                                if i != float(i):
                                    types_a.append(type(float(i)))
                            except ValueError:
                                types_a.append(type(i))
                                continue 

                        for i in second_str2:
                            try:
                                if i != float(i):
                                    types_b.append(type(float(i)))
                            except ValueError:
                                types_b.append(type(i))
                                continue 

                        for i in range(0, len(second_str1)):
                            if types_a[i] != types_b[i]:
                                err_type.append(f'В столбце "{first_str1[i]}" тип данных не соответствует ожидаемому. Ожидается: {types_a[i]}, Фактически: {types_b[i]}')

                        for i in err:
                            print(i)
                        
                        for i in err_type:
                            print(i)
                    
            except FileNotFoundError:
                print(f"Возникла следующая ошибка: [Errno 2] No such file or directory: {self.coll_1} or {self.coll_2}")

            except StopIteration:
                print('Возникла следующая ошибка: Первый файл оказалс пустым.')

            except TypeError:
                print('Возникла следующая ошибка: Второй файл оказался пустым.')


        def __del__(self):
            print('')

    prov = Error('var7.csv', 'var1.csv').check
    return prov


if __name__ == '__main__':
    main()