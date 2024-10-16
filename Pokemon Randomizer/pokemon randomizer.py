# Import necessary libraries
import subprocess
import time
import pyautogui

# Assign global variables for key mappings to simplify changes and improve readability
A = 'x'
B = 'z'
START = 'enter'
SELECT = 'backspace'
SHIFT = 'shift'
TAB = 'tab'
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
game_path = r"C:\Users\justi\OneDrive\Desktop\PokeRandoZX-v4_6_0\[FR] Randomized Nuzlocke.gba"


def run_randomizer():
    """
    Runs the batch file that executes the randomizer process.
    This process modifies the game file to apply randomization settings.
    """
    batch_file_path = r"C:\Users\justi\OneDrive\Desktop\PokeRandoZX-v4_6_0\launcher_WINDOWS.bat"
    # Execute the batch file using subprocess to ensure any paths or commands are correctly handled
    subprocess.run(["cmd", "/c", batch_file_path], check=True)


def run_game(file_path: str):
    """
    Launches the game using the file path provided.
    This function relies on the operating system's file association to open the game with the default emulator.
    """
    # Use cmd to start the game file, allowing the associated emulator to run it
    subprocess.run(["cmd", "/c", "start", "", file_path])


def press_key(key: str, delay: float = 0.5):
    """
    Simulates pressing a key by first pressing it down and then releasing it.
    Includes a delay after the key press to account for reaction time in the game or emulator.

    Parameters:
    - key: The key to simulate pressing.
    - delay: How long to wait after pressing the key, in seconds.
    """
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    time.sleep(delay)


def fast_forward():
    """
    Activates the emulator's fast-forward function to speed up gameplay.
    This is especially useful for skipping through lengthy dialogues or animations quickly.
    """
    # The specific key combination for fast-forwarding depends on the emulator's settings
    pyautogui.hotkey(SHIFT, TAB)
    # Wait a bit after activating fast-forward to let it take effect
    time.sleep(.2)


def name_main_character():
    """
    Automates the process of naming the main character.
    Uses a predefined sequence of key presses to input the name.
    """
    # Sequence to navigate through the naming screen and input a specific name
    # Adjust the sequence based on the desired name and on-screen keyboard layout
    delay = 0.2
    for i in range(2):
        press_key(DOWN, delay)
    for i in range(3):
        press_key(LEFT, delay)
    press_key(A)
    press_key(SELECT)
    for i in range(2):
        press_key(DOWN, delay)
    for i in range(3):
        press_key(RIGHT, delay)
    press_key(A)
    press_key(DOWN, delay)
    for i in range(2):
        press_key(RIGHT, delay)
    press_key(A)
    press_key(START)
    press_key(A)


def name_rival():
    """
    Automates the process of naming the rival character.
    Similar to naming the main character, it follows a specific sequence of key presses.
    """
    # Sequence to navigate and input a name for the rival
    # Customize based on the naming screen and desired name
    delay = .15
    press_key(DOWN, delay)
    for i in range(2):
        press_key(RIGHT, delay)
    press_key(A)
    press_key(SELECT)
    for i in range(2):
        press_key(DOWN, delay)
        press_key(LEFT, delay)
        press_key(A)
    press_key(DOWN, delay)
    for i in range(4):
        press_key(RIGHT, delay)
    press_key(A)
    for i in range(2):
        press_key(DOWN, delay)
    for i in range(3):
        press_key(LEFT, delay)
    press_key(A)
    for i in range(4):
        press_key(LEFT, delay)
    press_key(A)
    for i in range(2):
        press_key(UP, delay)
        press_key(LEFT, delay)
    press_key(A, delay + 0.1)
    press_key(A)


def options_menu():
    # Process through the option menu
    # Disable fast-forward to handle option menu with precise control
    fast_forward()

    press_key(START, .25)

    for i in range(2):
        press_key(UP, .25)

    fast_forward()

    press_key(A)

    fast_forward()

    press_key(RIGHT)

    for i in range(2):
        press_key(DOWN, .5)

    press_key(RIGHT, .1)

    fast_forward()

    for i in range(2):
        press_key(B, .5)


def start_game():
    """
    Main function to orchestrate the game startup sequence.
    This includes running the randomizer, launching the game, and then automating the initial setup.
    """
    # First, run the randomizer to prepare the game file
    print("Running the randomizer...")
    run_randomizer()
    print("Randomizer finished. Starting the game...")
    # Launch the game with the updated file
    run_game(game_path)

    # Wait for the game to launch and gain focus
    time.sleep(1)

    # Utilize fast-forward to speed through startup sequences
    fast_forward()

    # Process through the start screen and intro dialogues
    for i in range(2):
        press_key(START)
    for i in range(6):
        press_key(A)
    time.sleep(1)
    for i in range(11):
        press_key(A)

    # Disable fast-forward to handle naming with precise control
    fast_forward()

    # Automate naming the main character
    name_main_character()

    # Re-enable fast-forward to speed through subsequent dialogues
    fast_forward()
    for i in range(4):
        press_key(A)

    # Disable fast-forward to handle naming the rival with precise control
    fast_forward()
    name_rival()

    # Re-enable fast-forward to speed through subsequent dialogues
    fast_forward()
    for i in range(4):
        press_key(A, .25)

    options_menu()


# Execute the start_game function to run the entire automation process
start_game()
