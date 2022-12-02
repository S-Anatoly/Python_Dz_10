class Table:
    def __init__(self, rows, cols):  # Инициализация списка
        self.row = rows
        self.col = cols
        self.list1 = []
        for _ in range(self.row):
            self.list1.append([0] * self.col)

    def get_value(self, row, col):  # Поиск элемента в таблице
        if 0 <= row < len(self.list1) and 0 <= col < len(self.list1[0]):
            return self.list1[row][col]
        else:
            return None

    def set_value(self, row, col, value):  # Вставить элемент на позицию
        if 0 <= row < len(self.list1) and 0 <= col < len(self.list1[0]):
            self.list1[row][col] = value
        else:
            return None

    def n_rows(self):  # Возврат количества строк
        count = 0
        for i in range(len(self.list1)):
            count += 1
        return count

    def n_cols(self):  # Возврат количества столбцов
        count = 0
        for i in range(len(self.list1[0])):
            count += 1
        return count

    def delete_row(self, row):  # Удалить строку
        self.list1.pop(row)

    def delete_col(self, col):  # Удалит колонку
        for i in range(len(self.list1)):
            self.list1[i].pop(col)

    def add_row(self, row):  # Добавить строку
        self.list1.insert(row, [0] * self.col)

    def add_col(self, col):  # Добавить колонку
        for i in range(len(self.list1)):
            self.list1[i].insert(col, 0)


# # Пример 1
# tab = Table(3, 5)
# tab.set_value(0, 1, 10)
# tab.set_value(1, 2, 20)
# tab.set_value(2, 3, 30)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
# tab.add_row(1)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

##Пример 2
tab = Table(2, 2)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_col(1)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()
