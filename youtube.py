from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def lejupielādēt_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print('Video veiksmīgi ielādējies!')

    except Exception as e:
        print(e)

def atvērt_faila_dialogu():
    mape = filedialog.askdirectory()
    if mape:
        print(f"Izvēlētā mape {mape}")

    return mape

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Lūdzu ievaadi YouTube video URL: ")
    save_dir = atvērt_faila_dialogu()

    if save_dir:
        print("Lejupielāde sākta ...")
        lejupielādēt_video(video_url, save_dir)
    else:
        print("Nepareiza saglabāšanas lokācija")
