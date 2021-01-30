from pytube import YouTube, Playlist
import os, sys

EXIT = 0
SINGLE = 1
PLAYLIST = 2
VER = '1.0.0'

class clrs:
    OKORG = '\033[93m'
    ERROR = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def on_progress(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    bytes_received = filesize - bytes_remaining
    display_progress_bar(bytes_received, filesize)

def display_progress_bar(bytes_received, filesize, ch='█', scale=0.55):
    _, columns = get_terminal_size()
    max_width = int(columns * scale)
    filled = int(round(max_width * bytes_received / float(filesize)))
    remaining = max_width - filled
    bar = ch * filled + ' ' * remaining
    percent = round(100.0 * bytes_received / float(filesize), 1)
    text = ' ↳ |{bar}| {percent}%\r'.format(bar=bar, percent=percent)
    sys.stdout.write(text)
    sys.stdout.flush()

def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)

def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads/Videos')
    return download_path

def get_resolution(the_video):
    the_video = the_video.streams.filter(progressive = True)
    list_quality = [stream.resolution for stream in the_video]
    return list_quality

def singleDownload():
    print(clrs.BOLD + "Downloaded Videos Path : " + file_path() + clrs.ENDC)
    yt_url = input("YouTube URL => ")
    print ("Accessing the URL...")

    try:
        video = YouTube(yt_url, on_progress_callback=on_progress)
    except:
        print(clrs.ERROR + clrs.BOLD + "Error - Check your:\n  -Internet connection\n  -The URL is a YouTube URL\n" + clrs.ENDC)
        redo = main()
    
    list_quality = get_resolution(video)

    for idx, ps in enumerate(list_quality):
        print((idx + 1),"-", ps)
    
    try:
        print("Choose Video Quality")
        quality = int(input("Option => ")) - 1
    except:
        quality = 0

    video_type = video.streams.filter(progressive = True, res=list_quality[quality]).first()
    title = video.title
    print (clrs.OKORG + "Fetching: {}".format(title) + clrs.ENDC)
    global file_size
    file_size = video_type.filesize
    video_type.download(file_path())
 
    print ("\nVideo Saved.\nEnjoy Your Video.\n")
    again = main()

def playlistDownload():
    print(clrs.BOLD + "Downloaded Videos Path : " + file_path() + clrs.ENDC)
    yt_url = input("YouTube URL => ")
    print ("Accessing URL...")

    try:
        playlist = Playlist(yt_url)
    except:
        print(clrs.ERROR + clrs.BOLD + "Error - Check your:\n  -Internet connection\n  -The URL is a YouTube URL\n" + clrs.ENDC)
        redo = main()
    
    for video in playlist:
        title = video.title
        video.download(file_path())
    
    print ("\nVideos Saved.\nEnjoy Your Videos.\n")
    again = main()

def main():
    print(clrs.BOLD + "Yutub downloader " + VER + clrs.ENDC)
    print("YouTube Videos Options :")
    print("1 - Single")
    print("2 - Playlist")
    print("---")
    print("0 - Exit")
    
    try:
        select = int(input("Option => "))
    except:
        print(clrs.ERROR + clrs.BOLD + "Error - There is no such Option. \n" + clrs.ENDC)
        main()
    
    if select == SINGLE:
        singleDownload()    
    elif select == PLAYLIST:
        playlistDownload()
    elif select == EXIT:
        quit()
    else:
        print(clrs.ERROR + clrs.BOLD + "Error - There is no such Option. \n" + clrs.ENDC)
        main()

file_size = 0
if __name__ == "__main__":
    main()