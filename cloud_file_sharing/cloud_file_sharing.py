# File storage
# Youtube source: https://youtu.be/2535DhGy0oE
# Require package:
#  - pip install gofile

import gofile as go

def store_file(file):
    cur_server = go.getServer()
    print(cur_server)
    url = go.uploadFile(file)
    print("Download Link: ", url["downloadPage"])
