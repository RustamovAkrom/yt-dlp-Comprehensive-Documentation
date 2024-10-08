from app.download import YouTubeDownloader


def download_video():
    print("Ending code: end")

    urls = []

    while True:
        input_url = input("[Enter Url]: ")
        if input_url == "end":
            break
        urls.append(input_url)
        
    downloader = YouTubeDownloader(urls)
    downloader.download_video()


def download_audio():
    print("Ending code: end")

    urls = []

    while True:
        input_url = input("[Enter Url]: ")
        if input_url == "end":
            break
        urls.append(input_url)
    downloader = YouTubeDownloader(urls)
    downloader.download_audio()


def download_playlist():
    print("Ending code: end")

    urls = []

    while True:
        input_url = input("[Enter Url]: ")
        if input_url == "end":
            break
        urls.append(input_url)
    downloader = YouTubeDownloader(urls)
    downloader.download_playlist()