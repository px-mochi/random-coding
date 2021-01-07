'''
Something about 
- Unlimited Board
- Snek
- If snake uses E, it grows to the apple
- The rest is just Front (F), Left (L), Right (R)

Many inputs
- Input 1: Number of turns
- Input 2 + whatever 1 was: <Number of moves> <Moves>
EG:
2
6 ELERFF
6 FLERFF

Output
- If snek ded, print the turn number that it died on
- If snek win, print "YES" 
'''

def get_snake_direction(current_direction, move):
    # Default direction is North
    if current_direction == 'North':
        revised_move = move
    elif current_direction == 'West':
        if move == "L":
            revised_move = "D"
        elif move == "R":
            revised_move = "F"
        elif move == "F" or "E":
            revised_move = "L"
        else:
            print("This should not happen, impossible move?")
    elif current_direction == "South":
        if move == "L":
            revised_move = "R"
        elif move == "R":
            revised_move = "L"
        elif move == "F" or "E":
            revised_move = "D"
        else:
            print("This should not happen, impossible move?")
    else: # East
        if move == "L":
            revised_move = "F"
        elif move == "R":
            revised_move = "D"
        elif move == "F" or "E":
            revised_move = "R"
        else:
            print("This should not happen, impossible move?")

    return revised_move

def test_snake_turn(moves, movement):
    # Max snake length = 2401 (1 + 2400 'E')
    ''' Example board
    1------------ 2401
    |
    |
    |      x
    |
    2401
    x = snake. It starts at x:0, y:0. Since the board is infinite, i'm going to accept negative numbers.
    '''
    snake_length = 1
    x_positions = {0:0}
    y_positions = {0:0}
    compass = 'North'
    revised_move_to_compass = {"F":'North',"E":'North',"L":'West',"R":'East'}

    for i in range(moves):
        move = movement[i]
        
        if i == 0:
            current_direction = compass
        else:
            current_direction = revised_move_to_compass[movement[i-1]]
        revised_move = get_snake_direction(current_direction, move)
        # print(revised_move)

        # snek mapping
        all_snek_move_num_list =  list(x_positions.keys()) # Should be the same as y
        snek_positions = []
        for past_move in all_snek_move_num_list:
            snek_positions.append("{}:{}".format(x_positions[past_move],y_positions[past_move]))

        if revised_move == "L":
            y_positions[i+1] = y_positions[i]
            x_positions[i+1] = x_positions[i] - 1
        elif revised_move == "R":
            y_positions[i+1] = y_positions[i]
            x_positions[i+1] = x_positions[i] + 1
        elif revised_move == "F" or revised_move == "E":
            y_positions[i+1] = y_positions[i] + 1
            x_positions[i+1] = x_positions[i]
        else: # D
            y_positions[i+1] = y_positions[i] - 1
            x_positions[i+1] = x_positions[i]
            
        if move != "E":
            to_delete_x = sorted(list(x_positions.keys()))[0]
            to_delete_y = sorted(list(y_positions.keys()))[0]
            x_positions.pop(to_delete_x)
            y_positions.pop(to_delete_y)

        # Check if snake is eating itself
        current_x = x_positions[i+1]
        current_y = y_positions[i+1]
        current_pos = "{}:{}".format(current_x,current_y)
        if current_pos in snek_positions:
            print("{}--> {}:{}".format(i+1, current_x,current_y))
            print('move: {} | current_pos: {} | sneky {}'.format(move,current_pos,snek_positions))
            return i+1
        if i == moves - 1:
            return "YES"
        

def main():
    num_of_tests = input()
    for i in range(int(num_of_tests)):
        test_str = input()
        moves = int(test_str[0])
        movement = list(test_str.replace(str(moves),'').replace(' ',''))
        test_print = test_snake_turn(moves, movement)
        print(test_print)

if __name__ == '__main__':
    main()