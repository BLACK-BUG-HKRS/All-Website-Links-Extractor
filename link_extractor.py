import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama


colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW

internal_urls = set()
external_urls = set()

total_urls_visited = 0