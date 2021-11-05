from pytube import YouTube
from pytube.cli import on_progress

while True:
    try:
        link = input("Enter the youtube link here: ")
        url = YouTube(link, on_progress_callback=on_progress)
    except Exception as e:
        print("Invalid link")
        continue
    print()
    title = url.title
    length = url.length
    hours = length//3600
    minutes = (length-3600*hours)//60
    seconds = length % 60

    print("Title:", title)

    if (hours == 0 and minutes == 0):
        print("Length:",seconds, "sec")
    elif (hours == 0):
        print("Length:", minutes, "min", seconds, "sec")
    else:
        print("Length:", hours, "hrs", minutes, "min", seconds, "sec")

    confirmation = input("Do you want to download this ? Enter y/n to continue: ")
    print()
    if confirmation == "y":
        download_path = input("Enter download path. Leave EMPTY for current directory: ")
        if download_path is None:
            download_path = ""
        audio_or_video = int(input("Enter 1 for VIDEO or 2 for ONLY AUDIO: "))
        if audio_or_video == 2:
            stream = url.streams.get_by_itag(251)
            stream.download(download_path)
        elif audio_or_video == 1:
            video_quality = int(input("Select video quality. Enter 1 for 360p or 2 for 720p: "))
            if video_quality == 1:
                stream = url.streams.get_by_itag(18)
                stream.download(download_path)
            elif video_quality == 2:
                stream = url.streams.get_by_itag(22)
                stream.download(download_path)
            else:
                print("Not a valid input")
                print()
                continue
        print()
        print("Yayy... Successfully downloaded!")
        print()
        to_continue = input("Do you want to download more? Enter y/n: ")
        print()
        if to_continue != "y":
            break
        
    elif confirmation == "n":
        print("OK no problem")
    else:
        print("Invalid input")
    
