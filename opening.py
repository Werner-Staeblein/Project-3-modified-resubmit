from colorama import Fore


def opening_image():
    print(Fore.GREEN + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣻⢝⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⢷⡦⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣽⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢷⢾⣿⣿⡷⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣷⠱⠇⠈⡮⣹⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣞⠦⣻⠀⠀⢛⡴⢳⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣛⣛⣻⣿⣻⣿⣿⣿⣟⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠓⠓⠓⠓⠓⠛⠚⠚⠚⠚⢆⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣻⡭⢻⣟⣿⣏⣉⣿⣿⡟⢩⣍⢆⠀⠀⠀⠀
⠀⠀⡰⣛⡤⢜⣮⠕⠊⠉⠉⠉⠺⢝⡇⢤⣎⢦⠀⠀⠀
⠀⡴⠻⣀⡨⡞⠁⠀⠀⠀⠀⠀⠀⠀⠹⡇⣀⠝⢣⠀⠀
⣼⣔⣊⣑⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣊⣁⣢⣵⡀""")


def instructions():
    print("="*78)
    print("*" * 28 + " HOW TO PLAY THE GAME " + "*" * 28)
    print()
    print("""
    1. This is a traditional hangman game
    2. The goal is to guess well-known capital cities with a maximum of 6 tries         
    3. Guess the right capital city to escape the situation""")
    print()
    print("*" * 78)
    print("="*78)
    print("\n")
