def parent(num=10):
    print("printing from parent function {} ".format(num))
    def foo():
        print("printing from foo() function")
    def bar():
        print("printing from bar() function")
    if num == 10:
        return foo
    else:
        return bar
#foo=parent()
#bar=parent(11)
print(foo)
print(bar)

print(foo())
print(bar())

foo()
