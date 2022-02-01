import logging
import os

from ws_sdk.client import WSClient

from _version import __tool_name__, __version__, __description__

is_debug = logging.DEBUG if bool(os.environ.get("DEBUG", 0)) else logging.INFO

logger = logging.getLogger(__tool_name__)
logger.setLevel(is_debug)


formatter = logging.Formatter('%(levelname)s %(asctime)s %(thread)d %(name)s: %(message)s')
s_handler = logging.StreamHandler()
s_handler.setFormatter(formatter)
s_handler.setLevel(is_debug)
logger.addHandler(s_handler)

sdk_logger = logging.getLogger(WSClient.__module__)
sdk_logger.setLevel(is_debug)
sdk_logger.addHandler(s_handler)
sdk_logger.propagate = False

UA_DIR = "whitesource"


def get_ws_scopes() -> tuple:
    project_name = os.environ['WS_PROJ_NAME']
    product_token = os.environ['WS_PROD_TOKEN']
    org_token = os.environ['WS_ORG_TOKEN']
    ws_url = os.environ.get('WS_URL', "saas")

    return project_name, product_token, org_token, ws_url


def main():
    logger.info(f"Starting {__description__}. Version {__version__}")
    tool_details = (f"ps-{__tool_name__.replace('_','-')}", __version__)
    user_key = os.environ['WS_USER_KEY']
    project_name, product_token, org_token,ws_url = get_ws_scopes()

    ws_client = WSClient(user_key=user_key,
                         token=org_token,
                         url=ws_url,
                         tool_details=tool_details,
                         skip_ua_download=True,
                         ua_path=os.path.join(os.getcwd(), UA_DIR))

    scan_dir = os.environ.get('SCAN_DIR', "/SCAN_DIR")
    logger.info(f"Scanning: '{scan_dir}' into WS Organization Token: '{org_token}', Product Token: '{product_token}', Project: '{project_name}'")

    ret = ws_client.scan(scan_dir=scan_dir,
                         product_token=product_token,
                         project_name=project_name)

    logger.info(f"Finished scanning: {scan_dir}")

    return ret[0]


if __name__ == '__main__':
    main()
