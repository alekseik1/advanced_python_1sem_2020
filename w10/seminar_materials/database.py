import urllib.request
import time


urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org', 'https://vk.com',
    'http://moodle.phystech.edu/', 'https://google.com'
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
threads = []
for url in urls:
    read_url(url)
print(time.time() - start)
