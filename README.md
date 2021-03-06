
## How to use

### class URL

 - validator()
 - unquote() / decode()
 - enquote() / encode()


```python
In [1]: from scraper_tools import URL

In [2]: u = URL()

In [3]: u.validator('http://sample.om')
Out[3]: True

In [4]: u.validator('http://sample.')
Out[4]: False

In [5]: url = URL('http://www.example.com/sample?src=git&encode=jp')

In [6]: url.is_valid
Out[6]: True

In [7]: url.attrs
Out[7]:
{'url': 'http://www.example.com/sample?src=git&encode=jp',
 'is_valid': True,
 'scheme': 'http',
 'netloc': 'www.example.com',
 'username': None,
 'password': None,
 'hostname': 'www.example.com',
 'port': None,
 'path': '/sample',
 'params': '',
 'query': 'src=git&encode=jp',
 'fragment': '',
 'basename': 'sample'}

In [8]: url = URL('http://www.example.com/データ.txt')

In [9]: url.attrs
Out[9]:
{'url': 'http://www.example.com/%E3%83%87%E3%83%BC%E3%82%BF.txt',
 'is_valid': True,
 'scheme': 'http',
 'netloc': 'www.example.com',
 'username': None,
 'password': None,
 'hostname': 'www.example.com',
 'port': None,
 'path': '/%E3%83%87%E3%83%BC%E3%82%BF.txt',
 'params': '',
 'query': '',
 'fragment': '',
 'basename': 'データ.txt'}

In [10]: url.query
Out[10]: 'src=git&encode=jp'

In [11]: url.get_query_val('src')
Out[11]: 'git'

In [12]: url.set_query_val('src', 'csv')
Out[12]: 'http://www.example.com/sample?src=csv&encode=jp'

In [13]: url
Out[13]: http://www.example.com/sample?src=git&encode=jp

In [14]: url.set_query_val('src', 'csv',update=True)
Out[14]: 'http://www.example.com/sample?src=csv&encode=jp'

In [15]: url
Out[15]: http://www.example.com/sample?src=csv&encode=jp

In [16]: url.get_root_address()
Out[16]: 'http://www.example.com'

In [17]: url.strip_query()
Out[17]: 'http://www.example.com/sample'

In [18]: url = URL('https://ja.wikipedia.org/wiki/日本語')

In [19]: url
Out[19]: https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E

In [20]: url.unquote()
Out[20]: 'https://ja.wikipedia.org/wiki/日本語'

In [21]: url.decode()
Out[21]: 'https://ja.wikipedia.org/wiki/日本語'

```

### class Scraper

 -  get_random_user_agent()
 -  get_random_ipv4()
 -  get_random_ipv6()
 -  request()
 -  request_async()
 -  get_filename()
 -  get_links()
 -  download_file()

```python
n [1]: from scraper_tools import Scraper

In [2]: sc = Scraper()

In [3]: sc.get_random_user_agent()
Out[3]: 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'

In [4]: sc.get_random_user_agent()
Out[4]: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/'

In [5]: sc.get_random_user_agent()
Out[5]: 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'

In [6]: sc.get_random_user_agent()
Out[6]: 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'

In [7]: sc.get_random_user_agent()
Out[7]: 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'

In [8]: sc.get_random_user_agent()
Out[8]: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

In [9]: sc.get_random_user_agent()
Out[9]: 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'

In [10]: sc.get_random_ipv4()
Out[10]: '121.162.233.190'

In [11]: sc.get_random_ipv4()
Out[11]: '178.172.98.169'

In [12]: sc.get_random_ipv6()
Out[12]: '3d18:cb77:5387:3ee9:1e60:d5f3:d987:283a'

In [13]: sc.get_random_ipv6()
Out[13]: 'cfc1:a00d:9013:37a0:ed94:5e92:7fe7:e356'

In [14]:
```


```python
In [2]: from scraper_tools import URL, Scraper, LogConfig
   ...:
   ...: logconfig = LogConfig()
   ...: logconfig.level = 'INFO'
   ...: sc = Scraper(logconfig=logconfig)
   ...:
   ...: url = URL('https://www.houjin-bangou.nta.go.jp/download/zenken/#csv-unic
   ...: ode')
   ...: response = sc.request(url)
   ...:
   ...: content = response.content
   ...: print(f'code: {response.status_code}')
   ...:
code: 200

In [3]: from scraper_tools import Scraper, LogConfig
   ...:
   ...: logconfig = LogConfig()
   ...: logconfig.level = 'DEBUG'
   ...: sc = Scraper(logconfig=logconfig)
   ...:
   ...: url = URL('https://www.houjin-bangou.nta.go.jp/download/zenken/#csv-unic
   ...: ode')
   ...: response = sc.request(url)
   ...:
   ...: content = response.content
   ...: print(f'code: {response.status_code}')
2022-06-02T19:34:31.885790+0900 LOG configure: {'handlers': [{'sink': <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>, 'level': 'DEBUG', 'format': '<green>{time}</green> <level>{message}</level>', 'colorize': True, 'serialize': False}]}
2022-06-02T19:34:31.886414+0900 URL: https://www.houjin-bangou.nta.go.jp/download/zenken/#csv-unicode
2022-06-02T14:34:32.092599+0900 response status_code: 200
code: 200

In [4]: logconfig
Out[4]: LogConfig(sink=None, level=DEBUG, format=<green>{time}</green> <level>{message}</level>, colorize=True, serialize=False

In [5]:
```

## TODO

 - Rotating Requests through a pool of Proxies and change IPAddress.
   if you want to access with hide your ipaddress, you should try follows.
       - Using VPN service.
       - [torpy](https://github.com/torpyorg/torpy)
       - and/or others...

  **CAUTION**
  f you use a free proxy to login to something or enter personal information and POST it, you must be assured that it will be leaked.
  Keep in mind, it is like writing your credit card number and security code on a postcard.


## KNOWN PROBLEM
if you want to use this module(and/or requests_html, selenium) on ubuntu of VPN,you should try follows commands.

```bash
sudo apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
```

See Also: https://techoverflow.net/2020/09/29/how-to-fix-pyppeteer-pyppeteer-errors-browsererror-browser-closed-unexpectedly/
