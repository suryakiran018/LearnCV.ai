# Web scraping

* `
Extracting data from websites
`

by making HTTP requests to access the site's content and then parsing the HTML to collect specific information


---



## Essential Packages and Tools


*   ***requests*** – For Sending HTTP Requests

*   ***BeautifulSoup*** (from bs4) – For Parsing HTML
*   ***lxml*** – A High-Performance HTML/XML Parser
*   ***Selenium*** – For Scraping JavaScript-Rendered Content
*   ***Scrapy*** – A High-Level Web Scraping Framework
*   ***pandas*** – For Storing and Processing Scraped Data
*   ***fake_useragent*** – For Randomizing User-Agent Headers
*   ***PyQuery*** – jQuery-like Syntax for Parsing HTML
*   ***requests_html*** – For JavaScript Rendering (Alternative to Selenium)
*   ***CloudScraper*** – For Bypassing Anti-Scraping Techniques


---



Outline:
1. ***Basic scraping*** :   requests, BeautifulSoup, lxml.
2. ***Dynamic content*** :  Selenium, requests_html.
3. ***Scaling and efficiency*** :  Scrapy.
4. ***Data processing*** : pandas.
5. ***Bypassing anti-scraping*** : fake_useragent, cloudscraper.



## Setting Up Your Environment

* Web scraping in Python requires Python 3.x.

Creating a virtual environment:

```
# Navigate to your project directory
mkdir my_scraping_project
cd my_scraping_project

# Create a virtual environment (you can name it anything, here it's 'venv')
python -m venv venv
```

 Install Essential Libraries


```
pip install requests
pip install beautifulsoup4
pip install lxml
pip install fake-useragent
pip install selenium
pip install scrapy
pip install pandas
pip install requests-html

```

Set Up WebDriver for Selenium


```
# Install Google Chrome and the required WebDriver
!apt-get install -y chromium-chromedriver
!pip install selenium webdriver-manager
```








```python
!pip install requests
!pip install beautifulsoup4
!pip install lxml
!pip install fake-useragent
!pip install selenium
!pip install scrapy
!pip install pandas
!pip install requests-html
```

## HTTP Requests


```python
import requests

url = 'https://www.wikipedia.org/'  # Replace with the URL you want to scrape
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print('Successfully fetched the webpage')
else:
    print(f'Failed to retrieve the webpage, status code: {response.status_code}')
```

    Successfully fetched the webpage


### ***GET Request***

Typically used to fetch data, like web pages or API responses.


```python
import requests

response = requests.get('https://www.example.com')

print(response.text)
```

    <!doctype html>
    <html>
    <head>
        <title>Example Domain</title>
    
        <meta charset="utf-8" />
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
        body {
            background-color: #f0f0f2;
            margin: 0;
            padding: 0;
            font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
            
        }
        div {
            width: 600px;
            margin: 5em auto;
            padding: 2em;
            background-color: #fdfdff;
            border-radius: 0.5em;
            box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
        }
        a:link, a:visited {
            color: #38488f;
            text-decoration: none;
        }
        @media (max-width: 700px) {
            div {
                margin: 0 auto;
                width: auto;
            }
        }
        </style>    
    </head>
    
    <body>
    <div>
        <h1>Example Domain</h1>
        <p>This domain is for use in illustrative examples in documents. You may use this
        domain in literature without prior coordination or asking for permission.</p>
        <p><a href="https://www.iana.org/domains/example">More information...</a></p>
    </div>
    </body>
    </html>
    


### attributes of response


```python

# for attribute in dir(response):
#     print(attribute)
dir(response)
```




    ['__attrs__',
     '__bool__',
     '__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__enter__',
     '__eq__',
     '__exit__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getstate__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__nonzero__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setstate__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     '_content',
     '_content_consumed',
     '_next',
     'apparent_encoding',
     'close',
     'connection',
     'content',
     'cookies',
     'elapsed',
     'encoding',
     'headers',
     'history',
     'is_permanent_redirect',
     'is_redirect',
     'iter_content',
     'iter_lines',
     'json',
     'links',
     'next',
     'ok',
     'raise_for_status',
     'raw',
     'reason',
     'request',
     'status_code',
     'text',
     'url']




```python
# Print all attributes and methods of the response object
for key, value in response.__dict__.items():
    print(f"{key[:20].ljust(20)}: {value}")
```

    _content            : b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'
    _content_consumed   : True
    _next               : None
    status_code         : 200
    headers             : {'Content-Encoding': 'gzip', 'Age': '264683', 'Cache-Control': 'max-age=604800', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Mon, 09 Dec 2024 11:39:55 GMT', 'Etag': '"3147526947+gzip"', 'Expires': 'Mon, 16 Dec 2024 11:39:55 GMT', 'Last-Modified': 'Thu, 17 Oct 2019 07:18:26 GMT', 'Server': 'ECAcc (lac/5588)', 'Vary': 'Accept-Encoding', 'X-Cache': 'HIT', 'Content-Length': '648'}
    raw                 : <urllib3.response.HTTPResponse object at 0x79bf4279d270>
    url                 : https://www.example.com/
    encoding            : UTF-8
    history             : []
    reason              : OK
    cookies             : <RequestsCookieJar[]>
    elapsed             : 0:00:00.066073
    request             : <PreparedRequest [GET]>
    connection          : <requests.adapters.HTTPAdapter object at 0x79bf422960e0>



```python
# Headers
print(response.headers)
for key, value in response.headers.items():
    print(f"{key[:20].ljust(20)}:\t {value}")
```

    {'Content-Encoding': 'gzip', 'Age': '264683', 'Cache-Control': 'max-age=604800', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Mon, 09 Dec 2024 11:39:55 GMT', 'Etag': '"3147526947+gzip"', 'Expires': 'Mon, 16 Dec 2024 11:39:55 GMT', 'Last-Modified': 'Thu, 17 Oct 2019 07:18:26 GMT', 'Server': 'ECAcc (lac/5588)', 'Vary': 'Accept-Encoding', 'X-Cache': 'HIT', 'Content-Length': '648'}
    Content-Encoding    :	 gzip
    Age                 :	 264683
    Cache-Control       :	 max-age=604800
    Content-Type        :	 text/html; charset=UTF-8
    Date                :	 Mon, 09 Dec 2024 11:39:55 GMT
    Etag                :	 "3147526947+gzip"
    Expires             :	 Mon, 16 Dec 2024 11:39:55 GMT
    Last-Modified       :	 Thu, 17 Oct 2019 07:18:26 GMT
    Server              :	 ECAcc (lac/5588)
    Vary                :	 Accept-Encoding
    X-Cache             :	 HIT
    Content-Length      :	 648



```python
print(response.cookies)
```

    <RequestsCookieJar[]>



```python
print(response.url)
```

    https://www.example.com/



```python
# Check if there were any redirects
if response.history:
    print("Redirect History:", [r.url for r in response.history])
else:
    print("No redirects.")
```

    Redirect History: ['https://w3schools.com/python/demopage.htm']


###Handling Json data

https://jsonplaceholder.typicode.com/posts


```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)  # HTTP status code
print(len(response.text))         # Response content as a string
```

    200
    27520



```python
json_data = response.json()
print(f'Total length of Users info: {len(json_data)}')

print(f'\nPrinting first 5 Users info')
json_data[:5]
```

    Total length of Users info: 100
    
    Printing first 5 Users info





    [{'userId': 1,
      'id': 1,
      'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
      'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'},
     {'userId': 1,
      'id': 2,
      'title': 'qui est esse',
      'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'},
     {'userId': 1,
      'id': 3,
      'title': 'ea molestias quasi exercitationem repellat qui ipsa sit aut',
      'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'},
     {'userId': 1,
      'id': 4,
      'title': 'eum et est occaecati',
      'body': 'ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit'},
     {'userId': 1,
      'id': 5,
      'title': 'nesciunt quas odio',
      'body': 'repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque'}]




```python
print(json_data[0].keys())
print(json_data[0].values())
```

    dict_keys(['userId', 'id', 'title', 'body'])
    dict_values([1, 1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'])


### Handling Query Parameters


```python
url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}

response = requests.get(url, params=params)
response.json()

```




    [{'userId': 1,
      'id': 1,
      'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
      'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'},
     {'userId': 1,
      'id': 2,
      'title': 'qui est esse',
      'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'},
     {'userId': 1,
      'id': 3,
      'title': 'ea molestias quasi exercitationem repellat qui ipsa sit aut',
      'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'},
     {'userId': 1,
      'id': 4,
      'title': 'eum et est occaecati',
      'body': 'ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit'},
     {'userId': 1,
      'id': 5,
      'title': 'nesciunt quas odio',
      'body': 'repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque'},
     {'userId': 1,
      'id': 6,
      'title': 'dolorem eum magni eos aperiam quia',
      'body': 'ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae'},
     {'userId': 1,
      'id': 7,
      'title': 'magnam facilis autem',
      'body': 'dolore placeat quibusdam ea quo vitae\nmagni quis enim qui quis quo nemo aut saepe\nquidem repellat excepturi ut quia\nsunt ut sequi eos ea sed quas'},
     {'userId': 1,
      'id': 8,
      'title': 'dolorem dolore est ipsam',
      'body': 'dignissimos aperiam dolorem qui eum\nfacilis quibusdam animi sint suscipit qui sint possimus cum\nquaerat magni maiores excepturi\nipsam ut commodi dolor voluptatum modi aut vitae'},
     {'userId': 1,
      'id': 9,
      'title': 'nesciunt iure omnis dolorem tempora et accusantium',
      'body': 'consectetur animi nesciunt iure dolore\nenim quia ad\nveniam autem ut quam aut nobis\net est aut quod aut provident voluptas autem voluptas'},
     {'userId': 1,
      'id': 10,
      'title': 'optio molestias id quia eum',
      'body': 'quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error'}]




```python
url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1,'id': 1}

response = requests.get(url, params=params)
response.json()
```




    [{'userId': 1,
      'id': 1,
      'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
      'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}]



### Handling Timeouts


```python
try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=5)
    print(response.status_code)
except requests.exceptions.Timeout:
    print("The request timed out.")
```

    200


### ***POST Request***

Often used when submitting forms or uploading data.

Sends data to the server to create or update a resource.


```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
```

    201
    {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}


###Handling HTTP Errors
If a request fails (e.g., 404 or 500), requests won’t throw an exception unless you explicitly check for errors.


```python
response = requests.get('https://jsonplaceholder.typicode.com/invalid-url')
if response.status_code != 200:
    print(f"Error: {response.status_code}")
```

    Error: 404



```python
try:
    response = requests.get('https://jsonplaceholder.typicode.com/invalid-url')
    response.raise_for_status()  # Raises HTTPError for bad responses
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
```

    HTTP error occurred: 404 Client Error: Not Found for url: https://jsonplaceholder.typicode.com/invalid-url


### File Uploads


```python
url = 'https://httpbin.org/post'
files = {'file': open('example.txt', 'rb')}
response = requests.post(url, files=files)
print(response.text)
```

    {
      "args": {}, 
      "data": "", 
      "files": {
        "file": ""
      }, 
      "form": {}, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Content-Length": "147", 
        "Content-Type": "multipart/form-data; boundary=a2d5f2e91f62ff97e08a96b49e3bbdd0", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.32.3", 
        "X-Amzn-Trace-Id": "Root=1-6756d178-0e0cd5a87e4f90b07dcacd97"
      }, 
      "json": null, 
      "origin": "34.106.191.177", 
      "url": "https://httpbin.org/post"
    }
    


### ***PUT Request***

Updates an existing resource or creates one if it doesn't exist.


```python
import requests

# URL of the resource you want to update
url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url)
print("Original Post:")
response.json()
```

    Original Post:





    {'userId': 1,
     'id': 1,
     'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
     'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}




```python
# Data to send in the request (usually in JSON format for REST APIs)
data = {
    "title": "Updated Title",
    "body": "This is the updated body content.",
    "userId": 1
}

# Make the PUT request
response = requests.put(url, json=data)

# Print the response status code and the content returned by the server
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")

```

    Status Code: 200
    Response Body: {
      "title": "Updated Title",
      "body": "This is the updated body content.",
      "userId": 1,
      "id": 1
    }


### ***DELETE Request***
Deletes a specified resource from the server


```python
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
response.text
```




    '{}'



### ***PATCH Request***
Partially updates a resource.

Used when you want to update only specific fields in a resource.



```python
response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', data={'title': 'patched title'})
response.json()
```




    {'userId': 1,
     'id': 1,
     'title': 'patched title',
     'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}



### ***HEAD Request***
Similar to GET, but it retrieves only the headers, not the body of the response.


```python
response = requests.head('https://jsonplaceholder.typicode.com/posts')
print('response text',response.text)
response.headers
```

    response text 





    {'Date': 'Mon, 09 Dec 2024 12:17:54 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Connection': 'keep-alive', 'Report-To': '{"group":"heroku-nel","max_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1732622443&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=DIATkaSeZpMRslaMIpIn6QUX7JmrAjxmEh%2F5WUbiAJw%3D"}]}', 'Reporting-Endpoints': 'heroku-nel=https://nel.heroku.com/reports?ts=1732622443&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=DIATkaSeZpMRslaMIpIn6QUX7JmrAjxmEh%2F5WUbiAJw%3D', 'Nel': '{"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}', 'X-Powered-By': 'Express', 'X-Ratelimit-Limit': '1000', 'X-Ratelimit-Remaining': '999', 'X-Ratelimit-Reset': '1732622496', 'Vary': 'Origin, Accept-Encoding', 'Access-Control-Allow-Credentials': 'true', 'Cache-Control': 'max-age=43200', 'Pragma': 'no-cache', 'Expires': '-1', 'X-Content-Type-Options': 'nosniff', 'Etag': 'W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"', 'Content-Encoding': 'gzip', 'Via': '1.1 vegur', 'CF-Cache-Status': 'HIT', 'Age': '237', 'Server': 'cloudflare', 'CF-RAY': '8ef4ef48de2b0922-LAX', 'alt-svc': 'h3=":443"; ma=86400', 'server-timing': 'cfL4;desc="?proto=TCP&rtt=16298&min_rtt=16161&rtt_var=6158&sent=4&recv=6&lost=0&retrans=0&sent_bytes=2841&recv_bytes=784&delivery_rate=179196&cwnd=252&unsent_bytes=0&cid=5344784bdb24587b&ts=33&x=0"'}



### Basic Authentication


```python
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org/basic-auth/user/passwd'
response = requests.get(url, auth=HTTPBasicAuth('user', 'passwd'))
print(response.status_code)

```

    200


### requests.Session()


```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'my-app'})
    response1 = session.get('https://jsonplaceholder.typicode.com/posts')
    response2 = session.get('https://jsonplaceholder.typicode.com/users')

    print(response1.status_code)
    print(response2.status_code)
    session.close()

```

    200
    200


### Binary Response Content


```python
import requests
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

# Make a request to an endpoint that returns binary content (e.g., an image or PDF)
url = 'https://drive.google.com/uc?export=download&id=1D91UYKoobRN9Hh8Jqp_nz3i0vlyq3ehj'
response = requests.get(url)
print(response.status_code)

# The binary content is available in the 'content' attribute
binary_data = response.content

# binary content to image
i = Image.open(BytesIO(binary_data))
open_cv_image = np.array(i)
open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
cv2_imshow(cv2.resize(open_cv_image,(200,200)))
```

    200



    
![png](Web_Scraping_Tutorial_files/Web_Scraping_Tutorial_45_1.png)
    


## BeautifulSoup - Parsing the HTML Content


```python
import requests

# URL of the page to scrape
url = 'https://www.wikipedia.org'

# Send a GET request to the URL
response = requests.get(url)
response.text
```




    '<!DOCTYPE html>\n<html lang="en" class="no-js">\n<head>\n<meta charset="utf-8">\n<title>Wikipedia</title>\n<meta name="description" content="Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation.">\n<script>\ndocument.documentElement.className = document.documentElement.className.replace( /(^|\\s)no-js(\\s|$)/, "$1js-enabled$2" );\n</script>\n<meta name="viewport" content="initial-scale=1,user-scalable=yes">\n<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png">\n<link rel="shortcut icon" href="/static/favicon/wikipedia.ico">\n<link rel="license" href="//creativecommons.org/licenses/by-sa/4.0/">\n<style>\n.sprite{background-image:linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/sprite-de847d1a.svg);background-repeat:no-repeat;display:inline-block;vertical-align:middle}.svg-Commons-logo_sister{background-position:0 0;width:47px;height:47px}.svg-MediaWiki-logo_sister{background-position:0 -47px;width:42px;height:42px}.svg-Meta-Wiki-logo_sister{background-position:0 -89px;width:37px;height:37px}.svg-Wikibooks-logo_sister{background-position:0 -126px;width:37px;height:37px}.svg-Wikidata-logo_sister{background-position:0 -163px;width:49px;height:49px}.svg-Wikifunctions-logo_sister{background-position:0 -212px;width:50px;height:50px}.svg-Wikimedia-logo_black{background-position:0 -262px;width:42px;height:42px}.svg-Wikipedia_wordmark{background-position:0 -304px;width:176px;height:32px}.svg-Wikiquote-logo_sister{background-position:0 -336px;width:42px;height:42px}.svg-Wikisource-logo_sister{background-position:0 -378px;width:39px;height:39px}.svg-Wikispecies-logo_sister{background-position:0 -417px;width:42px;height:42px}.svg-Wikiversity-logo_sister{background-position:0 -459px;width:43px;height:37px}.svg-Wikivoyage-logo_sister{background-position:0 -496px;width:36px;height:36px}.svg-Wiktionary-logo_sister{background-position:0 -532px;width:37px;height:37px}.svg-arrow-down{background-position:0 -569px;width:12px;height:8px}.svg-arrow-down-blue{background-position:0 -577px;width:14px;height:14px}.svg-badge_google_play_store{background-position:0 -591px;width:124px;height:38px}.svg-badge_ios_app_store{background-position:0 -629px;width:110px;height:38px}.svg-language-icon{background-position:0 -667px;width:22px;height:22px}.svg-noimage{background-position:0 -689px;width:58px;height:58px}.svg-search-icon{background-position:0 -747px;width:22px;height:22px}.svg-wikipedia_app_tile{background-position:0 -769px;width:42px;height:42px}\n</style>\n<style>\nhtml{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-size:62.5%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:700}dfn{font-style:italic}h1{font-size:32px;font-size:3.2rem;margin:1.2rem 0}mark{background:#fef6e7;color:#000}small{font-size:13px;font-size:1.3rem}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}svg:not(:root){overflow:hidden}figure{margin:1.6rem 4rem}hr{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace,monospace;font-size:14px;font-size:1.4rem}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=button],input[type=reset],input[type=submit]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=checkbox],input[type=radio]{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:0}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{height:auto}input[type=search]{-webkit-appearance:none;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration{-webkit-appearance:none}input[type=search]:focus{outline-offset:-2px}fieldset{border:1px solid #a2a9b1;margin:0 .2rem;padding:.6rem 1rem 1.2rem}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:700}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}.hidden,[hidden]{display:none!important}.screen-reader-text{display:block;position:absolute!important;clip:rect(1px,1px,1px,1px);width:1px;height:1px;margin:-1px;border:0;padding:0;overflow:hidden}body{background-color:#fff;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Inter,Helvetica,Arial,sans-serif;font-size:14px;font-size:1.4rem;line-height:1.5;margin:.4rem 0 1.6rem}main{padding:0 1.28rem}a{-ms-touch-action:manipulation;touch-action:manipulation}a,a:active,a:focus{unicode-bidi:embed;outline:0;color:#36c;text-decoration:none}a:focus{outline:1px solid #36c}a:hover{text-decoration:underline}img{vertical-align:middle}hr,img{border:0}hr{clear:both;height:0;border-bottom:1px solid #c8ccd1;margin:.26rem 0}.pure-button{display:inline-block;zoom:1;line-height:normal;white-space:nowrap;text-align:center;cursor:pointer;-webkit-user-drag:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;background-color:#f8f9fa;color:#202122;position:relative;min-height:19.2px;min-height:1.92rem;min-width:16px;min-width:1.6rem;margin:.16rem 0;border:1px solid #a2a9b1;-moz-border-radius:2px;border-radius:2px;padding:.8rem 1.6rem;font-family:inherit;font-size:inherit;font-weight:700;text-decoration:none;vertical-align:top;-webkit-transition:background .1s ease,color .1s ease,border-color .1s ease,-webkit-box-shadow .1s ease;transition:background .1s ease,color .1s ease,border-color .1s ease,-webkit-box-shadow .1s ease;-o-transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease;-moz-transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease,-moz-box-shadow .1s ease;transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease;transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease,-webkit-box-shadow .1s ease,-moz-box-shadow .1s ease}.pure-button::-moz-focus-inner{padding:0;border:0}.pure-button-hover,.pure-button:hover{background-color:#fff;border-color:#a2a9b1;color:#404244}.pure-button-active,.pure-button:active{background-color:#eaecf0;border-color:#72777d;color:#000}.pure-button:focus{outline:1px solid transparent;border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c;-moz-box-shadow:inset 0 0 0 1px #36c;box-shadow:inset 0 0 0 1px #36c}.pure-button-primary-progressive{background-color:#36c;border-color:#36c;color:#fff}.pure-button-primary-progressive:hover{background:#447ff5;border-color:#447ff5}.pure-button-primary-progressive:active{background-color:#2a4b8d;border-color:#2a4b8d;-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none;color:#fff}.pure-button-primary-progressive:focus{-webkit-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;-moz-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;border-color:#36c}.pure-form input[type=search]{background-color:#fff;display:inline-block;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;border:1px solid #a2a9b1;-moz-border-radius:2px;border-radius:2px;padding:.8rem;-webkit-box-shadow:inset 0 0 0 1px #fff;-moz-box-shadow:inset 0 0 0 1px #fff;box-shadow:inset 0 0 0 1px #fff;vertical-align:middle}.pure-form input:focus:invalid{color:#d73333;border-color:#b32424}.pure-form fieldset{margin:0;padding:.56rem 0 1.2rem;border:0}@media only screen and (max-width:480px){.pure-form input[type=search]{display:block}}.central-textlogo-wrapper{display:inline-block;vertical-align:bottom}.central-textlogo{position:relative;margin:4rem auto .5rem;width:270px;font-family:Linux Libertine,Hoefler Text,Georgia,Times New Roman,Times,serif;font-size:30px;font-size:3rem;font-weight:400;line-height:33px;line-height:3.3rem;text-align:center;-moz-font-feature-settings:"ss05=1";-moz-font-feature-settings:"ss05";-webkit-font-feature-settings:"ss05";-ms-font-feature-settings:"ss05";font-feature-settings:"ss05"}.localized-slogan{display:block;font-family:Linux Libertine,Georgia,Times,"Source Serif Pro",serif;font-size:15px;font-size:1.5rem;font-weight:400}.central-textlogo__image{color:transparent;display:inline-block;overflow:hidden;text-indent:-10000px}.central-featured-logo{position:absolute;top:158px;left:35px}@media (max-width:480px){.central-textlogo{position:relative;height:70px;width:auto;margin:2rem 0 0;text-align:center;line-height:25px;line-height:2.5rem;text-indent:-10px;text-indent:-1rem;font-size:1em}.central-textlogo-wrapper{position:relative;top:12px;text-indent:2px;text-indent:.2rem}.svg-Wikipedia_wordmark{width:150px;height:25px;background-position:0 -260px;-webkit-background-size:100% 100%;-moz-background-size:100%;background-size:100%}.localized-slogan{font-size:14px;font-size:1.4rem}.central-featured-logo{position:relative;display:inline-block;width:57px;height:auto;left:0;top:0}}@media (max-width:240px){.central-textlogo__image{height:auto}}.central-featured{position:relative;height:325px;height:32.5rem;width:546px;width:54.6rem;max-width:100%;margin:0 auto;text-align:center;vertical-align:middle}.central-featured-lang{position:absolute;width:156px;width:15.6rem}.central-featured-lang .link-box{display:block;padding:0;text-decoration:none;white-space:normal}.central-featured-lang .link-box:hover strong{text-decoration:underline}.central-featured-lang :hover{background-color:#eaecf0}.central-featured-lang strong{display:block;font-size:16px;font-size:1.6rem}.central-featured-lang small{color:#54595d;display:inline-block;font-size:13px;font-size:1.3rem;line-height:1.6}.central-featured-lang em{font-style:italic}.central-featured-lang .emNonItalicLang{font-style:normal}.lang1{top:0;right:60%}.lang2{top:0;left:60%}.lang3{top:20%;right:70%}.lang4{top:20%;left:70%}.lang5{top:40%;right:72%}.lang6{top:40%;left:72%}.lang7{top:60%;right:70%}.lang8{top:60%;left:70%}.lang9{top:80%;right:60%}.lang10{top:80%;left:60%}@media (max-width:480px){.central-featured{width:auto;height:auto;margin-top:8rem;font-size:13px;font-size:1.3rem;text-align:left}.central-featured:after{content:" ";display:block;visibility:hidden;clear:both;height:0;font-size:0}.central-featured-lang{display:block;float:left;position:relative;top:auto;left:auto;right:auto;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;height:64px;height:6.4rem;width:33%;margin:0 0 16px;padding:0 1.6rem;font-size:14px;font-size:1.4rem;text-align:center}.central-featured-lang strong{font-size:14px;font-size:1.4rem;margin-bottom:4px}.central-featured-lang small{line-height:1.4}}@media (max-width:375px){.central-featured-lang{font-size:13px;font-size:1.3rem}}@media (max-width:240px){.central-featured-lang{width:100%}}.search-container{float:none;max-width:95%;width:540px;margin:.4rem auto 1.95rem;text-align:center;vertical-align:middle}.search-container fieldset{word-spacing:-4px}.search-container button{min-height:44px;min-height:4.4rem;margin:0;-moz-border-radius:0 2px 2px 0;border-radius:0 2px 2px 0;padding:.8rem 1.6rem;font-size:16px;font-size:1.6rem;z-index:2}.search-container button .svg-search-icon{text-indent:-9999px}.search-container input[type=search]::-webkit-search-results-button,.search-container input[type=search]::-webkit-search-results-decoration{-webkit-appearance:none}.search-container input::-webkit-calendar-picker-indicator{display:none}.search-container .sprite.svg-arrow-down{position:absolute;top:8px;top:.8rem;right:6px;right:.6rem}#searchInput{-webkit-appearance:none;width:100%;height:44px;height:4.4rem;border-width:1px 0 1px 1px;-moz-border-radius:2px 0 0 2px;border-radius:2px 0 0 2px;padding:.8rem 9.6rem .8rem 1.2rem;font-size:16px;font-size:1.6rem;line-height:1.6;-webkit-transition:background .1s ease,border-color .1s ease,-webkit-box-shadow .1s ease;transition:background .1s ease,border-color .1s ease,-webkit-box-shadow .1s ease;-o-transition:background .1s ease,border-color .1s ease,box-shadow .1s ease;-moz-transition:background .1s ease,border-color .1s ease,box-shadow .1s ease,-moz-box-shadow .1s ease;transition:background .1s ease,border-color .1s ease,box-shadow .1s ease;transition:background .1s ease,border-color .1s ease,box-shadow .1s ease,-webkit-box-shadow .1s ease,-moz-box-shadow .1s ease}#searchInput:hover{border-color:#72777d}#searchInput:focus{border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c;-moz-box-shadow:inset 0 0 0 1px #36c;box-shadow:inset 0 0 0 1px #36c;outline:1px solid transparent}.search-container .search-input{display:inline-block;position:relative;width:73%;vertical-align:top}@media only screen and (max-width:480px){.search-container .pure-form fieldset{margin-left:1rem;margin-right:6.6rem}.search-container .search-input{width:100%;margin-right:-6.6rem}.search-container .pure-form button{float:right;right:-56px;right:-5.6rem}}.suggestions-dropdown{background-color:#fff;display:inline-block;position:absolute;left:0;z-index:2;margin:0;padding:0;border:1px solid #a2a9b1;border-top:0;-webkit-box-shadow:0 2px 2px 0 rgba(0,0,0,.2);-moz-box-shadow:0 2px 2px 0 rgba(0,0,0,.2);box-shadow:0 2px 2px 0 rgba(0,0,0,.2);list-style-type:none;word-spacing:normal}.suggestion-link,.suggestions-dropdown{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:100%;text-align:left}.suggestion-link{display:block;position:relative;min-height:70px;min-height:7rem;padding:1rem 1rem 1rem 8.5rem;border-bottom:1px solid #eaecf0;color:inherit;text-decoration:none;text-align:initial;white-space:normal}.suggestion-link.active{background-color:#eaf3ff}a.suggestion-link:hover{text-decoration:none}a.suggestion-link:active,a.suggestion-link:focus{outline:0;white-space:normal}.suggestion-thumbnail{background-color:#eaecf0;background-image:url(portal/wikipedia.org/assets/img/noimage.png);background-image:-webkit-linear-gradient(transparent,transparent),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 56 56\'%3E%3Cpath fill=\'%23eee\' d=\'M0 0h56v56H0z\'/%3E%3Cpath fill=\'%23999\' d=\'M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z\'/%3E%3C/svg%3E");background-image:-webkit-linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:-webkit-gradient(linear,left top,left bottom,from(transparent),to(transparent)),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 56 56\'%3E%3Cpath fill=\'%23eee\' d=\'M0 0h56v56H0z\'/%3E%3Cpath fill=\'%23999\' d=\'M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z\'/%3E%3C/svg%3E");background-image:-moz- oldlinear-gradient(transparent,transparent),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 56 56\'%3E%3Cpath fill=\'%23eee\' d=\'M0 0h56v56H0z\'/%3E%3Cpath fill=\'%23999\' d=\'M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z\'/%3E%3C/svg%3E");background-image:-o-linear-gradient(transparent,transparent),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 56 56\'%3E%3Cpath fill=\'%23eee\' d=\'M0 0h56v56H0z\'/%3E%3Cpath fill=\'%23999\' d=\'M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z\'/%3E%3C/svg%3E");background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 56 56\'%3E%3Cpath fill=\'%23eee\' d=\'M0 0h56v56H0z\'/%3E%3Cpath fill=\'%23999\' d=\'M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z\'/%3E%3C/svg%3E");background-image:-webkit-gradient(linear,left top,left bottom,from(transparent),to(transparent)),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:-moz- oldlinear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:-o-linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:-o-linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.png);background-position:50%;background-repeat:no-repeat;-webkit-background-size:100% auto;-moz-background-size:100% auto;background-size:100% auto;-webkit-background-size:cover;-moz-background-size:cover;background-size:cover;height:100%;width:70px;width:7rem;position:absolute;top:0;left:0}.suggestion-title{margin:0 0 .78rem;color:#54595d;font-size:16px;font-size:1.6rem;line-height:18.72px;line-height:1.872rem}.suggestion-link.active .suggestion-title{color:#36c}.suggestion-highlight{font-style:normal;text-decoration:underline}.suggestion-description{color:#72777d;margin:0;font-size:13px;font-size:1.3rem;line-height:14.299px;line-height:1.43rem}.styled-select{display:none;position:absolute;top:10px;top:1rem;bottom:12px;bottom:1.2rem;right:12px;right:1.2rem;max-width:95px;max-width:9.5rem;height:24px;height:2.4rem;-moz-border-radius:2px;border-radius:2px}.styled-select:hover{background-color:#f8f9fa}.styled-select .hide-arrow{right:32px;right:3.2rem;max-width:68px;max-width:6.8rem;height:24px;height:2.4rem;overflow:hidden;text-align:right}.styled-select select{background:transparent;display:inline;overflow:hidden;height:24px;height:2.4rem;min-width:110px;min-width:11rem;max-width:110px;max-width:11rem;width:110px;width:11rem;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;border:0;line-height:24px;line-height:2.4rem;-webkit-appearance:none;-moz-appearance:window;text-indent:.01px;-o-text-overflow:"";text-overflow:"";opacity:0;-moz-appearance:none;appearance:none;cursor:pointer}.styled-select.no-js{width:95px;width:9.5rem}.styled-select.no-js select{opacity:1;margin:0;padding:0 2.4rem 0 .8rem;color:#54595d}.styled-select.no-js .hide-arrow{width:68px;width:6.8rem}.search-container .styled-select.no-js .js-langpicker-label{display:none}.styled-select.js-enabled .hide-arrow{padding:0 2.4rem 0 .8rem}.styled-select.js-enabled select{background:transparent;position:absolute;top:0;left:0;height:100%;z-index:1;width:100%;border:0;margin:0;padding:0 2.4rem;color:transparent;color:hsla(0,0%,100%,0)}.styled-select.js-enabled select option{color:#54595d}.styled-select.js-enabled select:hover{background-color:transparent}.styled-select-active-helper{display:none}.styled-select.js-enabled select:focus+.styled-select-active-helper{display:block;position:absolute;top:0;left:0;z-index:0;width:100%;height:100%;outline:1px solid #36c}.search-container .js-langpicker-label{display:inline-block;margin:0;color:#54595d;font-size:13px;font-size:1.3rem;line-height:24px;line-height:2.4rem;text-transform:uppercase}.styled-select select:hover{background-color:#f8f9fa}.styled-select select::-ms-expand{display:none}.styled-select select:focus{outline:1px solid transparent;-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none}@-moz-document url-prefix(){.styled-select select{width:110%}}.other-projects{display:inline-block;width:65%}.other-project{float:left;position:relative;width:33%;height:90px;height:9rem}.other-project-link{display:inline-block;min-height:50px;width:90%;padding:1em;white-space:nowrap}.other-project-link:hover{background-color:#eaecf0}a.other-project-link{text-decoration:none}.other-project-icon{display:inline-block;width:50px;text-align:center}.svg-Wikinews-logo_sister{background-image:url(portal/wikipedia.org/assets/img/Wikinews-logo_sister.png);background-position:0 0;-webkit-background-size:47px 26px;-moz-background-size:47px 26px;background-size:47px 26px;width:47px;height:26px}@media (-o-min-device-pixel-ratio:5/4),(-webkit-min-device-pixel-ratio:1.25),(min-resolution:120dpi){.svg-Wikinews-logo_sister{background-image:url(portal/wikipedia.org/assets/img/Wikinews-logo_sister@2x.png)}}.other-project-text,.other-project .sprite-project-logos{display:inline-block}.other-project-text{max-width:65%;font-size:14px;font-size:1.4rem;vertical-align:middle;white-space:normal}.other-project-tagline,.other-project-title{display:block}.other-project-tagline{color:#54595d;font-size:13px;font-size:1.3rem}@media screen and (max-width:768px){.other-projects{width:100%}.other-project{width:33%}}@media screen and (max-width:480px){.other-project{width:50%}.other-project-tagline{-webkit-hyphens:auto;-moz-hyphens:auto;-ms-hyphens:auto;hyphens:auto}}@media screen and (max-width:320px){.other-project-text{margin-right:5px;font-size:13px;font-size:1.3rem}}.lang-list-container{background-color:#f8f9fa;overflow:hidden;position:relative;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;max-height:0;width:80%;margin:-1.6rem auto 4.8rem;-webkit-transition:max-height .5s ease-out .16s,visibility .5s ease-in 1s;-o-transition:max-height .5s ease-out .16s,visibility .5s ease-in 1s;-moz-transition:max-height .5s ease-out .16s,visibility .5s ease-in 1s;transition:max-height .5s ease-out .16s,visibility .5s ease-in 1s}.js-enabled .lang-list-container{visibility:hidden}.lang-list-active .lang-list-container,.no-js .lang-list-container{visibility:visible;max-height:10000px;-webkit-transition:max-height 1s ease-in .2s,visibility 1000s ease-in 0ms;-o-transition:max-height 1s ease-in .2s,visibility 1000s ease-in 0ms;-moz-transition:max-height 1s ease-in .2s,visibility 1000s ease-in 0ms;transition:max-height 1s ease-in .2s,visibility 1000s ease-in 0ms}.no-js .lang-list-button{display:none}.lang-list-button-wrapper{text-align:center}.lang-list-button{background-color:#f8f9fa;display:inline;position:relative;z-index:1;margin:0 auto;padding:.6rem 1.2rem;outline:16px solid #fff;outline:1.6rem solid #fff;border:1px solid #a2a9b1;-moz-border-radius:2px;border-radius:2px;color:#36c;font-size:14px;font-size:1.4rem;font-weight:700;line-height:1;-webkit-transition:outline-width .1s ease-in .5s;-o-transition:outline-width .1s ease-in .5s;-moz-transition:outline-width .1s ease-in .5s;transition:outline-width .1s ease-in .5s}.lang-list-button:hover{background-color:#fff;border-color:#a2a9b1}.lang-list-button:focus{border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c;-moz-box-shadow:inset 0 0 0 1px #36c;box-shadow:inset 0 0 0 1px #36c}.lang-list-active .lang-list-button{background-color:#fff;outline:1px solid #fff;border-color:#72777d;-webkit-transition-delay:0s;-moz-transition-delay:0s;-o-transition-delay:0s;transition-delay:0s}.lang-list-button-text{padding:0 .64rem;vertical-align:middle}.lang-list-button i{display:inline-block;vertical-align:middle}.no-js .lang-list-border,.no-js .lang-list-button{display:none}.lang-list-border{background-color:#c8ccd1;display:block;position:relative;max-width:460px;width:80%;margin:-1.6rem auto 1.6rem;height:1px;-webkit-transition:max-width .2s ease-out .4s;-o-transition:max-width .2s ease-out .4s;-moz-transition:max-width .2s ease-out .4s;transition:max-width .2s ease-out .4s}.lang-list-active .lang-list-border{max-width:85%;-webkit-transition-delay:0s;-moz-transition-delay:0s;-o-transition-delay:0s;transition-delay:0s}.no-js .lang-list-content{padding:0}.lang-list-content{position:relative;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:100%;padding:1.6rem 1.6rem 0}.svg-arrow-down-blue{-webkit-transition:-webkit-transform .2s ease-out;transition:-webkit-transform .2s ease-out;-o-transition:transform .2s ease-out;-moz-transition:transform .2s ease-out,-moz-transform .2s ease-out;transition:transform .2s ease-out;transition:transform .2s ease-out,-webkit-transform .2s ease-out,-moz-transform .2s ease-out}.lang-list-active .svg-arrow-down-blue{-webkit-transform:rotate(180deg);-moz-transform:rotate(180deg);-ms-transform:rotate(180deg);transform:rotate(180deg)}.langlist{width:auto;margin:1.6rem 0;text-align:left}.langlist-others{font-weight:700;text-align:center}.hlist ul{margin:0;padding:0}.hlist li,.hlist ul ul{display:inline}.hlist li:before{content:" Â· ";font-weight:700}.hlist li:first-child:before{content:none}.hlist li>ul:before{content:"\\00a0("}.hlist li>ul:after{content:") "}.langlist>ul{-webkit-column-width:11.2rem;-moz-column-width:11.2rem;column-width:11.2rem}.langlist>ul>li{display:block;line-height:1.7;-webkit-column-break-inside:avoid;page-break-inside:avoid;break-inside:avoid}.no-js .langlist>ul{text-align:center;list-style-type:circle}.no-js .langlist>ul>li{display:inline-block;padding:0 .8rem}.langlist>ul>li:before{content:none}.langlist>ul>li a{white-space:normal}@media (max-width:480px){.langlist{font-size:inherit}.langlist a{word-wrap:break-word;white-space:normal}.lang-list-container{width:auto;margin-left:.8rem;margin-right:.8rem}.bookshelf{overflow:visible}}.bookshelf{display:block;border-top:1px solid #c8ccd1;-webkit-box-shadow:0 -1px 0 #fff;-moz-box-shadow:0 -1px 0 #fff;box-shadow:0 -1px 0 #fff;text-align:center;white-space:nowrap}.bookshelf .text{background-color:#f8f9fa;position:relative;top:-11.2px;top:-1.12rem;font-weight:400;padding:0 .8rem}.bookshelf-container{display:block;overflow:visible;width:100%;height:1px;margin:2.4rem 0 1.6rem;font-size:13px;font-size:1.3rem;font-weight:700;line-height:1.5}@media (max-width:480px){.bookshelf{width:auto;left:auto}.bookshelf-container{text-align:left;width:auto}}.app-badges .footer-sidebar-content{background-color:#f8f9fa}.app-badges .footer-sidebar-text{padding-top:.8rem;padding-bottom:.8rem}.app-badges .sprite.footer-sidebar-icon{top:8px;top:.8rem}.app-badges ul{margin:0;padding:0;list-style-type:none}.app-badge{display:inline-block}.app-badge a{color:transparent}@media screen and (max-width:768px){.app-badges .footer-sidebar-content{text-align:center}.app-badges .sprite.footer-sidebar-icon{display:inline-block;position:relative;margin:0;top:-3px;left:0;vertical-align:middle;-webkit-transform:scale(.7);-moz-transform:scale(.7);-ms-transform:scale(.7);transform:scale(.7)}}.footer{overflow:hidden;max-width:100%;margin:0 auto;padding:4.16rem 1.28rem 0;font-size:13px;font-size:1.3rem}.footer:after,.footer:before{content:" ";display:table}.footer:after{clear:both}.footer-sidebar{width:35%;float:left;clear:left;margin-bottom:3.2rem;vertical-align:top}.footer-sidebar-content{position:relative;max-width:350px;margin:0 auto}.sprite.footer-sidebar-icon{position:absolute;top:0;left:8px;left:.8rem}.footer-sidebar-text{position:relative;margin:0;padding-left:6rem;padding-right:2rem;color:#54595d}.site-license{color:#54595d;text-align:center}.site-license small:after{content:"\\2022";display:inline-block;font-size:13px;font-size:1.3rem;line-height:inherit;margin-left:.8rem;margin-right:.5rem}.site-license small:last-child:after{display:none}.footer hr{margin-top:1.28rem}@media screen and (max-width:768px){.footer{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;padding-top:1.28rem}.footer .footer-sidebar{-webkit-box-ordinal-group:1;-moz-box-ordinal-group:1;-webkit-order:1;-ms-flex-order:1;order:1}.footer .other-projects{-webkit-box-ordinal-group:2;-moz-box-ordinal-group:2;-webkit-order:2;-ms-flex-order:2;order:2}.footer .app-badges{-webkit-box-ordinal-group:3;-moz-box-ordinal-group:3;-webkit-order:3;-ms-flex-order:3;order:3}.footer hr{-webkit-box-ordinal-group:4;-moz-box-ordinal-group:4;-webkit-order:4;-ms-flex-order:4;order:4}.footer .site-license{-webkit-box-ordinal-group:5;-moz-box-ordinal-group:5;-webkit-order:5;-ms-flex-order:5;order:5}.footer-sidebar{width:100%}.sprite.footer-sidebar-icon{display:block;position:relative;left:0;margin:0 auto 1.28rem}.footer-sidebar-content{max-width:none}.footer-sidebar-text{margin:0;padding:0;text-align:center}}@media screen and (max-width:480px){.footer{padding:.96rem .64rem 1.28rem}}@media (max-width:480px){.search-container{margin-top:0;height:78px;height:7.8rem;position:absolute;top:96px;top:9.6rem;left:0;right:0;max-width:100%;width:auto;padding:0;text-align:left}.search-container label{display:none}.search-form #searchInput{max-width:40%;vertical-align:middle}.search-form .formBtn{max-width:25%;vertical-align:middle}form fieldset{margin:0;border-left:0;border-right:0}hr{margin-top:.65rem}}@media (-o-min-device-pixel-ratio:2/1),(-webkit-min-device-pixel-ratio:2),(min--moz-device-pixel-ratio:2),(min-resolution:2dppx),(min-resolution:192dpi){hr{border-bottom-width:.5px}}@supports (-webkit-marquee-style:slide){hr{border-bottom-width:1px}}.js-enabled .central-featured,.js-enabled .jsl10n{opacity:0}.jsl10n-visible .central-featured,.jsl10n-visible .jsl10n{opacity:1}@media print{body{background-color:transparent}a{color:#000!important;background:none!important;padding:0!important}a:link,a:visited{color:#520;background:transparent}img{border:0}}body{overflow-x:hidden}.banner,.banner *{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}.banner{display:none;position:relative;z-index:3}.banner.banner--visible{display:block}.banner__close{position:absolute;margin-top:-24px;margin-right:-24px;padding:12px;top:0;right:0;cursor:pointer;background:none;border:0}.banner__button{display:inline-block;border:1px solid;-moz-border-radius:2px;border-radius:2px;padding:8px 12px;cursor:pointer;font-weight:700;white-space:nowrap;line-height:1;margin-top:8px}.banner__button,.banner__button:hover{text-decoration:none}.overlay-banner-main{max-width:500px;position:fixed;right:10px;bottom:20px;background:#fff;-moz-border-radius:10px 10px 0 0;border-radius:10px 10px 0 0;width:-webkit-calc(100% - 20px);width:-moz-calc(100% - 20px);width:calc(100% - 20px);padding:0 8px 8px;height:80vh;border:1px solid #a2a9b1;-webkit-box-shadow:0 0 15px rgba(50,50,50,.25);-moz-box-shadow:0 0 15px rgba(50,50,50,.25);box-shadow:0 0 15px rgba(50,50,50,.25);-webkit-transition:all .15s ease-in-out;-o-transition:all .15s ease-in-out;-moz-transition:all .15s ease-in-out;transition:all .15s ease-in-out;-webkit-transform-origin:100% 50%;-moz-transform-origin:100% 50%;-ms-transform-origin:100% 50%;transform-origin:100% 50%;-webkit-transform:scale(.5);-moz-transform:scale(.5);-ms-transform:scale(.5);transform:scale(.5);visibility:hidden;opacity:0}body.overlay-banner-open .overlay-banner-main{visibility:visible;opacity:1;-webkit-transform:scale(1);-moz-transform:scale(1);-ms-transform:scale(1);transform:scale(1)}.overlay-banner-main-scroll{padding-bottom:16px;max-height:-webkit-calc(100% - 42px);max-height:-moz-calc(100% - 42px);max-height:calc(100% - 42px);overflow-y:auto;overflow-x:hidden;-webkit-transition:max-height .5s;-o-transition:max-height .5s;-moz-transition:max-height .5s;transition:max-height .5s}.overlay-banner-main .frb-header-minimize{top:-48px;position:absolute;right:10px;background:#000;background:rgba(0,0,0,.75);-moz-border-radius:12px 12px 0 0;border-radius:12px 12px 0 0;padding:6px 12px;color:#fff;font-weight:700;text-align:center;font-size:16px;cursor:pointer;width:48px;height:48px}.overlay-banner-main .frb-header-minimize,.overlay-banner-main .frb-header-minimize-icon{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center}.overlay-banner-main .frb-header-minimize-icon{width:40px;height:40px;-moz-border-radius:2px;border-radius:2px;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center}.overlay-banner-main .frb-header-minimize-icon svg{filter:url(\'data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg"><filter id="filter"><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="1 0" /><feFuncG type="table" tableValues="1 0" /><feFuncB type="table" tableValues="1 0" /></feComponentTransfer></filter></svg>#filter\');-webkit-filter:invert(1);filter:invert(1);width:25px;height:auto;margin-left:-2px}.overlay-banner-main-header{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;width:100%;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center}.overlay-banner-main-header a{-webkit-box-flex:1;-webkit-flex:1 0 auto;-moz-box-flex:1;-ms-flex:1 0 auto;flex:1 0 auto;text-align:center;padding:11px 6px;border:0;background:transparent;color:#36c;font-weight:700;position:relative}.overlay-banner-main-header a:hover{text-decoration:underline;cursor:pointer}.overlay-banner-main-message{position:relative;clear:both;margin-bottom:12px;padding:10px 15px;background-color:#308557;color:#fff;-moz-border-radius:1.5em;border-radius:1.5em;font-size:16px;line-height:1.5}@media (min-width:720px){.overlay-banner-main-message{padding:12px 20px;font-size:17px;line-height:1.5294117647}}.overlay-banner-main-message-greeting{font-size:1.5em;line-height:1.15;font-weight:700;text-align:center;margin-top:8px}.overlay-banner-main-message-subheading{font-size:16px;line-height:1.35;font-weight:700;text-align:center;margin-top:8px;margin-bottom:16px}.overlay-banner-main-message p{font-size:inherit!important;line-height:inherit!important;margin-bottom:16px}.overlay-banner-main .button-grid{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-column-gap:1%;-moz-column-gap:1%;column-gap:1%;row-gap:5px}.overlay-banner-main .banner-button,.overlay-banner-main .button-grid{width:100%;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex}.overlay-banner-main .banner-button{-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;height:54px;color:#36c;background-color:#f8f9fa;-moz-border-radius:10px;border-radius:10px;border:1px solid #a2a9b1;text-align:center;cursor:pointer;-webkit-transition:all .2s ease;-o-transition:all .2s ease;-moz-transition:all .2s ease;transition:all .2s ease;font-weight:700;padding:5px 6px;line-height:1}.overlay-banner-main .banner-button:focus,.overlay-banner-main .banner-button:focus-within{border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;-moz-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff}.overlay-banner-main .button-33{-webkit-box-flex:0;-webkit-flex:0 1 32%;-moz-box-flex:0;-ms-flex:0 1 32%;flex:0 1 32%;max-width:32%}.overlay-banner-main .button-67{-webkit-box-flex:0;-webkit-flex:0 1 65%;-moz-box-flex:0;-ms-flex:0 1 65%;flex:0 1 65%;max-width:65%}.overlay-banner-main .button-50{-webkit-box-flex:0;-webkit-flex:0 1 49%;-moz-box-flex:0;-ms-flex:0 1 49%;flex:0 1 49%;max-width:49%}.overlay-banner-main .button-center{margin:0 auto}.overlay-banner-main .button-collapse{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;width:auto;height:54px;color:#000;font-weight:700;background:transparent;border:0;text-transform:uppercase;margin-top:15px;cursor:pointer}.overlay-banner-main .button-collapse:hover{text-decoration:underline}.overlay-banner-main .banner-button-disabled{opacity:.5;color:#a2a9b1}.overlay-banner-main .banner-button.selected{background-color:#36c;border-color:#2a4b8d;color:#fff}.overlay-banner-main-amounts,.overlay-banner-main-frequency{position:relative;background-color:#dbf3ec;padding:15px;-moz-border-radius:1.5em;border-radius:1.5em;margin-bottom:10px}.overlay-banner-main-amounts .error-highlight,.overlay-banner-main-frequency .error-highlight{font-weight:500}.overlay-banner-main-amounts .button-grid,.overlay-banner-main-frequency .button-grid{padding:18px 0 10px}.overlay-banner-main-footer-cta{margin:8px 0;background-color:#f9dde9;color:#000;padding:10px 18px;font-size:16px;line-height:1.5;-moz-border-radius:1.5em;border-radius:1.5em}.frb-message-icon circle{fill:#b32424}.frb-message-icon path{fill:#fff}.overlay-banner-main-footer-identity{position:relative;clear:both;margin:20px 0 0;color:#000;-moz-border-radius:1.5em;border-radius:1.5em;line-height:1.3;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;padding:0 10px}.overlay-banner-main-footer-identity img{width:100%;max-width:110px;margin-right:10px}.overlay-banner-mini{position:fixed;right:0;left:0;bottom:-500px;z-index:9999;background:#308557;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-pack:start;-webkit-justify-content:flex-start;-moz-box-pack:start;-ms-flex-pack:start;justify-content:flex-start;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;border-top:2px solid #266a46;-webkit-box-shadow:0 -2px 10px 0 rgba(0,0,0,.25);-moz-box-shadow:0 -2px 10px 0 rgba(0,0,0,.25);box-shadow:0 -2px 10px 0 rgba(0,0,0,.25);-webkit-transition:all .3s ease;-o-transition:all .3s ease;-moz-transition:all .3s ease;transition:all .3s ease}.overlay-banner-mini.visible{bottom:-20px;right:0;left:0}.overlay-banner-mini .frb-conversation-close,.overlay-banner-mini .frb-conversation-open{top:-50px;position:absolute;right:10px;background:#000;background:rgba(0,0,0,.75);-moz-border-radius:12px 12px 0 0;border-radius:12px 12px 0 0;padding:6px 12px;color:#fff;font-weight:700;text-align:center;font-size:16px;display:none;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;cursor:pointer;width:48px;height:48px}.overlay-banner-mini .frb-conversation-open{right:60px}span.frb-conversation-close-icon:after,span.frb-conversation-close-icon:before{position:absolute;left:50%;top:12px;-webkit-transform:translateX(-50%);-moz-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);content:" ";height:25px;width:3px;margin-left:-1px;background-color:#fff}span.frb-conversation-close-icon:before{-webkit-transform:rotate(45deg);-moz-transform:rotate(45deg);-ms-transform:rotate(45deg);transform:rotate(45deg)}span.frb-conversation-close-icon:after{-webkit-transform:rotate(-45deg);-moz-transform:rotate(-45deg);-ms-transform:rotate(-45deg);transform:rotate(-45deg)}.frb-conversation-open-icon{width:40px;height:40px;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-moz-border-radius:2px;border-radius:2px;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center}.frb-conversation-open-icon svg{-webkit-transform:rotate(180deg);-moz-transform:rotate(180deg);-ms-transform:rotate(180deg);transform:rotate(180deg);filter:url(\'data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg"><filter id="filter"><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="1 0" /><feFuncG type="table" tableValues="1 0" /><feFuncB type="table" tableValues="1 0" /></feComponentTransfer></filter></svg>#filter\');-webkit-filter:invert(1);filter:invert(1);width:25px;height:auto}.overlay-banner-mini-message,.overlay-banner-mini.visible .frb-conversation-close,.overlay-banner-mini.visible .frb-conversation-open{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex}.overlay-banner-mini-message{-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;width:100%;padding:20px 20px 30px;cursor:pointer}.overlay-banner-mini-message-text{-webkit-box-flex:0;-webkit-flex:0 1 1200px;-moz-box-flex:0;-ms-flex:0 1 1200px;flex:0 1 1200px;max-width:1200px}@media (max-width:960px){.overlay-banner-mini-message{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap}.overlay-banner-mini-message-text{margin-bottom:10px}.overlay-banner-mini-message-actions,.overlay-banner-mini-message-text{-webkit-box-flex:0;-webkit-flex:0 0 100%;-moz-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}}.overlay-banner-mini-message h3{color:#fff;margin:0 0 5px;font-size:24px;font-family:Montserrat,Helvetica Neue,Helvetica,Arial,sans-serif}.overlay-banner-mini-message p{display:block;color:#fff;position:relative;margin:0 13px 5px 0;font-size:17px}.overlay-banner-mini .frb-message-icon{position:relative;top:0;margin-right:3px;-webkit-box-flex:0;-webkit-flex:0 0 30px;-moz-box-flex:0;-ms-flex:0 0 30px;flex:0 0 30px}.overlay-banner-mini .frb-message-icon circle{fill:#f0bc00}.overlay-banner-mini .frb-message-icon path{fill:#000}.overlay-banner-mini .frb-submit{position:relative;display:inline-block;padding:10px 15px;margin:0;width:240px;background-color:#f0bc00;border-color:#f0bc00;color:#000;-moz-border-radius:2px;border-radius:2px;text-align:center;font-weight:700;font-size:20px;cursor:pointer;-webkit-transition:background-color .5s ease;-o-transition:background-color .5s ease;-moz-transition:background-color .5s ease;transition:background-color .5s ease}.overlay-banner-mini .frb-submit:hover{background:#71d1b3;border-color:#71d1b3}.overlay-banner-mini .frb-submit:focus{border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;-moz-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff}@media (max-width:660px){.overlay-banner-mini-message h3{font-size:20px}.overlay-banner-mini-message p{font-size:13px}.overlay-banner-mini .frb-submit{width:100%}}.sr-only{border:0!important;clip:rect(1px,1px,1px,1px)!important;-webkit-clip-path:inset(50%)!important;clip-path:inset(50%)!important;height:1px!important;margin:-1px!important;overflow:hidden!important;padding:0!important;position:absolute!important;width:1px!important;white-space:nowrap!important}\n</style>\n<link rel="preconnect" href="//upload.wikimedia.org">\n<link rel="me" href="https://wikis.world/@wikipedia">\n<meta property="og:url" content>\n<meta property="og:title" content="Wikipedia, the free encyclopedia">\n<meta property="og:type" content="website">\n<meta property="og:description" content="Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation.">\n<meta property="og:image" content="https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png">\n</head>\n<body id="www-wikipedia-org">\n<main>\n<div class="central-textlogo">\n<img class="central-featured-logo" src="portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png" srcset="portal/wikipedia.org/assets/img/Wikipedia-logo-v2@1.5x.png 1.5x, portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png 2x" width="200" height="183" alt>\n<h1 class="central-textlogo-wrapper">\n<span class="central-textlogo__image sprite svg-Wikipedia_wordmark">\nWikipedia\n</span>\n<strong class="jsl10n localized-slogan" data-jsl10n="portal.slogan">The Free Encyclopedia</strong>\n</h1>\n</div>\n<nav data-jsl10n="top-ten-nav-label" aria-label="Top languages" class="central-featured" data-el-section="primary links">\n<!-- #1. en.wikipedia.org - 1,687,212,000 views/day -->\n<div class="central-featured-lang lang1" lang="en" dir="ltr">\n<a id="js-link-box-en" href="//en.wikipedia.org/" title="English â\x80\x94 Wikipedia â\x80\x94 The Free Encyclopedia" class="link-box" data-slogan="The Free Encyclopedia">\n<strong>English</strong>\n<small>6,918,000+ <span>articles</span></small>\n</a>\n</div>\n<!-- #2. ru.wikipedia.org - 204,861,000 views/day -->\n<div class="central-featured-lang lang2" lang="ru" dir="ltr">\n<a id="js-link-box-ru" href="//ru.wikipedia.org/" title="Russkiy â\x80\x94 Ð\x92Ð¸ÐºÐ¸Ð¿ÐµÐ´Ð¸Ñ\x8f â\x80\x94 Ð¡Ð²Ð¾Ð±Ð¾Ð´Ð½Ð°Ñ\x8f Ñ\x8dÐ½Ñ\x86Ð¸ÐºÐ»Ð¾Ð¿ÐµÐ´Ð¸Ñ\x8f" class="link-box" data-slogan="Ð¡Ð²Ð¾Ð±Ð¾Ð´Ð½Ð°Ñ\x8f Ñ\x8dÐ½Ñ\x86Ð¸ÐºÐ»Ð¾Ð¿ÐµÐ´Ð¸Ñ\x8f">\n<strong>Ð\xa0Ñ\x83Ñ\x81Ñ\x81ÐºÐ¸Ð¹</strong>\n<small>2Â\xa0012Â\xa0000+ <span>Ñ\x81Ñ\x82Ð°Ñ\x82ÐµÐ¹</span></small>\n</a>\n</div>\n<!-- #3. ja.wikipedia.org - 203,232,000 views/day -->\n<div class="central-featured-lang lang3" lang="ja" dir="ltr">\n<a id="js-link-box-ja" href="//ja.wikipedia.org/" title="Nihongo â\x80\x94 ã\x82¦ã\x82£ã\x82\xadã\x83\x9aã\x83\x87ã\x82£ã\x82¢ â\x80\x94 ã\x83\x95ã\x83ªã\x83¼ç\x99¾ç§\x91äº\x8bå\x85¸" class="link-box" data-slogan="ã\x83\x95ã\x83ªã\x83¼ç\x99¾ç§\x91äº\x8bå\x85¸">\n<strong>æ\x97¥æ\x9c¬èª\x9e</strong>\n<small>1,438,000+ <span>è¨\x98äº\x8b</span></small>\n</a>\n</div>\n<!-- #4. de.wikipedia.org - 174,277,000 views/day -->\n<div class="central-featured-lang lang4" lang="de" dir="ltr">\n<a id="js-link-box-de" href="//de.wikipedia.org/" title="Deutsch â\x80\x94 Wikipedia â\x80\x94 Die freie EnzyklopÃ¤die" class="link-box" data-slogan="Die freie EnzyklopÃ¤die">\n<strong>Deutsch</strong>\n<small>2.964.000+ <span>Artikel</span></small>\n</a>\n</div>\n<!-- #5. fr.wikipedia.org - 172,274,000 views/day -->\n<div class="central-featured-lang lang5" lang="fr" dir="ltr">\n<a id="js-link-box-fr" href="//fr.wikipedia.org/" title="franÃ§ais â\x80\x94 WikipÃ©dia â\x80\x94 Lâ\x80\x99encyclopÃ©die libre" class="link-box" data-slogan="Lâ\x80\x99encyclopÃ©die libre">\n<strong>FranÃ§ais</strong>\n<small>2â\x80¯650â\x80¯000+ <span>articles</span></small>\n</a>\n</div>\n<!-- #6. es.wikipedia.org - 167,709,000 views/day -->\n<div class="central-featured-lang lang6" lang="es" dir="ltr">\n<a id="js-link-box-es" href="//es.wikipedia.org/" title="EspaÃ±ol â\x80\x94 Wikipedia â\x80\x94 La enciclopedia libre" class="link-box" data-slogan="La enciclopedia libre">\n<strong>EspaÃ±ol</strong>\n<small>1.992.000+ <span>artÃ\xadculos</span></small>\n</a>\n</div>\n<!-- #7. it.wikipedia.org - 99,760,000 views/day -->\n<div class="central-featured-lang lang7" lang="it" dir="ltr">\n<a id="js-link-box-it" href="//it.wikipedia.org/" title="Italiano â\x80\x94 Wikipedia â\x80\x94 L&#x27;enciclopedia libera" class="link-box" data-slogan="L&#x27;enciclopedia libera">\n<strong>Italiano</strong>\n<small>1.893.000+ <span>voci</span></small>\n</a>\n</div>\n<!-- #8. zh.wikipedia.org - 97,847,000 views/day -->\n<div class="central-featured-lang lang8" lang="zh" dir="ltr">\n<a id="js-link-box-zh" href="//zh.wikipedia.org/" title="ZhÅ\x8dngwÃ©n â\x80\x94 ç»´å\x9fºç\x99¾ç§\x91 / ç¶\xadå\x9fºç\x99¾ç§\x91 â\x80\x94 è\x87ªç\x94±ç\x9a\x84ç\x99¾ç§\x91å\x85¨ä¹¦ / è\x87ªç\x94±ç\x9a\x84ç\x99¾ç§\x91å\x85¨æ\x9b¸" class="link-box localize-variant" data-slogan="è\x87ªç\x94±ç\x9a\x84ç\x99¾ç§\x91å\x85¨ä¹¦ / è\x87ªç\x94±ç\x9a\x84ç\x99¾ç§\x91å\x85¨æ\x9b¸">\n<strong>ä¸\xadæ\x96\x87</strong>\n<small>1,452,000+ <span>æ\x9d¡ç\x9b® / æ¢\x9dç\x9b®</span></small>\n</a>\n</div>\n<!-- #9. fa.wikipedia.org - 56,140,000 views/day -->\n<div class="central-featured-lang lang9" lang="fa" dir="rtl">\n<a id="js-link-box-fa" href="//fa.wikipedia.org/" title="FÄ\x81rsi â\x80\x94 Ù\x88Û\x8cÚ©Û\x8câ\x80\x8cÙ¾Ø¯Û\x8cØ§ â\x80\x94 Ø¯Ø§Ù\x86Ø´Ù\x86Ø§Ù\x85Ù\x87Ù\x94 Ø¢Ø²Ø§Ø¯" class="link-box" data-slogan="Ø¯Ø§Ù\x86Ø´Ù\x86Ø§Ù\x85Ù\x87Ù\x94 Ø¢Ø²Ø§Ø¯">\n<strong><bdi dir="rtl">Ù\x81Ø§Ø±Ø³Û\x8c</bdi></strong>\n<small>Û±Ù¬Û°Û²Û°Ù¬Û°Û°Û°+ <span>Ù\x85Ù\x82Ø§Ù\x84Ù\x87</span></small>\n</a>\n</div>\n<!-- #10. pt.wikipedia.org - 53,221,000 views/day -->\n<div class="central-featured-lang lang10" lang="pt" dir="ltr">\n<a id="js-link-box-pt" href="//pt.wikipedia.org/" title="PortuguÃªs â\x80\x94 WikipÃ©dia â\x80\x94 A enciclopÃ©dia livre" class="link-box" data-slogan="A enciclopÃ©dia livre">\n<strong>PortuguÃªs</strong>\n<small>1.138.000+ <span>artigos</span></small>\n</a>\n</div>\n</nav>\n<div role="search" class="search-container">\n<form class="pure-form" id="search-form" action="//www.wikipedia.org/search-redirect.php" data-el-section="search">\n<fieldset>\n<input type="hidden" name="family" value="Wikipedia">\n<input type="hidden" id="hiddenLanguageInput" name="language" value="en">\n<div class="search-input" id="search-input">\n<label for="searchInput" class="screen-reader-text" data-jsl10n="portal.search-input-label">Search Wikipedia</label>\n<input id="searchInput" name="search" type="search" size="20" autofocus="autofocus" accesskey="F" dir="auto" autocomplete="off">\n<div class="styled-select no-js">\n<div class="hide-arrow">\n<select id="searchLanguage" name="language">\n<option value="af" lang="af">Afrikaans</option><!-- Afrikaans -->\n<option value="ar" lang="ar">Ø§Ù\x84Ø¹Ø±Ø¨Ù\x8aØ©</option><!-- Al-Ê¿ArabÄ«yah -->\n<option value="ast" lang="ast">Asturianu</option>\n<option value="az" lang="az">AzÉ\x99rbaycanca</option><!-- AzÉ\x99rbaycanca -->\n<option value="bg" lang="bg">Ð\x91Ñ\x8aÐ»Ð³Ð°Ñ\x80Ñ\x81ÐºÐ¸</option><!-- BÇ\x8elgarski -->\n<option value="nan" lang="nan">é\x96©å\x8d\x97èª\x9e / BÃ¢n-lÃ¢m-gÃº</option><!-- BÃ¢n-lÃ¢m-gÃº -->\n<option value="bn" lang="bn">à¦¬à¦¾à¦\x82à¦²à¦¾</option><!-- Bangla -->\n<option value="be" lang="be">Ð\x91ÐµÐ»Ð°Ñ\x80Ñ\x83Ñ\x81ÐºÐ°Ñ\x8f</option><!-- Belaruskaya -->\n<option value="ca" lang="ca">CatalÃ\xa0</option>\n<option value="cs" lang="cs">Ä\x8ceÅ¡tina</option><!-- Ä\x8deÅ¡tina -->\n<option value="cy" lang="cy">Cymraeg</option><!-- Cymraeg -->\n<option value="da" lang="da">Dansk</option>\n<option value="de" lang="de">Deutsch</option>\n<option value="et" lang="et">Eesti</option>\n<option value="el" lang="el">Î\x95Î»Î»Î·Î½Î¹ÎºÎ¬</option><!-- EllÄ«nikÃ¡ -->\n<option value="en" lang="en" selected=selected>English</option><!-- English -->\n<option value="es" lang="es">EspaÃ±ol</option>\n<option value="eo" lang="eo">Esperanto</option>\n<option value="eu" lang="eu">Euskara</option>\n<option value="fa" lang="fa">Ù\x81Ø§Ø±Ø³Û\x8c</option><!-- FÄ\x81rsi -->\n<option value="fr" lang="fr">FranÃ§ais</option><!-- franÃ§ais -->\n<option value="gl" lang="gl">Galego</option>\n<option value="ko" lang="ko">í\x95\x9cêµ\xadì\x96´</option><!-- Hangugeo -->\n<option value="hy" lang="hy">Õ\x80Õ¡ÕµÕ¥Ö\x80Õ¥Õ¶</option><!-- Hayeren -->\n<option value="hi" lang="hi">à¤¹à¤¿à¤¨à¥\x8dà¤¦à¥\x80</option><!-- HindÄ« -->\n<option value="hr" lang="hr">Hrvatski</option>\n<option value="id" lang="id">Bahasa Indonesia</option>\n<option value="it" lang="it">Italiano</option>\n<option value="he" lang="he">×¢×\x91×¨×\x99×ª</option><!-- Ivrit -->\n<option value="ka" lang="ka">á\x83¥á\x83\x90á\x83\xa0á\x83\x97á\x83£á\x83\x9aá\x83\x98</option><!-- Kartuli -->\n<option value="lld" lang="lld">Ladin</option>\n<option value="la" lang="la">Latina</option>\n<option value="lv" lang="lv">LatvieÅ¡u</option>\n<option value="lt" lang="lt">LietuviÅ³</option>\n<option value="hu" lang="hu">Magyar</option>\n<option value="mk" lang="mk">Ð\x9cÐ°ÐºÐµÐ´Ð¾Ð½Ñ\x81ÐºÐ¸</option><!-- Makedonski -->\n<option value="arz" lang="arz">Ù\x85ØµØ±Ù\x89</option><!-- Maá¹£rÄ« -->\n<option value="ms" lang="ms">Bahasa Melayu</option><!-- Bahasa Melayu -->\n<option value="min" lang="min">Bahaso Minangkabau</option>\n<option value="my" lang="my">á\x80\x99á\x80¼á\x80\x94á\x80ºá\x80\x99á\x80¬á\x80\x98á\x80¬á\x80\x9eá\x80¬</option><!-- Myanmarsar -->\n<option value="nl" lang="nl">Nederlands</option>\n<option value="ja" lang="ja">æ\x97¥æ\x9c¬èª\x9e</option><!-- Nihongo -->\n<option value="no" lang="nb">Norsk (bokmÃ¥l)</option>\n<option value="nn" lang="nn">Norsk (nynorsk)</option>\n<option value="ce" lang="ce">Ð\x9dÐ¾Ñ\x85Ñ\x87Ð¸Ð¹Ð½</option><!-- NoxÃ§iyn -->\n<option value="uz" lang="uz">OÊ»zbekcha / Ð\x8eÐ·Ð±ÐµÐºÑ\x87Ð°</option><!-- OÊ»zbekcha -->\n<option value="pl" lang="pl">Polski</option>\n<option value="pt" lang="pt">PortuguÃªs</option>\n<option value="kk" lang="kk">Ò\x9aÐ°Ð·Ð°Ò\x9bÑ\x88Ð° / QazaqÅ\x9fa / Ù\x82Ø§Ø²Ø§Ù\x82Ø´Ø§</option>\n<option value="ro" lang="ro">RomÃ¢nÄ\x83</option><!-- RomÃ¢nÄ\x83 -->\n<option value="sq" lang="sq">Shqip</option>\n<option value="simple" lang="en">Simple English</option>\n<option value="ceb" lang="ceb">Sinugboanong Binisaya</option>\n<option value="sk" lang="sk">SlovenÄ\x8dina</option>\n<option value="sl" lang="sl">SlovenÅ¡Ä\x8dina</option><!-- slovenÅ¡Ä\x8dina -->\n<option value="sr" lang="sr">Ð¡Ñ\x80Ð¿Ñ\x81ÐºÐ¸ / Srpski</option>\n<option value="sh" lang="sh">Srpskohrvatski / Ð¡Ñ\x80Ð¿Ñ\x81ÐºÐ¾Ñ\x85Ñ\x80Ð²Ð°Ñ\x82Ñ\x81ÐºÐ¸</option>\n<option value="fi" lang="fi">Suomi</option><!-- suomi -->\n<option value="sv" lang="sv">Svenska</option>\n<option value="ta" lang="ta">à®¤à®®à®¿à®´à¯\x8d</option><!-- Tamiá¸» -->\n<option value="tt" lang="tt">Ð¢Ð°Ñ\x82Ð°Ñ\x80Ñ\x87Ð° / TatarÃ§a</option>\n<option value="te" lang="te">à°¤à±\x86à°²à±\x81à°\x97à±\x81</option><!-- Telugu -->\n<option value="th" lang="th">à¸\xa0à¸²à¸©à¸²à¹\x84à¸\x97à¸¢</option><!-- Phasa Thai -->\n<option value="tg" lang="tg">Ð¢Ð¾Ò·Ð¸ÐºÓ£</option><!-- TojikÄ« -->\n<option value="azb" lang="azb">ØªÛ\x86Ø±Ú©Ø¬Ù\x87</option><!-- TÃ¼rkce -->\n<option value="tr" lang="tr">TÃ¼rkÃ§e</option><!-- TÃ¼rkÃ§e -->\n<option value="uk" lang="uk">Ð£ÐºÑ\x80Ð°Ñ\x97Ð½Ñ\x81Ñ\x8cÐºÐ°</option><!-- Ukrayinsâ\x80\x99ka -->\n<option value="ur" lang="ur">Ø§Ø±Ø¯Ù\x88</option><!-- Urdu -->\n<option value="vi" lang="vi">Tiáº¿ng Viá»\x87t</option>\n<option value="war" lang="war">Winaray</option>\n<option value="zh" lang="zh">ä¸\xadæ\x96\x87</option><!-- ZhÅ\x8dngwÃ©n -->\n<option value="ru" lang="ru">Ð\xa0Ñ\x83Ñ\x81Ñ\x81ÐºÐ¸Ð¹</option><!-- Russkiy -->\n<option value="yue" lang="yue">ç²µèª\x9e</option>\n</select>\n<div class="styled-select-active-helper"></div>\n</div>\n<i class="sprite svg-arrow-down"></i>\n</div>\n</div>\n<button class="pure-button pure-button-primary-progressive" type="submit">\n<i class="sprite svg-search-icon" data-jsl10n="search-input-button">Search</i>\n</button>\n<input type="hidden" value="Go" name="go">\n</fieldset>\n</form>\n</div>\n<nav data-jsl10n="all-languages-nav-label" aria-label="All languages">\n<div class="lang-list-button-wrapper">\n<button id="js-lang-list-button" aria-expanded="false" aria-controls="js-lang-lists" class="lang-list-button">\n<i class="sprite svg-language-icon"></i>\n<span class="lang-list-button-text jsl10n" data-jsl10n="portal.language-button-text">Read Wikipedia in your language </span>\n<i class="sprite svg-arrow-down-blue"></i>\n</button>\n</div>\n<div class="lang-list-border"></div>\n<div class="lang-list-container">\n<div id="js-lang-lists" class="lang-list-content">\n<h2 class="bookshelf-container">\n<span class="bookshelf">\n<span class="text">\n<bdi dir="ltr">\n1,000,000+\n</bdi>\n<span class="jsl10n" data-jsl10n="entries">\narticles\n</span>\n</span>\n</span>\n</h2>\n<div class="langlist langlist-large hlist" data-el-section="secondary links">\n<ul>\n<li><a href="//ar.wikipedia.org/" lang="ar" title="Al-Ê¿ArabÄ«yah"><bdi dir="rtl">Ø§Ù\x84Ø¹Ø±Ø¨Ù\x8aØ©</bdi></a></li>\n<li><a href="//de.wikipedia.org/" lang="de">Deutsch</a></li>\n<li><a href="//en.wikipedia.org/" lang="en" title="English">English</a></li>\n<li><a href="//es.wikipedia.org/" lang="es">EspaÃ±ol</a></li>\n<li><a href="//fa.wikipedia.org/" lang="fa" title="FÄ\x81rsi"><bdi dir="rtl">Ù\x81Ø§Ø±Ø³Û\x8c</bdi></a></li>\n<li><a href="//fr.wikipedia.org/" lang="fr" title="franÃ§ais">FranÃ§ais</a></li>\n<li><a href="//it.wikipedia.org/" lang="it">Italiano</a></li>\n<li><a href="//arz.wikipedia.org/" lang="arz" title="Maá¹£rÄ«"><bdi dir="rtl">Ù\x85ØµØ±Ù\x89</bdi></a></li>\n<li><a href="//nl.wikipedia.org/" lang="nl">Nederlands</a></li>\n<li><a href="//ja.wikipedia.org/" lang="ja" title="Nihongo">æ\x97¥æ\x9c¬èª\x9e</a></li>\n<li><a href="//pl.wikipedia.org/" lang="pl">Polski</a></li>\n<li><a href="//pt.wikipedia.org/" lang="pt">PortuguÃªs</a></li>\n<li><a href="//ceb.wikipedia.org/" lang="ceb">Sinugboanong Binisaya</a></li>\n<li><a href="//sv.wikipedia.org/" lang="sv">Svenska</a></li>\n<li><a href="//uk.wikipedia.org/" lang="uk" title="Ukrayinsâ\x80\x99ka">Ð£ÐºÑ\x80Ð°Ñ\x97Ð½Ñ\x81Ñ\x8cÐºÐ°</a></li>\n<li><a href="//vi.wikipedia.org/" lang="vi">Tiáº¿ng Viá»\x87t</a></li>\n<li><a href="//war.wikipedia.org/" lang="war">Winaray</a></li>\n<li><a href="//zh.wikipedia.org/" lang="zh" title="ZhÅ\x8dngwÃ©n">ä¸\xadæ\x96\x87</a></li>\n<li><a href="//ru.wikipedia.org/" lang="ru" title="Russkiy">Ð\xa0Ñ\x83Ñ\x81Ñ\x81ÐºÐ¸Ð¹</a></li>\n</ul>\n</div>\n<h2 class="bookshelf-container">\n<span class="bookshelf">\n<span class="text">\n<bdi dir="ltr">\n100,000+\n</bdi>\n<span class="jsl10n" data-jsl10n="portal.entries">\narticles\n</span>\n</span>\n</span>\n</h2>\n<div class="langlist langlist-large hlist" data-el-section="secondary links">\n<ul>\n<li><a href="//af.wikipedia.org/" lang="af" title="Afrikaans">Afrikaans</a></li>\n<li><a href="//ast.wikipedia.org/" lang="ast">Asturianu</a></li>\n<li><a href="//az.wikipedia.org/" lang="az" title="AzÉ\x99rbaycanca">AzÉ\x99rbaycanca</a></li>\n<li><a href="//bg.wikipedia.org/" lang="bg" title="BÇ\x8elgarski">Ð\x91Ñ\x8aÐ»Ð³Ð°Ñ\x80Ñ\x81ÐºÐ¸</a></li>\n<li><a href="//zh-min-nan.wikipedia.org/" lang="nan" title="BÃ¢n-lÃ¢m-gÃº">é\x96©å\x8d\x97èª\x9e / BÃ¢n-lÃ¢m-gÃº</a></li>\n<li><a href="//bn.wikipedia.org/" lang="bn" title="Bangla">à¦¬à¦¾à¦\x82à¦²à¦¾</a></li>\n<li><a href="//be.wikipedia.org/" lang="be" title="Belaruskaya">Ð\x91ÐµÐ»Ð°Ñ\x80Ñ\x83Ñ\x81ÐºÐ°Ñ\x8f</a></li>\n<li><a href="//ca.wikipedia.org/" lang="ca">CatalÃ\xa0</a></li>\n<li><a href="//cs.wikipedia.org/" lang="cs" title="Ä\x8deÅ¡tina">Ä\x8ceÅ¡tina</a></li>\n<li><a href="//cy.wikipedia.org/" lang="cy" title="Cymraeg">Cymraeg</a></li>\n<li><a href="//da.wikipedia.org/" lang="da">Dansk</a></li>\n<li><a href="//et.wikipedia.org/" lang="et">Eesti</a></li>\n<li><a href="//el.wikipedia.org/" lang="el" title="EllÄ«nikÃ¡">Î\x95Î»Î»Î·Î½Î¹ÎºÎ¬</a></li>\n<li><a href="//eo.wikipedia.org/" lang="eo">Esperanto</a></li>\n<li><a href="//eu.wikipedia.org/" lang="eu">Euskara</a></li>\n<li><a href="//gl.wikipedia.org/" lang="gl">Galego</a></li>\n<li><a href="//ko.wikipedia.org/" lang="ko" title="Hangugeo">í\x95\x9cêµ\xadì\x96´</a></li>\n<li><a href="//hy.wikipedia.org/" lang="hy" title="Hayeren">Õ\x80Õ¡ÕµÕ¥Ö\x80Õ¥Õ¶</a></li>\n<li><a href="//hi.wikipedia.org/" lang="hi" title="HindÄ«">à¤¹à¤¿à¤¨à¥\x8dà¤¦à¥\x80</a></li>\n<li><a href="//hr.wikipedia.org/" lang="hr">Hrvatski</a></li>\n<li><a href="//id.wikipedia.org/" lang="id">Bahasa Indonesia</a></li>\n<li><a href="//he.wikipedia.org/" lang="he" title="Ivrit"><bdi dir="rtl">×¢×\x91×¨×\x99×ª</bdi></a></li>\n<li><a href="//ka.wikipedia.org/" lang="ka" title="Kartuli">á\x83¥á\x83\x90á\x83\xa0á\x83\x97á\x83£á\x83\x9aá\x83\x98</a></li>\n<li><a href="//lld.wikipedia.org/" lang="lld">Ladin</a></li>\n<li><a href="//la.wikipedia.org/" lang="la">Latina</a></li>\n<li><a href="//lv.wikipedia.org/" lang="lv">LatvieÅ¡u</a></li>\n<li><a href="//lt.wikipedia.org/" lang="lt">LietuviÅ³</a></li>\n<li><a href="//hu.wikipedia.org/" lang="hu">Magyar</a></li>\n<li><a href="//mk.wikipedia.org/" lang="mk" title="Makedonski">Ð\x9cÐ°ÐºÐµÐ´Ð¾Ð½Ñ\x81ÐºÐ¸</a></li>\n<li><a href="//ms.wikipedia.org/" lang="ms" title="Bahasa Melayu">Bahasa Melayu</a></li>\n<li><a href="//min.wikipedia.org/" lang="min">Bahaso Minangkabau</a></li>\n<li><a href="//my.wikipedia.org/" lang="my" title="Myanmarsar">á\x80\x99á\x80¼á\x80\x94á\x80ºá\x80\x99á\x80¬á\x80\x98á\x80¬á\x80\x9eá\x80¬</a></li>\n<li lang="no">Norsk<ul><li><a href="//no.wikipedia.org/" lang="nb">bokmÃ¥l</a></li><li><a href="//nn.wikipedia.org/" lang="nn">nynorsk</a></li></ul></li>\n<li><a href="//ce.wikipedia.org/" lang="ce" title="NoxÃ§iyn">Ð\x9dÐ¾Ñ\x85Ñ\x87Ð¸Ð¹Ð½</a></li>\n<li><a href="//uz.wikipedia.org/" lang="uz" title="OÊ»zbekcha">OÊ»zbekcha / Ð\x8eÐ·Ð±ÐµÐºÑ\x87Ð°</a></li>\n<li><a href="//kk.wikipedia.org/" lang="kk"><span lang="kk-Cyrl">Ò\x9aÐ°Ð·Ð°Ò\x9bÑ\x88Ð°</span> / <span lang="kk-Latn">QazaqÅ\x9fa</span> / <bdi lang="kk-Arab" dir="rtl">Ù\x82Ø§Ø²Ø§Ù\x82Ø´Ø§</bdi></a></li>\n<li><a href="//ro.wikipedia.org/" lang="ro" title="RomÃ¢nÄ\x83">RomÃ¢nÄ\x83</a></li>\n<li><a href="//sq.wikipedia.org/" lang="sq">Shqip</a></li>\n<li><a href="//simple.wikipedia.org/" lang="en">Simple English</a></li>\n<li><a href="//sk.wikipedia.org/" lang="sk">SlovenÄ\x8dina</a></li>\n<li><a href="//sl.wikipedia.org/" lang="sl" title="slovenÅ¡Ä\x8dina">SlovenÅ¡Ä\x8dina</a></li>\n<li><a href="//sr.wikipedia.org/" lang="sr">Ð¡Ñ\x80Ð¿Ñ\x81ÐºÐ¸ / Srpski</a></li>\n<li><a href="//sh.wikipedia.org/" lang="sh">Srpskohrvatski / Ð¡Ñ\x80Ð¿Ñ\x81ÐºÐ¾Ñ\x85Ñ\x80Ð²Ð°Ñ\x82Ñ\x81ÐºÐ¸</a></li>\n<li><a href="//fi.wikipedia.org/" lang="fi" title="suomi">Suomi</a></li>\n<li><a href="//ta.wikipedia.org/" lang="ta" title="Tamiá¸»">à®¤à®®à®¿à®´à¯\x8d</a></li>\n<li><a href="//tt.wikipedia.org/" lang="tt">Ð¢Ð°Ñ\x82Ð°Ñ\x80Ñ\x87Ð° / TatarÃ§a</a></li>\n<li><a href="//te.wikipedia.org/" lang="te" title="Telugu">à°¤à±\x86à°²à±\x81à°\x97à±\x81</a></li>\n<li><a href="//th.wikipedia.org/" lang="th" title="Phasa Thai">à¸\xa0à¸²à¸©à¸²à¹\x84à¸\x97à¸¢</a></li>\n<li><a href="//tg.wikipedia.org/" lang="tg" title="TojikÄ«">Ð¢Ð¾Ò·Ð¸ÐºÓ£</a></li>\n<li><a href="//azb.wikipedia.org/" lang="azb" title="TÃ¼rkce"><bdi dir="rtl">ØªÛ\x86Ø±Ú©Ø¬Ù\x87</bdi></a></li>\n<li><a href="//tr.wikipedia.org/" lang="tr" title="TÃ¼rkÃ§e">TÃ¼rkÃ§e</a></li>\n<li><a href="//ur.wikipedia.org/" lang="ur" title="Urdu"><bdi dir="rtl">Ø§Ø±Ø¯Ù\x88</bdi></a></li>\n<li><a href="//zh-yue.wikipedia.org/" lang="yue">ç²µèª\x9e</a></li>\n</ul>\n</div>\n<h2 class="bookshelf-container">\n<span class="bookshelf">\n<span class="text">\n<bdi dir="ltr">\n10,000+\n</bdi>\n<span class="jsl10n" data-jsl10n="portal.entries">\narticles\n</span>\n</span>\n</span>\n</h2>\n<div class="langlist hlist" data-el-section="secondary links">\n<ul>\n<li><a href="//ace.wikipedia.org/" lang="ace">Bahsa AcÃ¨h</a></li>\n<li><a href="//als.wikipedia.org/" lang="gsw">Alemannisch</a></li>\n<li><a href="//am.wikipedia.org/" lang="am" title="Ä\x80mariÃ±Ã±Ä\x81">á\x8a\xa0á\x88\x9bá\x88\xadá\x8a\x9b</a></li>\n<li><a href="//an.wikipedia.org/" lang="an">AragonÃ©s</a></li>\n<li><a href="//hyw.wikipedia.org/" lang="hyw" title="Arevmdahayeren">Ô±Ö\x80Õ¥Ö\x82Õ´Õ¿Õ¡Õ°Õ¡ÕµÕ¥Ö\x80Õ§Õ¶</a></li>\n<li><a href="//gor.wikipedia.org/" lang="gor">Bahasa Hulontalo</a></li>\n<li><a href="//ban.wikipedia.org/" lang="ban" title="Basa Bali">Basa Bali</a></li>\n<li><a href="//bjn.wikipedia.org/" lang="bjn">Bahasa Banjar</a></li>\n<li><a href="//map-bms.wikipedia.org/" lang="map-x-bms">Basa Banyumasan</a></li>\n<li><a href="//ba.wikipedia.org/" lang="ba" title="BaÅ\x9fqortsa">Ð\x91Ð°Ñ\x88Ò¡Ð¾Ñ\x80Ñ\x82Ñ\x81Ð°</a></li>\n<li><a href="//be-tarask.wikipedia.org/" lang="be-tarask" title="Bielaruskaja (taraÅ¡kievica)">Ð\x91ÐµÐ»Ð°Ñ\x80Ñ\x83Ñ\x81ÐºÐ°Ñ\x8f (Ñ\x82Ð°Ñ\x80Ð°Ñ\x88ÐºÐµÐ²Ñ\x96Ñ\x86Ð°)</a></li>\n<li><a href="//bcl.wikipedia.org/" lang="bcl">Bikol Central</a></li>\n<li><a href="//bpy.wikipedia.org/" lang="bpy" title="Bishnupriya Manipuri">à¦¬à¦¿à¦·à§\x8dà¦£à§\x81à¦ªà§\x8dà¦°à¦¿à¦¯à¦¼à¦¾ à¦®à¦£à¦¿à¦ªà§\x81à¦°à§\x80</a></li>\n<li><a href="//bar.wikipedia.org/" lang="bar">Boarisch</a></li>\n<li><a href="//bs.wikipedia.org/" lang="bs">Bosanski</a></li>\n<li><a href="//br.wikipedia.org/" lang="br">Brezhoneg</a></li>\n<li><a href="//cv.wikipedia.org/" lang="cv" title="Ä\x8cÄ\x83vaÅ¡la">Ð§Ó\x91Ð²Ð°Ñ\x88Ð»Ð°</a></li>\n<li><a href="//dag.wikipedia.org/" lang="dag">Dagbanli</a></li>\n<li><a href="//ary.wikipedia.org/" lang="ary" title="Darija"><bdi dir="rtl">Ø§Ù\x84Ø¯Ø§Ø±Ø¬Ø©</bdi></a></li>\n<li><a href="//nv.wikipedia.org/" lang="nv">DinÃ© Bizaad</a></li>\n<li><a href="//eml.wikipedia.org/" lang="roa-x-eml">EmigliÃ\xa0nâ\x80\x93RumagnÃ²l</a></li>\n<li><a href="//hif.wikipedia.org/" lang="hif">Fiji Hindi</a></li>\n<li><a href="//fo.wikipedia.org/" lang="fo">FÃ¸royskt</a></li>\n<li><a href="//fy.wikipedia.org/" lang="fy">Frysk</a></li>\n<li><a href="//ga.wikipedia.org/" lang="ga">Gaeilge</a></li>\n<li><a href="//gd.wikipedia.org/" lang="gd">GÃ\xa0idhlig</a></li>\n<li><a href="//glk.wikipedia.org/" lang="glk" title="GilÉ\x99ki"><bdi dir="rtl">Ú¯Û\x8cÙ\x84Ú©Û\x8c</bdi></a></li>\n<li><a href="//gu.wikipedia.org/" lang="gu" title="Gujarati">àª\x97à«\x81àª\x9càª°àª¾àª¤à«\x80</a></li>\n<li><a href="//hak.wikipedia.org/" lang="hak">Hak-kÃ¢-ngÃ® / å®¢å®¶èª\x9e</a></li>\n<li><a href="//ha.wikipedia.org/" lang="ha" title="Hausa">Hausa</a></li>\n<li><a href="//hsb.wikipedia.org/" lang="hsb">Hornjoserbsce</a></li>\n<li><a href="//io.wikipedia.org/" lang="io" title="Ido">Ido</a></li>\n<li><a href="//ig.wikipedia.org/" lang="ig">Igbo</a></li>\n<li><a href="//ilo.wikipedia.org/" lang="ilo">Ilokano</a></li>\n<li><a href="//ia.wikipedia.org/" lang="ia">Interlingua</a></li>\n<li><a href="//ie.wikipedia.org/" lang="ie">Interlingue</a></li>\n<li><a href="//os.wikipedia.org/" lang="os" title="Iron">Ð\x98Ñ\x80Ð¾Ð½</a></li>\n<li><a href="//is.wikipedia.org/" lang="is">Ã\x8dslenska</a></li>\n<li><a href="//jv.wikipedia.org/" lang="jv" title="Jawa">Jawa</a></li>\n<li><a href="//kn.wikipedia.org/" lang="kn" title="Kannada">à²\x95à²¨à³\x8dà²¨à²¡</a></li>\n<li><a href="//pam.wikipedia.org/" lang="pam">Kapampangan</a></li>\n<li><a href="//km.wikipedia.org/" lang="km" title="PhÃ©asa KhmÃ©r">á\x9e\x97á\x9e¶á\x9e\x9fá\x9e¶á\x9e\x81á\x9f\x92á\x9e\x98á\x9f\x82á\x9e\x9a</a></li>\n<li><a href="//avk.wikipedia.org/" lang="avk">Kotava</a></li>\n<li><a href="//ht.wikipedia.org/" lang="ht">KreyÃ²l Ayisyen</a></li>\n<li><a href="//ku.wikipedia.org/" lang="ku"><span lang="ku-Latn">KurdÃ®</span> / <bdi lang="ku-Arab" dir="rtl">Ù\x83Ù\x88Ø±Ø¯Û\x8c</bdi></a></li>\n<li><a href="//ckb.wikipedia.org/" lang="ckb" title="KurdÃ®y NawendÃ®"><bdi dir="rtl">Ú©Ù\x88Ø±Ø¯Û\x8cÛ\x8c Ù\x86Ø§Ù\x88Û\x95Ù\x86Ø¯Û\x8c</bdi></a></li>\n<li><a href="//ky.wikipedia.org/" lang="ky" title="KyrgyzÄ\x8da">Ð\x9aÑ\x8bÑ\x80Ð³Ñ\x8bÐ·Ñ\x87Ð°</a></li>\n<li><a href="//mrj.wikipedia.org/" lang="mjr" title="Kyryk Mary">Ð\x9aÑ\x8bÑ\x80Ñ\x8bÐº Ð¼Ð°Ñ\x80Ñ\x8b</a></li>\n<li><a href="//lb.wikipedia.org/" lang="lb">LÃ«tzebuergesch</a></li>\n<li><a href="//lij.wikipedia.org/" lang="lij">LÃ¬gure</a></li>\n<li><a href="//li.wikipedia.org/" lang="li">Limburgs</a></li>\n<li><a href="//lmo.wikipedia.org/" lang="lmo">Lombard</a></li>\n<li><a href="//mai.wikipedia.org/" lang="mai" title="MaithilÄ«">à¤®à¥\x88à¤¥à¤¿à¤²à¥\x80</a></li>\n<li><a href="//mg.wikipedia.org/" lang="mg">Malagasy</a></li>\n<li><a href="//ml.wikipedia.org/" lang="ml" title="Malayalam">à´®à´²à´¯à´¾à´³à´\x82</a></li>\n<li><a href="//mr.wikipedia.org/" lang="mr" title="Marathi">à¤®à¤°à¤¾à¤\xa0à¥\x80</a></li>\n<li><a href="//xmf.wikipedia.org/" lang="xmf" title="Margaluri">á\x83\x9bá\x83\x90á\x83\xa0á\x83\x92á\x83\x90á\x83\x9aá\x83£á\x83\xa0á\x83\x98</a></li>\n<li><a href="//mzn.wikipedia.org/" lang="mzn" title="MÃ¤zeruni"><bdi dir="rtl">Ù\x85Ø§Ø²Ù\x90Ø±Ù\x88Ù\x86Û\x8c</bdi></a></li>\n<li><a href="//cdo.wikipedia.org/" lang="cdo" title="Ming-deng-ngu">MÃ¬ng-dÄ\x95Ì¤ng-ngá¹³Ì\x84 / é\x96©æ\x9d±èª\x9e</a></li>\n<li><a href="//mn.wikipedia.org/" lang="mn" title="Mongol">Ð\x9cÐ¾Ð½Ð³Ð¾Ð»</a></li>\n<li><a href="//nap.wikipedia.org/" lang="nap">Napulitano</a></li>\n<li><a href="//new.wikipedia.org/" lang="new" title="Nepal Bhasa">à¤¨à¥\x87à¤ªà¤¾à¤² à¤\xadà¤¾à¤·à¤¾</a></li>\n<li><a href="//ne.wikipedia.org/" lang="ne" title="NepÄ\x81lÄ«">à¤¨à¥\x87à¤ªà¤¾à¤²à¥\x80</a></li>\n<li><a href="//frr.wikipedia.org/" lang="frr">Nordfriisk</a></li>\n<li><a href="//oc.wikipedia.org/" lang="oc">Occitan</a></li>\n<li><a href="//mhr.wikipedia.org/" lang="mhr" title="Olyk Marij">Ð\x9eÐ»Ñ\x8bÐº Ð¼Ð°Ñ\x80Ð¸Ð¹</a></li>\n<li><a href="//or.wikipedia.org/" lang="or" title="Oá¹\x9biÄ\x81">à¬\x93à¬¡à¬¿à¬¼à¬\x86</a></li>\n<li><a href="//as.wikipedia.org/" lang="as" title="Ã\x94xÃ´miya">à¦\x85à¦¸à¦®à§\x80à¦¯à¦¾à¦¼</a></li>\n<li><a href="//pa.wikipedia.org/" lang="pa" title="PaÃ±jÄ\x81bÄ« (GurmukhÄ«)">à¨ªà©°à¨\x9cà¨¾à¨¬à©\x80</a></li>\n<li><a href="//pnb.wikipedia.org/" lang="pnb" title="PaÃ±jÄ\x81bÄ« (ShÄ\x81hmukhÄ«)"><bdi dir="rtl">Ù¾Ù\x86Ø¬Ø§Ø¨Û\x8c (Ø´Ø§Û\x81 Ù\x85Ú©Ú¾Û\x8c)</bdi></a></li>\n<li><a href="//ps.wikipedia.org/" lang="ps" title="PaÊ\x82to"><bdi dir="rtl">Ù¾Ú\x9aØªÙ\x88</bdi></a></li>\n<li><a href="//pms.wikipedia.org/" lang="pms">PiemontÃ¨is</a></li>\n<li><a href="//nds.wikipedia.org/" lang="nds">PlattdÃ¼Ã¼tsch</a></li>\n<li><a href="//crh.wikipedia.org/" lang="crh">QÄ±rÄ±mtatarca</a></li>\n<li><a href="//qu.wikipedia.org/" lang="qu">Runa Simi</a></li>\n<li><a href="//sa.wikipedia.org/" lang="sa" title="Saá¹\x83ská¹\x9btam">à¤¸à¤\x82à¤¸à¥\x8dà¤\x95à¥\x83à¤¤à¤®à¥\x8d</a></li>\n<li><a href="//sat.wikipedia.org/" lang="sat" title="Santali">á±¥á±\x9fá±±á±\x9bá±\x9fá±²á±¤</a></li>\n<li><a href="//sah.wikipedia.org/" lang="sah" title="Saxa Tyla">Ð¡Ð°Ñ\x85Ð° Ð¢Ñ\x8bÐ»Ð°</a></li>\n<li><a href="//sco.wikipedia.org/" lang="sco">Scots</a></li>\n<li><a href="//sn.wikipedia.org/" lang="sn">ChiShona</a></li>\n<li><a href="//scn.wikipedia.org/" lang="scn">Sicilianu</a></li>\n<li><a href="//si.wikipedia.org/" lang="si" title="Siá¹\x83hala">à·\x83à·\x92à¶\x82à·\x84à¶½</a></li>\n<li><a href="//sd.wikipedia.org/" lang="sd" title="SindhÄ«"><bdi dir="rtl">Ø³Ù\x86Ú\x8cÙ\x8a</bdi></a></li>\n<li><a href="//szl.wikipedia.org/" lang="szl">Å\x9alÅ¯nski</a></li>\n<li><a href="//su.wikipedia.org/" lang="su">Basa Sunda</a></li>\n<li><a href="//sw.wikipedia.org/" lang="sw">Kiswahili</a></li>\n<li><a href="//tl.wikipedia.org/" lang="tl">Tagalog</a></li>\n<li><a href="//shn.wikipedia.org/" lang="shn">á\x81½á\x82\x83á\x82\x87á\x80\x9eá\x82\x83á\x82\x87á\x80\x90á\x82\x86á\x80¸</a></li>\n<li><a href="//zgh.wikipedia.org/" lang="zgh" title="Tamazight tanawayt">âµ\x9câ´°âµ\x8eâ´°âµ£âµ\x89âµ\x96âµ\x9c âµ\x9câ´°âµ\x8fâ´°âµ¡â´°âµ¢âµ\x9c</a></li>\n<li><a href="//tum.wikipedia.org/" lang="tum">chiTumbuka</a></li>\n<li><a href="//bug.wikipedia.org/" lang="bug">Basa Ugi</a></li>\n<li><a href="//vec.wikipedia.org/" lang="vec">VÃ¨neto</a></li>\n<li><a href="//vo.wikipedia.org/" lang="vo">VolapÃ¼k</a></li>\n<li><a href="//wa.wikipedia.org/" lang="wa">Walon</a></li>\n<li><a href="//zh-classical.wikipedia.org/" lang="lzh" title="WÃ©nyÃ¡n">æ\x96\x87è¨\x80</a></li>\n<li><a href="//wuu.wikipedia.org/" lang="wuu" title="WÃºyÇ\x94">å\x90´è¯\xad</a></li>\n<li><a href="//yi.wikipedia.org/" lang="yi" title="YidiÅ¡"><bdi dir="rtl">×\x99×\x99Ö´×\x93×\x99×©</bdi></a></li>\n<li><a href="//yo.wikipedia.org/" lang="yo">YorÃ¹bÃ¡</a></li>\n<li><a href="//diq.wikipedia.org/" lang="diq" title="Zazaki">Zazaki</a></li>\n<li><a href="//bat-smg.wikipedia.org/" lang="sgs">Å¾emaitÄ\x97Å¡ka</a></li>\n<li><a href="//zu.wikipedia.org/" lang="zu">isiZulu</a></li>\n<li><a href="//mni.wikipedia.org/" lang="mni">ê¯\x83ê¯¤ê¯\x87ê¯© ê¯\x82ê¯£ê¯\x9f</a></li>\n</ul>\n</div>\n<h2 class="bookshelf-container">\n<span class="bookshelf">\n<span class="text">\n<bdi dir="ltr">\n1,000+\n</bdi>\n<span class="jsl10n" data-jsl10n="portal.entries">\narticles\n</span>\n</span>\n</span>\n</h2>\n<div class="langlist hlist" data-el-section="secondary links">\n<ul>\n<li><a href="//lad.wikipedia.org/" lang="lad"><span lang="lad-Latn">Dzhudezmo</span> / <bdi lang="lad-Hebr" dir="rtl">×\x9c×\x90×\x93×\x99×\xa0×\x95</bdi></a></li>\n<li><a href="//kbd.wikipedia.org/" lang="kbd" title="Adighabze">Ð\x90Ð´Ñ\x8bÐ³Ñ\x8dÐ±Ð·Ñ\x8d</a></li>\n<li><a href="//ang.wikipedia.org/" lang="ang">Ã\x86nglisc</a></li>\n<li><a href="//smn.wikipedia.org/" lang="smn" title="anarÃ¢Å¡kielÃ¢">AnarÃ¢Å¡kielÃ¢</a></li>\n<li><a href="//anp.wikipedia.org/" lang="anp" title="Angika">à¤\x85à¤\x82à¤\x97à¤¿à¤\x95à¤¾</a></li>\n<li><a href="//ab.wikipedia.org/" lang="ab" title="aá¹\x97sshwa">Ð\x90Ô¥Ñ\x81Ñ\x88Ó\x99Ð°</a></li>\n<li><a href="//roa-rup.wikipedia.org/" lang="rup">armÃ£neashti</a></li>\n<li><a href="//frp.wikipedia.org/" lang="frp">Arpitan</a></li>\n<li><a href="//atj.wikipedia.org/" lang="atj">atikamekw</a></li>\n<li><a href="//arc.wikipedia.org/" lang="arc" title="Ä\x80tÃ»rÄ\x81yÃ¢"><bdi dir="rtl">Ü\x90Ü¬Ü\x98ÜªÜ\x9dÜ\x90</bdi></a></li>\n<li><a href="//gn.wikipedia.org/" lang="gn">AvaÃ±eâ\x80\x99áº½</a></li>\n<li><a href="//av.wikipedia.org/" lang="av" title="Avar">Ð\x90Ð²Ð°Ñ\x80</a></li>\n<li><a href="//ay.wikipedia.org/" lang="ay">Aymar</a></li>\n<li><a href="//bew.wikipedia.org/" lang="bew">Betawi</a></li>\n<li><a href="//bh.wikipedia.org/" lang="bh" title="BhÅ\x8djapurÄ«">à¤\xadà¥\x8bà¤\x9cà¤ªà¥\x81à¤°à¥\x80</a></li>\n<li><a href="//bi.wikipedia.org/" lang="bi">Bislama</a></li>\n<li><a href="//bo.wikipedia.org/" lang="bo" title="Bod Skad">à½\x96à½¼à½\x91à¼\x8bà½¡à½²à½\x82</a></li>\n<li><a href="//bxr.wikipedia.org/" lang="bxr" title="Buryad">Ð\x91Ñ\x83Ñ\x80Ñ\x8fÐ°Ð´</a></li>\n<li><a href="//cbk-zam.wikipedia.org/" lang="cbk-x-zam">Chavacano de Zamboanga</a></li>\n<li><a href="//ny.wikipedia.org/" lang="ny">Chichewa</a></li>\n<li><a href="//co.wikipedia.org/" lang="co">Corsu</a></li>\n<li><a href="//za.wikipedia.org/" lang="za">Vahcuengh / è©±å\x83®</a></li>\n<li><a href="//dga.wikipedia.org/" lang="dga">Dagaare</a></li>\n<li><a href="//se.wikipedia.org/" lang="se" title="davvisÃ¡megiella">DavvisÃ¡megiella</a></li>\n<li><a href="//pdc.wikipedia.org/" lang="pdc">Deitsch</a></li>\n<li><a href="//dv.wikipedia.org/" lang="dv" title="Divehi"><bdi dir="rtl">Þ\x8bÞ¨Þ\x88Þ¬Þ\x80Þ¨Þ\x84Þ¦Þ\x90Þ°</bdi></a></li>\n<li><a href="//dsb.wikipedia.org/" lang="dsb">Dolnoserbski</a></li>\n<li><a href="//dtp.wikipedia.org/" lang="dtp">Dusun Bundu-liwan</a></li>\n<li><a href="//myv.wikipedia.org/" lang="myv" title="Erzjanj">Ð\xadÑ\x80Ð·Ñ\x8fÐ½Ñ\x8c</a></li>\n<li><a href="//ext.wikipedia.org/" lang="ext">EstremeÃ±u</a></li>\n<li><a href="//fon.wikipedia.org/" lang="fon">FÉ\x94Ì\x80ngbÃ¨</a></li>\n<li><a href="//ff.wikipedia.org/" lang="ff">Fulfulde</a></li>\n<li><a href="//fur.wikipedia.org/" lang="fur">Furlan</a></li>\n<li><a href="//gv.wikipedia.org/" lang="gv">Gaelg</a></li>\n<li><a href="//gag.wikipedia.org/" lang="gag">Gagauz</a></li>\n<li><a href="//inh.wikipedia.org/" lang="inh" title="Ghalghai">Ð\x93Ó\x80Ð°Ð»Ð³Ó\x80Ð°Ð¹</a></li>\n<li><a href="//gpe.wikipedia.org/" lang="gpe">Ghanaian Pidgin</a></li>\n<li><a href="//ki.wikipedia.org/" lang="ki">GÄ©kÅ©yÅ©</a></li>\n<li><a href="//gan.wikipedia.org/" lang="gan" title="Gon ua" data-hans="èµ£è¯\xad" data-hant="è´\x9bèª\x9e" class="jscnconv">èµ£è¯\xad / è´\x9bèª\x9e</a></li>\n<li><a href="//guw.wikipedia.org/" lang="guw">Gungbe</a></li>\n<li><a href="//xal.wikipedia.org/" lang="xal" title="HalÊ¹mg">Ð¥Ð°Ð»Ñ\x8cÐ¼Ð³</a></li>\n<li><a href="//haw.wikipedia.org/" lang="haw">Ê»Å\x8clelo HawaiÊ»i</a></li>\n<li><a href="//rw.wikipedia.org/" lang="rw">Ikinyarwanda</a></li>\n<li><a href="//iba.wikipedia.org/" lang="iba">Jaku Iban</a></li>\n<li><a href="//kbp.wikipedia.org/" lang="kbp">KabÉ©yÉ\x9b</a></li>\n<li><a href="//csb.wikipedia.org/" lang="csb">KaszÃ«bsczi</a></li>\n<li><a href="//kw.wikipedia.org/" lang="kw">Kernewek</a></li>\n<li><a href="//kv.wikipedia.org/" lang="kv" title="Komi">Ð\x9aÐ¾Ð¼Ð¸</a></li>\n<li><a href="//koi.wikipedia.org/" lang="koi" title="Perem Komi">Ð\x9fÐµÑ\x80ÐµÐ¼ ÐºÐ¾Ð¼Ð¸</a></li>\n<li><a href="//kg.wikipedia.org/" lang="kg">Kongo</a></li>\n<li><a href="//gom.wikipedia.org/" lang="gom">à¤\x95à¥\x8bà¤\x82à¤\x95à¤£à¥\x80 / Konknni</a></li>\n<li><a href="//ks.wikipedia.org/" lang="ks" title="Koshur"><bdi dir="rtl">Ù\x83Ù²Ø´Ù\x8fØ±</bdi></a></li>\n<li><a href="//gcr.wikipedia.org/" lang="gcr" title="KriyÃ²l Gwiyannen">KriyÃ²l Gwiyannen</a></li>\n<li><a href="//kge.wikipedia.org/" lang="kge">Kumoring</a></li>\n<li><a href="//kus.wikipedia.org/" lang="kus">KÊ\x8bsaal</a></li>\n<li><a href="//lo.wikipedia.org/" lang="lo" title="Phaasaa Laao">àº\x9eàº²àºªàº²àº¥àº²àº§</a></li>\n<li><a href="//lbe.wikipedia.org/" lang="lbe" title="Lakku">Ð\x9bÐ°ÐºÐºÑ\x83</a></li>\n<li><a href="//ltg.wikipedia.org/" lang="ltg">LatgaÄ¼u</a></li>\n<li><a href="//lez.wikipedia.org/" lang="lez" title="Lezgi">Ð\x9bÐµÐ·Ð³Ð¸</a></li>\n<li><a href="//nia.wikipedia.org/" lang="nia">Li Niha</a></li>\n<li><a href="//ln.wikipedia.org/" lang="ln">LingÃ¡la</a></li>\n<li><a href="//lfn.wikipedia.org/" lang="lfn">Lingua Franca Nova</a></li>\n<li><a href="//olo.wikipedia.org/" lang="olo">livvinkarjala</a></li>\n<li><a href="//jbo.wikipedia.org/" lang="jbo">lojban</a></li>\n<li><a href="//lg.wikipedia.org/" lang="lg">Luganda</a></li>\n<li><a href="//mad.wikipedia.org/" lang="mad">MadhurÃ¢</a></li>\n<li><a href="//mt.wikipedia.org/" lang="mt">Malti</a></li>\n<li><a href="//btm.wikipedia.org/" lang="btm">Mandailing</a></li>\n<li><a href="//mi.wikipedia.org/" lang="mi">MÄ\x81ori</a></li>\n<li><a href="//tw.wikipedia.org/" lang="tw" title="Mfantse">Twi</a></li>\n<li><a href="//mwl.wikipedia.org/" lang="mwl">MirandÃ©s</a></li>\n<li><a href="//mdf.wikipedia.org/" lang="mdf" title="MokÅ¡enj">Ð\x9cÐ¾ÐºÑ\x88ÐµÐ½Ñ\x8c</a></li>\n<li><a href="//mnw.wikipedia.org/" lang="mnw">á\x80\x98á\x80¬á\x80\x9eá\x80¬ á\x80\x99á\x80\x94á\x80º</a></li>\n<li><a href="//mos.wikipedia.org/" lang="mos">Moore</a></li>\n<li><a href="//nqo.wikipedia.org/" lang="nqo" title="N&#x27;Ko">ß\x92ß\x9eß\x8f</a></li>\n<li><a href="//fj.wikipedia.org/" lang="fj">Na Vosa Vaka-Viti</a></li>\n<li><a href="//nah.wikipedia.org/" lang="nah">NÄ\x81huatlahtÅ\x8dlli</a></li>\n<li><a href="//pcm.wikipedia.org/" lang="pcm">NaijÃ¡</a></li>\n<li><a href="//nds-nl.wikipedia.org/" lang="nds-nl">Nedersaksisch</a></li>\n<li><a href="//nrm.wikipedia.org/" lang="roa-x-nrm">Nouormand / Normaund</a></li>\n<li><a href="//nov.wikipedia.org/" lang="nov">Novial</a></li>\n<li><a href="//om.wikipedia.org/" lang="om">Afaan Oromoo</a></li>\n<li><a href="//blk.wikipedia.org/" lang="blk">á\x80\x95á\x80¡á\x80\xadá\x80¯á\x80\x9dá\x80ºá\x82\x8fá\x80\x98á\x80¬á\x82\x8fá\x80\x9eá\x80¬á\x82\x8f</a></li>\n<li><a href="//pi.wikipedia.org/" lang="pi" title="PÄ\x81á¸·i">à¤ªà¤¾à¤²à¤¿</a></li>\n<li><a href="//pag.wikipedia.org/" lang="pag">PangasinÃ¡n</a></li>\n<li><a href="//ami.wikipedia.org/" lang="ami">Pangcah</a></li>\n<li><a href="//pap.wikipedia.org/" lang="pap">Papiamentu</a></li>\n<li><a href="//jam.wikipedia.org/" lang="jam">Patois</a></li>\n<li><a href="//pfl.wikipedia.org/" lang="pfl">PfÃ¤lzisch</a></li>\n<li><a href="//pcd.wikipedia.org/" lang="pcd">Picard</a></li>\n<li><a href="//krc.wikipedia.org/" lang="krc" title="QaraÃ§ayâ\x80\x93Malqar">Ð\x9aÑ\x8aÐ°Ñ\x80Ð°Ñ\x87Ð°Ð¹â\x80\x93Ð¼Ð°Ð»ÐºÑ\x8aÐ°Ñ\x80</a></li>\n<li><a href="//kaa.wikipedia.org/" lang="kaa" title="Qaraqalpaqsha">Qaraqalpaqsha</a></li>\n<li><a href="//ksh.wikipedia.org/" lang="ksh">Ripoarisch</a></li>\n<li><a href="//rm.wikipedia.org/" lang="rm">Rumantsch</a></li>\n<li><a href="//rue.wikipedia.org/" lang="rue" title="Rusinâ\x80\x99skyj">Ð\xa0Ñ\x83Ñ\x81Ð¸Ð½Ñ\x8cÑ\x81ÐºÑ\x8bÐ¹</a></li>\n<li><a href="//szy.wikipedia.org/" lang="szy">Sakizaya</a></li>\n<li><a href="//sm.wikipedia.org/" lang="sm">Gagana SÄ\x81moa</a></li>\n<li><a href="//skr.wikipedia.org/" lang="skr" title="Saraiki">Ø³Ø±Ø§Ø¦Û\x8cÚ©Û\x8c</a></li>\n<li><a href="//sc.wikipedia.org/" lang="sc" title="Sardu">Sardu</a></li>\n<li><a href="//trv.wikipedia.org/" lang="trv">Seediq</a></li>\n<li><a href="//stq.wikipedia.org/" lang="stq">Seeltersk</a></li>\n<li><a href="//st.wikipedia.org/" lang="st">Sesotho</a></li>\n<li><a href="//nso.wikipedia.org/" lang="nso">Sesotho sa Leboa</a></li>\n<li><a href="//tn.wikipedia.org/" lang="tn">Setswana</a></li>\n<li><a href="//cu.wikipedia.org/" lang="cu" title="SlovÄ\x9bnÄ\xadskÅ\xad">Ð¡Ð»Ð¾Ð²Ñ£Ì\x81Ð½Ñ\x8cÑ\x81ÐºÑ\x8a / â°\x94â°\x8eâ°\x91â°\x82â°¡â°\x90â°\xa0â°\x94â°\x8dâ°\x9f</a></li>\n<li><a href="//so.wikipedia.org/" lang="so">Soomaaliga</a></li>\n<li><a href="//srn.wikipedia.org/" lang="srn">Sranantongo</a></li>\n<li><a href="//ss.wikipedia.org/" lang="ss">SiSwati</a></li>\n<li><a href="//shi.wikipedia.org/" lang="shi">Taclá¸¥it</a></li>\n<li><a href="//ty.wikipedia.org/" lang="ty">Reo tahiti</a></li>\n<li><a href="//kab.wikipedia.org/" lang="kab" title="Taqbaylit">Taqbaylit</a></li>\n<li><a href="//roa-tara.wikipedia.org/" lang="roa">TarandÃ\xadne</a></li>\n<li><a href="//tay.wikipedia.org/" lang="tay">Tayal</a></li>\n<li><a href="//tet.wikipedia.org/" lang="tet">Tetun</a></li>\n<li><a href="//tpi.wikipedia.org/" lang="tpi">Tok Pisin</a></li>\n<li><a href="//tly.wikipedia.org/" lang="tly">tolÄ±Å\x9fi</a></li>\n<li><a href="//to.wikipedia.org/" lang="to">faka Tonga</a></li>\n<li><a href="//tk.wikipedia.org/" lang="tk">TÃ¼rkmenÃ§e</a></li>\n<li><a href="//kcg.wikipedia.org/" lang="kcg">Tyap</a></li>\n<li><a href="//tyv.wikipedia.org/" lang="tyv" title="Tyva dyl">Ð¢Ñ\x8bÐ²Ð° Ð´Ñ\x8bÐ»</a></li>\n<li><a href="//udm.wikipedia.org/" lang="udm" title="Udmurt">Ð£Ð´Ð¼Ñ\x83Ñ\x80Ñ\x82</a></li>\n<li><a href="//ug.wikipedia.org/" lang="ug"><bdi dir="rtl">Ø¦Û\x87Ù\x8aØºÛ\x87Ø±Ú\x86Ù\x87</bdi></a></li>\n<li><a href="//vep.wikipedia.org/" lang="vep">VepsÃ¤n</a></li>\n<li><a href="//fiu-vro.wikipedia.org/" lang="vro">vÃµro</a></li>\n<li><a href="//vls.wikipedia.org/" lang="vls">West-Vlams</a></li>\n<li><a href="//wo.wikipedia.org/" lang="wo">Wolof</a></li>\n<li><a href="//xh.wikipedia.org/" lang="xh">isiXhosa</a></li>\n<li><a href="//zea.wikipedia.org/" lang="zea">ZeÃªuws</a></li>\n<li><a href="//alt.wikipedia.org/" lang="alt">Ð°Ð»Ñ\x82Ð°Ð¹ Ñ\x82Ð¸Ð»</a></li>\n<li><a href="//awa.wikipedia.org/" lang="awa">à¤\x85à¤µà¤§à¥\x80</a></li>\n<li><a href="//dty.wikipedia.org/" lang="dty">à¤¡à¥\x8bà¤\x9fà¥\x87à¤²à¥\x80</a></li>\n<li><a href="//tcy.wikipedia.org/" lang="tcy">à²¤à³\x81à²³à³\x81</a></li>\n</ul>\n</div>\n<h2 class="bookshelf-container">\n<span class="bookshelf">\n<span class="text">\n<bdi dir="ltr">\n100+\n</bdi>\n<span class="jsl10n" data-jsl10n="portal.entries">\narticles\n</span>\n</span>\n</span>\n</h2>\n<div class="langlist langlist-tiny hlist" data-el-section="secondary links">\n<ul>\n<li><a href="//bdr.wikipedia.org/" lang="bdr">Bajau Sama</a></li>\n<li><a href="//bm.wikipedia.org/" lang="bm">Bamanankan</a></li>\n<li><a href="//bbc.wikipedia.org/" lang="bbc">Batak Toba</a></li>\n<li><a href="//ch.wikipedia.org/" lang="ch">Chamoru</a></li>\n<li><a href="//dz.wikipedia.org/" lang="dz" title="Rdzong-Kha">à½¢à¾«à½¼à½\x84à¼\x8bà½\x81</a></li>\n<li><a href="//ee.wikipedia.org/" lang="ee">EÊ\x8begbe</a></li>\n<li><a href="//gur.wikipedia.org/" lang="gur">Farefare</a></li>\n<li><a href="//got.wikipedia.org/" lang="got" title="Gutisk">ð\x90\x8c²ð\x90\x8c¿ð\x90\x8d\x84ð\x90\x8c¹ð\x90\x8d\x83ð\x90\x8cº</a></li>\n<li><a href="//igl.wikipedia.org/" lang="igl">Igala</a></li>\n<li><a href="//iu.wikipedia.org/" lang="iu">á\x90\x83á\x93\x84á\x92\x83á\x91\x8eá\x91\x90á\x91¦ / Inuktitut</a></li>\n<li><a href="//ik.wikipedia.org/" lang="ik">IÃ±upiak</a></li>\n<li><a href="//kl.wikipedia.org/" lang="kl">Kalaallisut</a></li>\n<li><a href="//fat.wikipedia.org/" lang="fat">Mfantse</a></li>\n<li><a href="//nr.wikipedia.org/" lang="nr" title="Ndebele seSewula, isi-">isiNdebele seSewula</a></li>\n<li><a href="//pih.wikipedia.org/" lang="pih">Norfuk / Pitkern</a></li>\n<li><a href="//ann.wikipedia.org/" lang="ann">Obolo</a></li>\n<li><a href="//pwn.wikipedia.org/" lang="pwn">pinayuanan</a></li>\n<li><a href="//pnt.wikipedia.org/" lang="pnt" title="PontiakÃ¡">Î\xa0Î¿Î½Ï\x84Î¹Î±ÎºÎ¬</a></li>\n<li><a href="//rmy.wikipedia.org/" lang="rmy">romani Ä\x8dhib</a></li>\n<li><a href="//rn.wikipedia.org/" lang="rn">Ikirundi</a></li>\n<li><a href="//rsk.wikipedia.org/" lang="rsk" title="ruski">Ñ\x80Ñ\x83Ñ\x81ÐºÐ¸</a></li>\n<li><a href="//sg.wikipedia.org/" lang="sg">SÃ¤ngÃ¶</a></li>\n<li><a href="//tdd.wikipedia.org/" lang="tdd" title="Tai taÉ¯ xoÅ\x8b">á¥\x96á¥\xadá¥°á¥\x96á¥¬á¥³á¥\x91á¥¨á¥\x92á¥°</a></li>\n<li><a href="//ti.wikipedia.org/" lang="ti" title="TÉ\x99gÉ\x99rÉ\x99Ã±a">á\x89µá\x8c\x8dá\x88\xadá\x8a\x9b</a></li>\n<li><a href="//din.wikipedia.org/" lang="din">ThuÉ\x94Å\x8bjÃ¤Å\x8b</a></li>\n<li><a href="//chr.wikipedia.org/" lang="chr" title="Tsalagi">á\x8f£á\x8e³á\x8e©</a></li>\n<li><a href="//chy.wikipedia.org/" lang="chy">TsÄ\x97hesenÄ\x97stsestotse</a></li>\n<li><a href="//ts.wikipedia.org/" lang="ts">Xitsonga</a></li>\n<li><a href="//ve.wikipedia.org/" lang="ve">Tshivená¸\x93a</a></li>\n<li><a href="//guc.wikipedia.org/" lang="guc">Wayuunaiki</a></li>\n<li><a href="//ady.wikipedia.org/" lang="ady">Ð°Ð´Ñ\x8bÐ³Ð°Ð±Ð·Ñ\x8d</a></li>\n</ul>\n</div>\n<div class="langlist langlist-others hlist" data-el-section="other languages">\n<a class="jsl10n" href="https://meta.wikimedia.org/wiki/Special:MyLanguage/List_of_Wikipedias" lang data-jsl10n="other-languages-label">Other languages</a>\n</div></div>\n</div>\n</nav>\n<hr>\n<div class="banner banner-overlay" id="portalBanner_en6C_2024_overlayBanner4">\n<div class="overlay-banner">\n<div class="overlay-banner-main">\n<button class="frb-header-minimize overlay-banner-toggle" aria-label="minimize">\n<span class="frb-header-minimize-icon">\n<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><g><path d="m17.5 4.75-7.5 7.5-7.5-7.5L1 6.25l9 9 9-9z"/></g></svg>\n</span>\n</button>\n<div class="overlay-banner-main-header">\n<a href="#">Donate now</a>\n</div>\n<div class="overlay-banner-main-scroll">\n<div class="overlay-banner-main-message">\n<div class="overlay-banner-main-message-greeting">The internet we were promised</div>\n<p class="overlay-banner-main-message-subheading">An important update for readers in <span class="banner__country">the United States</span>.</p>\n<p>\nYou deserve an explanation, so please don\'t skip this 1-minute read. We\'re sorry to interrupt, but this message will only be up for a short time. We ask you to reflect on the number of times you visited Wikipedia this past year and whether you\'re able to give <span class="banner__amount1">$2.75</span> to the Wikimedia Foundation. If everyone reading this gave just <span class="banner__amount1">$2.75</span>, we\'d hit our goal in a few hours.\n</p>\n<p>\nThe internet we were promisedâ\x80\x94a place of free, collaborative, and accessible knowledgeâ\x80\x94is under constant threat. On Wikipedia, volunteers work together to create and verify the pages you rely on, supported by tools that undo vandalism within minutes, ensuring the information you seek is trustworthy.\n</p>\n<p>\nJust 2% of our readers donate, so if you have given in the past and Wikipedia still provides you with <span class="banner__amount1">$2.75</span> worth of knowledge, kindly donate today. If you are undecided, remember that any contribution helps, whether it\'s <span class="banner__amount1">$2.75</span> or <span class="banner__amount2">$2.75</span>.\n</p>\n</div>\n<div class="overlay-banner-main-amounts">\n<div class="frb-message frb-message-amount">\n<span class="error-highlight">Please select an amount (<span class="banner__currency">USD</span>)</span>.\n<span class="frb-explanation">The average donation in <span class="banner__country">the United States</span> is around <span class="banner__average">$13</span>. Many first-time donors give <span class="banner__amount1">$2.75</span>. All that matters is that you\'re choosing to stand up for free, open information; and for that, you have our gratitude.</span>\n</div>\n<div id="amountsGrid" class="button-grid">\n<label class="banner-button button-33"><input type="radio" name="amount" value="2.75" class="sr-only"><span class="banner__amount1"></span></label>\n<label class="banner-button button-33"><input type="radio" name="amount" value="5" class="sr-only"><span class="banner__currency"></span>5</label>\n<label class="banner-button button-33"><input type="radio" name="amount" value="10" class="sr-only"><span class="banner__currency"></span>10</label>\n<label class="banner-button button-33"><input type="radio" name="amount" value="20" class="sr-only"><span class="banner__currency"></span>20</label>\n<label class="banner-button button-33"><input type="radio" name="amount" value="30" class="sr-only"><span class="banner__currency"></span>30</label>\n<label class="banner-button button-33"><input type="radio" name="amount" value="50" class="sr-only"><span class="banner__currency"></span>50</label>\n<label class="banner-button button-33"><input type="radio" name="amount" value="100" class="sr-only"><span class="banner__currency"></span>100</label>\n<label class="banner-button button-67"><input type="radio" name="amount" value="Other" class="sr-only">Other</label>\n</div>\n</div>\n<div class="overlay-banner-main-frequency button-grid">\n<div class="frb-message error-highlight">How often would you like to donate?</div>\n<div id="frequencyGrid" class="button-grid">\n<label class="banner-button button-50"><input type="radio" name="monthly" value="0" class="sr-only">One time</label>\n<label class="banner-button button-50"><input type="radio" name="monthly" value="1" class="sr-only">Give monthly</label>\n</div>\n</div>\n<a href="#" id="frb-donate" class="frb-submit banner-button banner-button-disabled">Donate Now</a>\n<div class="overlay-banner-main-footer">\n<div class="overlay-banner-main-footer-cta">\n<svg class="frb-message-icon" aria-hidden="true" width="20" height="20" viewBox="0 0 25 25" xmlns="http://www.w3.org/2000/svg"><g fill-rule="nonzero" fill="none"><circle cx="10.492" cy="14.492" r="10.492"/><path d="M12.681 11.754l-2.267 7.864c-.125.45-.188.745-.188.885 0 .08.033.156.1.226.066.07.136.105.21.105.125 0 .25-.055.376-.165.332-.273.73-.767 1.194-1.482l.376.22c-1.113 1.94-2.296 2.91-3.55 2.91-.48 0-.86-.135-1.144-.404a1.349 1.349 0 0 1-.426-1.023c0-.273.062-.62.188-1.04l1.537-5.286c.147-.51.221-.892.221-1.15a.566.566 0 0 0-.21-.432c-.14-.125-.332-.188-.575-.188-.11 0-.243.004-.398.011l.144-.442 3.749-.609h.663zm-.685-5.087c.457 0 .842.159 1.156.475.313.318.47.701.47 1.15 0 .45-.16.834-.476 1.15-.317.318-.7.476-1.15.476-.443 0-.822-.158-1.14-.475a1.566 1.566 0 0 1-.475-1.15c0-.45.157-.833.47-1.15a1.549 1.549 0 0 1 1.145-.476z"/></g></svg>\nWe ask you, sincerely: don\'t skip this, join the 2% of readers who give.\n</div>\n<div class="overlay-banner-main-footer-identity">\n<img src="https://upload.wikimedia.org/wikipedia/donate/1/14/Wikimedia_Foundation_logo_-_wordmark.svg" alt="Wikimedia Foundation Logo">\nProud host of Wikipedia and its sister sites\n</div>\n<button type="button" class="button-center button-collapse overlay-banner-toggle">Collapse</button>\n</div>\n</div>\n</div>\n<div class="overlay-banner-mini">\n<div class="frb-conversation-open frb-bubble-message-close overlay-banner-toggle" aria-label="open" style>\n<span class="frb-conversation-open-icon">\n<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><g><path d="m17.5 4.75-7.5 7.5-7.5-7.5L1 6.25l9 9 9-9z"/></g></svg>\n</span>\n</div>\n<div class="frb-conversation-close frb-bubble-message-close overlay-banner-close" aria-label="close" style>\n<span class="frb-conversation-close-icon"></span>\n</div>\n<div class="overlay-banner-mini-message overlay-banner-toggle">\n<div class="overlay-banner-mini-message-text">\n<h3>\n<svg class="frb-message-icon" aria-hidden="true" width="20" height="20" viewBox="0 0 25 25" xmlns="http://www.w3.org/2000/svg"><g fill-rule="nonzero" fill="none"><circle cx="10.492" cy="14.492" r="10.492"/><path d="M12.681 11.754l-2.267 7.864c-.125.45-.188.745-.188.885 0 .08.033.156.1.226.066.07.136.105.21.105.125 0 .25-.055.376-.165.332-.273.73-.767 1.194-1.482l.376.22c-1.113 1.94-2.296 2.91-3.55 2.91-.48 0-.86-.135-1.144-.404a1.349 1.349 0 0 1-.426-1.023c0-.273.062-.62.188-1.04l1.537-5.286c.147-.51.221-.892.221-1.15a.566.566 0 0 0-.21-.432c-.14-.125-.332-.188-.575-.188-.11 0-.243.004-.398.011l.144-.442 3.749-.609h.663zm-.685-5.087c.457 0 .842.159 1.156.475.313.318.47.701.47 1.15 0 .45-.16.834-.476 1.15-.317.318-.7.476-1.15.476-.443 0-.822-.158-1.14-.475a1.566 1.566 0 0 1-.475-1.15c0-.45.157-.833.47-1.15a1.549 1.549 0 0 1 1.145-.476z"/></g></svg>\nThe internet we were promised\n</h3>\n<p><strong>Hi. Please don\'t skip this 1-minute read.</strong> Today, our nonprofit asks for your support. It matters. When Wikipedia was created, it was one of the first spaces online where you could learn for free, without ads. This space is yours. Just 2% of our readers donate, so whatever gift you can afford helps.</p>\n<p>â\x80\x94 <em>The Wikimedia Foundation, host of Wikipedia and its sister sites</em>.</p>\n</div>\n<div class="overlay-banner-mini-message-actions">\n<a href="#" class="banner__button banner__button--progressive frb-submit">\nDonate now\n</a>\n</div>\n</div>\n</div>\n</div>\n</div>\n</main>\n<footer class="footer" data-el-section="other projects">\n<div class="footer-sidebar">\n<div class="footer-sidebar-content">\n<div class="footer-sidebar-icon sprite svg-Wikimedia-logo_black">\n</div>\n<div class="footer-sidebar-text jsl10n" data-jsl10n="portal.footer-description">\nWikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects.\n</div>\n<div class="footer-sidebar-text">\n<a href="https://donate.wikimedia.org/?wmf_medium=portal&wmf_campaign=portalFooter&wmf_source=portalFooter" target="_blank">\n<span class="jsl10n" data-jsl10n="footer-donate">You can support our work with a donation.</span>\n</a>\n</div>\n</div>\n</div>\n<div class="footer-sidebar app-badges">\n<div class="footer-sidebar-content">\n<div class="footer-sidebar-text">\n<div class="footer-sidebar-icon sprite svg-wikipedia_app_tile"></div>\n<strong class="jsl10n" data-jsl10n="portal.app-links.title">\n<a class="jsl10n" data-jsl10n="portal.app-links.url" href="https://en.wikipedia.org/wiki/List_of_Wikipedia_mobile_applications">\nDownload Wikipedia for Android or iOS\n</a>\n</strong>\n<p class="jsl10n" data-jsl10n="portal.app-links.description">\nSave your favorite articles to read offline, sync your reading lists across devices and customize your reading experience with the official Wikipedia app.\n</p>\n<ul>\n<li class="app-badge app-badge-android">\n<a target="_blank" rel="noreferrer" href="https://play.google.com/store/apps/details?id=org.wikipedia&referrer=utm_source%3Dportal%26utm_medium%3Dbutton%26anid%3Dadmob">\n<span class="jsl10n sprite svg-badge_google_play_store" data-jsl10n="portal.app-links.google-store">Google Play Store</span>\n</a>\n</li>\n<li class="app-badge app-badge-ios">\n<a target="_blank" rel="noreferrer" href="https://itunes.apple.com/app/apple-store/id324715238?pt=208305&ct=portal&mt=8">\n<span class="jsl10n sprite svg-badge_ios_app_store" data-jsl10n="portal.app-links.apple-store">Apple App Store</span>\n</a>\n</li>\n</ul>\n</div>\n</div>\n</div>\n<nav data-jsl10n="other-projects-nav-label" aria-label="Other projects" class="other-projects">\n<div class="other-project">\n<a class="other-project-link" href="//commons.wikimedia.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Commons-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="commons.name">Commons</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="commons.slogan">Free media collection</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wikivoyage.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikivoyage-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikivoyage.name">Wikivoyage</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikivoyage.slogan">Free travel guide</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wiktionary.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wiktionary-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wiktionary.name">Wiktionary</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wiktionary.slogan">Free dictionary</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wikibooks.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikibooks-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikibooks.name">Wikibooks</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikibooks.slogan">Free textbooks</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wikinews.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikinews-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikinews.name">Wikinews</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikinews.slogan">Free news source</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wikidata.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikidata-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikidata.name">Wikidata</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikidata.slogan">Free knowledge base</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wikiversity.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikiversity-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikiversity.name">Wikiversity</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikiversity.slogan">Free learning resources</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wikiquote.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikiquote-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikiquote.name">Wikiquote</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikiquote.slogan">Free quote compendium</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.mediawiki.org/">\n<div class="other-project-icon">\n<div class="sprite svg-MediaWiki-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="mediawiki.name">MediaWiki</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="mediawiki.slogan">Free &amp; open wiki software</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wikisource.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikisource-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikisource.name">Wikisource</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikisource.slogan">Free content library</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//species.wikimedia.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikispecies-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikispecies.name">Wikispecies</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikispecies.slogan">Free species directory</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//www.wikifunctions.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Wikifunctions-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="wikifunctions.name">Wikifunctions</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="wikifunctions.slogan">Free function library</span>\n</div>\n</a>\n</div>\n<div class="other-project">\n<a class="other-project-link" href="//meta.wikimedia.org/">\n<div class="other-project-icon">\n<div class="sprite svg-Meta-Wiki-logo_sister"></div>\n</div>\n<div class="other-project-text">\n<span class="other-project-title jsl10n" data-jsl10n="metawiki.name">Meta-Wiki</span>\n<span class="other-project-tagline jsl10n" data-jsl10n="metawiki.slogan">Community coordination &amp; documentation</span>\n</div>\n</a>\n</div>\n</nav>\n<hr>\n<p class="site-license">\n<small class="jsl10n" data-jsl10n="license">This page is available under the <a href="https://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike License</a></small>\n<small class="jsl10n" data-jsl10n="terms"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use">Terms of Use</a></small>\n<small class="jsl10n" data-jsl10n="privacy-policy"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy">Privacy Policy</a></small>\n</p>\n</footer>\n<script>\nvar rtlLangs = [\'ar\',\'arc\',\'ary\',\'arz\',\'bcc\',\'bgn\',\'bqi\',\'ckb\',\'dv\',\'fa\',\'glk\',\'he\',\'kk-cn\',\'kk-arab\',\'khw\',\'ks\',\'ku-arab\',\'lki\',\'luz\',\'mzn\',\'nqo\',\'pnb\',\'ps\',\'sd\',\'sdh\',\'skr\',\'ug\',\'ur\',\'yi\'],\n    translationsHash = \'8d587fac\',\n    /**\n     * This variable is used to convert the generic "portal" keyword in the data-jsl10n attributes\n     * e.g. \'data-jsl10n="portal.footer-description"\' into a portal-specific key, e.g. "wiki"\n     * for the Wikipedia portal.\n     */\n    translationsPortalKey = \'wiki\';\n    /**\n     * The wm-typeahead.js feature is used for search,and it uses domain name for searching. We want domain\n     * name to be portal Specific (different for every portal).So by declaring variable \'portalSearchDomain\'\n     * in index.handlebars we will make this portal Specific.\n    **/\n    portalSearchDomain = \'wikipedia.org\'\n    /*\n     This object is used by l10n scripts (page-localized.js, topten-localized.js)\n     to reveal the page content after l10n json is loaded.\n     A timer is also set to prevent JS from hiding page content indefinitelty.\n     This script is inlined to safeguard againt script loading errors and placed\n     at the top of the page to safeguard against any HTML loading/parsing errors.\n    */\n    wmL10nVisible = {\n        ready: false,\n        makeVisible: function(){\n            if ( !wmL10nVisible.ready ) {\n                wmL10nVisible.ready = true;\n                document.body.className += \' jsl10n-visible\';\n            }\n        }\n    };\n    window.setTimeout( wmL10nVisible.makeVisible, 1000 )\n</script>\n<script src="portal/wikipedia.org/assets/js/index-0b1f819930.js"></script>\n<script src="portal/wikipedia.org/assets/js/gt-ie9-ce3fe8e88d.js"></script>\n<style>\n.styled-select {\n        display: block;\n    }\n</style>\n</body>\n</html>\n'



Once you have the HTML content, you'll want to parse it to extract the data you're interested in.


```python
from bs4 import BeautifulSoup

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print the parsed HTML
    print(soup.prettify())  # 'prettify' formats the output for readability
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

```

    <!DOCTYPE html>
    <html class="no-js" lang="en">
     <head>
      <meta charset="utf-8"/>
      <title>
       Wikipedia
      </title>
      <meta content="Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation." name="description"/>
      <script>
       document.documentElement.className = document.documentElement.className.replace( /(^|\s)no-js(\s|$)/, "$1js-enabled$2" );
      </script>
      <meta content="initial-scale=1,user-scalable=yes" name="viewport"/>
      <link href="/static/apple-touch/wikipedia.png" rel="apple-touch-icon"/>
      <link href="/static/favicon/wikipedia.ico" rel="shortcut icon"/>
      <link href="//creativecommons.org/licenses/by-sa/4.0/" rel="license"/>
      <style>
       .sprite{background-image:linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/sprite-de847d1a.svg);background-repeat:no-repeat;display:inline-block;vertical-align:middle}.svg-Commons-logo_sister{background-position:0 0;width:47px;height:47px}.svg-MediaWiki-logo_sister{background-position:0 -47px;width:42px;height:42px}.svg-Meta-Wiki-logo_sister{background-position:0 -89px;width:37px;height:37px}.svg-Wikibooks-logo_sister{background-position:0 -126px;width:37px;height:37px}.svg-Wikidata-logo_sister{background-position:0 -163px;width:49px;height:49px}.svg-Wikifunctions-logo_sister{background-position:0 -212px;width:50px;height:50px}.svg-Wikimedia-logo_black{background-position:0 -262px;width:42px;height:42px}.svg-Wikipedia_wordmark{background-position:0 -304px;width:176px;height:32px}.svg-Wikiquote-logo_sister{background-position:0 -336px;width:42px;height:42px}.svg-Wikisource-logo_sister{background-position:0 -378px;width:39px;height:39px}.svg-Wikispecies-logo_sister{background-position:0 -417px;width:42px;height:42px}.svg-Wikiversity-logo_sister{background-position:0 -459px;width:43px;height:37px}.svg-Wikivoyage-logo_sister{background-position:0 -496px;width:36px;height:36px}.svg-Wiktionary-logo_sister{background-position:0 -532px;width:37px;height:37px}.svg-arrow-down{background-position:0 -569px;width:12px;height:8px}.svg-arrow-down-blue{background-position:0 -577px;width:14px;height:14px}.svg-badge_google_play_store{background-position:0 -591px;width:124px;height:38px}.svg-badge_ios_app_store{background-position:0 -629px;width:110px;height:38px}.svg-language-icon{background-position:0 -667px;width:22px;height:22px}.svg-noimage{background-position:0 -689px;width:58px;height:58px}.svg-search-icon{background-position:0 -747px;width:22px;height:22px}.svg-wikipedia_app_tile{background-position:0 -769px;width:42px;height:42px}
      </style>
      <style>
       html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-size:62.5%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:700}dfn{font-style:italic}h1{font-size:32px;font-size:3.2rem;margin:1.2rem 0}mark{background:#fef6e7;color:#000}small{font-size:13px;font-size:1.3rem}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}svg:not(:root){overflow:hidden}figure{margin:1.6rem 4rem}hr{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace,monospace;font-size:14px;font-size:1.4rem}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=button],input[type=reset],input[type=submit]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=checkbox],input[type=radio]{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:0}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{height:auto}input[type=search]{-webkit-appearance:none;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration{-webkit-appearance:none}input[type=search]:focus{outline-offset:-2px}fieldset{border:1px solid #a2a9b1;margin:0 .2rem;padding:.6rem 1rem 1.2rem}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:700}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}.hidden,[hidden]{display:none!important}.screen-reader-text{display:block;position:absolute!important;clip:rect(1px,1px,1px,1px);width:1px;height:1px;margin:-1px;border:0;padding:0;overflow:hidden}body{background-color:#fff;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Inter,Helvetica,Arial,sans-serif;font-size:14px;font-size:1.4rem;line-height:1.5;margin:.4rem 0 1.6rem}main{padding:0 1.28rem}a{-ms-touch-action:manipulation;touch-action:manipulation}a,a:active,a:focus{unicode-bidi:embed;outline:0;color:#36c;text-decoration:none}a:focus{outline:1px solid #36c}a:hover{text-decoration:underline}img{vertical-align:middle}hr,img{border:0}hr{clear:both;height:0;border-bottom:1px solid #c8ccd1;margin:.26rem 0}.pure-button{display:inline-block;zoom:1;line-height:normal;white-space:nowrap;text-align:center;cursor:pointer;-webkit-user-drag:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;background-color:#f8f9fa;color:#202122;position:relative;min-height:19.2px;min-height:1.92rem;min-width:16px;min-width:1.6rem;margin:.16rem 0;border:1px solid #a2a9b1;-moz-border-radius:2px;border-radius:2px;padding:.8rem 1.6rem;font-family:inherit;font-size:inherit;font-weight:700;text-decoration:none;vertical-align:top;-webkit-transition:background .1s ease,color .1s ease,border-color .1s ease,-webkit-box-shadow .1s ease;transition:background .1s ease,color .1s ease,border-color .1s ease,-webkit-box-shadow .1s ease;-o-transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease;-moz-transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease,-moz-box-shadow .1s ease;transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease;transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease,-webkit-box-shadow .1s ease,-moz-box-shadow .1s ease}.pure-button::-moz-focus-inner{padding:0;border:0}.pure-button-hover,.pure-button:hover{background-color:#fff;border-color:#a2a9b1;color:#404244}.pure-button-active,.pure-button:active{background-color:#eaecf0;border-color:#72777d;color:#000}.pure-button:focus{outline:1px solid transparent;border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c;-moz-box-shadow:inset 0 0 0 1px #36c;box-shadow:inset 0 0 0 1px #36c}.pure-button-primary-progressive{background-color:#36c;border-color:#36c;color:#fff}.pure-button-primary-progressive:hover{background:#447ff5;border-color:#447ff5}.pure-button-primary-progressive:active{background-color:#2a4b8d;border-color:#2a4b8d;-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none;color:#fff}.pure-button-primary-progressive:focus{-webkit-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;-moz-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;border-color:#36c}.pure-form input[type=search]{background-color:#fff;display:inline-block;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;border:1px solid #a2a9b1;-moz-border-radius:2px;border-radius:2px;padding:.8rem;-webkit-box-shadow:inset 0 0 0 1px #fff;-moz-box-shadow:inset 0 0 0 1px #fff;box-shadow:inset 0 0 0 1px #fff;vertical-align:middle}.pure-form input:focus:invalid{color:#d73333;border-color:#b32424}.pure-form fieldset{margin:0;padding:.56rem 0 1.2rem;border:0}@media only screen and (max-width:480px){.pure-form input[type=search]{display:block}}.central-textlogo-wrapper{display:inline-block;vertical-align:bottom}.central-textlogo{position:relative;margin:4rem auto .5rem;width:270px;font-family:Linux Libertine,Hoefler Text,Georgia,Times New Roman,Times,serif;font-size:30px;font-size:3rem;font-weight:400;line-height:33px;line-height:3.3rem;text-align:center;-moz-font-feature-settings:"ss05=1";-moz-font-feature-settings:"ss05";-webkit-font-feature-settings:"ss05";-ms-font-feature-settings:"ss05";font-feature-settings:"ss05"}.localized-slogan{display:block;font-family:Linux Libertine,Georgia,Times,"Source Serif Pro",serif;font-size:15px;font-size:1.5rem;font-weight:400}.central-textlogo__image{color:transparent;display:inline-block;overflow:hidden;text-indent:-10000px}.central-featured-logo{position:absolute;top:158px;left:35px}@media (max-width:480px){.central-textlogo{position:relative;height:70px;width:auto;margin:2rem 0 0;text-align:center;line-height:25px;line-height:2.5rem;text-indent:-10px;text-indent:-1rem;font-size:1em}.central-textlogo-wrapper{position:relative;top:12px;text-indent:2px;text-indent:.2rem}.svg-Wikipedia_wordmark{width:150px;height:25px;background-position:0 -260px;-webkit-background-size:100% 100%;-moz-background-size:100%;background-size:100%}.localized-slogan{font-size:14px;font-size:1.4rem}.central-featured-logo{position:relative;display:inline-block;width:57px;height:auto;left:0;top:0}}@media (max-width:240px){.central-textlogo__image{height:auto}}.central-featured{position:relative;height:325px;height:32.5rem;width:546px;width:54.6rem;max-width:100%;margin:0 auto;text-align:center;vertical-align:middle}.central-featured-lang{position:absolute;width:156px;width:15.6rem}.central-featured-lang .link-box{display:block;padding:0;text-decoration:none;white-space:normal}.central-featured-lang .link-box:hover strong{text-decoration:underline}.central-featured-lang :hover{background-color:#eaecf0}.central-featured-lang strong{display:block;font-size:16px;font-size:1.6rem}.central-featured-lang small{color:#54595d;display:inline-block;font-size:13px;font-size:1.3rem;line-height:1.6}.central-featured-lang em{font-style:italic}.central-featured-lang .emNonItalicLang{font-style:normal}.lang1{top:0;right:60%}.lang2{top:0;left:60%}.lang3{top:20%;right:70%}.lang4{top:20%;left:70%}.lang5{top:40%;right:72%}.lang6{top:40%;left:72%}.lang7{top:60%;right:70%}.lang8{top:60%;left:70%}.lang9{top:80%;right:60%}.lang10{top:80%;left:60%}@media (max-width:480px){.central-featured{width:auto;height:auto;margin-top:8rem;font-size:13px;font-size:1.3rem;text-align:left}.central-featured:after{content:" ";display:block;visibility:hidden;clear:both;height:0;font-size:0}.central-featured-lang{display:block;float:left;position:relative;top:auto;left:auto;right:auto;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;height:64px;height:6.4rem;width:33%;margin:0 0 16px;padding:0 1.6rem;font-size:14px;font-size:1.4rem;text-align:center}.central-featured-lang strong{font-size:14px;font-size:1.4rem;margin-bottom:4px}.central-featured-lang small{line-height:1.4}}@media (max-width:375px){.central-featured-lang{font-size:13px;font-size:1.3rem}}@media (max-width:240px){.central-featured-lang{width:100%}}.search-container{float:none;max-width:95%;width:540px;margin:.4rem auto 1.95rem;text-align:center;vertical-align:middle}.search-container fieldset{word-spacing:-4px}.search-container button{min-height:44px;min-height:4.4rem;margin:0;-moz-border-radius:0 2px 2px 0;border-radius:0 2px 2px 0;padding:.8rem 1.6rem;font-size:16px;font-size:1.6rem;z-index:2}.search-container button .svg-search-icon{text-indent:-9999px}.search-container input[type=search]::-webkit-search-results-button,.search-container input[type=search]::-webkit-search-results-decoration{-webkit-appearance:none}.search-container input::-webkit-calendar-picker-indicator{display:none}.search-container .sprite.svg-arrow-down{position:absolute;top:8px;top:.8rem;right:6px;right:.6rem}#searchInput{-webkit-appearance:none;width:100%;height:44px;height:4.4rem;border-width:1px 0 1px 1px;-moz-border-radius:2px 0 0 2px;border-radius:2px 0 0 2px;padding:.8rem 9.6rem .8rem 1.2rem;font-size:16px;font-size:1.6rem;line-height:1.6;-webkit-transition:background .1s ease,border-color .1s ease,-webkit-box-shadow .1s ease;transition:background .1s ease,border-color .1s ease,-webkit-box-shadow .1s ease;-o-transition:background .1s ease,border-color .1s ease,box-shadow .1s ease;-moz-transition:background .1s ease,border-color .1s ease,box-shadow .1s ease,-moz-box-shadow .1s ease;transition:background .1s ease,border-color .1s ease,box-shadow .1s ease;transition:background .1s ease,border-color .1s ease,box-shadow .1s ease,-webkit-box-shadow .1s ease,-moz-box-shadow .1s ease}#searchInput:hover{border-color:#72777d}#searchInput:focus{border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c;-moz-box-shadow:inset 0 0 0 1px #36c;box-shadow:inset 0 0 0 1px #36c;outline:1px solid transparent}.search-container .search-input{display:inline-block;position:relative;width:73%;vertical-align:top}@media only screen and (max-width:480px){.search-container .pure-form fieldset{margin-left:1rem;margin-right:6.6rem}.search-container .search-input{width:100%;margin-right:-6.6rem}.search-container .pure-form button{float:right;right:-56px;right:-5.6rem}}.suggestions-dropdown{background-color:#fff;display:inline-block;position:absolute;left:0;z-index:2;margin:0;padding:0;border:1px solid #a2a9b1;border-top:0;-webkit-box-shadow:0 2px 2px 0 rgba(0,0,0,.2);-moz-box-shadow:0 2px 2px 0 rgba(0,0,0,.2);box-shadow:0 2px 2px 0 rgba(0,0,0,.2);list-style-type:none;word-spacing:normal}.suggestion-link,.suggestions-dropdown{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:100%;text-align:left}.suggestion-link{display:block;position:relative;min-height:70px;min-height:7rem;padding:1rem 1rem 1rem 8.5rem;border-bottom:1px solid #eaecf0;color:inherit;text-decoration:none;text-align:initial;white-space:normal}.suggestion-link.active{background-color:#eaf3ff}a.suggestion-link:hover{text-decoration:none}a.suggestion-link:active,a.suggestion-link:focus{outline:0;white-space:normal}.suggestion-thumbnail{background-color:#eaecf0;background-image:url(portal/wikipedia.org/assets/img/noimage.png);background-image:-webkit-linear-gradient(transparent,transparent),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Cpath fill='%23eee' d='M0 0h56v56H0z'/%3E%3Cpath fill='%23999' d='M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z'/%3E%3C/svg%3E");background-image:-webkit-linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:-webkit-gradient(linear,left top,left bottom,from(transparent),to(transparent)),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Cpath fill='%23eee' d='M0 0h56v56H0z'/%3E%3Cpath fill='%23999' d='M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z'/%3E%3C/svg%3E");background-image:-moz- oldlinear-gradient(transparent,transparent),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Cpath fill='%23eee' d='M0 0h56v56H0z'/%3E%3Cpath fill='%23999' d='M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z'/%3E%3C/svg%3E");background-image:-o-linear-gradient(transparent,transparent),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Cpath fill='%23eee' d='M0 0h56v56H0z'/%3E%3Cpath fill='%23999' d='M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z'/%3E%3C/svg%3E");background-image:linear-gradient(transparent,transparent),url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Cpath fill='%23eee' d='M0 0h56v56H0z'/%3E%3Cpath fill='%23999' d='M36.4 13.5H17.8v24.9c0 1.4.9 2.3 2.3 2.3h18.7v-25c.1-1.4-1-2.2-2.4-2.2zM30.2 17h5.1v6.4h-5.1V17zm-8.8 0h6v1.8h-6V17zm0 4.6h6v1.8h-6v-1.8zm0 15.5v-1.8h13.8v1.8H21.4zm13.8-4.5H21.4v-1.8h13.8v1.8zm0-4.7H21.4v-1.8h13.8v1.8z'/%3E%3C/svg%3E");background-image:-webkit-gradient(linear,left top,left bottom,from(transparent),to(transparent)),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:-moz- oldlinear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:-o-linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.svg) !ie;background-image:-o-linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/noimage.png);background-position:50%;background-repeat:no-repeat;-webkit-background-size:100% auto;-moz-background-size:100% auto;background-size:100% auto;-webkit-background-size:cover;-moz-background-size:cover;background-size:cover;height:100%;width:70px;width:7rem;position:absolute;top:0;left:0}.suggestion-title{margin:0 0 .78rem;color:#54595d;font-size:16px;font-size:1.6rem;line-height:18.72px;line-height:1.872rem}.suggestion-link.active .suggestion-title{color:#36c}.suggestion-highlight{font-style:normal;text-decoration:underline}.suggestion-description{color:#72777d;margin:0;font-size:13px;font-size:1.3rem;line-height:14.299px;line-height:1.43rem}.styled-select{display:none;position:absolute;top:10px;top:1rem;bottom:12px;bottom:1.2rem;right:12px;right:1.2rem;max-width:95px;max-width:9.5rem;height:24px;height:2.4rem;-moz-border-radius:2px;border-radius:2px}.styled-select:hover{background-color:#f8f9fa}.styled-select .hide-arrow{right:32px;right:3.2rem;max-width:68px;max-width:6.8rem;height:24px;height:2.4rem;overflow:hidden;text-align:right}.styled-select select{background:transparent;display:inline;overflow:hidden;height:24px;height:2.4rem;min-width:110px;min-width:11rem;max-width:110px;max-width:11rem;width:110px;width:11rem;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;border:0;line-height:24px;line-height:2.4rem;-webkit-appearance:none;-moz-appearance:window;text-indent:.01px;-o-text-overflow:"";text-overflow:"";opacity:0;-moz-appearance:none;appearance:none;cursor:pointer}.styled-select.no-js{width:95px;width:9.5rem}.styled-select.no-js select{opacity:1;margin:0;padding:0 2.4rem 0 .8rem;color:#54595d}.styled-select.no-js .hide-arrow{width:68px;width:6.8rem}.search-container .styled-select.no-js .js-langpicker-label{display:none}.styled-select.js-enabled .hide-arrow{padding:0 2.4rem 0 .8rem}.styled-select.js-enabled select{background:transparent;position:absolute;top:0;left:0;height:100%;z-index:1;width:100%;border:0;margin:0;padding:0 2.4rem;color:transparent;color:hsla(0,0%,100%,0)}.styled-select.js-enabled select option{color:#54595d}.styled-select.js-enabled select:hover{background-color:transparent}.styled-select-active-helper{display:none}.styled-select.js-enabled select:focus+.styled-select-active-helper{display:block;position:absolute;top:0;left:0;z-index:0;width:100%;height:100%;outline:1px solid #36c}.search-container .js-langpicker-label{display:inline-block;margin:0;color:#54595d;font-size:13px;font-size:1.3rem;line-height:24px;line-height:2.4rem;text-transform:uppercase}.styled-select select:hover{background-color:#f8f9fa}.styled-select select::-ms-expand{display:none}.styled-select select:focus{outline:1px solid transparent;-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none}@-moz-document url-prefix(){.styled-select select{width:110%}}.other-projects{display:inline-block;width:65%}.other-project{float:left;position:relative;width:33%;height:90px;height:9rem}.other-project-link{display:inline-block;min-height:50px;width:90%;padding:1em;white-space:nowrap}.other-project-link:hover{background-color:#eaecf0}a.other-project-link{text-decoration:none}.other-project-icon{display:inline-block;width:50px;text-align:center}.svg-Wikinews-logo_sister{background-image:url(portal/wikipedia.org/assets/img/Wikinews-logo_sister.png);background-position:0 0;-webkit-background-size:47px 26px;-moz-background-size:47px 26px;background-size:47px 26px;width:47px;height:26px}@media (-o-min-device-pixel-ratio:5/4),(-webkit-min-device-pixel-ratio:1.25),(min-resolution:120dpi){.svg-Wikinews-logo_sister{background-image:url(portal/wikipedia.org/assets/img/Wikinews-logo_sister@2x.png)}}.other-project-text,.other-project .sprite-project-logos{display:inline-block}.other-project-text{max-width:65%;font-size:14px;font-size:1.4rem;vertical-align:middle;white-space:normal}.other-project-tagline,.other-project-title{display:block}.other-project-tagline{color:#54595d;font-size:13px;font-size:1.3rem}@media screen and (max-width:768px){.other-projects{width:100%}.other-project{width:33%}}@media screen and (max-width:480px){.other-project{width:50%}.other-project-tagline{-webkit-hyphens:auto;-moz-hyphens:auto;-ms-hyphens:auto;hyphens:auto}}@media screen and (max-width:320px){.other-project-text{margin-right:5px;font-size:13px;font-size:1.3rem}}.lang-list-container{background-color:#f8f9fa;overflow:hidden;position:relative;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;max-height:0;width:80%;margin:-1.6rem auto 4.8rem;-webkit-transition:max-height .5s ease-out .16s,visibility .5s ease-in 1s;-o-transition:max-height .5s ease-out .16s,visibility .5s ease-in 1s;-moz-transition:max-height .5s ease-out .16s,visibility .5s ease-in 1s;transition:max-height .5s ease-out .16s,visibility .5s ease-in 1s}.js-enabled .lang-list-container{visibility:hidden}.lang-list-active .lang-list-container,.no-js .lang-list-container{visibility:visible;max-height:10000px;-webkit-transition:max-height 1s ease-in .2s,visibility 1000s ease-in 0ms;-o-transition:max-height 1s ease-in .2s,visibility 1000s ease-in 0ms;-moz-transition:max-height 1s ease-in .2s,visibility 1000s ease-in 0ms;transition:max-height 1s ease-in .2s,visibility 1000s ease-in 0ms}.no-js .lang-list-button{display:none}.lang-list-button-wrapper{text-align:center}.lang-list-button{background-color:#f8f9fa;display:inline;position:relative;z-index:1;margin:0 auto;padding:.6rem 1.2rem;outline:16px solid #fff;outline:1.6rem solid #fff;border:1px solid #a2a9b1;-moz-border-radius:2px;border-radius:2px;color:#36c;font-size:14px;font-size:1.4rem;font-weight:700;line-height:1;-webkit-transition:outline-width .1s ease-in .5s;-o-transition:outline-width .1s ease-in .5s;-moz-transition:outline-width .1s ease-in .5s;transition:outline-width .1s ease-in .5s}.lang-list-button:hover{background-color:#fff;border-color:#a2a9b1}.lang-list-button:focus{border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c;-moz-box-shadow:inset 0 0 0 1px #36c;box-shadow:inset 0 0 0 1px #36c}.lang-list-active .lang-list-button{background-color:#fff;outline:1px solid #fff;border-color:#72777d;-webkit-transition-delay:0s;-moz-transition-delay:0s;-o-transition-delay:0s;transition-delay:0s}.lang-list-button-text{padding:0 .64rem;vertical-align:middle}.lang-list-button i{display:inline-block;vertical-align:middle}.no-js .lang-list-border,.no-js .lang-list-button{display:none}.lang-list-border{background-color:#c8ccd1;display:block;position:relative;max-width:460px;width:80%;margin:-1.6rem auto 1.6rem;height:1px;-webkit-transition:max-width .2s ease-out .4s;-o-transition:max-width .2s ease-out .4s;-moz-transition:max-width .2s ease-out .4s;transition:max-width .2s ease-out .4s}.lang-list-active .lang-list-border{max-width:85%;-webkit-transition-delay:0s;-moz-transition-delay:0s;-o-transition-delay:0s;transition-delay:0s}.no-js .lang-list-content{padding:0}.lang-list-content{position:relative;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:100%;padding:1.6rem 1.6rem 0}.svg-arrow-down-blue{-webkit-transition:-webkit-transform .2s ease-out;transition:-webkit-transform .2s ease-out;-o-transition:transform .2s ease-out;-moz-transition:transform .2s ease-out,-moz-transform .2s ease-out;transition:transform .2s ease-out;transition:transform .2s ease-out,-webkit-transform .2s ease-out,-moz-transform .2s ease-out}.lang-list-active .svg-arrow-down-blue{-webkit-transform:rotate(180deg);-moz-transform:rotate(180deg);-ms-transform:rotate(180deg);transform:rotate(180deg)}.langlist{width:auto;margin:1.6rem 0;text-align:left}.langlist-others{font-weight:700;text-align:center}.hlist ul{margin:0;padding:0}.hlist li,.hlist ul ul{display:inline}.hlist li:before{content:" Â· ";font-weight:700}.hlist li:first-child:before{content:none}.hlist li>ul:before{content:"\00a0("}.hlist li>ul:after{content:") "}.langlist>ul{-webkit-column-width:11.2rem;-moz-column-width:11.2rem;column-width:11.2rem}.langlist>ul>li{display:block;line-height:1.7;-webkit-column-break-inside:avoid;page-break-inside:avoid;break-inside:avoid}.no-js .langlist>ul{text-align:center;list-style-type:circle}.no-js .langlist>ul>li{display:inline-block;padding:0 .8rem}.langlist>ul>li:before{content:none}.langlist>ul>li a{white-space:normal}@media (max-width:480px){.langlist{font-size:inherit}.langlist a{word-wrap:break-word;white-space:normal}.lang-list-container{width:auto;margin-left:.8rem;margin-right:.8rem}.bookshelf{overflow:visible}}.bookshelf{display:block;border-top:1px solid #c8ccd1;-webkit-box-shadow:0 -1px 0 #fff;-moz-box-shadow:0 -1px 0 #fff;box-shadow:0 -1px 0 #fff;text-align:center;white-space:nowrap}.bookshelf .text{background-color:#f8f9fa;position:relative;top:-11.2px;top:-1.12rem;font-weight:400;padding:0 .8rem}.bookshelf-container{display:block;overflow:visible;width:100%;height:1px;margin:2.4rem 0 1.6rem;font-size:13px;font-size:1.3rem;font-weight:700;line-height:1.5}@media (max-width:480px){.bookshelf{width:auto;left:auto}.bookshelf-container{text-align:left;width:auto}}.app-badges .footer-sidebar-content{background-color:#f8f9fa}.app-badges .footer-sidebar-text{padding-top:.8rem;padding-bottom:.8rem}.app-badges .sprite.footer-sidebar-icon{top:8px;top:.8rem}.app-badges ul{margin:0;padding:0;list-style-type:none}.app-badge{display:inline-block}.app-badge a{color:transparent}@media screen and (max-width:768px){.app-badges .footer-sidebar-content{text-align:center}.app-badges .sprite.footer-sidebar-icon{display:inline-block;position:relative;margin:0;top:-3px;left:0;vertical-align:middle;-webkit-transform:scale(.7);-moz-transform:scale(.7);-ms-transform:scale(.7);transform:scale(.7)}}.footer{overflow:hidden;max-width:100%;margin:0 auto;padding:4.16rem 1.28rem 0;font-size:13px;font-size:1.3rem}.footer:after,.footer:before{content:" ";display:table}.footer:after{clear:both}.footer-sidebar{width:35%;float:left;clear:left;margin-bottom:3.2rem;vertical-align:top}.footer-sidebar-content{position:relative;max-width:350px;margin:0 auto}.sprite.footer-sidebar-icon{position:absolute;top:0;left:8px;left:.8rem}.footer-sidebar-text{position:relative;margin:0;padding-left:6rem;padding-right:2rem;color:#54595d}.site-license{color:#54595d;text-align:center}.site-license small:after{content:"\2022";display:inline-block;font-size:13px;font-size:1.3rem;line-height:inherit;margin-left:.8rem;margin-right:.5rem}.site-license small:last-child:after{display:none}.footer hr{margin-top:1.28rem}@media screen and (max-width:768px){.footer{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;-moz-box-orient:vertical;-moz-box-direction:normal;-ms-flex-direction:column;flex-direction:column;padding-top:1.28rem}.footer .footer-sidebar{-webkit-box-ordinal-group:1;-moz-box-ordinal-group:1;-webkit-order:1;-ms-flex-order:1;order:1}.footer .other-projects{-webkit-box-ordinal-group:2;-moz-box-ordinal-group:2;-webkit-order:2;-ms-flex-order:2;order:2}.footer .app-badges{-webkit-box-ordinal-group:3;-moz-box-ordinal-group:3;-webkit-order:3;-ms-flex-order:3;order:3}.footer hr{-webkit-box-ordinal-group:4;-moz-box-ordinal-group:4;-webkit-order:4;-ms-flex-order:4;order:4}.footer .site-license{-webkit-box-ordinal-group:5;-moz-box-ordinal-group:5;-webkit-order:5;-ms-flex-order:5;order:5}.footer-sidebar{width:100%}.sprite.footer-sidebar-icon{display:block;position:relative;left:0;margin:0 auto 1.28rem}.footer-sidebar-content{max-width:none}.footer-sidebar-text{margin:0;padding:0;text-align:center}}@media screen and (max-width:480px){.footer{padding:.96rem .64rem 1.28rem}}@media (max-width:480px){.search-container{margin-top:0;height:78px;height:7.8rem;position:absolute;top:96px;top:9.6rem;left:0;right:0;max-width:100%;width:auto;padding:0;text-align:left}.search-container label{display:none}.search-form #searchInput{max-width:40%;vertical-align:middle}.search-form .formBtn{max-width:25%;vertical-align:middle}form fieldset{margin:0;border-left:0;border-right:0}hr{margin-top:.65rem}}@media (-o-min-device-pixel-ratio:2/1),(-webkit-min-device-pixel-ratio:2),(min--moz-device-pixel-ratio:2),(min-resolution:2dppx),(min-resolution:192dpi){hr{border-bottom-width:.5px}}@supports (-webkit-marquee-style:slide){hr{border-bottom-width:1px}}.js-enabled .central-featured,.js-enabled .jsl10n{opacity:0}.jsl10n-visible .central-featured,.jsl10n-visible .jsl10n{opacity:1}@media print{body{background-color:transparent}a{color:#000!important;background:none!important;padding:0!important}a:link,a:visited{color:#520;background:transparent}img{border:0}}body{overflow-x:hidden}.banner,.banner *{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}.banner{display:none;position:relative;z-index:3}.banner.banner--visible{display:block}.banner__close{position:absolute;margin-top:-24px;margin-right:-24px;padding:12px;top:0;right:0;cursor:pointer;background:none;border:0}.banner__button{display:inline-block;border:1px solid;-moz-border-radius:2px;border-radius:2px;padding:8px 12px;cursor:pointer;font-weight:700;white-space:nowrap;line-height:1;margin-top:8px}.banner__button,.banner__button:hover{text-decoration:none}.overlay-banner-main{max-width:500px;position:fixed;right:10px;bottom:20px;background:#fff;-moz-border-radius:10px 10px 0 0;border-radius:10px 10px 0 0;width:-webkit-calc(100% - 20px);width:-moz-calc(100% - 20px);width:calc(100% - 20px);padding:0 8px 8px;height:80vh;border:1px solid #a2a9b1;-webkit-box-shadow:0 0 15px rgba(50,50,50,.25);-moz-box-shadow:0 0 15px rgba(50,50,50,.25);box-shadow:0 0 15px rgba(50,50,50,.25);-webkit-transition:all .15s ease-in-out;-o-transition:all .15s ease-in-out;-moz-transition:all .15s ease-in-out;transition:all .15s ease-in-out;-webkit-transform-origin:100% 50%;-moz-transform-origin:100% 50%;-ms-transform-origin:100% 50%;transform-origin:100% 50%;-webkit-transform:scale(.5);-moz-transform:scale(.5);-ms-transform:scale(.5);transform:scale(.5);visibility:hidden;opacity:0}body.overlay-banner-open .overlay-banner-main{visibility:visible;opacity:1;-webkit-transform:scale(1);-moz-transform:scale(1);-ms-transform:scale(1);transform:scale(1)}.overlay-banner-main-scroll{padding-bottom:16px;max-height:-webkit-calc(100% - 42px);max-height:-moz-calc(100% - 42px);max-height:calc(100% - 42px);overflow-y:auto;overflow-x:hidden;-webkit-transition:max-height .5s;-o-transition:max-height .5s;-moz-transition:max-height .5s;transition:max-height .5s}.overlay-banner-main .frb-header-minimize{top:-48px;position:absolute;right:10px;background:#000;background:rgba(0,0,0,.75);-moz-border-radius:12px 12px 0 0;border-radius:12px 12px 0 0;padding:6px 12px;color:#fff;font-weight:700;text-align:center;font-size:16px;cursor:pointer;width:48px;height:48px}.overlay-banner-main .frb-header-minimize,.overlay-banner-main .frb-header-minimize-icon{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center}.overlay-banner-main .frb-header-minimize-icon{width:40px;height:40px;-moz-border-radius:2px;border-radius:2px;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center}.overlay-banner-main .frb-header-minimize-icon svg{filter:url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg"><filter id="filter"><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="1 0" /><feFuncG type="table" tableValues="1 0" /><feFuncB type="table" tableValues="1 0" /></feComponentTransfer></filter></svg>#filter');-webkit-filter:invert(1);filter:invert(1);width:25px;height:auto;margin-left:-2px}.overlay-banner-main-header{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;width:100%;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center}.overlay-banner-main-header a{-webkit-box-flex:1;-webkit-flex:1 0 auto;-moz-box-flex:1;-ms-flex:1 0 auto;flex:1 0 auto;text-align:center;padding:11px 6px;border:0;background:transparent;color:#36c;font-weight:700;position:relative}.overlay-banner-main-header a:hover{text-decoration:underline;cursor:pointer}.overlay-banner-main-message{position:relative;clear:both;margin-bottom:12px;padding:10px 15px;background-color:#308557;color:#fff;-moz-border-radius:1.5em;border-radius:1.5em;font-size:16px;line-height:1.5}@media (min-width:720px){.overlay-banner-main-message{padding:12px 20px;font-size:17px;line-height:1.5294117647}}.overlay-banner-main-message-greeting{font-size:1.5em;line-height:1.15;font-weight:700;text-align:center;margin-top:8px}.overlay-banner-main-message-subheading{font-size:16px;line-height:1.35;font-weight:700;text-align:center;margin-top:8px;margin-bottom:16px}.overlay-banner-main-message p{font-size:inherit!important;line-height:inherit!important;margin-bottom:16px}.overlay-banner-main .button-grid{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-column-gap:1%;-moz-column-gap:1%;column-gap:1%;row-gap:5px}.overlay-banner-main .banner-button,.overlay-banner-main .button-grid{width:100%;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex}.overlay-banner-main .banner-button{-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;height:54px;color:#36c;background-color:#f8f9fa;-moz-border-radius:10px;border-radius:10px;border:1px solid #a2a9b1;text-align:center;cursor:pointer;-webkit-transition:all .2s ease;-o-transition:all .2s ease;-moz-transition:all .2s ease;transition:all .2s ease;font-weight:700;padding:5px 6px;line-height:1}.overlay-banner-main .banner-button:focus,.overlay-banner-main .banner-button:focus-within{border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;-moz-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff}.overlay-banner-main .button-33{-webkit-box-flex:0;-webkit-flex:0 1 32%;-moz-box-flex:0;-ms-flex:0 1 32%;flex:0 1 32%;max-width:32%}.overlay-banner-main .button-67{-webkit-box-flex:0;-webkit-flex:0 1 65%;-moz-box-flex:0;-ms-flex:0 1 65%;flex:0 1 65%;max-width:65%}.overlay-banner-main .button-50{-webkit-box-flex:0;-webkit-flex:0 1 49%;-moz-box-flex:0;-ms-flex:0 1 49%;flex:0 1 49%;max-width:49%}.overlay-banner-main .button-center{margin:0 auto}.overlay-banner-main .button-collapse{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;width:auto;height:54px;color:#000;font-weight:700;background:transparent;border:0;text-transform:uppercase;margin-top:15px;cursor:pointer}.overlay-banner-main .button-collapse:hover{text-decoration:underline}.overlay-banner-main .banner-button-disabled{opacity:.5;color:#a2a9b1}.overlay-banner-main .banner-button.selected{background-color:#36c;border-color:#2a4b8d;color:#fff}.overlay-banner-main-amounts,.overlay-banner-main-frequency{position:relative;background-color:#dbf3ec;padding:15px;-moz-border-radius:1.5em;border-radius:1.5em;margin-bottom:10px}.overlay-banner-main-amounts .error-highlight,.overlay-banner-main-frequency .error-highlight{font-weight:500}.overlay-banner-main-amounts .button-grid,.overlay-banner-main-frequency .button-grid{padding:18px 0 10px}.overlay-banner-main-footer-cta{margin:8px 0;background-color:#f9dde9;color:#000;padding:10px 18px;font-size:16px;line-height:1.5;-moz-border-radius:1.5em;border-radius:1.5em}.frb-message-icon circle{fill:#b32424}.frb-message-icon path{fill:#fff}.overlay-banner-main-footer-identity{position:relative;clear:both;margin:20px 0 0;color:#000;-moz-border-radius:1.5em;border-radius:1.5em;line-height:1.3;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;padding:0 10px}.overlay-banner-main-footer-identity img{width:100%;max-width:110px;margin-right:10px}.overlay-banner-mini{position:fixed;right:0;left:0;bottom:-500px;z-index:9999;background:#308557;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-pack:start;-webkit-justify-content:flex-start;-moz-box-pack:start;-ms-flex-pack:start;justify-content:flex-start;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;border-top:2px solid #266a46;-webkit-box-shadow:0 -2px 10px 0 rgba(0,0,0,.25);-moz-box-shadow:0 -2px 10px 0 rgba(0,0,0,.25);box-shadow:0 -2px 10px 0 rgba(0,0,0,.25);-webkit-transition:all .3s ease;-o-transition:all .3s ease;-moz-transition:all .3s ease;transition:all .3s ease}.overlay-banner-mini.visible{bottom:-20px;right:0;left:0}.overlay-banner-mini .frb-conversation-close,.overlay-banner-mini .frb-conversation-open{top:-50px;position:absolute;right:10px;background:#000;background:rgba(0,0,0,.75);-moz-border-radius:12px 12px 0 0;border-radius:12px 12px 0 0;padding:6px 12px;color:#fff;font-weight:700;text-align:center;font-size:16px;display:none;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;cursor:pointer;width:48px;height:48px}.overlay-banner-mini .frb-conversation-open{right:60px}span.frb-conversation-close-icon:after,span.frb-conversation-close-icon:before{position:absolute;left:50%;top:12px;-webkit-transform:translateX(-50%);-moz-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);content:" ";height:25px;width:3px;margin-left:-1px;background-color:#fff}span.frb-conversation-close-icon:before{-webkit-transform:rotate(45deg);-moz-transform:rotate(45deg);-ms-transform:rotate(45deg);transform:rotate(45deg)}span.frb-conversation-close-icon:after{-webkit-transform:rotate(-45deg);-moz-transform:rotate(-45deg);-ms-transform:rotate(-45deg);transform:rotate(-45deg)}.frb-conversation-open-icon{width:40px;height:40px;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-moz-border-radius:2px;border-radius:2px;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center}.frb-conversation-open-icon svg{-webkit-transform:rotate(180deg);-moz-transform:rotate(180deg);-ms-transform:rotate(180deg);transform:rotate(180deg);filter:url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg"><filter id="filter"><feComponentTransfer color-interpolation-filters="sRGB"><feFuncR type="table" tableValues="1 0" /><feFuncG type="table" tableValues="1 0" /><feFuncB type="table" tableValues="1 0" /></feComponentTransfer></filter></svg>#filter');-webkit-filter:invert(1);filter:invert(1);width:25px;height:auto}.overlay-banner-mini-message,.overlay-banner-mini.visible .frb-conversation-close,.overlay-banner-mini.visible .frb-conversation-open{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex}.overlay-banner-mini-message{-webkit-box-align:center;-webkit-align-items:center;-moz-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-moz-box-pack:center;-ms-flex-pack:center;justify-content:center;width:100%;padding:20px 20px 30px;cursor:pointer}.overlay-banner-mini-message-text{-webkit-box-flex:0;-webkit-flex:0 1 1200px;-moz-box-flex:0;-ms-flex:0 1 1200px;flex:0 1 1200px;max-width:1200px}@media (max-width:960px){.overlay-banner-mini-message{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap}.overlay-banner-mini-message-text{margin-bottom:10px}.overlay-banner-mini-message-actions,.overlay-banner-mini-message-text{-webkit-box-flex:0;-webkit-flex:0 0 100%;-moz-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}}.overlay-banner-mini-message h3{color:#fff;margin:0 0 5px;font-size:24px;font-family:Montserrat,Helvetica Neue,Helvetica,Arial,sans-serif}.overlay-banner-mini-message p{display:block;color:#fff;position:relative;margin:0 13px 5px 0;font-size:17px}.overlay-banner-mini .frb-message-icon{position:relative;top:0;margin-right:3px;-webkit-box-flex:0;-webkit-flex:0 0 30px;-moz-box-flex:0;-ms-flex:0 0 30px;flex:0 0 30px}.overlay-banner-mini .frb-message-icon circle{fill:#f0bc00}.overlay-banner-mini .frb-message-icon path{fill:#000}.overlay-banner-mini .frb-submit{position:relative;display:inline-block;padding:10px 15px;margin:0;width:240px;background-color:#f0bc00;border-color:#f0bc00;color:#000;-moz-border-radius:2px;border-radius:2px;text-align:center;font-weight:700;font-size:20px;cursor:pointer;-webkit-transition:background-color .5s ease;-o-transition:background-color .5s ease;-moz-transition:background-color .5s ease;transition:background-color .5s ease}.overlay-banner-mini .frb-submit:hover{background:#71d1b3;border-color:#71d1b3}.overlay-banner-mini .frb-submit:focus{border-color:#36c;-webkit-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;-moz-box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff}@media (max-width:660px){.overlay-banner-mini-message h3{font-size:20px}.overlay-banner-mini-message p{font-size:13px}.overlay-banner-mini .frb-submit{width:100%}}.sr-only{border:0!important;clip:rect(1px,1px,1px,1px)!important;-webkit-clip-path:inset(50%)!important;clip-path:inset(50%)!important;height:1px!important;margin:-1px!important;overflow:hidden!important;padding:0!important;position:absolute!important;width:1px!important;white-space:nowrap!important}
      </style>
      <link href="//upload.wikimedia.org" rel="preconnect"/>
      <link href="https://wikis.world/@wikipedia" rel="me"/>
      <meta content="" property="og:url"/>
      <meta content="Wikipedia, the free encyclopedia" property="og:title"/>
      <meta content="website" property="og:type"/>
      <meta content="Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation." property="og:description"/>
      <meta content="https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png" property="og:image"/>
     </head>
     <body id="www-wikipedia-org">
      <main>
       <div class="central-textlogo">
        <img alt="" class="central-featured-logo" height="183" src="portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png" srcset="portal/wikipedia.org/assets/img/Wikipedia-logo-v2@1.5x.png 1.5x, portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png 2x" width="200"/>
        <h1 class="central-textlogo-wrapper">
         <span class="central-textlogo__image sprite svg-Wikipedia_wordmark">
          Wikipedia
         </span>
         <strong class="jsl10n localized-slogan" data-jsl10n="portal.slogan">
          The Free Encyclopedia
         </strong>
        </h1>
       </div>
       <nav aria-label="Top languages" class="central-featured" data-el-section="primary links" data-jsl10n="top-ten-nav-label">
        <!-- #1. en.wikipedia.org - 1,687,212,000 views/day -->
        <div class="central-featured-lang lang1" dir="ltr" lang="en">
         <a class="link-box" data-slogan="The Free Encyclopedia" href="//en.wikipedia.org/" id="js-link-box-en" title="English â Wikipedia â The Free Encyclopedia">
          <strong>
           English
          </strong>
          <small>
           6,918,000+
           <span>
            articles
           </span>
          </small>
         </a>
        </div>
        <!-- #2. ru.wikipedia.org - 204,861,000 views/day -->
        <div class="central-featured-lang lang2" dir="ltr" lang="ru">
         <a class="link-box" data-slogan="Ð¡Ð²Ð¾Ð±Ð¾Ð´Ð½Ð°Ñ ÑÐ½ÑÐ¸ÐºÐ»Ð¾Ð¿ÐµÐ´Ð¸Ñ" href="//ru.wikipedia.org/" id="js-link-box-ru" title="Russkiy â ÐÐ¸ÐºÐ¸Ð¿ÐµÐ´Ð¸Ñ â Ð¡Ð²Ð¾Ð±Ð¾Ð´Ð½Ð°Ñ ÑÐ½ÑÐ¸ÐºÐ»Ð¾Ð¿ÐµÐ´Ð¸Ñ">
          <strong>
           Ð ÑÑÑÐºÐ¸Ð¹
          </strong>
          <small>
           2Â 012Â 000+
           <span>
            ÑÑÐ°ÑÐµÐ¹
           </span>
          </small>
         </a>
        </div>
        <!-- #3. ja.wikipedia.org - 203,232,000 views/day -->
        <div class="central-featured-lang lang3" dir="ltr" lang="ja">
         <a class="link-box" data-slogan="ããªã¼ç¾ç§äºå¸" href="//ja.wikipedia.org/" id="js-link-box-ja" title="Nihongo â ã¦ã£ã­ããã£ã¢ â ããªã¼ç¾ç§äºå¸">
          <strong>
           æ¥æ¬èª
          </strong>
          <small>
           1,438,000+
           <span>
            è¨äº
           </span>
          </small>
         </a>
        </div>
        <!-- #4. de.wikipedia.org - 174,277,000 views/day -->
        <div class="central-featured-lang lang4" dir="ltr" lang="de">
         <a class="link-box" data-slogan="Die freie EnzyklopÃ¤die" href="//de.wikipedia.org/" id="js-link-box-de" title="Deutsch â Wikipedia â Die freie EnzyklopÃ¤die">
          <strong>
           Deutsch
          </strong>
          <small>
           2.964.000+
           <span>
            Artikel
           </span>
          </small>
         </a>
        </div>
        <!-- #5. fr.wikipedia.org - 172,274,000 views/day -->
        <div class="central-featured-lang lang5" dir="ltr" lang="fr">
         <a class="link-box" data-slogan="LâencyclopÃ©die libre" href="//fr.wikipedia.org/" id="js-link-box-fr" title="franÃ§ais â WikipÃ©dia â LâencyclopÃ©die libre">
          <strong>
           FranÃ§ais
          </strong>
          <small>
           2â¯650â¯000+
           <span>
            articles
           </span>
          </small>
         </a>
        </div>
        <!-- #6. es.wikipedia.org - 167,709,000 views/day -->
        <div class="central-featured-lang lang6" dir="ltr" lang="es">
         <a class="link-box" data-slogan="La enciclopedia libre" href="//es.wikipedia.org/" id="js-link-box-es" title="EspaÃ±ol â Wikipedia â La enciclopedia libre">
          <strong>
           EspaÃ±ol
          </strong>
          <small>
           1.992.000+
           <span>
            artÃ­culos
           </span>
          </small>
         </a>
        </div>
        <!-- #7. it.wikipedia.org - 99,760,000 views/day -->
        <div class="central-featured-lang lang7" dir="ltr" lang="it">
         <a class="link-box" data-slogan="L'enciclopedia libera" href="//it.wikipedia.org/" id="js-link-box-it" title="Italiano â Wikipedia â L'enciclopedia libera">
          <strong>
           Italiano
          </strong>
          <small>
           1.893.000+
           <span>
            voci
           </span>
          </small>
         </a>
        </div>
        <!-- #8. zh.wikipedia.org - 97,847,000 views/day -->
        <div class="central-featured-lang lang8" dir="ltr" lang="zh">
         <a class="link-box localize-variant" data-slogan="èªç±çç¾ç§å¨ä¹¦ / èªç±çç¾ç§å¨æ¸" href="//zh.wikipedia.org/" id="js-link-box-zh" title="ZhÅngwÃ©n â ç»´åºç¾ç§ / ç¶­åºç¾ç§ â èªç±çç¾ç§å¨ä¹¦ / èªç±çç¾ç§å¨æ¸">
          <strong>
           ä¸­æ
          </strong>
          <small>
           1,452,000+
           <span>
            æ¡ç® / æ¢ç®
           </span>
          </small>
         </a>
        </div>
        <!-- #9. fa.wikipedia.org - 56,140,000 views/day -->
        <div class="central-featured-lang lang9" dir="rtl" lang="fa">
         <a class="link-box" data-slogan="Ø¯Ø§ÙØ´ÙØ§ÙÙÙ Ø¢Ø²Ø§Ø¯" href="//fa.wikipedia.org/" id="js-link-box-fa" title="FÄrsi â ÙÛÚ©ÛâÙ¾Ø¯ÛØ§ â Ø¯Ø§ÙØ´ÙØ§ÙÙÙ Ø¢Ø²Ø§Ø¯">
          <strong>
           <bdi dir="rtl">
            ÙØ§Ø±Ø³Û
           </bdi>
          </strong>
          <small>
           Û±Ù¬Û°Û²Û°Ù¬Û°Û°Û°+
           <span>
            ÙÙØ§ÙÙ
           </span>
          </small>
         </a>
        </div>
        <!-- #10. pt.wikipedia.org - 53,221,000 views/day -->
        <div class="central-featured-lang lang10" dir="ltr" lang="pt">
         <a class="link-box" data-slogan="A enciclopÃ©dia livre" href="//pt.wikipedia.org/" id="js-link-box-pt" title="PortuguÃªs â WikipÃ©dia â A enciclopÃ©dia livre">
          <strong>
           PortuguÃªs
          </strong>
          <small>
           1.138.000+
           <span>
            artigos
           </span>
          </small>
         </a>
        </div>
       </nav>
       <div class="search-container" role="search">
        <form action="//www.wikipedia.org/search-redirect.php" class="pure-form" data-el-section="search" id="search-form">
         <fieldset>
          <input name="family" type="hidden" value="Wikipedia"/>
          <input id="hiddenLanguageInput" name="language" type="hidden" value="en"/>
          <div class="search-input" id="search-input">
           <label class="screen-reader-text" data-jsl10n="portal.search-input-label" for="searchInput">
            Search Wikipedia
           </label>
           <input accesskey="F" autocomplete="off" autofocus="autofocus" dir="auto" id="searchInput" name="search" size="20" type="search"/>
           <div class="styled-select no-js">
            <div class="hide-arrow">
             <select id="searchLanguage" name="language">
              <option lang="af" value="af">
               Afrikaans
              </option>
              <!-- Afrikaans -->
              <option lang="ar" value="ar">
               Ø§ÙØ¹Ø±Ø¨ÙØ©
              </option>
              <!-- Al-Ê¿ArabÄ«yah -->
              <option lang="ast" value="ast">
               Asturianu
              </option>
              <option lang="az" value="az">
               AzÉrbaycanca
              </option>
              <!-- AzÉrbaycanca -->
              <option lang="bg" value="bg">
               ÐÑÐ»Ð³Ð°ÑÑÐºÐ¸
              </option>
              <!-- BÇlgarski -->
              <option lang="nan" value="nan">
               é©åèª / BÃ¢n-lÃ¢m-gÃº
              </option>
              <!-- BÃ¢n-lÃ¢m-gÃº -->
              <option lang="bn" value="bn">
               à¦¬à¦¾à¦à¦²à¦¾
              </option>
              <!-- Bangla -->
              <option lang="be" value="be">
               ÐÐµÐ»Ð°ÑÑÑÐºÐ°Ñ
              </option>
              <!-- Belaruskaya -->
              <option lang="ca" value="ca">
               CatalÃ
              </option>
              <option lang="cs" value="cs">
               ÄeÅ¡tina
              </option>
              <!-- ÄeÅ¡tina -->
              <option lang="cy" value="cy">
               Cymraeg
              </option>
              <!-- Cymraeg -->
              <option lang="da" value="da">
               Dansk
              </option>
              <option lang="de" value="de">
               Deutsch
              </option>
              <option lang="et" value="et">
               Eesti
              </option>
              <option lang="el" value="el">
               ÎÎ»Î»Î·Î½Î¹ÎºÎ¬
              </option>
              <!-- EllÄ«nikÃ¡ -->
              <option lang="en" selected="selected" value="en">
               English
              </option>
              <!-- English -->
              <option lang="es" value="es">
               EspaÃ±ol
              </option>
              <option lang="eo" value="eo">
               Esperanto
              </option>
              <option lang="eu" value="eu">
               Euskara
              </option>
              <option lang="fa" value="fa">
               ÙØ§Ø±Ø³Û
              </option>
              <!-- FÄrsi -->
              <option lang="fr" value="fr">
               FranÃ§ais
              </option>
              <!-- franÃ§ais -->
              <option lang="gl" value="gl">
               Galego
              </option>
              <option lang="ko" value="ko">
               íêµ­ì´
              </option>
              <!-- Hangugeo -->
              <option lang="hy" value="hy">
               ÕÕ¡ÕµÕ¥ÖÕ¥Õ¶
              </option>
              <!-- Hayeren -->
              <option lang="hi" value="hi">
               à¤¹à¤¿à¤¨à¥à¤¦à¥
              </option>
              <!-- HindÄ« -->
              <option lang="hr" value="hr">
               Hrvatski
              </option>
              <option lang="id" value="id">
               Bahasa Indonesia
              </option>
              <option lang="it" value="it">
               Italiano
              </option>
              <option lang="he" value="he">
               ×¢××¨××ª
              </option>
              <!-- Ivrit -->
              <option lang="ka" value="ka">
               á¥áá áá£áá
              </option>
              <!-- Kartuli -->
              <option lang="lld" value="lld">
               Ladin
              </option>
              <option lang="la" value="la">
               Latina
              </option>
              <option lang="lv" value="lv">
               LatvieÅ¡u
              </option>
              <option lang="lt" value="lt">
               LietuviÅ³
              </option>
              <option lang="hu" value="hu">
               Magyar
              </option>
              <option lang="mk" value="mk">
               ÐÐ°ÐºÐµÐ´Ð¾Ð½ÑÐºÐ¸
              </option>
              <!-- Makedonski -->
              <option lang="arz" value="arz">
               ÙØµØ±Ù
              </option>
              <!-- Maá¹£rÄ« -->
              <option lang="ms" value="ms">
               Bahasa Melayu
              </option>
              <!-- Bahasa Melayu -->
              <option lang="min" value="min">
               Bahaso Minangkabau
              </option>
              <option lang="my" value="my">
               áá¼ááºáá¬áá¬áá¬
              </option>
              <!-- Myanmarsar -->
              <option lang="nl" value="nl">
               Nederlands
              </option>
              <option lang="ja" value="ja">
               æ¥æ¬èª
              </option>
              <!-- Nihongo -->
              <option lang="nb" value="no">
               Norsk (bokmÃ¥l)
              </option>
              <option lang="nn" value="nn">
               Norsk (nynorsk)
              </option>
              <option lang="ce" value="ce">
               ÐÐ¾ÑÑÐ¸Ð¹Ð½
              </option>
              <!-- NoxÃ§iyn -->
              <option lang="uz" value="uz">
               OÊ»zbekcha / ÐÐ·Ð±ÐµÐºÑÐ°
              </option>
              <!-- OÊ»zbekcha -->
              <option lang="pl" value="pl">
               Polski
              </option>
              <option lang="pt" value="pt">
               PortuguÃªs
              </option>
              <option lang="kk" value="kk">
               ÒÐ°Ð·Ð°ÒÑÐ° / QazaqÅa / ÙØ§Ø²Ø§ÙØ´Ø§
              </option>
              <option lang="ro" value="ro">
               RomÃ¢nÄ
              </option>
              <!-- RomÃ¢nÄ -->
              <option lang="sq" value="sq">
               Shqip
              </option>
              <option lang="en" value="simple">
               Simple English
              </option>
              <option lang="ceb" value="ceb">
               Sinugboanong Binisaya
              </option>
              <option lang="sk" value="sk">
               SlovenÄina
              </option>
              <option lang="sl" value="sl">
               SlovenÅ¡Äina
              </option>
              <!-- slovenÅ¡Äina -->
              <option lang="sr" value="sr">
               Ð¡ÑÐ¿ÑÐºÐ¸ / Srpski
              </option>
              <option lang="sh" value="sh">
               Srpskohrvatski / Ð¡ÑÐ¿ÑÐºÐ¾ÑÑÐ²Ð°ÑÑÐºÐ¸
              </option>
              <option lang="fi" value="fi">
               Suomi
              </option>
              <!-- suomi -->
              <option lang="sv" value="sv">
               Svenska
              </option>
              <option lang="ta" value="ta">
               à®¤à®®à®¿à®´à¯
              </option>
              <!-- Tamiá¸» -->
              <option lang="tt" value="tt">
               Ð¢Ð°ÑÐ°ÑÑÐ° / TatarÃ§a
              </option>
              <option lang="te" value="te">
               à°¤à±à°²à±à°à±
              </option>
              <!-- Telugu -->
              <option lang="th" value="th">
               à¸ à¸²à¸©à¸²à¹à¸à¸¢
              </option>
              <!-- Phasa Thai -->
              <option lang="tg" value="tg">
               Ð¢Ð¾Ò·Ð¸ÐºÓ£
              </option>
              <!-- TojikÄ« -->
              <option lang="azb" value="azb">
               ØªÛØ±Ú©Ø¬Ù
              </option>
              <!-- TÃ¼rkce -->
              <option lang="tr" value="tr">
               TÃ¼rkÃ§e
              </option>
              <!-- TÃ¼rkÃ§e -->
              <option lang="uk" value="uk">
               Ð£ÐºÑÐ°ÑÐ½ÑÑÐºÐ°
              </option>
              <!-- Ukrayinsâka -->
              <option lang="ur" value="ur">
               Ø§Ø±Ø¯Ù
              </option>
              <!-- Urdu -->
              <option lang="vi" value="vi">
               Tiáº¿ng Viá»t
              </option>
              <option lang="war" value="war">
               Winaray
              </option>
              <option lang="zh" value="zh">
               ä¸­æ
              </option>
              <!-- ZhÅngwÃ©n -->
              <option lang="ru" value="ru">
               Ð ÑÑÑÐºÐ¸Ð¹
              </option>
              <!-- Russkiy -->
              <option lang="yue" value="yue">
               ç²µèª
              </option>
             </select>
             <div class="styled-select-active-helper">
             </div>
            </div>
            <i class="sprite svg-arrow-down">
            </i>
           </div>
          </div>
          <button class="pure-button pure-button-primary-progressive" type="submit">
           <i class="sprite svg-search-icon" data-jsl10n="search-input-button">
            Search
           </i>
          </button>
          <input name="go" type="hidden" value="Go"/>
         </fieldset>
        </form>
       </div>
       <nav aria-label="All languages" data-jsl10n="all-languages-nav-label">
        <div class="lang-list-button-wrapper">
         <button aria-controls="js-lang-lists" aria-expanded="false" class="lang-list-button" id="js-lang-list-button">
          <i class="sprite svg-language-icon">
          </i>
          <span class="lang-list-button-text jsl10n" data-jsl10n="portal.language-button-text">
           Read Wikipedia in your language
          </span>
          <i class="sprite svg-arrow-down-blue">
          </i>
         </button>
        </div>
        <div class="lang-list-border">
        </div>
        <div class="lang-list-container">
         <div class="lang-list-content" id="js-lang-lists">
          <h2 class="bookshelf-container">
           <span class="bookshelf">
            <span class="text">
             <bdi dir="ltr">
              1,000,000+
             </bdi>
             <span class="jsl10n" data-jsl10n="entries">
              articles
             </span>
            </span>
           </span>
          </h2>
          <div class="langlist langlist-large hlist" data-el-section="secondary links">
           <ul>
            <li>
             <a href="//ar.wikipedia.org/" lang="ar" title="Al-Ê¿ArabÄ«yah">
              <bdi dir="rtl">
               Ø§ÙØ¹Ø±Ø¨ÙØ©
              </bdi>
             </a>
            </li>
            <li>
             <a href="//de.wikipedia.org/" lang="de">
              Deutsch
             </a>
            </li>
            <li>
             <a href="//en.wikipedia.org/" lang="en" title="English">
              English
             </a>
            </li>
            <li>
             <a href="//es.wikipedia.org/" lang="es">
              EspaÃ±ol
             </a>
            </li>
            <li>
             <a href="//fa.wikipedia.org/" lang="fa" title="FÄrsi">
              <bdi dir="rtl">
               ÙØ§Ø±Ø³Û
              </bdi>
             </a>
            </li>
            <li>
             <a href="//fr.wikipedia.org/" lang="fr" title="franÃ§ais">
              FranÃ§ais
             </a>
            </li>
            <li>
             <a href="//it.wikipedia.org/" lang="it">
              Italiano
             </a>
            </li>
            <li>
             <a href="//arz.wikipedia.org/" lang="arz" title="Maá¹£rÄ«">
              <bdi dir="rtl">
               ÙØµØ±Ù
              </bdi>
             </a>
            </li>
            <li>
             <a href="//nl.wikipedia.org/" lang="nl">
              Nederlands
             </a>
            </li>
            <li>
             <a href="//ja.wikipedia.org/" lang="ja" title="Nihongo">
              æ¥æ¬èª
             </a>
            </li>
            <li>
             <a href="//pl.wikipedia.org/" lang="pl">
              Polski
             </a>
            </li>
            <li>
             <a href="//pt.wikipedia.org/" lang="pt">
              PortuguÃªs
             </a>
            </li>
            <li>
             <a href="//ceb.wikipedia.org/" lang="ceb">
              Sinugboanong Binisaya
             </a>
            </li>
            <li>
             <a href="//sv.wikipedia.org/" lang="sv">
              Svenska
             </a>
            </li>
            <li>
             <a href="//uk.wikipedia.org/" lang="uk" title="Ukrayinsâka">
              Ð£ÐºÑÐ°ÑÐ½ÑÑÐºÐ°
             </a>
            </li>
            <li>
             <a href="//vi.wikipedia.org/" lang="vi">
              Tiáº¿ng Viá»t
             </a>
            </li>
            <li>
             <a href="//war.wikipedia.org/" lang="war">
              Winaray
             </a>
            </li>
            <li>
             <a href="//zh.wikipedia.org/" lang="zh" title="ZhÅngwÃ©n">
              ä¸­æ
             </a>
            </li>
            <li>
             <a href="//ru.wikipedia.org/" lang="ru" title="Russkiy">
              Ð ÑÑÑÐºÐ¸Ð¹
             </a>
            </li>
           </ul>
          </div>
          <h2 class="bookshelf-container">
           <span class="bookshelf">
            <span class="text">
             <bdi dir="ltr">
              100,000+
             </bdi>
             <span class="jsl10n" data-jsl10n="portal.entries">
              articles
             </span>
            </span>
           </span>
          </h2>
          <div class="langlist langlist-large hlist" data-el-section="secondary links">
           <ul>
            <li>
             <a href="//af.wikipedia.org/" lang="af" title="Afrikaans">
              Afrikaans
             </a>
            </li>
            <li>
             <a href="//ast.wikipedia.org/" lang="ast">
              Asturianu
             </a>
            </li>
            <li>
             <a href="//az.wikipedia.org/" lang="az" title="AzÉrbaycanca">
              AzÉrbaycanca
             </a>
            </li>
            <li>
             <a href="//bg.wikipedia.org/" lang="bg" title="BÇlgarski">
              ÐÑÐ»Ð³Ð°ÑÑÐºÐ¸
             </a>
            </li>
            <li>
             <a href="//zh-min-nan.wikipedia.org/" lang="nan" title="BÃ¢n-lÃ¢m-gÃº">
              é©åèª / BÃ¢n-lÃ¢m-gÃº
             </a>
            </li>
            <li>
             <a href="//bn.wikipedia.org/" lang="bn" title="Bangla">
              à¦¬à¦¾à¦à¦²à¦¾
             </a>
            </li>
            <li>
             <a href="//be.wikipedia.org/" lang="be" title="Belaruskaya">
              ÐÐµÐ»Ð°ÑÑÑÐºÐ°Ñ
             </a>
            </li>
            <li>
             <a href="//ca.wikipedia.org/" lang="ca">
              CatalÃ
             </a>
            </li>
            <li>
             <a href="//cs.wikipedia.org/" lang="cs" title="ÄeÅ¡tina">
              ÄeÅ¡tina
             </a>
            </li>
            <li>
             <a href="//cy.wikipedia.org/" lang="cy" title="Cymraeg">
              Cymraeg
             </a>
            </li>
            <li>
             <a href="//da.wikipedia.org/" lang="da">
              Dansk
             </a>
            </li>
            <li>
             <a href="//et.wikipedia.org/" lang="et">
              Eesti
             </a>
            </li>
            <li>
             <a href="//el.wikipedia.org/" lang="el" title="EllÄ«nikÃ¡">
              ÎÎ»Î»Î·Î½Î¹ÎºÎ¬
             </a>
            </li>
            <li>
             <a href="//eo.wikipedia.org/" lang="eo">
              Esperanto
             </a>
            </li>
            <li>
             <a href="//eu.wikipedia.org/" lang="eu">
              Euskara
             </a>
            </li>
            <li>
             <a href="//gl.wikipedia.org/" lang="gl">
              Galego
             </a>
            </li>
            <li>
             <a href="//ko.wikipedia.org/" lang="ko" title="Hangugeo">
              íêµ­ì´
             </a>
            </li>
            <li>
             <a href="//hy.wikipedia.org/" lang="hy" title="Hayeren">
              ÕÕ¡ÕµÕ¥ÖÕ¥Õ¶
             </a>
            </li>
            <li>
             <a href="//hi.wikipedia.org/" lang="hi" title="HindÄ«">
              à¤¹à¤¿à¤¨à¥à¤¦à¥
             </a>
            </li>
            <li>
             <a href="//hr.wikipedia.org/" lang="hr">
              Hrvatski
             </a>
            </li>
            <li>
             <a href="//id.wikipedia.org/" lang="id">
              Bahasa Indonesia
             </a>
            </li>
            <li>
             <a href="//he.wikipedia.org/" lang="he" title="Ivrit">
              <bdi dir="rtl">
               ×¢××¨××ª
              </bdi>
             </a>
            </li>
            <li>
             <a href="//ka.wikipedia.org/" lang="ka" title="Kartuli">
              á¥áá áá£áá
             </a>
            </li>
            <li>
             <a href="//lld.wikipedia.org/" lang="lld">
              Ladin
             </a>
            </li>
            <li>
             <a href="//la.wikipedia.org/" lang="la">
              Latina
             </a>
            </li>
            <li>
             <a href="//lv.wikipedia.org/" lang="lv">
              LatvieÅ¡u
             </a>
            </li>
            <li>
             <a href="//lt.wikipedia.org/" lang="lt">
              LietuviÅ³
             </a>
            </li>
            <li>
             <a href="//hu.wikipedia.org/" lang="hu">
              Magyar
             </a>
            </li>
            <li>
             <a href="//mk.wikipedia.org/" lang="mk" title="Makedonski">
              ÐÐ°ÐºÐµÐ´Ð¾Ð½ÑÐºÐ¸
             </a>
            </li>
            <li>
             <a href="//ms.wikipedia.org/" lang="ms" title="Bahasa Melayu">
              Bahasa Melayu
             </a>
            </li>
            <li>
             <a href="//min.wikipedia.org/" lang="min">
              Bahaso Minangkabau
             </a>
            </li>
            <li>
             <a href="//my.wikipedia.org/" lang="my" title="Myanmarsar">
              áá¼ááºáá¬áá¬áá¬
             </a>
            </li>
            <li lang="no">
             Norsk
             <ul>
              <li>
               <a href="//no.wikipedia.org/" lang="nb">
                bokmÃ¥l
               </a>
              </li>
              <li>
               <a href="//nn.wikipedia.org/" lang="nn">
                nynorsk
               </a>
              </li>
             </ul>
            </li>
            <li>
             <a href="//ce.wikipedia.org/" lang="ce" title="NoxÃ§iyn">
              ÐÐ¾ÑÑÐ¸Ð¹Ð½
             </a>
            </li>
            <li>
             <a href="//uz.wikipedia.org/" lang="uz" title="OÊ»zbekcha">
              OÊ»zbekcha / ÐÐ·Ð±ÐµÐºÑÐ°
             </a>
            </li>
            <li>
             <a href="//kk.wikipedia.org/" lang="kk">
              <span lang="kk-Cyrl">
               ÒÐ°Ð·Ð°ÒÑÐ°
              </span>
              /
              <span lang="kk-Latn">
               QazaqÅa
              </span>
              /
              <bdi dir="rtl" lang="kk-Arab">
               ÙØ§Ø²Ø§ÙØ´Ø§
              </bdi>
             </a>
            </li>
            <li>
             <a href="//ro.wikipedia.org/" lang="ro" title="RomÃ¢nÄ">
              RomÃ¢nÄ
             </a>
            </li>
            <li>
             <a href="//sq.wikipedia.org/" lang="sq">
              Shqip
             </a>
            </li>
            <li>
             <a href="//simple.wikipedia.org/" lang="en">
              Simple English
             </a>
            </li>
            <li>
             <a href="//sk.wikipedia.org/" lang="sk">
              SlovenÄina
             </a>
            </li>
            <li>
             <a href="//sl.wikipedia.org/" lang="sl" title="slovenÅ¡Äina">
              SlovenÅ¡Äina
             </a>
            </li>
            <li>
             <a href="//sr.wikipedia.org/" lang="sr">
              Ð¡ÑÐ¿ÑÐºÐ¸ / Srpski
             </a>
            </li>
            <li>
             <a href="//sh.wikipedia.org/" lang="sh">
              Srpskohrvatski / Ð¡ÑÐ¿ÑÐºÐ¾ÑÑÐ²Ð°ÑÑÐºÐ¸
             </a>
            </li>
            <li>
             <a href="//fi.wikipedia.org/" lang="fi" title="suomi">
              Suomi
             </a>
            </li>
            <li>
             <a href="//ta.wikipedia.org/" lang="ta" title="Tamiá¸»">
              à®¤à®®à®¿à®´à¯
             </a>
            </li>
            <li>
             <a href="//tt.wikipedia.org/" lang="tt">
              Ð¢Ð°ÑÐ°ÑÑÐ° / TatarÃ§a
             </a>
            </li>
            <li>
             <a href="//te.wikipedia.org/" lang="te" title="Telugu">
              à°¤à±à°²à±à°à±
             </a>
            </li>
            <li>
             <a href="//th.wikipedia.org/" lang="th" title="Phasa Thai">
              à¸ à¸²à¸©à¸²à¹à¸à¸¢
             </a>
            </li>
            <li>
             <a href="//tg.wikipedia.org/" lang="tg" title="TojikÄ«">
              Ð¢Ð¾Ò·Ð¸ÐºÓ£
             </a>
            </li>
            <li>
             <a href="//azb.wikipedia.org/" lang="azb" title="TÃ¼rkce">
              <bdi dir="rtl">
               ØªÛØ±Ú©Ø¬Ù
              </bdi>
             </a>
            </li>
            <li>
             <a href="//tr.wikipedia.org/" lang="tr" title="TÃ¼rkÃ§e">
              TÃ¼rkÃ§e
             </a>
            </li>
            <li>
             <a href="//ur.wikipedia.org/" lang="ur" title="Urdu">
              <bdi dir="rtl">
               Ø§Ø±Ø¯Ù
              </bdi>
             </a>
            </li>
            <li>
             <a href="//zh-yue.wikipedia.org/" lang="yue">
              ç²µèª
             </a>
            </li>
           </ul>
          </div>
          <h2 class="bookshelf-container">
           <span class="bookshelf">
            <span class="text">
             <bdi dir="ltr">
              10,000+
             </bdi>
             <span class="jsl10n" data-jsl10n="portal.entries">
              articles
             </span>
            </span>
           </span>
          </h2>
          <div class="langlist hlist" data-el-section="secondary links">
           <ul>
            <li>
             <a href="//ace.wikipedia.org/" lang="ace">
              Bahsa AcÃ¨h
             </a>
            </li>
            <li>
             <a href="//als.wikipedia.org/" lang="gsw">
              Alemannisch
             </a>
            </li>
            <li>
             <a href="//am.wikipedia.org/" lang="am" title="ÄmariÃ±Ã±Ä">
              á áá­á
             </a>
            </li>
            <li>
             <a href="//an.wikipedia.org/" lang="an">
              AragonÃ©s
             </a>
            </li>
            <li>
             <a href="//hyw.wikipedia.org/" lang="hyw" title="Arevmdahayeren">
              Ô±ÖÕ¥ÖÕ´Õ¿Õ¡Õ°Õ¡ÕµÕ¥ÖÕ§Õ¶
             </a>
            </li>
            <li>
             <a href="//gor.wikipedia.org/" lang="gor">
              Bahasa Hulontalo
             </a>
            </li>
            <li>
             <a href="//ban.wikipedia.org/" lang="ban" title="Basa Bali">
              Basa Bali
             </a>
            </li>
            <li>
             <a href="//bjn.wikipedia.org/" lang="bjn">
              Bahasa Banjar
             </a>
            </li>
            <li>
             <a href="//map-bms.wikipedia.org/" lang="map-x-bms">
              Basa Banyumasan
             </a>
            </li>
            <li>
             <a href="//ba.wikipedia.org/" lang="ba" title="BaÅqortsa">
              ÐÐ°ÑÒ¡Ð¾ÑÑÑÐ°
             </a>
            </li>
            <li>
             <a href="//be-tarask.wikipedia.org/" lang="be-tarask" title="Bielaruskaja (taraÅ¡kievica)">
              ÐÐµÐ»Ð°ÑÑÑÐºÐ°Ñ (ÑÐ°ÑÐ°ÑÐºÐµÐ²ÑÑÐ°)
             </a>
            </li>
            <li>
             <a href="//bcl.wikipedia.org/" lang="bcl">
              Bikol Central
             </a>
            </li>
            <li>
             <a href="//bpy.wikipedia.org/" lang="bpy" title="Bishnupriya Manipuri">
              à¦¬à¦¿à¦·à§à¦£à§à¦ªà§à¦°à¦¿à¦¯à¦¼à¦¾ à¦®à¦£à¦¿à¦ªà§à¦°à§
             </a>
            </li>
            <li>
             <a href="//bar.wikipedia.org/" lang="bar">
              Boarisch
             </a>
            </li>
            <li>
             <a href="//bs.wikipedia.org/" lang="bs">
              Bosanski
             </a>
            </li>
            <li>
             <a href="//br.wikipedia.org/" lang="br">
              Brezhoneg
             </a>
            </li>
            <li>
             <a href="//cv.wikipedia.org/" lang="cv" title="ÄÄvaÅ¡la">
              Ð§ÓÐ²Ð°ÑÐ»Ð°
             </a>
            </li>
            <li>
             <a href="//dag.wikipedia.org/" lang="dag">
              Dagbanli
             </a>
            </li>
            <li>
             <a href="//ary.wikipedia.org/" lang="ary" title="Darija">
              <bdi dir="rtl">
               Ø§ÙØ¯Ø§Ø±Ø¬Ø©
              </bdi>
             </a>
            </li>
            <li>
             <a href="//nv.wikipedia.org/" lang="nv">
              DinÃ© Bizaad
             </a>
            </li>
            <li>
             <a href="//eml.wikipedia.org/" lang="roa-x-eml">
              EmigliÃ nâRumagnÃ²l
             </a>
            </li>
            <li>
             <a href="//hif.wikipedia.org/" lang="hif">
              Fiji Hindi
             </a>
            </li>
            <li>
             <a href="//fo.wikipedia.org/" lang="fo">
              FÃ¸royskt
             </a>
            </li>
            <li>
             <a href="//fy.wikipedia.org/" lang="fy">
              Frysk
             </a>
            </li>
            <li>
             <a href="//ga.wikipedia.org/" lang="ga">
              Gaeilge
             </a>
            </li>
            <li>
             <a href="//gd.wikipedia.org/" lang="gd">
              GÃ idhlig
             </a>
            </li>
            <li>
             <a href="//glk.wikipedia.org/" lang="glk" title="GilÉki">
              <bdi dir="rtl">
               Ú¯ÛÙÚ©Û
              </bdi>
             </a>
            </li>
            <li>
             <a href="//gu.wikipedia.org/" lang="gu" title="Gujarati">
              àªà«àªàª°àª¾àª¤à«
             </a>
            </li>
            <li>
             <a href="//hak.wikipedia.org/" lang="hak">
              Hak-kÃ¢-ngÃ® / å®¢å®¶èª
             </a>
            </li>
            <li>
             <a href="//ha.wikipedia.org/" lang="ha" title="Hausa">
              Hausa
             </a>
            </li>
            <li>
             <a href="//hsb.wikipedia.org/" lang="hsb">
              Hornjoserbsce
             </a>
            </li>
            <li>
             <a href="//io.wikipedia.org/" lang="io" title="Ido">
              Ido
             </a>
            </li>
            <li>
             <a href="//ig.wikipedia.org/" lang="ig">
              Igbo
             </a>
            </li>
            <li>
             <a href="//ilo.wikipedia.org/" lang="ilo">
              Ilokano
             </a>
            </li>
            <li>
             <a href="//ia.wikipedia.org/" lang="ia">
              Interlingua
             </a>
            </li>
            <li>
             <a href="//ie.wikipedia.org/" lang="ie">
              Interlingue
             </a>
            </li>
            <li>
             <a href="//os.wikipedia.org/" lang="os" title="Iron">
              ÐÑÐ¾Ð½
             </a>
            </li>
            <li>
             <a href="//is.wikipedia.org/" lang="is">
              Ãslenska
             </a>
            </li>
            <li>
             <a href="//jv.wikipedia.org/" lang="jv" title="Jawa">
              Jawa
             </a>
            </li>
            <li>
             <a href="//kn.wikipedia.org/" lang="kn" title="Kannada">
              à²à²¨à³à²¨à²¡
             </a>
            </li>
            <li>
             <a href="//pam.wikipedia.org/" lang="pam">
              Kapampangan
             </a>
            </li>
            <li>
             <a href="//km.wikipedia.org/" lang="km" title="PhÃ©asa KhmÃ©r">
              áá¶áá¶ááááá
             </a>
            </li>
            <li>
             <a href="//avk.wikipedia.org/" lang="avk">
              Kotava
             </a>
            </li>
            <li>
             <a href="//ht.wikipedia.org/" lang="ht">
              KreyÃ²l Ayisyen
             </a>
            </li>
            <li>
             <a href="//ku.wikipedia.org/" lang="ku">
              <span lang="ku-Latn">
               KurdÃ®
              </span>
              /
              <bdi dir="rtl" lang="ku-Arab">
               ÙÙØ±Ø¯Û
              </bdi>
             </a>
            </li>
            <li>
             <a href="//ckb.wikipedia.org/" lang="ckb" title="KurdÃ®y NawendÃ®">
              <bdi dir="rtl">
               Ú©ÙØ±Ø¯ÛÛ ÙØ§ÙÛÙØ¯Û
              </bdi>
             </a>
            </li>
            <li>
             <a href="//ky.wikipedia.org/" lang="ky" title="KyrgyzÄa">
              ÐÑÑÐ³ÑÐ·ÑÐ°
             </a>
            </li>
            <li>
             <a href="//mrj.wikipedia.org/" lang="mjr" title="Kyryk Mary">
              ÐÑÑÑÐº Ð¼Ð°ÑÑ
             </a>
            </li>
            <li>
             <a href="//lb.wikipedia.org/" lang="lb">
              LÃ«tzebuergesch
             </a>
            </li>
            <li>
             <a href="//lij.wikipedia.org/" lang="lij">
              LÃ¬gure
             </a>
            </li>
            <li>
             <a href="//li.wikipedia.org/" lang="li">
              Limburgs
             </a>
            </li>
            <li>
             <a href="//lmo.wikipedia.org/" lang="lmo">
              Lombard
             </a>
            </li>
            <li>
             <a href="//mai.wikipedia.org/" lang="mai" title="MaithilÄ«">
              à¤®à¥à¤¥à¤¿à¤²à¥
             </a>
            </li>
            <li>
             <a href="//mg.wikipedia.org/" lang="mg">
              Malagasy
             </a>
            </li>
            <li>
             <a href="//ml.wikipedia.org/" lang="ml" title="Malayalam">
              à´®à´²à´¯à´¾à´³à´
             </a>
            </li>
            <li>
             <a href="//mr.wikipedia.org/" lang="mr" title="Marathi">
              à¤®à¤°à¤¾à¤ à¥
             </a>
            </li>
            <li>
             <a href="//xmf.wikipedia.org/" lang="xmf" title="Margaluri">
              ááá áááá£á á
             </a>
            </li>
            <li>
             <a href="//mzn.wikipedia.org/" lang="mzn" title="MÃ¤zeruni">
              <bdi dir="rtl">
               ÙØ§Ø²ÙØ±ÙÙÛ
              </bdi>
             </a>
            </li>
            <li>
             <a href="//cdo.wikipedia.org/" lang="cdo" title="Ming-deng-ngu">
              MÃ¬ng-dÄÌ¤ng-ngá¹³Ì / é©æ±èª
             </a>
            </li>
            <li>
             <a href="//mn.wikipedia.org/" lang="mn" title="Mongol">
              ÐÐ¾Ð½Ð³Ð¾Ð»
             </a>
            </li>
            <li>
             <a href="//nap.wikipedia.org/" lang="nap">
              Napulitano
             </a>
            </li>
            <li>
             <a href="//new.wikipedia.org/" lang="new" title="Nepal Bhasa">
              à¤¨à¥à¤ªà¤¾à¤² à¤­à¤¾à¤·à¤¾
             </a>
            </li>
            <li>
             <a href="//ne.wikipedia.org/" lang="ne" title="NepÄlÄ«">
              à¤¨à¥à¤ªà¤¾à¤²à¥
             </a>
            </li>
            <li>
             <a href="//frr.wikipedia.org/" lang="frr">
              Nordfriisk
             </a>
            </li>
            <li>
             <a href="//oc.wikipedia.org/" lang="oc">
              Occitan
             </a>
            </li>
            <li>
             <a href="//mhr.wikipedia.org/" lang="mhr" title="Olyk Marij">
              ÐÐ»ÑÐº Ð¼Ð°ÑÐ¸Ð¹
             </a>
            </li>
            <li>
             <a href="//or.wikipedia.org/" lang="or" title="Oá¹iÄ">
              à¬à¬¡à¬¿à¬¼à¬
             </a>
            </li>
            <li>
             <a href="//as.wikipedia.org/" lang="as" title="ÃxÃ´miya">
              à¦à¦¸à¦®à§à¦¯à¦¾à¦¼
             </a>
            </li>
            <li>
             <a href="//pa.wikipedia.org/" lang="pa" title="PaÃ±jÄbÄ« (GurmukhÄ«)">
              à¨ªà©°à¨à¨¾à¨¬à©
             </a>
            </li>
            <li>
             <a href="//pnb.wikipedia.org/" lang="pnb" title="PaÃ±jÄbÄ« (ShÄhmukhÄ«)">
              <bdi dir="rtl">
               Ù¾ÙØ¬Ø§Ø¨Û (Ø´Ø§Û ÙÚ©Ú¾Û)
              </bdi>
             </a>
            </li>
            <li>
             <a href="//ps.wikipedia.org/" lang="ps" title="PaÊto">
              <bdi dir="rtl">
               Ù¾ÚØªÙ
              </bdi>
             </a>
            </li>
            <li>
             <a href="//pms.wikipedia.org/" lang="pms">
              PiemontÃ¨is
             </a>
            </li>
            <li>
             <a href="//nds.wikipedia.org/" lang="nds">
              PlattdÃ¼Ã¼tsch
             </a>
            </li>
            <li>
             <a href="//crh.wikipedia.org/" lang="crh">
              QÄ±rÄ±mtatarca
             </a>
            </li>
            <li>
             <a href="//qu.wikipedia.org/" lang="qu">
              Runa Simi
             </a>
            </li>
            <li>
             <a href="//sa.wikipedia.org/" lang="sa" title="Saá¹ská¹tam">
              à¤¸à¤à¤¸à¥à¤à¥à¤¤à¤®à¥
             </a>
            </li>
            <li>
             <a href="//sat.wikipedia.org/" lang="sat" title="Santali">
              á±¥á±á±±á±á±á±²á±¤
             </a>
            </li>
            <li>
             <a href="//sah.wikipedia.org/" lang="sah" title="Saxa Tyla">
              Ð¡Ð°ÑÐ° Ð¢ÑÐ»Ð°
             </a>
            </li>
            <li>
             <a href="//sco.wikipedia.org/" lang="sco">
              Scots
             </a>
            </li>
            <li>
             <a href="//sn.wikipedia.org/" lang="sn">
              ChiShona
             </a>
            </li>
            <li>
             <a href="//scn.wikipedia.org/" lang="scn">
              Sicilianu
             </a>
            </li>
            <li>
             <a href="//si.wikipedia.org/" lang="si" title="Siá¹hala">
              à·à·à¶à·à¶½
             </a>
            </li>
            <li>
             <a href="//sd.wikipedia.org/" lang="sd" title="SindhÄ«">
              <bdi dir="rtl">
               Ø³ÙÚÙ
              </bdi>
             </a>
            </li>
            <li>
             <a href="//szl.wikipedia.org/" lang="szl">
              ÅlÅ¯nski
             </a>
            </li>
            <li>
             <a href="//su.wikipedia.org/" lang="su">
              Basa Sunda
             </a>
            </li>
            <li>
             <a href="//sw.wikipedia.org/" lang="sw">
              Kiswahili
             </a>
            </li>
            <li>
             <a href="//tl.wikipedia.org/" lang="tl">
              Tagalog
             </a>
            </li>
            <li>
             <a href="//shn.wikipedia.org/" lang="shn">
              á½áááááááá¸
             </a>
            </li>
            <li>
             <a href="//zgh.wikipedia.org/" lang="zgh" title="Tamazight tanawayt">
              âµâ´°âµâ´°âµ£âµâµâµ âµâ´°âµâ´°âµ¡â´°âµ¢âµ
             </a>
            </li>
            <li>
             <a href="//tum.wikipedia.org/" lang="tum">
              chiTumbuka
             </a>
            </li>
            <li>
             <a href="//bug.wikipedia.org/" lang="bug">
              Basa Ugi
             </a>
            </li>
            <li>
             <a href="//vec.wikipedia.org/" lang="vec">
              VÃ¨neto
             </a>
            </li>
            <li>
             <a href="//vo.wikipedia.org/" lang="vo">
              VolapÃ¼k
             </a>
            </li>
            <li>
             <a href="//wa.wikipedia.org/" lang="wa">
              Walon
             </a>
            </li>
            <li>
             <a href="//zh-classical.wikipedia.org/" lang="lzh" title="WÃ©nyÃ¡n">
              æè¨
             </a>
            </li>
            <li>
             <a href="//wuu.wikipedia.org/" lang="wuu" title="WÃºyÇ">
              å´è¯­
             </a>
            </li>
            <li>
             <a href="//yi.wikipedia.org/" lang="yi" title="YidiÅ¡">
              <bdi dir="rtl">
               ××Ö´×××©
              </bdi>
             </a>
            </li>
            <li>
             <a href="//yo.wikipedia.org/" lang="yo">
              YorÃ¹bÃ¡
             </a>
            </li>
            <li>
             <a href="//diq.wikipedia.org/" lang="diq" title="Zazaki">
              Zazaki
             </a>
            </li>
            <li>
             <a href="//bat-smg.wikipedia.org/" lang="sgs">
              Å¾emaitÄÅ¡ka
             </a>
            </li>
            <li>
             <a href="//zu.wikipedia.org/" lang="zu">
              isiZulu
             </a>
            </li>
            <li>
             <a href="//mni.wikipedia.org/" lang="mni">
              ê¯ê¯¤ê¯ê¯© ê¯ê¯£ê¯
             </a>
            </li>
           </ul>
          </div>
          <h2 class="bookshelf-container">
           <span class="bookshelf">
            <span class="text">
             <bdi dir="ltr">
              1,000+
             </bdi>
             <span class="jsl10n" data-jsl10n="portal.entries">
              articles
             </span>
            </span>
           </span>
          </h2>
          <div class="langlist hlist" data-el-section="secondary links">
           <ul>
            <li>
             <a href="//lad.wikipedia.org/" lang="lad">
              <span lang="lad-Latn">
               Dzhudezmo
              </span>
              /
              <bdi dir="rtl" lang="lad-Hebr">
               ××××× ×
              </bdi>
             </a>
            </li>
            <li>
             <a href="//kbd.wikipedia.org/" lang="kbd" title="Adighabze">
              ÐÐ´ÑÐ³ÑÐ±Ð·Ñ
             </a>
            </li>
            <li>
             <a href="//ang.wikipedia.org/" lang="ang">
              Ãnglisc
             </a>
            </li>
            <li>
             <a href="//smn.wikipedia.org/" lang="smn" title="anarÃ¢Å¡kielÃ¢">
              AnarÃ¢Å¡kielÃ¢
             </a>
            </li>
            <li>
             <a href="//anp.wikipedia.org/" lang="anp" title="Angika">
              à¤à¤à¤à¤¿à¤à¤¾
             </a>
            </li>
            <li>
             <a href="//ab.wikipedia.org/" lang="ab" title="aá¹sshwa">
              ÐÔ¥ÑÑÓÐ°
             </a>
            </li>
            <li>
             <a href="//roa-rup.wikipedia.org/" lang="rup">
              armÃ£neashti
             </a>
            </li>
            <li>
             <a href="//frp.wikipedia.org/" lang="frp">
              Arpitan
             </a>
            </li>
            <li>
             <a href="//atj.wikipedia.org/" lang="atj">
              atikamekw
             </a>
            </li>
            <li>
             <a href="//arc.wikipedia.org/" lang="arc" title="ÄtÃ»rÄyÃ¢">
              <bdi dir="rtl">
               ÜÜ¬ÜÜªÜÜ
              </bdi>
             </a>
            </li>
            <li>
             <a href="//gn.wikipedia.org/" lang="gn">
              AvaÃ±eâáº½
             </a>
            </li>
            <li>
             <a href="//av.wikipedia.org/" lang="av" title="Avar">
              ÐÐ²Ð°Ñ
             </a>
            </li>
            <li>
             <a href="//ay.wikipedia.org/" lang="ay">
              Aymar
             </a>
            </li>
            <li>
             <a href="//bew.wikipedia.org/" lang="bew">
              Betawi
             </a>
            </li>
            <li>
             <a href="//bh.wikipedia.org/" lang="bh" title="BhÅjapurÄ«">
              à¤­à¥à¤à¤ªà¥à¤°à¥
             </a>
            </li>
            <li>
             <a href="//bi.wikipedia.org/" lang="bi">
              Bislama
             </a>
            </li>
            <li>
             <a href="//bo.wikipedia.org/" lang="bo" title="Bod Skad">
              à½à½¼à½à¼à½¡à½²à½
             </a>
            </li>
            <li>
             <a href="//bxr.wikipedia.org/" lang="bxr" title="Buryad">
              ÐÑÑÑÐ°Ð´
             </a>
            </li>
            <li>
             <a href="//cbk-zam.wikipedia.org/" lang="cbk-x-zam">
              Chavacano de Zamboanga
             </a>
            </li>
            <li>
             <a href="//ny.wikipedia.org/" lang="ny">
              Chichewa
             </a>
            </li>
            <li>
             <a href="//co.wikipedia.org/" lang="co">
              Corsu
             </a>
            </li>
            <li>
             <a href="//za.wikipedia.org/" lang="za">
              Vahcuengh / è©±å®
             </a>
            </li>
            <li>
             <a href="//dga.wikipedia.org/" lang="dga">
              Dagaare
             </a>
            </li>
            <li>
             <a href="//se.wikipedia.org/" lang="se" title="davvisÃ¡megiella">
              DavvisÃ¡megiella
             </a>
            </li>
            <li>
             <a href="//pdc.wikipedia.org/" lang="pdc">
              Deitsch
             </a>
            </li>
            <li>
             <a href="//dv.wikipedia.org/" lang="dv" title="Divehi">
              <bdi dir="rtl">
               ÞÞ¨ÞÞ¬ÞÞ¨ÞÞ¦ÞÞ°
              </bdi>
             </a>
            </li>
            <li>
             <a href="//dsb.wikipedia.org/" lang="dsb">
              Dolnoserbski
             </a>
            </li>
            <li>
             <a href="//dtp.wikipedia.org/" lang="dtp">
              Dusun Bundu-liwan
             </a>
            </li>
            <li>
             <a href="//myv.wikipedia.org/" lang="myv" title="Erzjanj">
              Ð­ÑÐ·ÑÐ½Ñ
             </a>
            </li>
            <li>
             <a href="//ext.wikipedia.org/" lang="ext">
              EstremeÃ±u
             </a>
            </li>
            <li>
             <a href="//fon.wikipedia.org/" lang="fon">
              FÉÌngbÃ¨
             </a>
            </li>
            <li>
             <a href="//ff.wikipedia.org/" lang="ff">
              Fulfulde
             </a>
            </li>
            <li>
             <a href="//fur.wikipedia.org/" lang="fur">
              Furlan
             </a>
            </li>
            <li>
             <a href="//gv.wikipedia.org/" lang="gv">
              Gaelg
             </a>
            </li>
            <li>
             <a href="//gag.wikipedia.org/" lang="gag">
              Gagauz
             </a>
            </li>
            <li>
             <a href="//inh.wikipedia.org/" lang="inh" title="Ghalghai">
              ÐÓÐ°Ð»Ð³ÓÐ°Ð¹
             </a>
            </li>
            <li>
             <a href="//gpe.wikipedia.org/" lang="gpe">
              Ghanaian Pidgin
             </a>
            </li>
            <li>
             <a href="//ki.wikipedia.org/" lang="ki">
              GÄ©kÅ©yÅ©
             </a>
            </li>
            <li>
             <a class="jscnconv" data-hans="èµ£è¯­" data-hant="è´èª" href="//gan.wikipedia.org/" lang="gan" title="Gon ua">
              èµ£è¯­ / è´èª
             </a>
            </li>
            <li>
             <a href="//guw.wikipedia.org/" lang="guw">
              Gungbe
             </a>
            </li>
            <li>
             <a href="//xal.wikipedia.org/" lang="xal" title="HalÊ¹mg">
              Ð¥Ð°Ð»ÑÐ¼Ð³
             </a>
            </li>
            <li>
             <a href="//haw.wikipedia.org/" lang="haw">
              Ê»Ålelo HawaiÊ»i
             </a>
            </li>
            <li>
             <a href="//rw.wikipedia.org/" lang="rw">
              Ikinyarwanda
             </a>
            </li>
            <li>
             <a href="//iba.wikipedia.org/" lang="iba">
              Jaku Iban
             </a>
            </li>
            <li>
             <a href="//kbp.wikipedia.org/" lang="kbp">
              KabÉ©yÉ
             </a>
            </li>
            <li>
             <a href="//csb.wikipedia.org/" lang="csb">
              KaszÃ«bsczi
             </a>
            </li>
            <li>
             <a href="//kw.wikipedia.org/" lang="kw">
              Kernewek
             </a>
            </li>
            <li>
             <a href="//kv.wikipedia.org/" lang="kv" title="Komi">
              ÐÐ¾Ð¼Ð¸
             </a>
            </li>
            <li>
             <a href="//koi.wikipedia.org/" lang="koi" title="Perem Komi">
              ÐÐµÑÐµÐ¼ ÐºÐ¾Ð¼Ð¸
             </a>
            </li>
            <li>
             <a href="//kg.wikipedia.org/" lang="kg">
              Kongo
             </a>
            </li>
            <li>
             <a href="//gom.wikipedia.org/" lang="gom">
              à¤à¥à¤à¤à¤£à¥ / Konknni
             </a>
            </li>
            <li>
             <a href="//ks.wikipedia.org/" lang="ks" title="Koshur">
              <bdi dir="rtl">
               ÙÙ²Ø´ÙØ±
              </bdi>
             </a>
            </li>
            <li>
             <a href="//gcr.wikipedia.org/" lang="gcr" title="KriyÃ²l Gwiyannen">
              KriyÃ²l Gwiyannen
             </a>
            </li>
            <li>
             <a href="//kge.wikipedia.org/" lang="kge">
              Kumoring
             </a>
            </li>
            <li>
             <a href="//kus.wikipedia.org/" lang="kus">
              KÊsaal
             </a>
            </li>
            <li>
             <a href="//lo.wikipedia.org/" lang="lo" title="Phaasaa Laao">
              àºàº²àºªàº²àº¥àº²àº§
             </a>
            </li>
            <li>
             <a href="//lbe.wikipedia.org/" lang="lbe" title="Lakku">
              ÐÐ°ÐºÐºÑ
             </a>
            </li>
            <li>
             <a href="//ltg.wikipedia.org/" lang="ltg">
              LatgaÄ¼u
             </a>
            </li>
            <li>
             <a href="//lez.wikipedia.org/" lang="lez" title="Lezgi">
              ÐÐµÐ·Ð³Ð¸
             </a>
            </li>
            <li>
             <a href="//nia.wikipedia.org/" lang="nia">
              Li Niha
             </a>
            </li>
            <li>
             <a href="//ln.wikipedia.org/" lang="ln">
              LingÃ¡la
             </a>
            </li>
            <li>
             <a href="//lfn.wikipedia.org/" lang="lfn">
              Lingua Franca Nova
             </a>
            </li>
            <li>
             <a href="//olo.wikipedia.org/" lang="olo">
              livvinkarjala
             </a>
            </li>
            <li>
             <a href="//jbo.wikipedia.org/" lang="jbo">
              lojban
             </a>
            </li>
            <li>
             <a href="//lg.wikipedia.org/" lang="lg">
              Luganda
             </a>
            </li>
            <li>
             <a href="//mad.wikipedia.org/" lang="mad">
              MadhurÃ¢
             </a>
            </li>
            <li>
             <a href="//mt.wikipedia.org/" lang="mt">
              Malti
             </a>
            </li>
            <li>
             <a href="//btm.wikipedia.org/" lang="btm">
              Mandailing
             </a>
            </li>
            <li>
             <a href="//mi.wikipedia.org/" lang="mi">
              MÄori
             </a>
            </li>
            <li>
             <a href="//tw.wikipedia.org/" lang="tw" title="Mfantse">
              Twi
             </a>
            </li>
            <li>
             <a href="//mwl.wikipedia.org/" lang="mwl">
              MirandÃ©s
             </a>
            </li>
            <li>
             <a href="//mdf.wikipedia.org/" lang="mdf" title="MokÅ¡enj">
              ÐÐ¾ÐºÑÐµÐ½Ñ
             </a>
            </li>
            <li>
             <a href="//mnw.wikipedia.org/" lang="mnw">
              áá¬áá¬ áááº
             </a>
            </li>
            <li>
             <a href="//mos.wikipedia.org/" lang="mos">
              Moore
             </a>
            </li>
            <li>
             <a href="//nqo.wikipedia.org/" lang="nqo" title="N'Ko">
              ßßß
             </a>
            </li>
            <li>
             <a href="//fj.wikipedia.org/" lang="fj">
              Na Vosa Vaka-Viti
             </a>
            </li>
            <li>
             <a href="//nah.wikipedia.org/" lang="nah">
              NÄhuatlahtÅlli
             </a>
            </li>
            <li>
             <a href="//pcm.wikipedia.org/" lang="pcm">
              NaijÃ¡
             </a>
            </li>
            <li>
             <a href="//nds-nl.wikipedia.org/" lang="nds-nl">
              Nedersaksisch
             </a>
            </li>
            <li>
             <a href="//nrm.wikipedia.org/" lang="roa-x-nrm">
              Nouormand / Normaund
             </a>
            </li>
            <li>
             <a href="//nov.wikipedia.org/" lang="nov">
              Novial
             </a>
            </li>
            <li>
             <a href="//om.wikipedia.org/" lang="om">
              Afaan Oromoo
             </a>
            </li>
            <li>
             <a href="//blk.wikipedia.org/" lang="blk">
              áá¡á­á¯ááºááá¬ááá¬á
             </a>
            </li>
            <li>
             <a href="//pi.wikipedia.org/" lang="pi" title="PÄá¸·i">
              à¤ªà¤¾à¤²à¤¿
             </a>
            </li>
            <li>
             <a href="//pag.wikipedia.org/" lang="pag">
              PangasinÃ¡n
             </a>
            </li>
            <li>
             <a href="//ami.wikipedia.org/" lang="ami">
              Pangcah
             </a>
            </li>
            <li>
             <a href="//pap.wikipedia.org/" lang="pap">
              Papiamentu
             </a>
            </li>
            <li>
             <a href="//jam.wikipedia.org/" lang="jam">
              Patois
             </a>
            </li>
            <li>
             <a href="//pfl.wikipedia.org/" lang="pfl">
              PfÃ¤lzisch
             </a>
            </li>
            <li>
             <a href="//pcd.wikipedia.org/" lang="pcd">
              Picard
             </a>
            </li>
            <li>
             <a href="//krc.wikipedia.org/" lang="krc" title="QaraÃ§ayâMalqar">
              ÐÑÐ°ÑÐ°ÑÐ°Ð¹âÐ¼Ð°Ð»ÐºÑÐ°Ñ
             </a>
            </li>
            <li>
             <a href="//kaa.wikipedia.org/" lang="kaa" title="Qaraqalpaqsha">
              Qaraqalpaqsha
             </a>
            </li>
            <li>
             <a href="//ksh.wikipedia.org/" lang="ksh">
              Ripoarisch
             </a>
            </li>
            <li>
             <a href="//rm.wikipedia.org/" lang="rm">
              Rumantsch
             </a>
            </li>
            <li>
             <a href="//rue.wikipedia.org/" lang="rue" title="Rusinâskyj">
              Ð ÑÑÐ¸Ð½ÑÑÐºÑÐ¹
             </a>
            </li>
            <li>
             <a href="//szy.wikipedia.org/" lang="szy">
              Sakizaya
             </a>
            </li>
            <li>
             <a href="//sm.wikipedia.org/" lang="sm">
              Gagana SÄmoa
             </a>
            </li>
            <li>
             <a href="//skr.wikipedia.org/" lang="skr" title="Saraiki">
              Ø³Ø±Ø§Ø¦ÛÚ©Û
             </a>
            </li>
            <li>
             <a href="//sc.wikipedia.org/" lang="sc" title="Sardu">
              Sardu
             </a>
            </li>
            <li>
             <a href="//trv.wikipedia.org/" lang="trv">
              Seediq
             </a>
            </li>
            <li>
             <a href="//stq.wikipedia.org/" lang="stq">
              Seeltersk
             </a>
            </li>
            <li>
             <a href="//st.wikipedia.org/" lang="st">
              Sesotho
             </a>
            </li>
            <li>
             <a href="//nso.wikipedia.org/" lang="nso">
              Sesotho sa Leboa
             </a>
            </li>
            <li>
             <a href="//tn.wikipedia.org/" lang="tn">
              Setswana
             </a>
            </li>
            <li>
             <a href="//cu.wikipedia.org/" lang="cu" title="SlovÄnÄ­skÅ­">
              Ð¡Ð»Ð¾Ð²Ñ£ÌÐ½ÑÑÐºÑ / â°â°â°â°â°¡â°â° â°â°â°
             </a>
            </li>
            <li>
             <a href="//so.wikipedia.org/" lang="so">
              Soomaaliga
             </a>
            </li>
            <li>
             <a href="//srn.wikipedia.org/" lang="srn">
              Sranantongo
             </a>
            </li>
            <li>
             <a href="//ss.wikipedia.org/" lang="ss">
              SiSwati
             </a>
            </li>
            <li>
             <a href="//shi.wikipedia.org/" lang="shi">
              Taclá¸¥it
             </a>
            </li>
            <li>
             <a href="//ty.wikipedia.org/" lang="ty">
              Reo tahiti
             </a>
            </li>
            <li>
             <a href="//kab.wikipedia.org/" lang="kab" title="Taqbaylit">
              Taqbaylit
             </a>
            </li>
            <li>
             <a href="//roa-tara.wikipedia.org/" lang="roa">
              TarandÃ­ne
             </a>
            </li>
            <li>
             <a href="//tay.wikipedia.org/" lang="tay">
              Tayal
             </a>
            </li>
            <li>
             <a href="//tet.wikipedia.org/" lang="tet">
              Tetun
             </a>
            </li>
            <li>
             <a href="//tpi.wikipedia.org/" lang="tpi">
              Tok Pisin
             </a>
            </li>
            <li>
             <a href="//tly.wikipedia.org/" lang="tly">
              tolÄ±Åi
             </a>
            </li>
            <li>
             <a href="//to.wikipedia.org/" lang="to">
              faka Tonga
             </a>
            </li>
            <li>
             <a href="//tk.wikipedia.org/" lang="tk">
              TÃ¼rkmenÃ§e
             </a>
            </li>
            <li>
             <a href="//kcg.wikipedia.org/" lang="kcg">
              Tyap
             </a>
            </li>
            <li>
             <a href="//tyv.wikipedia.org/" lang="tyv" title="Tyva dyl">
              Ð¢ÑÐ²Ð° Ð´ÑÐ»
             </a>
            </li>
            <li>
             <a href="//udm.wikipedia.org/" lang="udm" title="Udmurt">
              Ð£Ð´Ð¼ÑÑÑ
             </a>
            </li>
            <li>
             <a href="//ug.wikipedia.org/" lang="ug">
              <bdi dir="rtl">
               Ø¦ÛÙØºÛØ±ÚÙ
              </bdi>
             </a>
            </li>
            <li>
             <a href="//vep.wikipedia.org/" lang="vep">
              VepsÃ¤n
             </a>
            </li>
            <li>
             <a href="//fiu-vro.wikipedia.org/" lang="vro">
              vÃµro
             </a>
            </li>
            <li>
             <a href="//vls.wikipedia.org/" lang="vls">
              West-Vlams
             </a>
            </li>
            <li>
             <a href="//wo.wikipedia.org/" lang="wo">
              Wolof
             </a>
            </li>
            <li>
             <a href="//xh.wikipedia.org/" lang="xh">
              isiXhosa
             </a>
            </li>
            <li>
             <a href="//zea.wikipedia.org/" lang="zea">
              ZeÃªuws
             </a>
            </li>
            <li>
             <a href="//alt.wikipedia.org/" lang="alt">
              Ð°Ð»ÑÐ°Ð¹ ÑÐ¸Ð»
             </a>
            </li>
            <li>
             <a href="//awa.wikipedia.org/" lang="awa">
              à¤à¤µà¤§à¥
             </a>
            </li>
            <li>
             <a href="//dty.wikipedia.org/" lang="dty">
              à¤¡à¥à¤à¥à¤²à¥
             </a>
            </li>
            <li>
             <a href="//tcy.wikipedia.org/" lang="tcy">
              à²¤à³à²³à³
             </a>
            </li>
           </ul>
          </div>
          <h2 class="bookshelf-container">
           <span class="bookshelf">
            <span class="text">
             <bdi dir="ltr">
              100+
             </bdi>
             <span class="jsl10n" data-jsl10n="portal.entries">
              articles
             </span>
            </span>
           </span>
          </h2>
          <div class="langlist langlist-tiny hlist" data-el-section="secondary links">
           <ul>
            <li>
             <a href="//bdr.wikipedia.org/" lang="bdr">
              Bajau Sama
             </a>
            </li>
            <li>
             <a href="//bm.wikipedia.org/" lang="bm">
              Bamanankan
             </a>
            </li>
            <li>
             <a href="//bbc.wikipedia.org/" lang="bbc">
              Batak Toba
             </a>
            </li>
            <li>
             <a href="//ch.wikipedia.org/" lang="ch">
              Chamoru
             </a>
            </li>
            <li>
             <a href="//dz.wikipedia.org/" lang="dz" title="Rdzong-Kha">
              à½¢à¾«à½¼à½à¼à½
             </a>
            </li>
            <li>
             <a href="//ee.wikipedia.org/" lang="ee">
              EÊegbe
             </a>
            </li>
            <li>
             <a href="//gur.wikipedia.org/" lang="gur">
              Farefare
             </a>
            </li>
            <li>
             <a href="//got.wikipedia.org/" lang="got" title="Gutisk">
              ð²ð¿ðð¹ððº
             </a>
            </li>
            <li>
             <a href="//igl.wikipedia.org/" lang="igl">
              Igala
             </a>
            </li>
            <li>
             <a href="//iu.wikipedia.org/" lang="iu">
              áááááá¦ / Inuktitut
             </a>
            </li>
            <li>
             <a href="//ik.wikipedia.org/" lang="ik">
              IÃ±upiak
             </a>
            </li>
            <li>
             <a href="//kl.wikipedia.org/" lang="kl">
              Kalaallisut
             </a>
            </li>
            <li>
             <a href="//fat.wikipedia.org/" lang="fat">
              Mfantse
             </a>
            </li>
            <li>
             <a href="//nr.wikipedia.org/" lang="nr" title="Ndebele seSewula, isi-">
              isiNdebele seSewula
             </a>
            </li>
            <li>
             <a href="//pih.wikipedia.org/" lang="pih">
              Norfuk / Pitkern
             </a>
            </li>
            <li>
             <a href="//ann.wikipedia.org/" lang="ann">
              Obolo
             </a>
            </li>
            <li>
             <a href="//pwn.wikipedia.org/" lang="pwn">
              pinayuanan
             </a>
            </li>
            <li>
             <a href="//pnt.wikipedia.org/" lang="pnt" title="PontiakÃ¡">
              Î Î¿Î½ÏÎ¹Î±ÎºÎ¬
             </a>
            </li>
            <li>
             <a href="//rmy.wikipedia.org/" lang="rmy">
              romani Ähib
             </a>
            </li>
            <li>
             <a href="//rn.wikipedia.org/" lang="rn">
              Ikirundi
             </a>
            </li>
            <li>
             <a href="//rsk.wikipedia.org/" lang="rsk" title="ruski">
              ÑÑÑÐºÐ¸
             </a>
            </li>
            <li>
             <a href="//sg.wikipedia.org/" lang="sg">
              SÃ¤ngÃ¶
             </a>
            </li>
            <li>
             <a href="//tdd.wikipedia.org/" lang="tdd" title="Tai taÉ¯ xoÅ">
              á¥á¥­á¥°á¥á¥¬á¥³á¥á¥¨á¥á¥°
             </a>
            </li>
            <li>
             <a href="//ti.wikipedia.org/" lang="ti" title="TÉgÉrÉÃ±a">
              áµáá­á
             </a>
            </li>
            <li>
             <a href="//din.wikipedia.org/" lang="din">
              ThuÉÅjÃ¤Å
             </a>
            </li>
            <li>
             <a href="//chr.wikipedia.org/" lang="chr" title="Tsalagi">
              á£á³á©
             </a>
            </li>
            <li>
             <a href="//chy.wikipedia.org/" lang="chy">
              TsÄhesenÄstsestotse
             </a>
            </li>
            <li>
             <a href="//ts.wikipedia.org/" lang="ts">
              Xitsonga
             </a>
            </li>
            <li>
             <a href="//ve.wikipedia.org/" lang="ve">
              Tshivená¸a
             </a>
            </li>
            <li>
             <a href="//guc.wikipedia.org/" lang="guc">
              Wayuunaiki
             </a>
            </li>
            <li>
             <a href="//ady.wikipedia.org/" lang="ady">
              Ð°Ð´ÑÐ³Ð°Ð±Ð·Ñ
             </a>
            </li>
           </ul>
          </div>
          <div class="langlist langlist-others hlist" data-el-section="other languages">
           <a class="jsl10n" data-jsl10n="other-languages-label" href="https://meta.wikimedia.org/wiki/Special:MyLanguage/List_of_Wikipedias" lang="">
            Other languages
           </a>
          </div>
         </div>
        </div>
       </nav>
       <hr/>
       <div class="banner banner-overlay" id="portalBanner_en6C_2024_overlayBanner4">
        <div class="overlay-banner">
         <div class="overlay-banner-main">
          <button aria-label="minimize" class="frb-header-minimize overlay-banner-toggle">
           <span class="frb-header-minimize-icon">
            <svg aria-hidden="true" height="20" viewbox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg">
             <g>
              <path d="m17.5 4.75-7.5 7.5-7.5-7.5L1 6.25l9 9 9-9z">
              </path>
             </g>
            </svg>
           </span>
          </button>
          <div class="overlay-banner-main-header">
           <a href="#">
            Donate now
           </a>
          </div>
          <div class="overlay-banner-main-scroll">
           <div class="overlay-banner-main-message">
            <div class="overlay-banner-main-message-greeting">
             The internet we were promised
            </div>
            <p class="overlay-banner-main-message-subheading">
             An important update for readers in
             <span class="banner__country">
              the United States
             </span>
             .
            </p>
            <p>
             You deserve an explanation, so please don't skip this 1-minute read. We're sorry to interrupt, but this message will only be up for a short time. We ask you to reflect on the number of times you visited Wikipedia this past year and whether you're able to give
             <span class="banner__amount1">
              $2.75
             </span>
             to the Wikimedia Foundation. If everyone reading this gave just
             <span class="banner__amount1">
              $2.75
             </span>
             , we'd hit our goal in a few hours.
            </p>
            <p>
             The internet we were promisedâa place of free, collaborative, and accessible knowledgeâis under constant threat. On Wikipedia, volunteers work together to create and verify the pages you rely on, supported by tools that undo vandalism within minutes, ensuring the information you seek is trustworthy.
            </p>
            <p>
             Just 2% of our readers donate, so if you have given in the past and Wikipedia still provides you with
             <span class="banner__amount1">
              $2.75
             </span>
             worth of knowledge, kindly donate today. If you are undecided, remember that any contribution helps, whether it's
             <span class="banner__amount1">
              $2.75
             </span>
             or
             <span class="banner__amount2">
              $2.75
             </span>
             .
            </p>
           </div>
           <div class="overlay-banner-main-amounts">
            <div class="frb-message frb-message-amount">
             <span class="error-highlight">
              Please select an amount (
              <span class="banner__currency">
               USD
              </span>
              )
             </span>
             .
             <span class="frb-explanation">
              The average donation in
              <span class="banner__country">
               the United States
              </span>
              is around
              <span class="banner__average">
               $13
              </span>
              . Many first-time donors give
              <span class="banner__amount1">
               $2.75
              </span>
              . All that matters is that you're choosing to stand up for free, open information; and for that, you have our gratitude.
             </span>
            </div>
            <div class="button-grid" id="amountsGrid">
             <label class="banner-button button-33">
              <input class="sr-only" name="amount" type="radio" value="2.75"/>
              <span class="banner__amount1">
              </span>
             </label>
             <label class="banner-button button-33">
              <input class="sr-only" name="amount" type="radio" value="5"/>
              <span class="banner__currency">
              </span>
              5
             </label>
             <label class="banner-button button-33">
              <input class="sr-only" name="amount" type="radio" value="10"/>
              <span class="banner__currency">
              </span>
              10
             </label>
             <label class="banner-button button-33">
              <input class="sr-only" name="amount" type="radio" value="20"/>
              <span class="banner__currency">
              </span>
              20
             </label>
             <label class="banner-button button-33">
              <input class="sr-only" name="amount" type="radio" value="30"/>
              <span class="banner__currency">
              </span>
              30
             </label>
             <label class="banner-button button-33">
              <input class="sr-only" name="amount" type="radio" value="50"/>
              <span class="banner__currency">
              </span>
              50
             </label>
             <label class="banner-button button-33">
              <input class="sr-only" name="amount" type="radio" value="100"/>
              <span class="banner__currency">
              </span>
              100
             </label>
             <label class="banner-button button-67">
              <input class="sr-only" name="amount" type="radio" value="Other"/>
              Other
             </label>
            </div>
           </div>
           <div class="overlay-banner-main-frequency button-grid">
            <div class="frb-message error-highlight">
             How often would you like to donate?
            </div>
            <div class="button-grid" id="frequencyGrid">
             <label class="banner-button button-50">
              <input class="sr-only" name="monthly" type="radio" value="0"/>
              One time
             </label>
             <label class="banner-button button-50">
              <input class="sr-only" name="monthly" type="radio" value="1"/>
              Give monthly
             </label>
            </div>
           </div>
           <a class="frb-submit banner-button banner-button-disabled" href="#" id="frb-donate">
            Donate Now
           </a>
           <div class="overlay-banner-main-footer">
            <div class="overlay-banner-main-footer-cta">
             <svg aria-hidden="true" class="frb-message-icon" height="20" viewbox="0 0 25 25" width="20" xmlns="http://www.w3.org/2000/svg">
              <g fill="none" fill-rule="nonzero">
               <circle cx="10.492" cy="14.492" r="10.492">
               </circle>
               <path d="M12.681 11.754l-2.267 7.864c-.125.45-.188.745-.188.885 0 .08.033.156.1.226.066.07.136.105.21.105.125 0 .25-.055.376-.165.332-.273.73-.767 1.194-1.482l.376.22c-1.113 1.94-2.296 2.91-3.55 2.91-.48 0-.86-.135-1.144-.404a1.349 1.349 0 0 1-.426-1.023c0-.273.062-.62.188-1.04l1.537-5.286c.147-.51.221-.892.221-1.15a.566.566 0 0 0-.21-.432c-.14-.125-.332-.188-.575-.188-.11 0-.243.004-.398.011l.144-.442 3.749-.609h.663zm-.685-5.087c.457 0 .842.159 1.156.475.313.318.47.701.47 1.15 0 .45-.16.834-.476 1.15-.317.318-.7.476-1.15.476-.443 0-.822-.158-1.14-.475a1.566 1.566 0 0 1-.475-1.15c0-.45.157-.833.47-1.15a1.549 1.549 0 0 1 1.145-.476z">
               </path>
              </g>
             </svg>
             We ask you, sincerely: don't skip this, join the 2% of readers who give.
            </div>
            <div class="overlay-banner-main-footer-identity">
             <img alt="Wikimedia Foundation Logo" src="https://upload.wikimedia.org/wikipedia/donate/1/14/Wikimedia_Foundation_logo_-_wordmark.svg"/>
             Proud host of Wikipedia and its sister sites
            </div>
            <button class="button-center button-collapse overlay-banner-toggle" type="button">
             Collapse
            </button>
           </div>
          </div>
         </div>
         <div class="overlay-banner-mini">
          <div aria-label="open" class="frb-conversation-open frb-bubble-message-close overlay-banner-toggle" style="">
           <span class="frb-conversation-open-icon">
            <svg aria-hidden="true" height="20" viewbox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg">
             <g>
              <path d="m17.5 4.75-7.5 7.5-7.5-7.5L1 6.25l9 9 9-9z">
              </path>
             </g>
            </svg>
           </span>
          </div>
          <div aria-label="close" class="frb-conversation-close frb-bubble-message-close overlay-banner-close" style="">
           <span class="frb-conversation-close-icon">
           </span>
          </div>
          <div class="overlay-banner-mini-message overlay-banner-toggle">
           <div class="overlay-banner-mini-message-text">
            <h3>
             <svg aria-hidden="true" class="frb-message-icon" height="20" viewbox="0 0 25 25" width="20" xmlns="http://www.w3.org/2000/svg">
              <g fill="none" fill-rule="nonzero">
               <circle cx="10.492" cy="14.492" r="10.492">
               </circle>
               <path d="M12.681 11.754l-2.267 7.864c-.125.45-.188.745-.188.885 0 .08.033.156.1.226.066.07.136.105.21.105.125 0 .25-.055.376-.165.332-.273.73-.767 1.194-1.482l.376.22c-1.113 1.94-2.296 2.91-3.55 2.91-.48 0-.86-.135-1.144-.404a1.349 1.349 0 0 1-.426-1.023c0-.273.062-.62.188-1.04l1.537-5.286c.147-.51.221-.892.221-1.15a.566.566 0 0 0-.21-.432c-.14-.125-.332-.188-.575-.188-.11 0-.243.004-.398.011l.144-.442 3.749-.609h.663zm-.685-5.087c.457 0 .842.159 1.156.475.313.318.47.701.47 1.15 0 .45-.16.834-.476 1.15-.317.318-.7.476-1.15.476-.443 0-.822-.158-1.14-.475a1.566 1.566 0 0 1-.475-1.15c0-.45.157-.833.47-1.15a1.549 1.549 0 0 1 1.145-.476z">
               </path>
              </g>
             </svg>
             The internet we were promised
            </h3>
            <p>
             <strong>
              Hi. Please don't skip this 1-minute read.
             </strong>
             Today, our nonprofit asks for your support. It matters. When Wikipedia was created, it was one of the first spaces online where you could learn for free, without ads. This space is yours. Just 2% of our readers donate, so whatever gift you can afford helps.
            </p>
            <p>
             â
             <em>
              The Wikimedia Foundation, host of Wikipedia and its sister sites
             </em>
             .
            </p>
           </div>
           <div class="overlay-banner-mini-message-actions">
            <a class="banner__button banner__button--progressive frb-submit" href="#">
             Donate now
            </a>
           </div>
          </div>
         </div>
        </div>
       </div>
      </main>
      <footer class="footer" data-el-section="other projects">
       <div class="footer-sidebar">
        <div class="footer-sidebar-content">
         <div class="footer-sidebar-icon sprite svg-Wikimedia-logo_black">
         </div>
         <div class="footer-sidebar-text jsl10n" data-jsl10n="portal.footer-description">
          Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects.
         </div>
         <div class="footer-sidebar-text">
          <a href="https://donate.wikimedia.org/?wmf_medium=portal&amp;wmf_campaign=portalFooter&amp;wmf_source=portalFooter" target="_blank">
           <span class="jsl10n" data-jsl10n="footer-donate">
            You can support our work with a donation.
           </span>
          </a>
         </div>
        </div>
       </div>
       <div class="footer-sidebar app-badges">
        <div class="footer-sidebar-content">
         <div class="footer-sidebar-text">
          <div class="footer-sidebar-icon sprite svg-wikipedia_app_tile">
          </div>
          <strong class="jsl10n" data-jsl10n="portal.app-links.title">
           <a class="jsl10n" data-jsl10n="portal.app-links.url" href="https://en.wikipedia.org/wiki/List_of_Wikipedia_mobile_applications">
            Download Wikipedia for Android or iOS
           </a>
          </strong>
          <p class="jsl10n" data-jsl10n="portal.app-links.description">
           Save your favorite articles to read offline, sync your reading lists across devices and customize your reading experience with the official Wikipedia app.
          </p>
          <ul>
           <li class="app-badge app-badge-android">
            <a href="https://play.google.com/store/apps/details?id=org.wikipedia&amp;referrer=utm_source%3Dportal%26utm_medium%3Dbutton%26anid%3Dadmob" rel="noreferrer" target="_blank">
             <span class="jsl10n sprite svg-badge_google_play_store" data-jsl10n="portal.app-links.google-store">
              Google Play Store
             </span>
            </a>
           </li>
           <li class="app-badge app-badge-ios">
            <a href="https://itunes.apple.com/app/apple-store/id324715238?pt=208305&amp;ct=portal&amp;mt=8" rel="noreferrer" target="_blank">
             <span class="jsl10n sprite svg-badge_ios_app_store" data-jsl10n="portal.app-links.apple-store">
              Apple App Store
             </span>
            </a>
           </li>
          </ul>
         </div>
        </div>
       </div>
       <nav aria-label="Other projects" class="other-projects" data-jsl10n="other-projects-nav-label">
        <div class="other-project">
         <a class="other-project-link" href="//commons.wikimedia.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Commons-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="commons.name">
            Commons
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="commons.slogan">
            Free media collection
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wikivoyage.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikivoyage-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikivoyage.name">
            Wikivoyage
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikivoyage.slogan">
            Free travel guide
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wiktionary.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wiktionary-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wiktionary.name">
            Wiktionary
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wiktionary.slogan">
            Free dictionary
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wikibooks.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikibooks-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikibooks.name">
            Wikibooks
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikibooks.slogan">
            Free textbooks
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wikinews.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikinews-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikinews.name">
            Wikinews
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikinews.slogan">
            Free news source
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wikidata.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikidata-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikidata.name">
            Wikidata
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikidata.slogan">
            Free knowledge base
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wikiversity.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikiversity-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikiversity.name">
            Wikiversity
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikiversity.slogan">
            Free learning resources
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wikiquote.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikiquote-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikiquote.name">
            Wikiquote
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikiquote.slogan">
            Free quote compendium
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.mediawiki.org/">
          <div class="other-project-icon">
           <div class="sprite svg-MediaWiki-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="mediawiki.name">
            MediaWiki
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="mediawiki.slogan">
            Free &amp; open wiki software
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wikisource.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikisource-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikisource.name">
            Wikisource
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikisource.slogan">
            Free content library
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//species.wikimedia.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikispecies-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikispecies.name">
            Wikispecies
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikispecies.slogan">
            Free species directory
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//www.wikifunctions.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Wikifunctions-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="wikifunctions.name">
            Wikifunctions
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="wikifunctions.slogan">
            Free function library
           </span>
          </div>
         </a>
        </div>
        <div class="other-project">
         <a class="other-project-link" href="//meta.wikimedia.org/">
          <div class="other-project-icon">
           <div class="sprite svg-Meta-Wiki-logo_sister">
           </div>
          </div>
          <div class="other-project-text">
           <span class="other-project-title jsl10n" data-jsl10n="metawiki.name">
            Meta-Wiki
           </span>
           <span class="other-project-tagline jsl10n" data-jsl10n="metawiki.slogan">
            Community coordination &amp; documentation
           </span>
          </div>
         </a>
        </div>
       </nav>
       <hr/>
       <p class="site-license">
        <small class="jsl10n" data-jsl10n="license">
         This page is available under the
         <a href="https://creativecommons.org/licenses/by-sa/4.0/">
          Creative Commons Attribution-ShareAlike License
         </a>
        </small>
        <small class="jsl10n" data-jsl10n="terms">
         <a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use">
          Terms of Use
         </a>
        </small>
        <small class="jsl10n" data-jsl10n="privacy-policy">
         <a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy">
          Privacy Policy
         </a>
        </small>
       </p>
      </footer>
      <script>
       var rtlLangs = ['ar','arc','ary','arz','bcc','bgn','bqi','ckb','dv','fa','glk','he','kk-cn','kk-arab','khw','ks','ku-arab','lki','luz','mzn','nqo','pnb','ps','sd','sdh','skr','ug','ur','yi'],
        translationsHash = '8d587fac',
        /**
         * This variable is used to convert the generic "portal" keyword in the data-jsl10n attributes
         * e.g. 'data-jsl10n="portal.footer-description"' into a portal-specific key, e.g. "wiki"
         * for the Wikipedia portal.
         */
        translationsPortalKey = 'wiki';
        /**
         * The wm-typeahead.js feature is used for search,and it uses domain name for searching. We want domain
         * name to be portal Specific (different for every portal).So by declaring variable 'portalSearchDomain'
         * in index.handlebars we will make this portal Specific.
        **/
        portalSearchDomain = 'wikipedia.org'
        /*
         This object is used by l10n scripts (page-localized.js, topten-localized.js)
         to reveal the page content after l10n json is loaded.
         A timer is also set to prevent JS from hiding page content indefinitelty.
         This script is inlined to safeguard againt script loading errors and placed
         at the top of the page to safeguard against any HTML loading/parsing errors.
        */
        wmL10nVisible = {
            ready: false,
            makeVisible: function(){
                if ( !wmL10nVisible.ready ) {
                    wmL10nVisible.ready = true;
                    document.body.className += ' jsl10n-visible';
                }
            }
        };
        window.setTimeout( wmL10nVisible.makeVisible, 1000 )
      </script>
      <script src="portal/wikipedia.org/assets/js/index-0b1f819930.js">
      </script>
      <script src="portal/wikipedia.org/assets/js/gt-ie9-ce3fe8e88d.js">
      </script>
      <style>
       .styled-select {
            display: block;
        }
      </style>
     </body>
    </html>
    


### soup.find()

Find the first occurrence of a tag

soup.find() returns the first matching tag.


```python
# Find the first <h1> tag in the HTML
h1_tag = soup.find('h1')
print(h1_tag.text)  # Extract the text from the <h1> tag

```

    
    
    Wikipedia
    
    The Free Encyclopedia
    



```python
  # Extract the text from the <p> inside <body> tag
soup = BeautifulSoup(response.text, 'html.parser')
h1_tag = soup.find('body').find('p')
print(h1_tag.text)
```

    An important update for readers in the United States.



```python
# Find the first <p> tag in the HTML
h1_tag = soup.find('p')
print(h1_tag.text)  # Extract the text from the <p> tag

```

    An important update for readers in the United States.


### soup.find_all()
Find all occurrences of a tag

soup.find_all() returns all matching tags.


```python
# Find all <a> tags (links) in the HTML
a_tags = soup.find_all('a')

print(len(a_tags))

# Print the href attribute of each link
for a in a_tags[:3]:
    print(a.get('href'))

```

    372
    //en.wikipedia.org/
    //ru.wikipedia.org/
    //ja.wikipedia.org/



```python
# Find all <div> tags in the HTML
div_tags = soup.find_all('div')

print(len(div_tags))

# Print the class name attribute of each div
for div in div_tags[:3]:
    print('-------------------')
    print('classname',div.get('class'), '\n div text', div.text)

```

    109
    -------------------
    classname ['central-textlogo'] 
     div text 
    
    
    
    Wikipedia
    
    The Free Encyclopedia
    
    
    -------------------
    classname ['central-featured-lang', 'lang1'] 
     div text 
    
    English
    6,918,000+ articles
    
    
    -------------------
    classname ['central-featured-lang', 'lang2'] 
     div text 
    
    Ð ÑÑÑÐºÐ¸Ð¹
    2Â 012Â 000+ ÑÑÐ°ÑÐµÐ¹
    
    


### Accessing Tags by Class or ID

You can use the class_ parameter to search by class and id for searching by ID.


```python
# Find a tag with a specific class
div_with_class = soup.find('div', class_='central-textlogo')
print(div_with_class.text)

```

    
    
    
    
    Wikipedia
    
    The Free Encyclopedia
    
    



```python
# Find a tag with a specific ID
element_with_id = soup.find(id='amountsGrid')
print(element_with_id.text)
```

    
    
    5
    10
    20
    30
    50
    100
    Other
    


### Navigating the HTML Tree
BeautifulSoup allows you to navigate through the HTML tree with methods like .parent, .children, .next_sibling, etc.


```python
# Get the parent of a tag
h1_tag = soup.find('h1')
parent_tag = h1_tag.parent
print('parent of h1_tag:',parent_tag)

# Get all children of a parent_tag tag
print('\nchildrens of parent_tag:')
for child in parent_tag:
    print(child)

# Get the next sibling of a tag
next_sibling = parent_tag.find_next_sibling()
print(next_sibling)

```

    parent of h1_tag: <div class="central-textlogo">
    <img alt="" class="central-featured-logo" height="183" src="portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png" srcset="portal/wikipedia.org/assets/img/Wikipedia-logo-v2@1.5x.png 1.5x, portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png 2x" width="200"/>
    <h1 class="central-textlogo-wrapper">
    <span class="central-textlogo__image sprite svg-Wikipedia_wordmark">
    Wikipedia
    </span>
    <strong class="jsl10n localized-slogan" data-jsl10n="portal.slogan">The Free Encyclopedia</strong>
    </h1>
    </div>
    childrens of parent_tag:
    
    
    <img alt="" class="central-featured-logo" height="183" src="portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png" srcset="portal/wikipedia.org/assets/img/Wikipedia-logo-v2@1.5x.png 1.5x, portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png 2x" width="200"/>
    
    
    <h1 class="central-textlogo-wrapper">
    <span class="central-textlogo__image sprite svg-Wikipedia_wordmark">
    Wikipedia
    </span>
    <strong class="jsl10n localized-slogan" data-jsl10n="portal.slogan">The Free Encyclopedia</strong>
    </h1>
    
    
    <nav aria-label="Top languages" class="central-featured" data-el-section="primary links" data-jsl10n="top-ten-nav-label">
    <!-- #1. en.wikipedia.org - 1,687,212,000 views/day -->
    <div class="central-featured-lang lang1" dir="ltr" lang="en">
    <a class="link-box" data-slogan="The Free Encyclopedia" href="//en.wikipedia.org/" id="js-link-box-en" title="English â Wikipedia â The Free Encyclopedia">
    <strong>English</strong>
    <small>6,918,000+ <span>articles</span></small>
    </a>
    </div>
    <!-- #2. ru.wikipedia.org - 204,861,000 views/day -->
    <div class="central-featured-lang lang2" dir="ltr" lang="ru">
    <a class="link-box" data-slogan="Ð¡Ð²Ð¾Ð±Ð¾Ð´Ð½Ð°Ñ ÑÐ½ÑÐ¸ÐºÐ»Ð¾Ð¿ÐµÐ´Ð¸Ñ" href="//ru.wikipedia.org/" id="js-link-box-ru" title="Russkiy â ÐÐ¸ÐºÐ¸Ð¿ÐµÐ´Ð¸Ñ â Ð¡Ð²Ð¾Ð±Ð¾Ð´Ð½Ð°Ñ ÑÐ½ÑÐ¸ÐºÐ»Ð¾Ð¿ÐµÐ´Ð¸Ñ">
    <strong>Ð ÑÑÑÐºÐ¸Ð¹</strong>
    <small>2Â 012Â 000+ <span>ÑÑÐ°ÑÐµÐ¹</span></small>
    </a>
    </div>
    <!-- #3. ja.wikipedia.org - 203,232,000 views/day -->
    <div class="central-featured-lang lang3" dir="ltr" lang="ja">
    <a class="link-box" data-slogan="ããªã¼ç¾ç§äºå¸" href="//ja.wikipedia.org/" id="js-link-box-ja" title="Nihongo â ã¦ã£ã­ããã£ã¢ â ããªã¼ç¾ç§äºå¸">
    <strong>æ¥æ¬èª</strong>
    <small>1,438,000+ <span>è¨äº</span></small>
    </a>
    </div>
    <!-- #4. de.wikipedia.org - 174,277,000 views/day -->
    <div class="central-featured-lang lang4" dir="ltr" lang="de">
    <a class="link-box" data-slogan="Die freie EnzyklopÃ¤die" href="//de.wikipedia.org/" id="js-link-box-de" title="Deutsch â Wikipedia â Die freie EnzyklopÃ¤die">
    <strong>Deutsch</strong>
    <small>2.964.000+ <span>Artikel</span></small>
    </a>
    </div>
    <!-- #5. fr.wikipedia.org - 172,274,000 views/day -->
    <div class="central-featured-lang lang5" dir="ltr" lang="fr">
    <a class="link-box" data-slogan="LâencyclopÃ©die libre" href="//fr.wikipedia.org/" id="js-link-box-fr" title="franÃ§ais â WikipÃ©dia â LâencyclopÃ©die libre">
    <strong>FranÃ§ais</strong>
    <small>2â¯650â¯000+ <span>articles</span></small>
    </a>
    </div>
    <!-- #6. es.wikipedia.org - 167,709,000 views/day -->
    <div class="central-featured-lang lang6" dir="ltr" lang="es">
    <a class="link-box" data-slogan="La enciclopedia libre" href="//es.wikipedia.org/" id="js-link-box-es" title="EspaÃ±ol â Wikipedia â La enciclopedia libre">
    <strong>EspaÃ±ol</strong>
    <small>1.992.000+ <span>artÃ­culos</span></small>
    </a>
    </div>
    <!-- #7. it.wikipedia.org - 99,760,000 views/day -->
    <div class="central-featured-lang lang7" dir="ltr" lang="it">
    <a class="link-box" data-slogan="L'enciclopedia libera" href="//it.wikipedia.org/" id="js-link-box-it" title="Italiano â Wikipedia â L'enciclopedia libera">
    <strong>Italiano</strong>
    <small>1.893.000+ <span>voci</span></small>
    </a>
    </div>
    <!-- #8. zh.wikipedia.org - 97,847,000 views/day -->
    <div class="central-featured-lang lang8" dir="ltr" lang="zh">
    <a class="link-box localize-variant" data-slogan="èªç±çç¾ç§å¨ä¹¦ / èªç±çç¾ç§å¨æ¸" href="//zh.wikipedia.org/" id="js-link-box-zh" title="ZhÅngwÃ©n â ç»´åºç¾ç§ / ç¶­åºç¾ç§ â èªç±çç¾ç§å¨ä¹¦ / èªç±çç¾ç§å¨æ¸">
    <strong>ä¸­æ</strong>
    <small>1,452,000+ <span>æ¡ç® / æ¢ç®</span></small>
    </a>
    </div>
    <!-- #9. fa.wikipedia.org - 56,140,000 views/day -->
    <div class="central-featured-lang lang9" dir="rtl" lang="fa">
    <a class="link-box" data-slogan="Ø¯Ø§ÙØ´ÙØ§ÙÙÙ Ø¢Ø²Ø§Ø¯" href="//fa.wikipedia.org/" id="js-link-box-fa" title="FÄrsi â ÙÛÚ©ÛâÙ¾Ø¯ÛØ§ â Ø¯Ø§ÙØ´ÙØ§ÙÙÙ Ø¢Ø²Ø§Ø¯">
    <strong><bdi dir="rtl">ÙØ§Ø±Ø³Û</bdi></strong>
    <small>Û±Ù¬Û°Û²Û°Ù¬Û°Û°Û°+ <span>ÙÙØ§ÙÙ</span></small>
    </a>
    </div>
    <!-- #10. pt.wikipedia.org - 53,221,000 views/day -->
    <div class="central-featured-lang lang10" dir="ltr" lang="pt">
    <a class="link-box" data-slogan="A enciclopÃ©dia livre" href="//pt.wikipedia.org/" id="js-link-box-pt" title="PortuguÃªs â WikipÃ©dia â A enciclopÃ©dia livre">
    <strong>PortuguÃªs</strong>
    <small>1.138.000+ <span>artigos</span></small>
    </a>
    </div>
    </nav>


### Extracting Attributes

You can extract attributes of a tag using get().


```python
# Extract the href attribute from an <a> tag
link = a_tags[0]
href = link.get('href')
print(f"Link: {href}")

```

    Link: //en.wikipedia.org/


### Parsing Specific HTML Content


```python
import requests
from bs4 import BeautifulSoup

# Example URL
url = 'https://www.wikipedia.org'

# Send a request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all titles (in this case, all <a> tags with class 'jsl10n')
    story_links = soup.find_all('a', class_='jsl10n')

    # Print the titles and URLs
    for story in story_links:
        title = story.text
        link = story.get('href')
        print(f"Title: {title}\nURL: {link}\n")
else:
    print("Failed to retrieve the page.")

```

    Title: Other languages
    URL: https://meta.wikimedia.org/wiki/Special:MyLanguage/List_of_Wikipedias
    
    Title: 
    Download Wikipedia for Android or iOS
    
    URL: https://en.wikipedia.org/wiki/List_of_Wikipedia_mobile_applications
    


## Selenium - Handling Dynamic Content

If a website relies on JavaScript to load content dynamically (e.g., infinite scrolling), requests and BeautifulSoup won’t be sufficient. In that case, you can use Selenium, which automates a web browser to load pages and execute JavaScript.


```python
!apt-get update -y  # Update the package lists
!apt install -y chromium-chromedriver  # Install Chromium and Chromedriver
```

    
0% [Working]
            
Get:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease [3,626 B]
    Get:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease [1,581 B]
    Hit:3 http://archive.ubuntu.com/ubuntu jammy InRelease
    Get:4 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
    Get:5 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
    Get:6 https://r2u.stat.illinois.edu/ubuntu jammy InRelease [6,555 B]
    Get:7 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  Packages [1,192 kB]
    Get:8 https://r2u.stat.illinois.edu/ubuntu jammy/main all Packages [8,531 kB]
    Get:9 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease [18.1 kB]
    Get:10 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
    Hit:11 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease
    Hit:12 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease
    Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2,741 kB]
    Get:14 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [2,454 kB]
    Get:15 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy/main amd64 Packages [32.9 kB]
    Get:16 https://r2u.stat.illinois.edu/ubuntu jammy/main amd64 Packages [2,626 kB]
    Get:17 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [3,453 kB]
    Get:18 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1,225 kB]
    Fetched 22.7 MB in 3s (6,897 kB/s)
    Reading package lists... Done
    W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    The following additional packages will be installed:
      apparmor chromium-browser libfuse3-3 liblzo2-2 libudev1 snapd squashfs-tools systemd-hwe-hwdb
      udev
    Suggested packages:
      apparmor-profiles-extra apparmor-utils fuse3 zenity | kdialog
    The following NEW packages will be installed:
      apparmor chromium-browser chromium-chromedriver libfuse3-3 liblzo2-2 snapd squashfs-tools
      systemd-hwe-hwdb udev
    The following packages will be upgraded:
      libudev1
    1 upgraded, 9 newly installed, 0 to remove and 51 not upgraded.
    Need to get 30.2 MB of archives.
    After this operation, 123 MB of additional disk space will be used.
    Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 apparmor amd64 3.0.4-2ubuntu2.4 [598 kB]
    Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 liblzo2-2 amd64 2.10-2build3 [53.7 kB]
    Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 squashfs-tools amd64 1:4.5-3build1 [159 kB]
    Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libudev1 amd64 249.11-0ubuntu3.12 [78.2 kB]
    Get:5 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 udev amd64 249.11-0ubuntu3.12 [1,557 kB]
    Get:6 http://archive.ubuntu.com/ubuntu jammy/main amd64 libfuse3-3 amd64 3.10.5-1build1 [81.2 kB]
    Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 snapd amd64 2.66.1+22.04 [27.6 MB]
    Get:8 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 chromium-browser amd64 1:85.0.4183.83-0ubuntu2.22.04.1 [49.2 kB]
    Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 chromium-chromedriver amd64 1:85.0.4183.83-0ubuntu2.22.04.1 [2,308 B]
    Get:10 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 systemd-hwe-hwdb all 249.11.5 [3,228 B]
    Fetched 30.2 MB in 2s (13.0 MB/s)
    Preconfiguring packages ...
    Selecting previously unselected package apparmor.
    (Reading database ... 123632 files and directories currently installed.)
    Preparing to unpack .../apparmor_3.0.4-2ubuntu2.4_amd64.deb ...
    Unpacking apparmor (3.0.4-2ubuntu2.4) ...
    Selecting previously unselected package liblzo2-2:amd64.
    Preparing to unpack .../liblzo2-2_2.10-2build3_amd64.deb ...
    Unpacking liblzo2-2:amd64 (2.10-2build3) ...
    Selecting previously unselected package squashfs-tools.
    Preparing to unpack .../squashfs-tools_1%3a4.5-3build1_amd64.deb ...
    Unpacking squashfs-tools (1:4.5-3build1) ...
    Preparing to unpack .../libudev1_249.11-0ubuntu3.12_amd64.deb ...
    Unpacking libudev1:amd64 (249.11-0ubuntu3.12) over (249.11-0ubuntu3.10) ...
    Setting up libudev1:amd64 (249.11-0ubuntu3.12) ...
    Selecting previously unselected package udev.
    (Reading database ... 123840 files and directories currently installed.)
    Preparing to unpack .../udev_249.11-0ubuntu3.12_amd64.deb ...
    Unpacking udev (249.11-0ubuntu3.12) ...
    Selecting previously unselected package libfuse3-3:amd64.
    Preparing to unpack .../libfuse3-3_3.10.5-1build1_amd64.deb ...
    Unpacking libfuse3-3:amd64 (3.10.5-1build1) ...
    Selecting previously unselected package snapd.
    Preparing to unpack .../snapd_2.66.1+22.04_amd64.deb ...
    Unpacking snapd (2.66.1+22.04) ...
    Setting up apparmor (3.0.4-2ubuntu2.4) ...
    Created symlink /etc/systemd/system/sysinit.target.wants/apparmor.service → /lib/systemd/system/apparmor.service.
    Setting up liblzo2-2:amd64 (2.10-2build3) ...
    Setting up squashfs-tools (1:4.5-3build1) ...
    Setting up udev (249.11-0ubuntu3.12) ...
    invoke-rc.d: could not determine current runlevel
    invoke-rc.d: policy-rc.d denied execution of start.
    Setting up libfuse3-3:amd64 (3.10.5-1build1) ...
    Setting up snapd (2.66.1+22.04) ...
    Created symlink /etc/systemd/system/multi-user.target.wants/snapd.apparmor.service → /lib/systemd/system/snapd.apparmor.service.
    Created symlink /etc/systemd/system/multi-user.target.wants/snapd.autoimport.service → /lib/systemd/system/snapd.autoimport.service.
    Created symlink /etc/systemd/system/multi-user.target.wants/snapd.core-fixup.service → /lib/systemd/system/snapd.core-fixup.service.
    Created symlink /etc/systemd/system/multi-user.target.wants/snapd.recovery-chooser-trigger.service → /lib/systemd/system/snapd.recovery-chooser-trigger.service.
    Created symlink /etc/systemd/system/multi-user.target.wants/snapd.seeded.service → /lib/systemd/system/snapd.seeded.service.
    Created symlink /etc/systemd/system/cloud-final.service.wants/snapd.seeded.service → /lib/systemd/system/snapd.seeded.service.
    Unit /lib/systemd/system/snapd.seeded.service is added as a dependency to a non-existent unit cloud-final.service.
    Created symlink /etc/systemd/system/multi-user.target.wants/snapd.service → /lib/systemd/system/snapd.service.
    Created symlink /etc/systemd/system/timers.target.wants/snapd.snap-repair.timer → /lib/systemd/system/snapd.snap-repair.timer.
    Created symlink /etc/systemd/system/sockets.target.wants/snapd.socket → /lib/systemd/system/snapd.socket.
    Created symlink /etc/systemd/system/final.target.wants/snapd.system-shutdown.service → /lib/systemd/system/snapd.system-shutdown.service.
    Selecting previously unselected package chromium-browser.
    (Reading database ... 124069 files and directories currently installed.)
    Preparing to unpack .../chromium-browser_1%3a85.0.4183.83-0ubuntu2.22.04.1_amd64.deb ...
    => Installing the chromium snap
    ==> Checking connectivity with the snap store
    ===> System doesn't have a working snapd, skipping
    Unpacking chromium-browser (1:85.0.4183.83-0ubuntu2.22.04.1) ...
    Selecting previously unselected package chromium-chromedriver.
    Preparing to unpack .../chromium-chromedriver_1%3a85.0.4183.83-0ubuntu2.22.04.1_amd64.deb ...
    Unpacking chromium-chromedriver (1:85.0.4183.83-0ubuntu2.22.04.1) ...
    Selecting previously unselected package systemd-hwe-hwdb.
    Preparing to unpack .../systemd-hwe-hwdb_249.11.5_all.deb ...
    Unpacking systemd-hwe-hwdb (249.11.5) ...
    Setting up systemd-hwe-hwdb (249.11.5) ...
    Setting up chromium-browser (1:85.0.4183.83-0ubuntu2.22.04.1) ...
    update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/x-www-browser (x-www-browser) in auto mode
    update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/gnome-www-browser (gnome-www-browser) in auto mode
    Setting up chromium-chromedriver (1:85.0.4183.83-0ubuntu2.22.04.1) ...
    Processing triggers for udev (249.11-0ubuntu3.12) ...
    Processing triggers for hicolor-icon-theme (0.17-2) ...
    Processing triggers for libc-bin (2.35-0ubuntu3.4) ...
    /sbin/ldconfig.real: /usr/local/lib/libtbb.so.12 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libtcm.so.1 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libtbbmalloc_proxy.so.2 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libhwloc.so.15 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libtbbmalloc.so.2 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libur_adapter_level_zero.so.0 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_5.so.3 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libtcm_debug.so.1 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libumf.so.0 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_0.so.3 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libtbbbind.so.3 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libur_adapter_opencl.so.0 is not a symbolic link
    
    /sbin/ldconfig.real: /usr/local/lib/libur_loader.so.0 is not a symbolic link
    
    Processing triggers for man-db (2.10.2-1) ...
    Processing triggers for dbus (1.12.20-2ubuntu4.1) ...



```python
!pip install selenium  # Install Selenium
```

    Requirement already satisfied: selenium in /usr/local/lib/python3.10/dist-packages (4.27.1)
    Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.10/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.26.20)
    Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.10/dist-packages (from selenium) (0.27.0)
    Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.10/dist-packages (from selenium) (0.11.1)
    Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.10/dist-packages (from selenium) (2024.8.30)
    Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.10/dist-packages (from selenium) (4.12.2)
    Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.10/dist-packages (from selenium) (1.8.0)
    Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (24.2.0)
    Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (2.4.0)
    Requirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (3.10)
    Requirement already satisfied: outcome in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)
    Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (1.3.1)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (1.2.2)
    Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.10/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)
    Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)
    Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)


### Selenium webdriver in google colab

Create Selenium options

This is an import part because the selenium will not work like usual in your google colab environment, because google colab is Ubuntu terminal based without gui so selenium webdriver will crash immediately upon start so you can add below-mentioned options.


```python
from selenium import webdriver
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver
```


```python
driver = web_driver()

driver.get('https://www.google.com')

# Print the title of the page
print(driver.title)

driver.quit()
```

    Google


### Extracting the HTML


```python
driver = web_driver()
driver.get("http://books.toscrape.com/")
print(driver.title)
print(driver.current_url)
```

    All products | Books to Scrape - Sandbox
    https://books.toscrape.com/



```python
html_content = driver.page_source
html_content
```




    '<html lang="en-us" class="no-js"><!--<![endif]--><head>\n        <title>\n    All products | Books to Scrape - Sandbox\n</title>\n\n        <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n        <meta name="created" content="24th Jun 2016 09:29">\n        <meta name="description" content="">\n        <meta name="viewport" content="width=device-width">\n        <meta name="robots" content="NOARCHIVE,NOCACHE">\n\n        <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->\n        <!--[if lt IE 9]>\n        <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>\n        <![endif]-->\n\n        \n            <link rel="shortcut icon" href="static/oscar/favicon.ico">\n        \n\n        \n        \n    \n    \n        <link rel="stylesheet" type="text/css" href="static/oscar/css/styles.css">\n    \n    <link rel="stylesheet" href="static/oscar/js/bootstrap-datetimepicker/bootstrap-datetimepicker.css">\n    <link rel="stylesheet" type="text/css" href="static/oscar/css/datetimepicker.css">\n\n\n        \n        \n\n        \n\n        \n            \n            \n\n        \n    </head>\n\n    <body id="default" class="default">\n        \n        \n    \n    \n    <header class="header container-fluid">\n        <div class="page_inner">\n            <div class="row">\n                <div class="col-sm-8 h1"><a href="index.html">Books to Scrape</a><small> We love being scraped!</small>\n</div>\n\n                \n            </div>\n        </div>\n    </header>\n\n    \n    \n<div class="container-fluid page">\n    <div class="page_inner">\n        \n    <ul class="breadcrumb">\n        <li>\n            <a href="index.html">Home</a>\n        </li>\n        <li class="active">All products</li>\n    </ul>\n\n        <div class="row">\n\n            <aside class="sidebar col-sm-4 col-md-3">\n                \n                <div id="promotions_left">\n                    \n                </div>\n                \n    \n    \n        \n        <div class="side_categories">\n            <ul class="nav nav-list">\n                \n                    <li>\n                        <a href="catalogue/category/books_1/index.html">\n                            \n                                Books\n                            \n                        </a>\n\n                        <ul>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/travel_2/index.html">\n                            \n                                Travel\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/mystery_3/index.html">\n                            \n                                Mystery\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/historical-fiction_4/index.html">\n                            \n                                Historical Fiction\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/sequential-art_5/index.html">\n                            \n                                Sequential Art\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/classics_6/index.html">\n                            \n                                Classics\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/philosophy_7/index.html">\n                            \n                                Philosophy\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/romance_8/index.html">\n                            \n                                Romance\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/womens-fiction_9/index.html">\n                            \n                                Womens Fiction\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/fiction_10/index.html">\n                            \n                                Fiction\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/childrens_11/index.html">\n                            \n                                Childrens\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/religion_12/index.html">\n                            \n                                Religion\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/nonfiction_13/index.html">\n                            \n                                Nonfiction\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/music_14/index.html">\n                            \n                                Music\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/default_15/index.html">\n                            \n                                Default\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/science-fiction_16/index.html">\n                            \n                                Science Fiction\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/sports-and-games_17/index.html">\n                            \n                                Sports and Games\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/add-a-comment_18/index.html">\n                            \n                                Add a comment\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/fantasy_19/index.html">\n                            \n                                Fantasy\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/new-adult_20/index.html">\n                            \n                                New Adult\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/young-adult_21/index.html">\n                            \n                                Young Adult\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/science_22/index.html">\n                            \n                                Science\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/poetry_23/index.html">\n                            \n                                Poetry\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/paranormal_24/index.html">\n                            \n                                Paranormal\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/art_25/index.html">\n                            \n                                Art\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/psychology_26/index.html">\n                            \n                                Psychology\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/autobiography_27/index.html">\n                            \n                                Autobiography\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/parenting_28/index.html">\n                            \n                                Parenting\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/adult-fiction_29/index.html">\n                            \n                                Adult Fiction\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/humor_30/index.html">\n                            \n                                Humor\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/horror_31/index.html">\n                            \n                                Horror\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/history_32/index.html">\n                            \n                                History\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/food-and-drink_33/index.html">\n                            \n                                Food and Drink\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/christian-fiction_34/index.html">\n                            \n                                Christian Fiction\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/business_35/index.html">\n                            \n                                Business\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/biography_36/index.html">\n                            \n                                Biography\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/thriller_37/index.html">\n                            \n                                Thriller\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/contemporary_38/index.html">\n                            \n                                Contemporary\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/spirituality_39/index.html">\n                            \n                                Spirituality\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/academic_40/index.html">\n                            \n                                Academic\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/self-help_41/index.html">\n                            \n                                Self Help\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/historical_42/index.html">\n                            \n                                Historical\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/christian_43/index.html">\n                            \n                                Christian\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/suspense_44/index.html">\n                            \n                                Suspense\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/short-stories_45/index.html">\n                            \n                                Short Stories\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/novels_46/index.html">\n                            \n                                Novels\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/health_47/index.html">\n                            \n                                Health\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/politics_48/index.html">\n                            \n                                Politics\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/cultural_49/index.html">\n                            \n                                Cultural\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/erotica_50/index.html">\n                            \n                                Erotica\n                            \n                        </a>\n\n                        </li>\n                        \n                \n                    <li>\n                        <a href="catalogue/category/books/crime_51/index.html">\n                            \n                                Crime\n                            \n                        </a>\n\n                        </li>\n                        \n                            </ul></li>\n                        \n                \n            </ul>\n        </div>\n    \n    \n\n            </aside>\n\n            <div class="col-sm-8 col-md-9">\n                \n                <div class="page-header action">\n                    <h1>All products</h1>\n                </div>\n                \n\n                \n\n\n\n<div id="messages">\n\n</div>\n\n\n                <div id="promotions">\n                    \n                </div>\n\n                \n    <form method="get" class="form-horizontal">\n        \n        <div style="display:none">\n            \n            \n        </div>\n\n        \n            \n                \n                    <strong>1000</strong> results - showing <strong>1</strong> to <strong>20</strong>.\n                \n            \n            \n        \n    </form>\n    \n        <section>\n            <div class="alert alert-warning" role="alert"><strong>Warning!</strong> This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.</div>\n\n            <div>\n                <ol class="row">\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Three">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£51.77</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/tipping-the-velvet_999/index.html"><img src="media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg" alt="Tipping the Velvet" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating One">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£53.74</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/soumission_998/index.html"><img src="media/cache/3e/ef/3eef99c9d9adef34639f510662022830.jpg" alt="Soumission" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating One">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/soumission_998/index.html" title="Soumission">Soumission</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£50.10</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/sharp-objects_997/index.html"><img src="media/cache/32/51/3251cf3a3412f53f339e42cac2134093.jpg" alt="Sharp Objects" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Four">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/sharp-objects_997/index.html" title="Sharp Objects">Sharp Objects</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£47.82</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/sapiens-a-brief-history-of-humankind_996/index.html"><img src="media/cache/be/a5/bea5697f2534a2f86a3ef27b5a8c12a6.jpg" alt="Sapiens: A Brief History of Humankind" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Five">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/sapiens-a-brief-history-of-humankind_996/index.html" title="Sapiens: A Brief History of Humankind">Sapiens: A Brief History ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£54.23</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/the-requiem-red_995/index.html"><img src="media/cache/68/33/68339b4c9bc034267e1da611ab3b34f8.jpg" alt="The Requiem Red" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating One">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/the-requiem-red_995/index.html" title="The Requiem Red">The Requiem Red</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£22.65</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html"><img src="media/cache/92/27/92274a95b7c251fea59a2b8a78275ab4.jpg" alt="The Dirty Little Secrets of Getting Your Dream Job" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Four">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html" title="The Dirty Little Secrets of Getting Your Dream Job">The Dirty Little Secrets ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£33.34</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html"><img src="media/cache/3d/54/3d54940e57e662c4dd1f3ff00c78cc64.jpg" alt="The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Three">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html" title="The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull">The Coming Woman: A ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£17.93</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html"><img src="media/cache/66/88/66883b91f6804b2323c8369331cb7dd1.jpg" alt="The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Four">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html" title="The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics">The Boys in the ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£22.60</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/the-black-maria_991/index.html"><img src="media/cache/58/46/5846057e28022268153beff6d352b06c.jpg" alt="The Black Maria" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating One">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/the-black-maria_991/index.html" title="The Black Maria">The Black Maria</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£52.15</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html"><img src="media/cache/be/f4/bef44da28c98f905a3ebec0b87be8530.jpg" alt="Starving Hearts (Triangular Trade Trilogy, #1)" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Two">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html" title="Starving Hearts (Triangular Trade Trilogy, #1)">Starving Hearts (Triangular Trade ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£13.99</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/shakespeares-sonnets_989/index.html"><img src="media/cache/10/48/1048f63d3b5061cd2f424d20b3f9b666.jpg" alt="Shakespeare\'s Sonnets" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Four">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/shakespeares-sonnets_989/index.html" title="Shakespeare\'s Sonnets">Shakespeare\'s Sonnets</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£20.66</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/set-me-free_988/index.html"><img src="media/cache/5b/88/5b88c52633f53cacf162c15f4f823153.jpg" alt="Set Me Free" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Five">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/set-me-free_988/index.html" title="Set Me Free">Set Me Free</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£17.46</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html"><img src="media/cache/94/b1/94b1b8b244bce9677c2f29ccc890d4d2.jpg" alt="Scott Pilgrim\'s Precious Little Life (Scott Pilgrim #1)" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Five">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" title="Scott Pilgrim\'s Precious Little Life (Scott Pilgrim #1)">Scott Pilgrim\'s Precious Little ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£52.29</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/rip-it-up-and-start-again_986/index.html"><img src="media/cache/81/c4/81c4a973364e17d01f217e1188253d5e.jpg" alt="Rip it Up and Start Again" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Five">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/rip-it-up-and-start-again_986/index.html" title="Rip it Up and Start Again">Rip it Up and ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£35.02</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html"><img src="media/cache/54/60/54607fe8945897cdcced0044103b10b6.jpg" alt="Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Three">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html" title="Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991">Our Band Could Be ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£57.25</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/olio_984/index.html"><img src="media/cache/55/33/553310a7162dfbc2c6d19a84da0df9e1.jpg" alt="Olio" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating One">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/olio_984/index.html" title="Olio">Olio</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£23.88</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html"><img src="media/cache/09/a3/09a3aef48557576e1a85ba7efea8ecb7.jpg" alt="Mesaerion: The Best Science Fiction Stories 1800-1849" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating One">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html" title="Mesaerion: The Best Science Fiction Stories 1800-1849">Mesaerion: The Best Science ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£37.59</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/libertarianism-for-beginners_982/index.html"><img src="media/cache/0b/bc/0bbcd0a6f4bcd81ccb1049a52736406e.jpg" alt="Libertarianism for Beginners" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Two">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/libertarianism-for-beginners_982/index.html" title="Libertarianism for Beginners">Libertarianism for Beginners</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£51.33</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">\n\n\n\n\n\n\n    <article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/its-only-the-himalayas_981/index.html"><img src="media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg" alt="It\'s Only the Himalayas" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p class="star-rating Two">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/its-only-the-himalayas_981/index.html" title="It\'s Only the Himalayas">It\'s Only the Himalayas</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£45.17</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>\n\n</li>\n                    \n                </ol>\n                \n\n\n\n    <div>\n        <ul class="pager">\n            \n            <li class="current">\n            \n                Page 1 of 50\n            \n            </li>\n            \n                <li class="next"><a href="catalogue/page-2.html">next</a></li>\n            \n        </ul>\n    </div>\n\n\n            </div>\n        </section>\n    \n\n\n            </div>\n\n        </div><!-- /row -->\n    </div><!-- /page_inner -->\n</div><!-- /container-fluid -->\n\n\n    \n<footer class="footer container-fluid">\n    \n        \n    \n</footer>\n\n\n        \n        \n  \n            <!-- jQuery -->\n            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n            <script>window.jQuery || document.write(\'<script src="static/oscar/js/jquery/jquery-1.9.1.min.js"><\\/script>\')</script><script src="static/oscar/js/jquery/jquery-1.9.1.min.js"></script>\n        \n  \n\n\n        \n        \n    \n        \n    <!-- Twitter Bootstrap -->\n    <script type="text/javascript" src="static/oscar/js/bootstrap3/bootstrap.min.js"></script>\n    <!-- Oscar -->\n    <script src="static/oscar/js/oscar/ui.js" type="text/javascript" charset="utf-8"></script>\n\n    <script src="static/oscar/js/bootstrap-datetimepicker/bootstrap-datetimepicker.js" type="text/javascript" charset="utf-8"></script>\n    <script src="static/oscar/js/bootstrap-datetimepicker/locales/bootstrap-datetimepicker.all.js" type="text/javascript" charset="utf-8"></script>\n\n\n        \n        \n    \n\n    \n\n\n        \n        <script type="text/javascript">\n            $(function() {\n                \n    \n    \n    oscar.init();\n\n    oscar.search.init();\n\n            });\n        </script>\n\n        \n        <!-- Version: N/A -->\n        \n    \n\n</body></html>'



### Parsing the HTML Content


```python
# You can now use BeautifulSoup to parse the HTML content
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract data
print(soup.prettify())
```

    <html class="no-js" lang="en-us">
     <!--<![endif]-->
     <head>
      <title>
       All products | Books to Scrape - Sandbox
      </title>
      <meta content="text/html; charset=utf-8" http-equiv="content-type"/>
      <meta content="24th Jun 2016 09:29" name="created"/>
      <meta content="" name="description"/>
      <meta content="width=device-width" name="viewport"/>
      <meta content="NOARCHIVE,NOCACHE" name="robots"/>
      <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
      <!--[if lt IE 9]>
            <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
            <![endif]-->
      <link href="static/oscar/favicon.ico" rel="shortcut icon"/>
      <link href="static/oscar/css/styles.css" rel="stylesheet" type="text/css"/>
      <link href="static/oscar/js/bootstrap-datetimepicker/bootstrap-datetimepicker.css" rel="stylesheet"/>
      <link href="static/oscar/css/datetimepicker.css" rel="stylesheet" type="text/css"/>
     </head>
     <body class="default" id="default">
      <header class="header container-fluid">
       <div class="page_inner">
        <div class="row">
         <div class="col-sm-8 h1">
          <a href="index.html">
           Books to Scrape
          </a>
          <small>
           We love being scraped!
          </small>
         </div>
        </div>
       </div>
      </header>
      <div class="container-fluid page">
       <div class="page_inner">
        <ul class="breadcrumb">
         <li>
          <a href="index.html">
           Home
          </a>
         </li>
         <li class="active">
          All products
         </li>
        </ul>
        <div class="row">
         <aside class="sidebar col-sm-4 col-md-3">
          <div id="promotions_left">
          </div>
          <div class="side_categories">
           <ul class="nav nav-list">
            <li>
             <a href="catalogue/category/books_1/index.html">
              Books
             </a>
             <ul>
              <li>
               <a href="catalogue/category/books/travel_2/index.html">
                Travel
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/mystery_3/index.html">
                Mystery
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/historical-fiction_4/index.html">
                Historical Fiction
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/sequential-art_5/index.html">
                Sequential Art
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/classics_6/index.html">
                Classics
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/philosophy_7/index.html">
                Philosophy
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/romance_8/index.html">
                Romance
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/womens-fiction_9/index.html">
                Womens Fiction
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/fiction_10/index.html">
                Fiction
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/childrens_11/index.html">
                Childrens
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/religion_12/index.html">
                Religion
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/nonfiction_13/index.html">
                Nonfiction
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/music_14/index.html">
                Music
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/default_15/index.html">
                Default
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/science-fiction_16/index.html">
                Science Fiction
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/sports-and-games_17/index.html">
                Sports and Games
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/add-a-comment_18/index.html">
                Add a comment
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/fantasy_19/index.html">
                Fantasy
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/new-adult_20/index.html">
                New Adult
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/young-adult_21/index.html">
                Young Adult
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/science_22/index.html">
                Science
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/poetry_23/index.html">
                Poetry
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/paranormal_24/index.html">
                Paranormal
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/art_25/index.html">
                Art
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/psychology_26/index.html">
                Psychology
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/autobiography_27/index.html">
                Autobiography
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/parenting_28/index.html">
                Parenting
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/adult-fiction_29/index.html">
                Adult Fiction
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/humor_30/index.html">
                Humor
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/horror_31/index.html">
                Horror
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/history_32/index.html">
                History
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/food-and-drink_33/index.html">
                Food and Drink
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/christian-fiction_34/index.html">
                Christian Fiction
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/business_35/index.html">
                Business
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/biography_36/index.html">
                Biography
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/thriller_37/index.html">
                Thriller
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/contemporary_38/index.html">
                Contemporary
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/spirituality_39/index.html">
                Spirituality
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/academic_40/index.html">
                Academic
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/self-help_41/index.html">
                Self Help
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/historical_42/index.html">
                Historical
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/christian_43/index.html">
                Christian
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/suspense_44/index.html">
                Suspense
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/short-stories_45/index.html">
                Short Stories
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/novels_46/index.html">
                Novels
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/health_47/index.html">
                Health
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/politics_48/index.html">
                Politics
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/cultural_49/index.html">
                Cultural
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/erotica_50/index.html">
                Erotica
               </a>
              </li>
              <li>
               <a href="catalogue/category/books/crime_51/index.html">
                Crime
               </a>
              </li>
             </ul>
            </li>
           </ul>
          </div>
         </aside>
         <div class="col-sm-8 col-md-9">
          <div class="page-header action">
           <h1>
            All products
           </h1>
          </div>
          <div id="messages">
          </div>
          <div id="promotions">
          </div>
          <form class="form-horizontal" method="get">
           <div style="display:none">
           </div>
           <strong>
            1000
           </strong>
           results - showing
           <strong>
            1
           </strong>
           to
           <strong>
            20
           </strong>
           .
          </form>
          <section>
           <div class="alert alert-warning" role="alert">
            <strong>
             Warning!
            </strong>
            This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.
           </div>
           <div>
            <ol class="row">
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/a-light-in-the-attic_1000/index.html">
                 <img alt="A Light in the Attic" class="thumbnail" src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/>
                </a>
               </div>
               <p class="star-rating Three">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">
                 A Light in the ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £51.77
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/tipping-the-velvet_999/index.html">
                 <img alt="Tipping the Velvet" class="thumbnail" src="media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg"/>
                </a>
               </div>
               <p class="star-rating One">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/tipping-the-velvet_999/index.html" title="Tipping the Velvet">
                 Tipping the Velvet
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £53.74
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/soumission_998/index.html">
                 <img alt="Soumission" class="thumbnail" src="media/cache/3e/ef/3eef99c9d9adef34639f510662022830.jpg"/>
                </a>
               </div>
               <p class="star-rating One">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/soumission_998/index.html" title="Soumission">
                 Soumission
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £50.10
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/sharp-objects_997/index.html">
                 <img alt="Sharp Objects" class="thumbnail" src="media/cache/32/51/3251cf3a3412f53f339e42cac2134093.jpg"/>
                </a>
               </div>
               <p class="star-rating Four">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/sharp-objects_997/index.html" title="Sharp Objects">
                 Sharp Objects
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £47.82
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/sapiens-a-brief-history-of-humankind_996/index.html">
                 <img alt="Sapiens: A Brief History of Humankind" class="thumbnail" src="media/cache/be/a5/bea5697f2534a2f86a3ef27b5a8c12a6.jpg"/>
                </a>
               </div>
               <p class="star-rating Five">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/sapiens-a-brief-history-of-humankind_996/index.html" title="Sapiens: A Brief History of Humankind">
                 Sapiens: A Brief History ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £54.23
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/the-requiem-red_995/index.html">
                 <img alt="The Requiem Red" class="thumbnail" src="media/cache/68/33/68339b4c9bc034267e1da611ab3b34f8.jpg"/>
                </a>
               </div>
               <p class="star-rating One">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/the-requiem-red_995/index.html" title="The Requiem Red">
                 The Requiem Red
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £22.65
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html">
                 <img alt="The Dirty Little Secrets of Getting Your Dream Job" class="thumbnail" src="media/cache/92/27/92274a95b7c251fea59a2b8a78275ab4.jpg"/>
                </a>
               </div>
               <p class="star-rating Four">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html" title="The Dirty Little Secrets of Getting Your Dream Job">
                 The Dirty Little Secrets ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £33.34
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html">
                 <img alt="The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull" class="thumbnail" src="media/cache/3d/54/3d54940e57e662c4dd1f3ff00c78cc64.jpg"/>
                </a>
               </div>
               <p class="star-rating Three">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html" title="The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull">
                 The Coming Woman: A ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £17.93
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html">
                 <img alt="The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics" class="thumbnail" src="media/cache/66/88/66883b91f6804b2323c8369331cb7dd1.jpg"/>
                </a>
               </div>
               <p class="star-rating Four">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html" title="The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics">
                 The Boys in the ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £22.60
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/the-black-maria_991/index.html">
                 <img alt="The Black Maria" class="thumbnail" src="media/cache/58/46/5846057e28022268153beff6d352b06c.jpg"/>
                </a>
               </div>
               <p class="star-rating One">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/the-black-maria_991/index.html" title="The Black Maria">
                 The Black Maria
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £52.15
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html">
                 <img alt="Starving Hearts (Triangular Trade Trilogy, #1)" class="thumbnail" src="media/cache/be/f4/bef44da28c98f905a3ebec0b87be8530.jpg"/>
                </a>
               </div>
               <p class="star-rating Two">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html" title="Starving Hearts (Triangular Trade Trilogy, #1)">
                 Starving Hearts (Triangular Trade ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £13.99
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/shakespeares-sonnets_989/index.html">
                 <img alt="Shakespeare's Sonnets" class="thumbnail" src="media/cache/10/48/1048f63d3b5061cd2f424d20b3f9b666.jpg"/>
                </a>
               </div>
               <p class="star-rating Four">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/shakespeares-sonnets_989/index.html" title="Shakespeare's Sonnets">
                 Shakespeare's Sonnets
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £20.66
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/set-me-free_988/index.html">
                 <img alt="Set Me Free" class="thumbnail" src="media/cache/5b/88/5b88c52633f53cacf162c15f4f823153.jpg"/>
                </a>
               </div>
               <p class="star-rating Five">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/set-me-free_988/index.html" title="Set Me Free">
                 Set Me Free
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £17.46
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html">
                 <img alt="Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)" class="thumbnail" src="media/cache/94/b1/94b1b8b244bce9677c2f29ccc890d4d2.jpg"/>
                </a>
               </div>
               <p class="star-rating Five">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" title="Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)">
                 Scott Pilgrim's Precious Little ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £52.29
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/rip-it-up-and-start-again_986/index.html">
                 <img alt="Rip it Up and Start Again" class="thumbnail" src="media/cache/81/c4/81c4a973364e17d01f217e1188253d5e.jpg"/>
                </a>
               </div>
               <p class="star-rating Five">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/rip-it-up-and-start-again_986/index.html" title="Rip it Up and Start Again">
                 Rip it Up and ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £35.02
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html">
                 <img alt="Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991" class="thumbnail" src="media/cache/54/60/54607fe8945897cdcced0044103b10b6.jpg"/>
                </a>
               </div>
               <p class="star-rating Three">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html" title="Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991">
                 Our Band Could Be ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £57.25
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/olio_984/index.html">
                 <img alt="Olio" class="thumbnail" src="media/cache/55/33/553310a7162dfbc2c6d19a84da0df9e1.jpg"/>
                </a>
               </div>
               <p class="star-rating One">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/olio_984/index.html" title="Olio">
                 Olio
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £23.88
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html">
                 <img alt="Mesaerion: The Best Science Fiction Stories 1800-1849" class="thumbnail" src="media/cache/09/a3/09a3aef48557576e1a85ba7efea8ecb7.jpg"/>
                </a>
               </div>
               <p class="star-rating One">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html" title="Mesaerion: The Best Science Fiction Stories 1800-1849">
                 Mesaerion: The Best Science ...
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £37.59
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/libertarianism-for-beginners_982/index.html">
                 <img alt="Libertarianism for Beginners" class="thumbnail" src="media/cache/0b/bc/0bbcd0a6f4bcd81ccb1049a52736406e.jpg"/>
                </a>
               </div>
               <p class="star-rating Two">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/libertarianism-for-beginners_982/index.html" title="Libertarianism for Beginners">
                 Libertarianism for Beginners
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £51.33
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
             <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
              <article class="product_pod">
               <div class="image_container">
                <a href="catalogue/its-only-the-himalayas_981/index.html">
                 <img alt="It's Only the Himalayas" class="thumbnail" src="media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg"/>
                </a>
               </div>
               <p class="star-rating Two">
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
                <i class="icon-star">
                </i>
               </p>
               <h3>
                <a href="catalogue/its-only-the-himalayas_981/index.html" title="It's Only the Himalayas">
                 It's Only the Himalayas
                </a>
               </h3>
               <div class="product_price">
                <p class="price_color">
                 £45.17
                </p>
                <p class="instock availability">
                 <i class="icon-ok">
                 </i>
                 In stock
                </p>
                <form>
                 <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">
                  Add to basket
                 </button>
                </form>
               </div>
              </article>
             </li>
            </ol>
            <div>
             <ul class="pager">
              <li class="current">
               Page 1 of 50
              </li>
              <li class="next">
               <a href="catalogue/page-2.html">
                next
               </a>
              </li>
             </ul>
            </div>
           </div>
          </section>
         </div>
        </div>
        <!-- /row -->
       </div>
       <!-- /page_inner -->
      </div>
      <!-- /container-fluid -->
      <footer class="footer container-fluid">
      </footer>
      <!-- jQuery -->
      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js">
      </script>
      <script>
       window.jQuery || document.write('<script src="static/oscar/js/jquery/jquery-1.9.1.min.js"><\/script>')
      </script>
      <script src="static/oscar/js/jquery/jquery-1.9.1.min.js">
      </script>
      <!-- Twitter Bootstrap -->
      <script src="static/oscar/js/bootstrap3/bootstrap.min.js" type="text/javascript">
      </script>
      <!-- Oscar -->
      <script charset="utf-8" src="static/oscar/js/oscar/ui.js" type="text/javascript">
      </script>
      <script charset="utf-8" src="static/oscar/js/bootstrap-datetimepicker/bootstrap-datetimepicker.js" type="text/javascript">
      </script>
      <script charset="utf-8" src="static/oscar/js/bootstrap-datetimepicker/locales/bootstrap-datetimepicker.all.js" type="text/javascript">
      </script>
      <script type="text/javascript">
       $(function() {
                    
        
        
        oscar.init();
    
        oscar.search.init();
    
                });
      </script>
      <!-- Version: N/A -->
     </body>
    </html>
    


### Extracting specific data


```python
# trying to extract each product name and product price
product_articles = soup.find_all('article', class_='product_pod')

for product in product_articles:
    product_name = product.find('h3')
    product_price = product.find('p',class_='price_color')
    print(product_name.text[:40].ljust(40), '   : ', product_price.text)
```

    A Light in the ...                          :  £51.77
    Tipping the Velvet                          :  £53.74
    Soumission                                  :  £50.10
    Sharp Objects                               :  £47.82
    Sapiens: A Brief History ...                :  £54.23
    The Requiem Red                             :  £22.65
    The Dirty Little Secrets ...                :  £33.34
    The Coming Woman: A ...                     :  £17.93
    The Boys in the ...                         :  £22.60
    The Black Maria                             :  £52.15
    Starving Hearts (Triangular Trade ...       :  £13.99
    Shakespeare's Sonnets                       :  £20.66
    Set Me Free                                 :  £17.46
    Scott Pilgrim's Precious Little ...         :  £52.29
    Rip it Up and ...                           :  £35.02
    Our Band Could Be ...                       :  £57.25
    Olio                                        :  £23.88
    Mesaerion: The Best Science ...             :  £37.59
    Libertarianism for Beginners                :  £51.33
    It's Only the Himalayas                     :  £45.17


### Common Strategies in By


```python
from selenium.webdriver.common.by import By

driver = web_driver()
driver.get("https://en.wikipedia.org/wiki/Product_(business)")
print(driver.title)
print(driver.current_url)
```

    Product (business) - Wikipedia
    https://en.wikipedia.org/wiki/Product_(business)


#### By.ID:

* Searches for elements based on their HTML ID.

* `<div id="element_id">`

* `element = driver.find_element(By.ID, 'element_id')`


```python
element = driver.find_element(By.ID, 'Product_model')
element.text
```




    'Product model'



#### By.CLASS_NAME:

* Finds an element by its class attribute.

* `element = driver.find_element(By.CLASS_NAME, 'class_name')`


```python
# finding no. of times references refered in wikipedia
references_elements = driver.find_elements(By.CLASS_NAME, 'reference')

len(references_elements)
```




    38




```python
# finding no. of references in wikipedia
references_elements = driver.find_elements(By.CLASS_NAME, 'reference-text')

print('total no. of references = ', len(references_elements))
# for ref in references_elements:
#     print(ref.text)
```

    total no. of references =  36


#### By.NAME:

* Finds an element by its name attribute.

* `<input name="element_name">`

* `element = driver.find_element(By.NAME, 'element_name')`


```python
element = driver.find_element(By.NAME, 'skin-client-pref-vector-feature-custom-font-size-group')
element.text
```




    ''



#### By.TAG_NAME:

* Finds an element by its tag name (e.g., div, h1, p, etc.).

* `element = driver.find_element(By.TAG_NAME, 'h1')`


```python
element = driver.find_element(By.TAG_NAME, 'h1')
element.text
```




    'Product (business)'



#### By.CSS_SELECTOR:

* Finds an element using a CSS selector, which is more flexible for complex queries.

* `element = driver.find_element(By.CSS_SELECTOR, 'div.classname')`


```python
# find reference-text - returns first reference
element = driver.find_element(By.CSS_SELECTOR, 'span.reference-text')
element.text
```




    'Kotler, P., Armstrong, G., Brown, L., and Adam, S. (2006) Marketing, 7th Ed. Pearson Education Australia/Prentice Hall.'




```python
# find total no. of references
elements = driver.find_elements(By.CSS_SELECTOR, 'span.reference-text')
len(elements)
```




    36




```python
# find references, that have exteral references(external text)
elements = driver.find_elements(By.CSS_SELECTOR, 'span.reference-text > a.external')
len(elements)
```




    22



#### By.XPATH:

* Finds an element using an XPath expression. This can be very powerful for locating elements based on their position in the DOM or more complex patterns.

* `<span class='classname'><a class='a_classname'>Link</a> </span>`

* `element = driver.find_element(By.XPATH, '//span[@class="classname"]')`


```python
# find reference-text - returns first reference
element = driver.find_element(By.XPATH, '//span[@class="reference-text"]')
element.text
```




    'Kotler, P., Armstrong, G., Brown, L., and Adam, S. (2006) Marketing, 7th Ed. Pearson Education Australia/Prentice Hall.'




```python
# find references, that have exteral references(external text)
elements = driver.find_elements(By.XPATH, '//span[@class="reference-text"]/a[@class="external text"]')
len(elements)
```




    22




#### By.LINK_TEXT:

* Finds a link by its text. Useful for finding anchor (<a>) tags.

* `<a>Click here</a>`

* `element = driver.find_element(By.LINK_TEXT, 'Click here')`


```python
element = driver.find_element(By.LINK_TEXT, 'Log in')
element.text
```




    'Log in'



#### By.PARTIAL_LINK_TEXT:

* Similar to LINK_TEXT, but matches part of the link text.

* `<a>Click here</a>`

* `element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Click')`


```python
element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Log')
element.text
```




    'Log in'



### Taking screenshots




```python
# load the page
driver = web_driver()
driver.get("https://en.wikipedia.org/wiki/Product_(business)")
print(driver.title)
print(driver.current_url)
```

    Product (business) - Wikipedia
    https://en.wikipedia.org/wiki/Product_(business)



```python
# Set the desired window size (optional)
driver.set_window_size(1920, 1080)  # This sets the browser window to 1920x1080

# Take a screenshot and save it to a file
driver.save_screenshot('scraping_screenshot.png')
```




    True




```python
import cv2
from google.colab.patches import cv2_imshow

scraping_screenshot = cv2.imread('scraping_screenshot.png')
cv2_imshow(scraping_screenshot)
```


    
![png](Web_Scraping_Tutorial_files/Web_Scraping_Tutorial_105_0.png)
    


### Handling Interactions (Clicking Buttons, Scrolling)

#### Clicking Buttons


```python
#load the page
driver = web_driver()
driver.get("https://en.wikipedia.org/wiki/Product_(business)")
print(driver.title)
print(driver.current_url)
```

    Product (business) - Wikipedia
    https://en.wikipedia.org/wiki/Product_(business)



```python
# Find a button using its CSS class
button = driver.find_element(By.CSS_SELECTOR, 'button.cdx-button')  # Replace with your button's selector
button.text
```




    'Search'




```python
# Find a button using its CSS class and click it
button = driver.find_element(By.CSS_SELECTOR, 'button.cdx-button')  # Replace with your button's selector
button.click()

# Take a screenshot and save it to a file
driver.save_screenshot('scraping_screenshot_btn_click.png')
```




    True




```python
import cv2
from google.colab.patches import cv2_imshow

scraping_screenshot = cv2.imread('scraping_screenshot_btn_click.png')
cv2_imshow(scraping_screenshot)
```


    
![png](Web_Scraping_Tutorial_files/Web_Scraping_Tutorial_111_0.png)
    


#### Scrolling the Page using JavaScript


```python
driver = web_driver()
driver.get("https://en.wikipedia.org/wiki/Product_(business)")
print(driver.title)
print(driver.current_url)
```

    Product (business) - Wikipedia
    https://en.wikipedia.org/wiki/Product_(business)


Scroll to page bottom by javascript

`window.scrollTo(0, document.body.scrollHeight);`


```python
# Scroll down the page using JavaScript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Take a screenshot and save it to a file
driver.save_screenshot('scraping_screenshot_scroll_page.png')
```




    True




```python
import cv2
from google.colab.patches import cv2_imshow

scraping_screenshot = cv2.imread('scraping_screenshot_scroll_page.png')
cv2_imshow(scraping_screenshot)
```


    
![png](Web_Scraping_Tutorial_files/Web_Scraping_Tutorial_116_0.png)
    


#### Scrolling to an Element (using ActionChains)

ActionChains: This is a class in Selenium that helps with advanced interactions, like mouse movements and keyboard actions. Here, it is used to scroll to the desired element (move_to_element()).


```python
from selenium.webdriver.common.action_chains import ActionChains

# Locate the element you want to scroll to
element = driver.find_element(By.CLASS_NAME, 'mw-heading3')

# Use ActionChains to scroll to the element
actions = ActionChains(driver)
actions.move_to_element(element).perform()


# Take a screenshot and save it to a file
driver.save_screenshot('scraping_screenshot_scroll_to_element.png')
```




    True




```python
import cv2
from google.colab.patches import cv2_imshow

scraping_screenshot = cv2.imread('scraping_screenshot_scroll_to_element.png')
cv2_imshow(scraping_screenshot)
```


    
![png](Web_Scraping_Tutorial_files/Web_Scraping_Tutorial_119_0.png)
    


#### Handling Keyboard Inputs (e.g., typing into text fields)


```python
driver = web_driver()
driver.get("https://en.wikipedia.org/wiki/Product_(business)")
print(driver.title)
print(driver.current_url)
```

    Product (business) - Wikipedia
    https://en.wikipedia.org/wiki/Product_(business)



```python
# click search-button to open search space
driver.set_window_size(1920, 1080)
button = driver.find_element(By.CSS_SELECTOR, 'button.cdx-button')  # Replace with your button's selector
print(button.text)
button.click()
```

    Search



```python
from selenium.webdriver.common.keys import Keys

# Find the text field (e.g., search box) and type into it
search_box = driver.find_element(By.CSS_SELECTOR, 'input.oo-ui-inputWidget-input')  # Replace with your input selector
search_box.send_keys("Purushotham")  # Simulate typing

# Take a screenshot and save it to a file
driver.save_screenshot('scraping_screenshot_keyboard_input_1.png')

search_box.send_keys(Keys.RETURN)  # Simulate pressing Enter

# Take a screenshot and save it to a file
driver.save_screenshot('scraping_screenshot_keyboard_input_2.png')
```




    True




```python
scraping_screenshot = cv2.imread('scraping_screenshot_keyboard_input_1.png')
cv2_imshow(scraping_screenshot)

scraping_screenshot = cv2.imread('scraping_screenshot_keyboard_input_2.png')
cv2_imshow(scraping_screenshot)
```


    
![png](Web_Scraping_Tutorial_files/Web_Scraping_Tutorial_124_0.png)
    



    
![png](Web_Scraping_Tutorial_files/Web_Scraping_Tutorial_124_1.png)
    


####Handling Alerts and Popups


**How to Handle Alerts in Selenium?**

Handling alerts manually is a tedious task. To reduce human intervention and ease this task, Selenium provides a wide range of functionalities and methods to handle alerts.



The following methods are useful to handle alerts in Selenium:

1. Void dismiss(): This method is used when the ‘Cancel’ button is clicked in the alert box.

  `driver.switchTo().alert().dismiss();`

2. Void accept(): This method is used to click on the ‘OK’ button of the alert.

  `driver.switchTo().alert().accept();`

3. String getText(): This method is used to capture the alert message.

  `driver.switchTo().alert().getText();`

4. Void sendKeys(String stringToSend): This method is used to send data to the alert box.

  `driver.switchTo().alert().sendKeys("Text");`


```python
driver = web_driver()
driver.get("https://demoqa.com/alerts")
print(driver.title)
print(driver.current_url)
```

    DEMOQA
    https://demoqa.com/alerts



```python
import time

driver.set_window_size(1920, 1080)
driver.find_element(By.ID, 'alertButton').click()
```


```python
from selenium.webdriver.common.alert import Alert

# Switch to the alert and accept it
alert = Alert(driver)
alert.accept()
```

###Waiting for an element to be present


```python

```
