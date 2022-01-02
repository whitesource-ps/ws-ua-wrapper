import logging
import os
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
from ibm_secrets_manager_sdk.secrets_manager_v1 import SecretsManagerV1

from ws_sdk import WSClient, ws_constants

from _version import __tool_name__, __version__, __description__
from ws_sdk.web import WS

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

URL = "saas"    # https://ibm.whitesourcesoftware.com/
IBM_CLOUD_API_KEY = os.environ['IBM_CLOUD_API_KEY']
SERVICE_URL = os.environ['SERVICE_URL']
GLOBAL_TOKEN_ID = os.environ['GLOBAL_TOKEN_ID']
USER_KEY_ID = os.environ['USER_KEY_ID']


def get_scopes() -> tuple:
    project_name = os.environ['WS_PROJ_NAME']
    product_name = os.environ['WS_PROD_NAME']
    org_name = os.environ['WS_ORG_NAME']

    return project_name, product_name, org_name


def get_user_key_from_vault() -> tuple:
    def get_from_vault_resp(res: dict) -> dict:
        ret = res['result']['resources'][0]
        logger.debug(f"Returning: {ret['name']}")

        return ret['secret_data']['payload']

    secrets_manager = SecretsManagerV1(authenticator=IAMAuthenticator(apikey=IBM_CLOUD_API_KEY, ))
    secrets_manager.set_service_url(SERVICE_URL)

    user_key_resp = secrets_manager.get_secret('arbitrary', USER_KEY_ID)
    user_key = get_from_vault_resp(user_key_resp.__dict__)
    global_token_resp = secrets_manager.get_secret('arbitrary', GLOBAL_TOKEN_ID)
    global_token = get_from_vault_resp(global_token_resp.__dict__)

    return user_key, global_token


def get_org(ws_g_conn, org_name) -> str:
    logger.debug(f"Get organizations of Global Organization token: '{ws_g_conn.token}'")
    orgs = ws_g_conn.get_organizations(name=org_name)

    return orgs[0] if orgs else None


def main():
    logger.info(f"Starting {__description__}. Version {__version__}")
    tool_details = (f"ps-{__tool_name__.replace('_','-')}", __version__)
    user_key, global_token = get_user_key_from_vault()
    project_name, product_name, org_name = get_scopes()

    ws_global_conn = WS(user_key=user_key,
                        token=global_token,
                        token_type=ws_constants.ScopeTypes.GLOBAL,
                        url=URL,
                        tool_details=tool_details)

    org = get_org(ws_global_conn, org_name)

    ws_client = WSClient(user_key=user_key,
                         token=org['token'],
                         url=URL,
                         tool_details=tool_details,
                         skip_ua_download=True,
                         ua_path=os.path.join(os.getcwd(), "whitesource"))

    scan_dir = os.environ.get('WS_SCAN_DIR', "/SCAN_DIR")
    logger.info(f"Scanning: '{scan_dir}' into WS Organization: '{org_name}', Product: {product_name}, Project: '{project_name}'")
    ret = ws_client.scan(scan_dir=scan_dir,
                         product_name=product_name,
                         project_name=project_name)
    logger.info(f"Finished scanning: {scan_dir}")

    return ret[0]


if __name__ == '__main__':
    main()
