go test命令只能在一个相应的目录下执行所有文件。
文件名必须是 `_test.go`结尾的，这样在执行go test时才会执行到相应的代码。
必须import testing这个包
所有的测试用例函数必须是Test开头。
测试用例会按照源代码中写的顺序依次执行。
`func TestXxx(t *testig.T)`
通过调用testing.T的Error, Errorf, FailNow, Fatal, FatalIf方法，说明测试不通过，调用Log方法用来记录测试的信息。
