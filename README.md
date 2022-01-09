[![Logo](https://whitesource-resources.s3.amazonaws.com/ws-sig-images/Whitesource_Logo_178x44.png)](https://www.whitesourcesoftware.com/)  
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![CI](https://github.com/whitesource-ps/ws-ua-wrapper/actions/workflows/ci.yml/badge.svg)](https://github.com/whitesource-ps/ws-ua-wrapper/actions/workflows/ci.yml)
[![Python 3.6](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Blue_Python_3.6%2B_Shield_Badge.svg/86px-Blue_Python_3.6%2B_Shield_Badge.svg.png)](https://www.python.org/downloads/release/python-360/)
[![GitHub release](https://img.shields.io/github/v/release/whitesource-ps/ws-sbom-spdx-report)](https://github.com/whitesource-ps/ws-ua-wrapper/releases/latest)  
[![PyPI](https://img.shields.io/pypi/v/ws-ua-wrapper?style=plastic)](https://pypi.org/project/ws-ua-wrapper/)
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
