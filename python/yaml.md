YAML使用冒号加缩进的方式代表层级（属性）关系，使用短横杠(-)代表数组元素。

```yaml
#YAML格式
environments:
    dev:
        url: http://dev.bar.com
        name: Developer Setup
    prod:
        url: http://foo.bar.com
        name: My Cool App
my:
    servers:
        - dev.bar.com
        - foo.bar.com
```



```python
pip install pyyaml

```

