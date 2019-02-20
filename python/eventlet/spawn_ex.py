from eventlet import spawn


def foo(n):
    print "enter foo", n
    print "foo finish"
    return 'foo result'


def bar(n):
    print "enter bar", n
    print "bar finish"
    return "bar result"


def other(n):
    print "enter other", n
    print "other finish"
    return "other result"

n = 3
print "program begin"
foo_ret = spawn(foo, n)
print "get foo_ret"
bar_ret = spawn(bar, n)
print "get bar_ret"
other_ret = spawn(other, 10)

print "begin foo_ret_wait"
other_result = other_ret.wait()
print 'other_result', other_result
foo_result = foo_ret.wait()
print 'foo_result', foo_result
print "begin bar_ret_wait"
bar_result = bar_ret.wait()
print 'bar_result', bar_result
print "finish all"
