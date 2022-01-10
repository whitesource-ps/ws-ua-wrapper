[![Logo](https://whitesource-resources.s3.amazonaws.com/ws-sig-images/Whitesource_Logo_178x44.png)](https://www.whitesourcesoftware.com/)  
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![CI](https://github.com/whitesource-ps/ws-ua-wrapper/actions/workflows/ci.yml/badge.svg)](https://github.com/whitesource-ps/ws-ua-wrapper/actions/workflows/ci.yml)
[![Python 3.7+](https://upload.wikimedia.org/wikipedia/commons/7/76/Blue_Python_3.7%2B_Shield_Badge.svg)
[![GitHub release](https://img.shields.io/github/v/release/whitesource-ps/ws-ua-wrapper)](https://github.com/whitesource-ps/ws-ua-wrapper/releases/latest)
# [WhiteSource Unified Agent Wrapper](https://github.com/whitesource-ps/ws-ua-wrapper)
White Source Unified Wrapper delivered as Docker image that consists of 2 pre-steps prior to scan:
* Retrieves secret from IBM Secret Server
* Extract WS scopes (Organization ,Product and Products)

The tool is delivered as Docker image ready for deployment and as a script to customize the docker prior of building it. 

The tool is designed 

Parameters:

| Name              | Description                                       |
|:------------------|:--------------------------------------------------|
| IBM_CLOUD_API_KEY | Key to access IBM Secret Server                   |
| SERVICE_URL       | Vault URL of IBM Secret Server                    |
| GLOBAL_TOKEN_ID   | ID of WS global token secret in IBM secret Server |
| USER_KEY_ID       | ID of WS user key secret in IBM secret Server     |

## Prerequisites
Docker environment or equivalent.

## Deployment of the Docker image
Execute:
```shell
docker pull whitesourcetools/ws-ua-wrapper
docker run --name ws-ua-wrapper -v /<PROJECT_ROOT_DIR>:/SCAN_DIR:ro -e ...
```

## Using script to generate Docker Image
1. Generate new Dockerfile by executing: `python3 prep_dockerfile.py`
2. Edit the file according to your needs (package manager, language tools, etc...).
3. Build the image.
