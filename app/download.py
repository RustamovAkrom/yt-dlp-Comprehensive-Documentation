import yt_dlp as youtube_dl


class YouTubeDownloader:
    def __init__(self, url_list: list[str], base_path=None, base_quiet=False):

        self.url_list = url_list
        self.base_path = base_path
        self.base_quiet = base_quiet

    def download_video(self, path="download/videos/", format="best"):
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

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.url_list)

        return f"Successfully download video to path: {path}"
        
    def get_info_dict(self):
        """
        Извлечение метаданных.
        """

        info_list = []

        ydl_opts = {"quiet": True, "skip_download": True}

        for url in self.url_list:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                info_list.append(info_dict)

        return info_list

    def download_audio(self, path="download/audios/", format="bestaudio/best"):
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

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.url_list)
        
        return f"Successfully download audio to path: {path}"

    def download_playlist(self, path="download/playlists/", format="best"):
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

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.url_list)

        return f"Successfully download playlist to path: {path}"