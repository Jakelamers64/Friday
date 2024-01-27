import requests

url = "https://chrt.fm/track/138C95/prfx.byspotify.com/e/play.podtrac.com/npr-510312/traffic.megaphone.fm/NPR6189812339.mp3?d=2421&size=38748622&e=1197954644&t=podcast&p=510312&sc=siteplayer&aw_0_1st.playerid=siteplayer"
filename = "your_desired_filename.mp3"

response = requests.get(url)

print("eee")

if response.status_code == 200:
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"File {filename} downloaded successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
