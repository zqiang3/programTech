import greenlet

def foo(n):
    print "enter foo", n
    test_gr.switch(32)
    print "foo finish"

def test(n):
    print "enter test", n
    foo_gr.switch(23)
    print "test finish"


greenlet = greenlet.greenlet
current = greenlet.getcurrent()
foo_gr = greenlet(foo, current)
test_gr = greenlet(test, current)
foo_gr.switch(2)