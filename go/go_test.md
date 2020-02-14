go test命令只能在一个相应的目录下执行所有文件。
文件名必须是 `_test.go`结尾的，这样在执行go test时才会执行到相应的代码。
必须import testing这个包
所有的测试用例函数必须是Test开头。
测试用例会按照源代码中写的顺序依次执行。
`func TestXxx(t *testig.T)`
通过调用testing.T的Error, Errorf, FailNow, Fatal, FatalIf方法，说明测试不通过，调用Log方法用来记录测试的信息。



## stretchr/testify

link: https://github.com/stretchr/testify



### assert

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {

  // assert equality
  assert.Equal(t, 123, 123, "they should be equal")

  // assert inequality
  assert.NotEqual(t, 123, 456, "they should not be equal")

  // assert for nil (good for errors)
  assert.Nil(t, object)

  // assert for not nil (good when you expect something)
  if assert.NotNil(t, object) {

    // now we know that object isn't nil, we are safe to make
    // further assertions without causing any errors
    assert.Equal(t, "Something", object.Value)

  }

}
```

### mock

