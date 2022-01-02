import os
import shutil
import requests

from ws_sdk import ws_utilities

DOCKER_FILE_MERGED = "DockerfileMerged"
DOCKER_FILE_ADDON = "resources/DockerfileAddon"
ws_ua_docker = "https://github.com/whitesource/unified-agent-distribution/raw/master/dockerized/Dockerfile"


def backup_file(file_path):
    if os.path.exists(file_path):
        print(f"Backing up {file_path}")
        shutil.copyfile(file_path, file_path + ".backup")
    else:
        print(f"{file_path} does not exist. Nothing to backup")


def get_docker_file_from_gh():
    file_path = os.path.join(os.getcwd(), "resources/Dockerfile")
    backup_file(file_path)

    print(f"Downloading docker file from: {ws_ua_docker}")
    req = requests.get(url=ws_ua_docker)

    return req.text


def download_ua():
    ua_path = os.path.join(os.getcwd(), "whitesource")
    print(f"Downloading Unified Agent into: {ua_path}")
    ws_utilities.download_ua(path=ua_path)


def prep_docker_file():
    ws_docker_file = get_docker_file_from_gh()
    ps_docker_addon_file = open(os.path.join(os.getcwd(), DOCKER_FILE_ADDON)).read()

    print(f"Merging WhiteSource official Dockerfile with {DOCKER_FILE_ADDON}")
    merged_docker_file = ws_docker_file + '\n\n\n############################PS Addons############################\n\n\n' + ps_docker_addon_file
    file_path = os.path.join(os.getcwd(), DOCKER_FILE_MERGED)
    backup_file(file_path)

    with open(file_path, 'w') as fp:
        fp.write(merged_docker_file)


def main():
    # download_ua()
    prep_docker_file()

    print(f"Finished Docker Image preparations. To continue edit: '{DOCKER_FILE_MERGED}' and build the image")


if __name__ == '__main__':
    main()
