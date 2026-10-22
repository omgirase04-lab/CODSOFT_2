# Tic-Tac-Toe AI — CodSoft Internship Task 2

A playable command-line Tic-Tac-Toe game in which a human (`X`) plays against an AI (`O`). The AI uses **Minimax with alpha-beta pruning** to choose optimal moves and cannot be beaten when it plays correctly.

## Requirements

- Python 3.9 or newer
- No third-party packages

## Run the game

Open a terminal in this folder and run:

```bash
python game.py
```

Choose a numbered position from 1 to 9:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

You are `X`, and the AI is `O`. Enter `q` to quit. The game reports a win or draw at the end.

## Run tests

```bash
python -m unittest -v
```

The tests cover win and draw detection, move validation, AI winning moves, AI blocking moves, terminal positions, and reset functionality.

## How the AI works

1. The AI considers every empty square as a candidate move.
2. Minimax recursively simulates the remaining game: the AI (`O`) maximizes the score, while the human (`X`) minimizes it.
3. A win for the AI receives a positive score, a human win receives a negative score, and a draw receives zero.
4. Earlier wins and later losses are preferred, so the AI tries to win quickly and delay defeat.
5. Alpha-beta pruning stops exploring branches that cannot change the final choice, reducing unnecessary search.

Because Tic-Tac-Toe has a small state space, this exhaustive search is fast enough for a command-line game.

## Project structure

```text
CODSOFT_TASK2/
├── game.py
├── test_game.py
├── README.md
├── requirements.txt
└── .gitignore
```

## GitHub publishing

Create or use the repository name specified by your internship coordinator. The internship PDF asks interns to keep their tasks in a separate repository using the `CODSOFT_TASKSNO` naming convention; if one repository is intended for all tasks, place this project in a `Task2/` subfolder.

```bash
git init
git add .
git commit -m "Complete CodSoft Task 2: Tic-Tac-Toe Minimax AI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CODSOFT_TASKSNO.git
git push -u origin main
```

Replace `YOUR_USERNAME` and the repository name with your actual details.

## Suggested demo video (60–90 seconds)

1. Introduce the project as CodSoft AI Internship Task 2.
2. Show the board and explain that you play as `X`.
3. Demonstrate the AI blocking an immediate threat or taking a winning move.
4. Explain Minimax and alpha-beta pruning briefly.
5. Run `python -m unittest -v`.
6. Show the real GitHub repository link.

## Suggested LinkedIn caption

> Completed Task 2 of my CodSoft Artificial Intelligence internship: Tic-Tac-Toe AI using Python. The AI uses the Minimax algorithm with alpha-beta pruning to evaluate possible moves and play optimally against a human player. I also added unit tests for game logic and AI decisions.
>
> GitHub: [add your real repository link]
>
> @CODSOFT #codsoft #artificialintelligence #python #internship #minimax
