# coding: utf-8

# Вам заданы начальные координаты короля, пешки A и пешки B. Найдите наименьшее
# количество ходов, за которое король сможет побить пешку A. Король не может 
# ходить на поля, которые находятся под ударом пешек, а также не может выходить 
# за пределы доски. Король может побить пешку B, однако делать это не обязательно.
# Пешкам передвигаться запрещено.

# Технические условия

#    Входные данные

#    Состоит из нескольких тестов. Каждая строка описывает один тест и содержит
#    начальное положение короля, пешки A и пешки B. Каждая позиция описывается
#    двумя символами. Первый символ задает столбец ('a' - 'h'), а второй символ
#    задает строку ('1' - '8'). Все три позиции разные. Начальное положение
#    короля не находится под ударом ни одной пешки.

#    Выходные данные

#    Для каждого теста вывести в отдельной строке наименьшее количество ходов,
#    за которое король сможет побить пешку A.


# Сложность: меньше чем 8 ** 8
# 
# Примечание: я решил что пешки чёрные, а король - белый

rows = ('a','b','c','d','e','f','g','h')
columns = (1, 2, 3, 4, 5, 6, 7, 8)


def position_to_indexes(position):
    row = rows.index(position[0])
    column = columns.index(int(position[1]))
    return row, column


def indexes_to_position(row, column):
    return rows[row] + str(columns[column])


def move_position(old_row, old_column, row_move, column_move):
    new_row = old_row + row_move
    new_column = old_column + column_move
    if 8 > new_row > -1 and 8 > new_column > -1:
        return new_row, new_column
    else:
        return None, None


def my_algo(king, pawn_A, pawn_B):

    king_row, king_column = position_to_indexes(king)
    pawn_A_row, pawn_A_column = position_to_indexes(pawn_A)
    pawn_B_row, pawn_B_column = position_to_indexes(pawn_B)

    pawn_B_hits = [
        move_position(pawn_B_row, pawn_B_column, 1, -1), 
        move_position(pawn_B_row, pawn_B_column, -1, -1)]

    pawn_A_hits = [
        move_position(pawn_A_row, pawn_A_column, 1, -1), 
        move_position(pawn_A_row, pawn_A_column, -1, -1)]

    def king_moves(current_row, current_column, pawn_B_exists, move_number):
        moves = []
        for i in (0, -1, 1):
            for j in (0, -1, 1):
                if i or j:
                    new_row, new_column = move_position(current_row, current_column, i, j)
                    if new_row is not None\
                            and ((new_row, new_column) not in pawn_B_hits or not pawn_B_exists)\
                            and ((new_row, new_column) not in pawn_A_hits):
                        not_on_pawn_B = new_row != pawn_B_row or new_column != pawn_B_column
                        moves.append((new_row, new_column, 
                            not_on_pawn_B and pawn_B_exists, move_number + 1))
        return moves

    i = 0
    positions = [(king_row, king_column, True, 0)]
    while True:
        new_positions = king_moves(*positions[i])
        for new_position in new_positions:
            if not (new_position[0], new_position[1]) in [(p[0], p[1]) for p in positions]:
                positions.append(new_position)
            if (new_position[0], new_position[1]) == (pawn_A_row, pawn_A_column):
                return new_position[3]
        print positions
        i += 1


# examples:

print my_algo('a1', 'd4', 'c3')
print my_algo('h1', 'a8', 'b7')
print my_algo('h1', 'h8', 'h3')
