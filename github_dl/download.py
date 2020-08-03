import requests

def download_file(url):
    res = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, "w+") as f:
        f.write(res.text)
    return filename

filename = download_file("https://github.com/ytdl-org/youtube-dl/raw/master/.travis.yml")
