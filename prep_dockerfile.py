import os
import shutil
import requests
from ws_sdk import ws_utilities
ws_ua_docker = "https://github.com/whitesource/unified-agent-distribution/raw/master/dockerized/Dockerfile"


def download_docker_file():
    file_path = os.path.join(os.getcwd(), "Dockerfile")
    print(f"Backing up {file_path}")
    shutil.copyfile(file_path, file_path + ".backup")

    print(f"Downloading docker file from: {ws_ua_docker}")
    req = requests.get(url=ws_ua_docker)
    with open(file_path, 'w') as fp:
        fp.write(req.text)


def download_ua():
    ua_path = os.path.join(os.getcwd(), "resources")
    print(f"Downloading Unified Agent into: {ua_path}")
    ws_utilities.download_ua(path=ua_path)


def main():
    download_docker_file()
    download_ua()


if __name__ == '__main__':
    main()
