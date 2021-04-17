import requests
import subprocess
import os
import pytube
import threading


from Interface.IError import IError


class Downloader():
    def __init__(self, current_selection, filename):
        self.install = threading.Thread(target=self.install_current_slc, args=(current_selection, filename))
        self.install.start()

        # Questa funzione permette di installare i programmi, prende come parametro
        # la selezione dalla lista e il nome del file
    def install_current_slc(self, current_selection, filename):
        req = requests.get(current_selection)

        with open(filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size = 8192):
                if chunk:
                    f.write(chunk)

        os.system(f"move {filename} Downloads/{filename}")
        subprocess.call([f"Downloads/{filename}"])


    def download_from_yt(self, url, quality, mode):
        def start_thread():
            try:
                if mode == 'mp4':
                    youtube = pytube.YouTube(url)
                    video = youtube.streams.get_highest_resolution()

                    video.download("Downloads")
                else:
                    youtube = pytube.YouTube(url)
                    video = youtube.streams.filter(only_audio=True).first()

                    video.download("Downloads")
            except Exception as e:
                error = IError(f"Failed to download: {e}")
                error.exec_()

        t = threading.Thread(target=start_thread, args=())
        return t.start()
