#File storage
# Youtube source: https://www.youtube.com/watch?v=2535DhGy0oE&t=1s
import gofile as go

def store_file(file):
    cur_server = go.getServer()
    print(cur_server)
    url = go.uploadFile(file)
    print("Download Link: ", url["downloadPage"])
