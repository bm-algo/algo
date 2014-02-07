# Problem Statement
#     Crow Keith is looking at the goose cage in the zoo. The bottom of the cage 
#     is divided into a grid of square cells. There are some birds sitting on 
#     those cells (with at most one bird per cell). Some of them are geese and 
#     all the others are ducks. Keith wants to know which birds are geese. 
#     He knows the following facts about them:

#     There is at least one goose in the cage.
#     Each bird within Manhattan distance dist of any goose is also a goose.

# You are given a String[] field and the int dist. The array field describes 
# the bottom of the cage. Each character of each element of field describes 
# one of the cells. The meaning of individual characters follows.

#     The character 'v' represents a cell that contains a bird.
#     The character '.' represents an empty cell.

# Return the number of possible sets of geese in the cage, modulo 1,000,000,007. 
# Note that for some of the test cases there can be no possible sets of geese.
 
# Definition
        
# Class:  GooseInZooDivTwo
# Method: count
# Parameters: String[], int
# Returns:    int
# Method signature:   int count(String[] field, int dist)
# (be sure your method is public)


def count(field, dist):
    column_count = len(field[0])
    row_count = len(field)

    def next_positions(current_row, current_column, step):
        positions = []
        for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            new_row = current_row + i
            new_column = current_column + j
            if row_count > new_row > -1 and column_count > new_column > -1:
                positions.append((new_row, new_column, step + 1))
        return positions

    def dist_positions(current_row, current_column):
        i = 0
        positions = [(current_row, current_column, 0)]
        while True:
            if i == len(positions):
                return []
            new_positions = next_positions(*positions[i])
            # print 'new_positions', new_positions
            for new_position in new_positions:
                if new_position[2] > dist:
                    return [(p[0], p[1]) for p in positions]
                if not (new_position[0], new_position[1]) in [(p[0], p[1]) for p in positions]:
                    positions.append(new_position)
            i += 1

    def goose_positions(goose_row, goose_column):
        positions = [(goose_row, goose_column)]
        for p in positions:
            dp = dist_positions(*p)
            for row, column in dp:
                if field[row][column] == 'v' and (row, column) not in positions:
                    positions.append((row, column))
        return positions

    goose_sets_count = 0
    marked_as_goose = []

    for row_index, row in enumerate(field):
        for column_index, column in enumerate(row):
            if field[row_index][column_index] == 'v' and\
                    (row_index, column_index) not in marked_as_goose:
                positions = goose_positions(row_index, column_index)
                marked_as_goose += [(row, column) for row, column in positions]
                goose_sets_count += 1

    return (2 ** goose_sets_count - 1) % 1000000007

# example:

# print 'ANSWER', count(['v.v.v'], 4)

field = ["v.v..................v............................"
,".v......v..................v.....................v"
,"..v.....v....v.........v...............v......v..."
,".........vvv...vv.v.........v.v..................v"
,".....v..........v......v..v...v.......v..........."
,"...................vv...............v.v..v.v..v..."
,".v.vv.................v..............v............"
,"..vv.......v...vv.v............vv.....v.....v....."
,"....v..........v....v........v.......v.v.v........"
,".v.......v.............v.v..........vv......v....."
,"....v.v.......v........v.....v.................v.."
,"....v..v..v.v..............v.v.v....v..........v.."
,"..........v...v...................v..............v"
,"..v........v..........................v....v..v..."
,"....................v..v.........vv........v......"
,"..v......v...............................v.v......"
,"..v.v..............v........v...............vv.vv."
,"...vv......v...............v.v..............v....."
,"............................v..v.................v"
,".v.............v.......v.........................."
,"......v...v........................v.............."
,".........v.....v..............vv.................."
,"................v..v..v.........v....v.......v...."
,"........v.....v.............v......v.v............"
,"...........v....................v.v....v.v.v...v.."
,"...........v......................v...v..........."
,"..........vv...........v.v.....................v.."
,".....................v......v............v...v...."
,".....vv..........................vv.v.....v.v....."
,".vv.......v...............v.......v..v.....v......"
,"............v................v..........v....v...."
,"................vv...v............................"
,"................v...........v........v...v....v..."
,"..v...v...v.............v...v........v....v..v...."
,"......v..v.......v........v..v....vv.............."
,"...........v..........v........v.v................"
,"v.v......v................v....................v.."
,".v........v................................v......"
,"............................v...v.......v........."
,"........................vv.v..............v...vv.."
,".......................vv........v.............v.."
,"...v.............v.........................v......"
,"....v......vv...........................v........."
,"....vv....v................v...vv..............v.."
,".................................................."
,"vv........v...v..v.....v..v..................v...."
,".........v..............v.vv.v.............v......"
,".......v.....v......v...............v............."
,"..v..................v................v....v......"
,".....v.....v.....................v.v......v......."]

dist = 3

print count(field, dist)

