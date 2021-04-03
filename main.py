import song
import video
import url

def banner():
    print("-"*45)
    print('''
    
                                           MMMM      MMMMM    UUU     UUU    LLL     TTTTTTTTTTT     III
                                           MMMMMM   MMMMMM    UUU     UUU    LLL     TTTTTTTTTTT     III
                                           MMM MMM MMM MMM    UUU     UUU    LLL         TTT         III
                                           MMM  MMMMM  MMM     UUU   UUU     LLL         TTT         III
                                           MMM         MMM      UUU UUU      LLLLLLLL    TTT         III
                                           MMM         MMM       UUUUU       LLLLLLLL    TTT         III
        
        DDD              OOO        WWW              WWW    NNNN       NNN   LLL          OOO           AAAAA          DDD          EEEEEEEE   RRRRR
        DDDDDD         OOO OOO      WWW              WWW    NNNNN      NNN   LLL        OOO OOO        AAA AAA         DDDDD        EEEEEEEE   RRR RR
        DDD  DDD      OOO   OOO     WWW              WWW    NNN NNN    NNN   LLL       OOO   OOO      AAA   AAA        DDD  DDD     EEE        RRR  RRR 
        DDD    DDD   OOO      OOO   WWW    WWWWW     WWW    NNN  NNN   NNN   LLL      OOO     OOO    AAAAAAAAAAA       DDD    DDD   EEEEEEE    RRR  RRR 
        DDD    DDD   OOO      OOO   WWW  WWW   WWW   WWW    NNN   NNN  NNN   LLL      OOO     OOO   AAAAAAAAAAAAA      DDD    DDD   EEEEEEE    RRRRRR
        DDD  DDD      OOO    OOO    WWW WWW     WWW  WWW    NNN    NNN NNN   LLL       OOO   OOO   AAA         AAA     DDD  DDD     EEE        RRRRR
        DDDDDD         OOO  OOO     WWWWW         WWWWWW    NNN     NNNNNN   LLLLLLL    OOO OOO   AAA           AAA    DDDDD        EEEEEEEE   RRR  RRR
        DDD               OOO       WWWW            WWWW    NNN       NNNN   LLLLLLL      OOO    AAA             AAA   DDD          EEEEEEEE   RRR   RRR
    ''')

def song_dl(songs):
    try:
        song.dl(songs)
    except:
        print("An error occured")

def video_dl(videos):
    try:
        video.dl(videos)
    except:
        print("An error occured")

def url_dl(urls):
    try:
        url.dl(urls)
    except:
        print("An error occured")

def spotify_dl(playlist):
    

def main():
    banner()
    ch = input("Do you want to enter a song or video or or a spotify playlist or directly a URL?: ")
    if ch.lower() == "song":
        songs = input("Name(s) of the song seperated with commas (,): ")
        songs = songs.split(",")
        song_dl(songs)
    elif ch.lower() == "video":
        vids = input("Input Video Title(s) seperated with commas (,): ")
        vids = vids.split(",")
        video_dl(vids)
    elif ch.lower() == "spotify" or ch.lower() == "spotify playlist":
        playlist = input("Enter your playlist URL: ")
        spotify_dl(playlist)
    elif ch.lower() == "url":
        urls = input("Input URL: ")
        urls = urls.split(",")
        url_dl(urls)


if __name__ == '__main__':
    main()


