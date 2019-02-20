```python
import requests
r = requests.get('https://api.github.com/events')
r = requests.post('http://httpbin.org/post', data = {'key':'value'})

>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('http://httpbin.org/delete')
>>> r = requests.head('http://httpbin.org/get')
>>> r = requests.options('http://httpbin.org/get')

# 传递url参数
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get("http://httpbin.org/get", params=payload)

# 响应头
headers = {'user-agent': 'my-app/0.0.1'}
r.request.get(url, headers=headers)

# 响应内容
r.text
r.encoding
r.content
r.json()
r.raw
r.raw.read(10)
```

