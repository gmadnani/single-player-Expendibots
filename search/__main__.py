import sys
import json

from search.util import print_move, print_boom, print_board, find_solution, move_function, print_sol


def main():
    with open(sys.argv[1]) as file:
        data = json.load(file)

        # TODO: find and print winning action sequence
        win_pos = find_solution(data)
        paths,booms = move_function(data, win_pos)
        print_sol(data, paths, booms)


        #print()
        #print("Data to help check validity of solution.")
        #print(data)
        #print("Winning Positions:",win_pos)
        #print("Path to win:",paths)

if __name__ == '__main__':
    main()
