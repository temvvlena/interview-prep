BOARD_COLS = 7
BOARD_ROWS = 6


class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1]

    def print_board(self):
        print("\n")
        for c in range(BOARD_COLS):
            print(f" ({c + 1})", end="")
        print("\n")
        for row in range(len(self.board)):
            print('| ', end="")
            for col in range(len(self.board[0])):
                print(f"{self.board[row][col]} | ", end="")
            print('\n')
        print(f"{'-' * 35}\n")

    def which_turn(self):
        players = ["X", "O"]
        return players[self.turns % 2]

    def turn(self, column):
        for r in range(BOARD_ROWS - 1, -1, -1):
            if self.board[r][column] == " ":
                self.board[r][column] = self.which_turn()
                self.last_move = [r, column]
                self.turns += 1
                return True
        return False


def play():
    g = Board()

    game_over = False
    while not game_over:
        g.print_board()
        valid_move = False
        while not valid_move:
            user_move = input(f"{g.which_turn()}'s Turn - pick a column (1-{BOARD_COLS}): ")
            try:
                valid_move = g.turn(int(user_move) - 1)
            except:
                print(f"Please choose a number between 1 and {BOARD_COLS}")
    g.print_board()


if __name__ == "__main__":
    play()
