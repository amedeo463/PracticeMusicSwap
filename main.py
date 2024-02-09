import requests

downloadUrl = "https://newgrounds.com/audio/download/"

GDFolder = ""
try:
    exec(open("settings.txt", "r").read())
except:
    print("Oops! There is a problem with the 'settings.txt' file.")
    print("Close this program and go check if such file does not exist or has problems.")
    while True:
        pass

print("Welcome to PracticeMusicSwap!\nThis program helps you change the practice mode of GD to any song in Newgrounds!")
print("Pro tip: If you want to restore the original practice song, give no input.")
err = True
while err:
    songID = input("Song ID (numbers at the end of the song URL): ")
    err = False
    if songID == "":
        print("No input was given! Restoring original song...")
        with open("Original/StayInsideMe.mp3", "rb") as original:
            open(GDFolder+"/Resources/StayInsideMe.mp3", "wb").write(original.read())
    else:
        try:
            print("downloading song to RAM...")
            song = requests.get(downloadUrl+songID)
        except:
            err = True
            print("Oops! Something went wrong!\n Check your internet and/or if the song ID is wrong.")
    
        if not err:
            print("Overwriting current practice song...")
            try:
                open(GDFolder+"/Resources/StayInsideMe.mp3", "wb").write(song.content)
            except:
                err = True
                print("Oops! There was a problem while Overwriting the song.")

print("Done!")
print("You can close this program.")
while True:
    pass
