import argparse
import os
import shutil
import requests

from ws_ua_wrapper._version import __description__
from ws_sdk import ws_utilities

DOCKER_FILE = "../resources/DockerfileOfficial"
DOCKER_FILE_ADDON = "./resources/DockerfileAddon"
DOCKER_FILE_MERGED = "./Dockerfile"
ws_ua_docker = "https://github.com/whitesource/unified-agent-distribution/raw/master/dockerized/Dockerfile"
ALL_PKG_MAN = "all"
DEFAULT = None
PKG_MANS = [ALL_PKG_MAN, DEFAULT]

global conf


def backup_file(file_path):
    if os.path.exists(file_path):
        print(f"Backing up {file_path}")
        shutil.copyfile(file_path, file_path + ".backup")
    else:
        print(f"{file_path} does not exist. Nothing to backup")


def get_docker_file_from_gh():
    file_path = os.path.join(os.getcwd(), DOCKER_FILE)
    backup_file(file_path)

    print(f"Downloading docker file from: {ws_ua_docker}")
    req = requests.get(url=ws_ua_docker)

    return req.text


def download_ua():
    ua_path = os.path.join(os.getcwd(), "../whitesource")
    print(f"Downloading Unified Agent into: {ua_path}")
    ws_utilities.download_ua(path=ua_path)


def prep_docker_file():
    def enable_all_pkg_managers(dockerfile):
        new_dockerfile = ""
        start_uncommenting = False
        for line in dockerfile.splitlines():
            if "#RUN" in line:
                start_uncommenting = True
            if start_uncommenting and line and line.startswith(("#RUN", "#ENV", "#USER", "#  ", "#\t", "# ARG", "# CMD")):
                print(f"Uncommenting: {line}")
                line = line[1:].strip()

            new_dockerfile = new_dockerfile + line + '\n'

        return new_dockerfile

    docker_file = get_docker_file_from_gh()
    if conf.include == ALL_PKG_MAN:
        print(f"Enabling: {conf.include} package managers")
        docker_file = enable_all_pkg_managers(docker_file)

    ps_docker_addon_file = open(os.path.join(os.getcwd(), DOCKER_FILE_ADDON)).read()

    print(f"Merging WhiteSource official Dockerfile with {DOCKER_FILE_ADDON}")
    merged_docker_file = docker_file + '\n\n\n############################PS Addons############################\n\n\n' + ps_docker_addon_file
    file_path = os.path.join(os.getcwd(), DOCKER_FILE_MERGED)
    backup_file(file_path)

    with open(file_path, 'w') as fp:
        fp.write(merged_docker_file)


def parse_config():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('-i', '--includePackageManager',
                        help="Which Package manager to include",
                        dest='include',
                        choices=PKG_MANS,
                        default=None)

    return parser.parse_args()


def main():
    global conf
    # download_ua()
    conf = parse_config()
    prep_docker_file()

    print(f"Finished Docker Image preparations. To continue edit: '{DOCKER_FILE_MERGED}' and build the image")


if __name__ == '__main__':
    main()
