[![Logo](https://whitesource-resources.s3.amazonaws.com/ws-sig-images/Whitesource_Logo_178x44.png)](https://www.whitesourcesoftware.com/)  
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![CI](https://github.com/whitesource-ps/ws-ua-wrapper/actions/workflows/ci.yml/badge.svg)](https://github.com/whitesource-ps/ws-ua-wrapper/actions/workflows/ci.yml)
[![Python 3.7+](https://upload.wikimedia.org/wikipedia/commons/7/76/Blue_Python_3.7%2B_Shield_Badge.svg)
[![GitHub release](https://img.shields.io/github/v/release/whitesource-ps/ws-ua-wrapper)](https://github.com/whitesource-ps/ws-ua-wrapper/releases/latest)
# [WhiteSource Unified Agent Wrapper](https://github.com/whitesource-ps/ws-ua-wrapper)
White Source Unified Wrapper delivered as Docker image to simplify UA scan via Docker.

The tool is delivered as Docker image ready for deployment and as a script to customize the docker prior of building it. 

Parameters:

| Name          | Description                                             |
|:--------------|:--------------------------------------------------------|
| WS_ORG_TOKEN  | WhiteSource Organization token to scan into             |
| WS_USER_KEY   | User key to use for scan*                               |
| WS_PROD_TOKEN | WhiteSource Product token to scan into                  |
| WS_PROJ_NANE  | Name of WS project to scan into (Created if not exists) |
| SCAN_DIR      | Directory name to scan                                  |

* Minimal user key permissions: Product Integrator on the scanner project

## Prerequisites
Docker environment or equivalent.

## Deployment of the Docker image
Execute:
```shell
docker pull whitesourcetools/ws_ua_wrapper:<TAG>
docker run --name <CONTAINER_NAME> -v /<PROJECT_ROOT_DIR>:/SCAN_DIR:ro \
                                -e WS_ORG_TOKEN=<WS_ORG_TOKEN> \
                                -e WS_USER_KEY=<WS_USER_KEY> \
                                -e WS_PROD_TOKEN=<WS_PROD_TOKEN> \
                                -e WS_PROJ_NANE=<WS_PROJ_NANE> \
                                whitesourcetools/ws_ua_wrapper:<TAG> 
```

## Using script to generate Docker Image
1. Generate new Dockerfile (and enable all package managers) by executing: `python3 prep_dockerfile.py -i all`
2. Edit the file according to your needs (package manager, language tools, etc...).
3. Build the image.

## Debug
* Set env var: DEBUG=1