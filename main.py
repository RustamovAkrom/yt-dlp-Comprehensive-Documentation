import yt_dlp as youtube_dl


class YouTubeDownloader:
    def __init__(self, url_list: list[str], base_path=None, base_quiet=False):

        self.url_list = url_list
        self.base_path = base_path
        self.base_quiet = base_quiet

    def download_video(self, path="download/videos/", format="best") -> None:
        """
        Загрузка видео.
        """

        path = path + "%(title)s.%(ext)s"
        ydl_opts = {}

        ydl_opts["format"] = format
        ydl_opts["quiet"] = self.base_quiet

        if self.base_path is not None:
            ydl_opts["outtmpl"] = self.base_path
        else:
            ydl_opts["outtmpl"] = path

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(self.url_list)
        except Exception as e:
            print(e)

        else:
            print("Successfully downloaded.")

    def get_info_dict(self) -> list[dict]:
        """
        Извлечение метаданных.
        """

        info_list = []

        ydl_opts = {"quiet": True, "skip_download": True}
        try:
            for url in self.url_list:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=False)
                    info_list.append(info_dict)
        except Exception as e:
            print(e)

        return info_list

    def download_audio(self, path="download/audios/", format="bestaudio/best") -> None:
        """
        Загрузка аудио.
        """

        path = path + "%(title)s.%(ext)s"
        ydl_opts = {}

        ydl_opts["format"] = format
        ydl_opts["extractaudio"] = True
        ydl_opts["quiet"] = self.base_quiet

        if self.base_path is not None:
            ydl_opts["outtmpl"] = self.base_path
        else:
            ydl_opts["outtmpl"] = path

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(self.url_list)

        except Exception as e:
            print(e)

        else:
            print("Successfully downloaded.")

    def download_playlist(self, path="download/playlists/", format="best") -> None:
        """
        Загрузка плейлиста.
        """

        path + path + "%(playlist)s/%(title)s.%(ext)s"
        ydl_opts = {}

        ydl_opts["format"] = format
        ydl_opts["quiet"] = self.base_quiet

        if self.base_path is not None:
            ydl_opts["outtmpl"] = self.base_path
        else:
            ydl_opts["outtmpl"] = path

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(self.url_list)
        except Exception as e:
            print(e)

        else:
            print("Successfully downloaded.")


if __name__ == "__main__":

    downloader = YouTubeDownloader(
        [
            "https://www.youtube.com/shorts/y9OaB2FHG7s?feature=share",
            "https://www.youtube.com/shorts/7H4NfZ-jMzM?feature=share",
        ]
    )

    # print(downloader.get_info_dict())

    # downloader.download_video()
    # downloader.download_audio()
    # downloader.download_playlist()
