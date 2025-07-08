import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import MatrixScanner
from kmk.keys import KC
from kmk.extensions.encoder import EncoderHandler

keyboard = KMKKeyboard()

# matrix config
row_pins = (board.D0,)
col_pins = (board.D1, board.D2, board.D3, board.D4, board.D5)

keyboard.matrix = MatrixScanner(
    rows=row_pins,
    columns=col_pins,
    intervals=5,
    value_when_pressed=False,
    diode_orientation='ROW2COL'
)

# encoder config
encoder = EncoderHandler()
encoder.pins = (
    (board.D6, board.D7),  # left encoder
    (board.D8, board.D9),  # right encoder
)
keyboard.extensions.append(encoder)

# encoder handlers
def handle_encoder_0(index, direction):
    if direction == 1:
        keyboard.send(KC.VOLU)  # volume up
    elif direction == -1:
        keyboard.send(KC.VOLD)  # volume down

def handle_encoder_1(index, direction):
    if direction == 1:
        keyboard.send(KC.RIGHT)  # next beatmap/menu
    elif direction == -1:
        keyboard.send(KC.LEFT)   # previous beatmap/menu

encoder.handlers = [handle_encoder_0, handle_encoder_1]

# keymap
keyboard.keymap = [
    [KC.Z, KC.X, KC.ENTER, KC.ESC, KC.SPACE]  # can change later maybe
]

if __name__ == '__main__':
    keyboard.go()
