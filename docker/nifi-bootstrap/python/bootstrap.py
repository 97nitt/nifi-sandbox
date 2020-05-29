import argparse
import logging
import sys

# must setup logging here, before NiPyApi attempts to configure logging
logging.basicConfig(
    format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
    level=logging.INFO)

from clients.nifi import NiFiApi
from utils.http import HttpChecker

parser = argparse.ArgumentParser()
parser.add_argument("--nifi", help="NiFi base URL", default="http://localhost:8080")
parser.add_argument("--registry", help="NiFi Registry base URL", default="http://localhost:18080")

def main():
    args = parser.parse_args()

    # create NiFi API nifi (verify API is available first)
    if HttpChecker(f"{args.nifi}/nifi").get():
        api = NiFiApi(args.nifi)
        # create NiFi Registry nifi (verify registry is available first)
        if HttpChecker(f"{args.registry}/nifi-registry").get():
            api.create_registry_client(args.registry)
        else:
            sys.exit(1)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
