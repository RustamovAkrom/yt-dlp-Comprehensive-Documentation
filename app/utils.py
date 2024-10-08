from colorama import Fore, Style


def print_menu(s: str):
    print(Fore.BLUE, s, Style.RESET_ALL)


def print_error(s: str):
    print(Fore.RED, s, Style.RESET_ALL)


def print_success(s: str):
    print(Fore.GREEN, s, Style.RESET_ALL)


def print_info(s: str):
    print(Fore.BLUE, s, Style.RESET_ALL)