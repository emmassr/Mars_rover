# test the orientation
#test the movement

#1. Decide what data structure we are going to
# use for coordinates and direction

#2. Start with testing orientation e.g. Input -> 2, 3 north, rotate_left (L input)
# Output -> 2, 3, west
from robot import move_forward, rotate_left, rotate_right, final_position_of_mars_rover, validate_position


def test_move_forward_in_east_direction():
    input = {'x': 2, 'y': 3, 'orientation': 'E'}
    assert move_forward(input) == {'x': 3, 'y': 3, 'orientation': 'E'}

def test_move_forward_in_north_direction():
    input = {'x': 2, 'y': 3, 'orientation': 'N'}
    assert move_forward(input) == {'x': 2, 'y': 4, 'orientation': 'N'}

#testmove forward in south and west direction!
def test_move_forward_in_south_direction():
    input = {'x': 2, 'y': 3, 'orientation': 'S'}
    assert move_forward(input) == {'x': 2, 'y': 2, 'orientation': 'S'}

def test_move_forward_in_west_direction():
    input = {'x': 2, 'y': 3, 'orientation': 'W'}
    assert move_forward(input) == {'x': 1, 'y': 3, 'orientation': 'W'}


def test_rotate_left_90_degrees_from_west():
    input = {'x': 2, 'y': 3, 'orientation': 'W'}
    assert rotate_left(input) == {'x': 2, 'y': 3, 'orientation': 'S'}

def test_rotate_left_90_degrees_from_east():
    input = {'x': 2, 'y': 3, 'orientation': 'E'}
    assert rotate_left(input) == {'x': 2, 'y': 3, 'orientation': 'N'}

def test_rotate_left_90_degrees_from_north():
    input = {'x': 2, 'y': 3, 'orientation': 'N'}
    assert rotate_left(input) == {'x': 2, 'y': 3, 'orientation': 'W'}

def test_rotate_left_90_degrees_from_south():
    input = {'x': 5, 'y': 6, 'orientation': 'S'}
    assert rotate_left(input) == {'x': 5, 'y': 6, 'orientation': 'E'}

def test_rotate_right_90_degrees_from_south():
    input = {'x': 2, 'y': 3, 'orientation': 'S'}
    assert rotate_right(input) == {'x': 2, 'y': 3, 'orientation': 'W'}


def test_rotate_right_90_degrees_from_north():
    input = {'x': 2, 'y': 3, 'orientation': 'N'}
    assert rotate_right(input) == {'x': 2, 'y': 3, 'orientation': 'E'}

def test_rotate_right_90_degrees_from_west():
    input = {'x': 2, 'y': 3, 'orientation': 'W'}
    assert rotate_right(input) == {'x': 2, 'y': 3, 'orientation': 'N'}

def test_rotate_right_90_degrees_from_east():
    input = {'x': 2, 'y': 3, 'orientation': 'E'}
    assert rotate_right(input) == {'x': 2, 'y': 3, 'orientation': 'S'}

def test_one__rotation_move_left():
    starting_position = {'x': 2, 'y': 3, 'orientation': 'N'}
    moves = ['L']
    assert final_position_of_mars_rover(starting_position,moves, 5,5) == {'x': 2, 'y': 3, 'orientation': 'W'}

def test_two_moves():
    starting_position = {'x': 2, 'y': 3, 'orientation': 'N'}
    moves = ['L','F']
    assert final_position_of_mars_rover(starting_position,moves,5,5) == {'x': 1, 'y': 3, 'orientation': 'W'}

def test_one_move_forward():
    starting_position = {'x': 2, 'y': 3, 'orientation': 'N'}
    moves = ['F']
    assert final_position_of_mars_rover(starting_position,moves,5,5) == {'x': 2, 'y': 4, 'orientation': 'N'}

def test_one_rotation_move_right():
    starting_position = {'x': 2, 'y': 3, 'orientation': 'N'}
    moves = ['R']
    assert final_position_of_mars_rover(starting_position,moves,5,5) == {'x': 2, 'y': 3, 'orientation': 'E'}


def test_final_position_using_example_one():
    starting_position = {'x': 2, 'y': 3, 'orientation': 'E'}
    moves = ['L','F','R','F','F']
    assert final_position_of_mars_rover(starting_position,moves,4,8) == {'x': 4, 'y': 4, 'orientation': 'E'}

def test_final_position_using_example_two():
    starting_position = {'x': 0, 'y': 2, 'orientation': 'N'}
    moves = ['F', 'F', 'L', 'F', 'R', 'F', 'F']
    assert final_position_of_mars_rover(starting_position,moves,4,8) == {'x': 0, 'y': 4, 'orientation': 'W'}

def test_invalid_y_position_on_grid():
    position = {'x':1, 'y': 2, 'orientation': 'N' }
    x_size = 5
    y_size = 1
    assert validate_position(position, x_size, y_size) == False

def test_invalid_negative_y_position_on_grid():
    position = {'x':1, 'y': -1, 'orientation': 'N' }
    x_size = 5
    y_size = 1
    assert validate_position(position, x_size, y_size) == False

def test_invalid_negative_x_position_on_grid():
    position = {'x':-1, 'y': 1, 'orientation': 'N' }
    x_size = 5
    y_size = 1
    assert validate_position(position, x_size, y_size) == False

def test_invalid_x_position_on_grid():
    position = {'x':5, 'y': 2, 'orientation': 'N' }
    x_size = 1
    y_size = 2
    assert validate_position(position, x_size, y_size) == False

def test_valid_x_and_y_position():
    position = {'x': 5, 'y': 2, 'orientation': 'N'}
    x_size = 6
    y_size = 2
    assert validate_position(position, x_size, y_size) == True

def test_when_x_is_zero():
    position = {'x': 0, 'y': 2, 'orientation': 'N'}
    x_size = 6
    y_size = 2
    assert validate_position(position, x_size, y_size) == True
