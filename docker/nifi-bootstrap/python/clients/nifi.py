import logging

from nipyapi.config import nifi_config
from nipyapi.nifi.apis.controller_api import ControllerApi

logger = logging.getLogger(__name__)

class NiFiApi:
    """
    NiFi API nifi.
    """

    def __init__(self, base_url: str):
        """
        Constructor.

        :param base_url: NiFi base URL
        """
        nifi_config.host = f"{base_url}/nifi-api"
        self.controller = ControllerApi()

    def create_registry_client(self, base_url: str):
        """
        Create NiFi Registry nifi
        :param base_url: base URL of NiFi Registry
        """
        url = f"{base_url}/nifi-registry"
        logger.info(f"Creating NiFi Registry client: {url}")
        try:
            self.controller.create_registry_client({
                "revision": {
                    "version": 0
                },
                "component": {
                    "name": "NiFi Registry",
                    "uri": url
                }
            })
            logger.info("Successfully created NiFi Registry client")

        except Exception:
            logger.exception("Failed to create NiFi Registry client")
