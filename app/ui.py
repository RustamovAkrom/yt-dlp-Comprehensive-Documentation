from app.download import YouTubeDownloader
from app.utils import print_menu, print_error
from app.services import download_video, download_audio, download_playlist


def main_menu():
    print_menu("[Dovload Video] -----------------> 1")
    print_menu("[Dovload Auido] -----------------> 2")
    print_menu("[Dovload Play List] -------------> 3")
    print_menu("[Quit] --------------------------> q")

    choice = input("[>]:")

    if choice == "q":
        return
    
    try:
        download_menu(choice)
    except (Exception) as e:
        print_error(f"Exception: {e}")
    
    main_menu()

def download_menu(choice: str):
    match choice:
        case "0":
            exit(1)
        case "1":
            download_video()
        case "2":
            download_audio()
        case "3":
            download_playlist()
