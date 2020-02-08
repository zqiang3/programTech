This module implements a file-like class, [`StringIO`](https://docs.python.org/2/library/stringio.html#StringIO.StringIO), that reads and writes a string buffer (also known as *memory files*).



## Usage

```python
import StringIO

output = StringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
```

