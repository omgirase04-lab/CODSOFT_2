"""Tic-Tac-Toe AI using Minimax with alpha-beta pruning.

CodSoft Artificial Intelligence Internship - Task 2.
"""

from math import inf


HUMAN = "X"
AI = "O"
EMPTY = " "


class TicTacToe:
    """Game engine and unbeatable Minimax AI."""

    WINNING_LINES = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )

    def __init__(self):
        self.board = [EMPTY] * 9

    def available_moves(self, board=None):
        """Return all currently empty positions as indices."""
        board = self.board if board is None else board
        return [i for i, cell in enumerate(board) if cell == EMPTY]

    @classmethod
    def winner(cls, board):
        """Return X or O if there is a winner, otherwise None."""
        for a, b, c in cls.WINNING_LINES:
            if board[a] != EMPTY and board[a] == board[b] == board[c]:
                return board[a]
        return None

    @classmethod
    def is_draw(cls, board):
        return cls.winner(board) is None and EMPTY not in board

    @classmethod
    def is_terminal(cls, board):
        return cls.winner(board) is not None or EMPTY not in board

    def minimax(self, board, is_maximizing, depth=0, alpha=-inf, beta=inf):
        """Score a position recursively; alpha-beta pruning skips irrelevant branches."""
        result = self.winner(board)
        if result == AI:
            return 10 - depth
        if result == HUMAN:
            return depth - 10
        if EMPTY not in board:
            return 0

        if is_maximizing:
            best_score = -inf
            for move in self.available_moves(board):
                board[move] = AI
                score = self.minimax(board, False, depth + 1, alpha, beta)
                board[move] = EMPTY
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score

        best_score = inf
        for move in self.available_moves(board):
            board[move] = HUMAN
            score = self.minimax(board, True, depth + 1, alpha, beta)
            board[move] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

    def best_move(self, board=None):
        """Find the best move for O; returns None if no move is possible."""
        board = self.board if board is None else list(board)
        if self.is_terminal(board):
            return None

        best_score = -inf
        move_choice = None
        for move in self.available_moves(board):
            board[move] = AI
            score = self.minimax(board, False, depth=1)
            board[move] = EMPTY
            if score > best_score:
                best_score = score
                move_choice = move
        return move_choice

    def play_move(self, position, player):
        """Place X or O at a 1-based position. Return True if accepted."""
        if player not in (HUMAN, AI):
            raise ValueError("Player must be 'X' or 'O'.")
        if not isinstance(position, int) or not 1 <= position <= 9:
            return False
        if self.board[position - 1] != EMPTY or self.is_terminal(self.board):
            return False
        self.board[position - 1] = player
        return True

    def reset(self):
        self.board = [EMPTY] * 9


def render_board(board):
    """Return a readable board with numbers in empty cells."""
    cells = [str(i + 1) if value == EMPTY else value for i, value in enumerate(board)]
    return (
        f"\n {cells[0]} | {cells[1]} | {cells[2]}\n"
        "---+---+---\n"
        f" {cells[3]} | {cells[4]} | {cells[5]}\n"
        "---+---+---\n"
        f" {cells[6]} | {cells[7]} | {cells[8]}\n"
    )


def main():
    game = TicTacToe()
    print("=" * 48)
    print("            TIC-TAC-TOE AI")
    print("     CodSoft Artificial Intelligence - Task 2")
    print("=" * 48)
    print("You are X; the AI is O. Choose a position from 1 to 9.")
    print("Enter q at any time to quit.")
    print(render_board(game.board))

    while not game.is_terminal(game.board):
        raw = input("Your move (1-9): ").strip().lower()
        if raw in {"q", "quit", "exit"}:
            print("Thanks for playing. Goodbye!")
            return
        if not raw.isdigit() or not game.play_move(int(raw), HUMAN):
            print("Invalid move. Choose an empty position numbered 1-9.")
            continue

        print(render_board(game.board))
        if game.winner(game.board) == HUMAN:
            break
        if game.is_draw(game.board):
            break

        move = game.best_move()
        if move is not None:
            game.play_move(move + 1, AI)
            print(f"AI chooses position {move + 1}.")
            print(render_board(game.board))

    result = game.winner(game.board)
    if result == HUMAN:
        print("Congratulations! You won.")
    elif result == AI:
        print("AI wins. Better luck next time!")
    else:
        print("It's a draw!")
    print("Run the program again to play a new game.")


if __name__ == "__main__":
    main()
