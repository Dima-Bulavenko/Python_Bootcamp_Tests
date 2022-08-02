import os
import requests
from moviepy.editor import VideoFileClip
from getpass import getuser
video_url = 'https://v16-webapp.tiktok.com/57b837a33733f8d3279ed1b64aef2b33/62e8ad8c/video/tos/useast2a/tos-useast2a-ve-0068c004/195ae17f689c4000a2c587d466a06ee5/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C0%7C0&br=2160&bt=1080&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8Z~OCKwe2Nbcoyl7Gb&mime_type=video_mp4&qs=0&rc=aDo2aTZlZ2c7ZTRmZzdlOEBpMzw8Ojg0azxyczMzOjczM0A2XzVeLmBfNTExLS8wNDReYSMxbGxwLW5mazVfLS0wMTZzcw%3D%3D&l=202208012252200102171350340E76381E'


def convert_to_gif(url):
    responce = requests.get(url)
    video_name = "video.mp4"
    if responce.status_code == 200:
        with open(video_name, 'wb') as file:
            file.write(responce.content)

        with VideoFileClip(video_name) as video:
            video.write_gif(f'/home/{getuser()}/TikTok-example-1.gif', program='ffmpeg', fps=10)

        os.remove(video_name)

        return "It's OK"

    return "can't connect by link"


# print(convert_to_gif(video_url))
# print(getuser())