import logging
import requests
import time

logger = logging.getLogger(__name__)

class HttpChecker:
    """
    Used to test an HTTP resource to verify a service is available.
    """

    def __init__(self, url: str):
        """
        Constructor.

        :param url: URL to check
        """
        self.url = url

    def get(self, status: int = 200, sleep: int = 1, max_attempts: int = 100) -> bool:
        """
        Wait for a GET request to return a desired status code.

        :param status: desired response status (default is 200)
        :param sleep: seconds to wait between requests (default is 1)
        :param max_attempts: maximum number of attempts (default is 10)
        """
        logger.info(f"Waiting for {self.url} to respond with a status of {status}")
        count = 1
        while True:
            try:
                response = requests.get(self.url)
                logger.info(f"Attempt #{count} received status code {response.status_code}")
                if response.status_code == status:
                    logger.info("Success!")
                    return True

            except Exception as e:
                logger.info(f"Attempt #{count} failed: {e}")

            if count < max_attempts:
                count += 1
                time.sleep(sleep)
            else:
                logger.error("Giving up!")
                return False
