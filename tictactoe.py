"""Tic Tac Toe

Modified version for the final project.

Features:
1. Custom size, color, and centering for X and O.
2. Prevention of moves on occupied squares.
3. Detection of wins and ties.
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    color('black')
    width(1)

    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player centered with custom color and width."""
    color('red')
    width(8)

    # Keep a margin so the X is centered inside the square.
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    """Draw O player centered with custom color and width."""
    color('blue')
    width(8)

    # Start at the bottom-center of the circle to keep it centered.
    up()
    goto(x + 67, y + 20)
    setheading(0)
    down()
    circle(47)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


# Game state:
# - player stores the current turn: 0 represents X and 1 represents O.
# - board maps each occupied grid coordinate to the player who selected it.
# - game_over prevents additional moves after a win or a tie.
state = {
    'player': 0,
    'board': {},
    'game_over': False
}


# Drawing functions associated with each player.
players = [drawx, drawo]

# Text labels used to report the winner.
symbols = ['X', 'O']


def check_winner():
    """Return the winning player or None if there is no winner."""
    board = state['board']

    # Possible winning combinations using board coordinates.
    winning_lines = [
        # Rows
        [(-200, 66), (-67, 66), (66, 66)],
        [(-200, -67), (-67, -67), (66, -67)],
        [(-200, -200), (-67, -200), (66, -200)],

        # Columns
        [(-200, 66), (-200, -67), (-200, -200)],
        [(-67, 66), (-67, -67), (-67, -200)],
        [(66, 66), (66, -67), (66, -200)],

        # Diagonals
        [(-200, 66), (-67, -67), (66, -200)],
        [(66, 66), (-67, -67), (-200, -200)]
    ]

    # Review every possible winning line.
    for line_positions in winning_lines:

        # Continue only if all three positions have already been played.
        if all(position in board for position in line_positions):
            values = [board[position] for position in line_positions]

            # The same player occupying all three positions means a win.
            if values[0] == values[1] == values[2]:
                return values[0]

    return None


def show_result(message):
    """Display the final result on the game window."""
    up()
    goto(0, 165)
    color('green')

    write(
        message,
        align='center',
        font=('Arial', 22, 'bold')
    )

    update()


def tap(x, y):
    """Process a move only if the square is available."""

    # Ignore clicks after the game has finished.
    if state['game_over']:
        return

    # Convert the click coordinates to the lower-left corner
    # of the corresponding grid square.
    x = floor(x)
    y = floor(y)

    # Use the square coordinates as a unique board position.
    position = (x, y)

    # Ignore the click if the square is already occupied.
    if position in state['board']:
        return

    player = state['player']
    draw = players[player]

    # Save the move before changing to the next player.
    state['board'][position] = player

    # Draw the symbol that corresponds to the current player.
    draw(x, y)
    update()

    # Check whether the current move created a winning combination.
    winner = check_winner()

    if winner is not None:
        state['game_over'] = True
        show_result(f'{symbols[winner]} wins!')
        return

    # If all nine squares are occupied and nobody won,
    # the game ends in a tie.
    if len(state['board']) == 9:
        state['game_over'] = True
        show_result('Tie game!')
        return

    # Change player only if the game continues.
    state['player'] = not player


# Configure the game window.
setup(420, 420, 370, 0)
title('Tic Tac Toe')

hideturtle()
tracer(False)

# Draw the initial board.
grid()
update()

# Register mouse clicks and start the Turtle event loop.
onscreenclick(tap)
done()