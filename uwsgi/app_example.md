## ex1

```python
def application(environ, start_response):
    from io import StringIO
    sio = StringIO()
    sio.write('hello world!\n')
    for k, v in environ.items():
        print(k, '=', repr(v))
        sio.write('{0} = {1}\n'.format(k, v))

    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    return [sio.getvalue().encode('utf-8')]
```

