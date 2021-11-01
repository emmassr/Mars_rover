
from functools import reduce

def move_forward(input):
    if input["orientation"] == 'E':
        return {'x': input['x'] + 1, 'y': input['y'], 'orientation': input['orientation']}
    elif input["orientation"] == 'N':
        return {'x': input['x'], 'y': input['y'] + 1, 'orientation': input['orientation']}
    elif input["orientation"] == 'S':
        return {'x': input['x'], 'y': input['y'] - 1, 'orientation': input['orientation']}
    elif input["orientation"] == 'W':
        return {'x': input['x'] - 1, 'y': input['y'], 'orientation': input['orientation']}

def rotate_left(input):
    if input['orientation'] == 'W':
        return {'x': input['x'], 'y': input['y'], 'orientation': 'S'}
    elif input['orientation'] == 'E':
        return {'x': input['x'], 'y': input['y'], 'orientation': 'N'}
    elif input['orientation'] == 'N':
        return {'x': input['x'], 'y': input['y'], 'orientation': 'W'}
    elif input['orientation'] == 'S':
        return {'x': input['x'], 'y': input['y'], 'orientation': 'E'}

def rotate_right(input):
    if input['orientation'] == 'S':
        return {'x': input['x'], 'y': input['y'], 'orientation': 'W'}
    if input['orientation'] == 'N':
        return {'x': input['x'], 'y': input['y'], 'orientation': 'E'}
    if input['orientation'] == 'W':
        return {'x': input['x'], 'y': input['y'], 'orientation': 'N'}
    if input['orientation'] == 'E':
        return {'x': input['x'], 'y': input['y'], 'orientation': 'S'}

# def final_position_of_mars_rover(starting_position,moves):
#         if len(moves) == 1:
#             if moves == ['L']:
#                 return rotate_left(starting_position)
#             elif moves == ['R']:
#                 return rotate_right(starting_position)
#             else:
#                 return move_forward(starting_position)
#         else:
#             #if len(moves) == 2:
#                 #for element in moves
#              # if element in moves is L return rotate left
#             #if R rotate right
#             #if F move forward
#             return move_forward(rotate_left(starting_position))

def final_position_of_mars_rover(starting_position, moves,x_size, y_size):
    position = starting_position
    for move in moves:
        if move == 'R':
            if validate_position(rotate_right(position), x_size, y_size):
                position = rotate_right(position)
            else:
                return position
        elif move == 'L':
            if validate_position(rotate_left(position), x_size, y_size):
                position = rotate_left(position)
            else:
                return position
        else:
            if validate_position(move_forward(position), x_size, y_size):
                position = move_forward(position)
            else:
                return position
    return position


def validate_position(position, x_size, y_size):
    return y_size >= position['y'] >= 0 and x_size >= position['x'] >= 0

# build the validate position function to return True/False

# write one more test to validate the x_position against the x_size
# then use this validate position in final position method
# for each move call this validate function to check whether the position is valid
#     if valid awesome carry on with next move
#     if not valid stop moving and return final valid position

# new stuff to investigate...fix the logic in the final position of mars rover method.

# 