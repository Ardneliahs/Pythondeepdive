import os, time
filedir = "/opt/test"
now_epoch = int(time.time())
for each_file in os.listdir(filedir):
    file_path = os.path.join(filedir,each_file)
    if os.path.isfile(file_path):
        filemtime = os.path.getctime(file_path)
        if now_epoch - filemtime > 14400:
            print(file_path)
