# 命名空间和作用域

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


'''
A namespace is a mapping from names to objects.Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future.
A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

the innermost scope, which is searched first, contains the local names
the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
the next-to-last scope contains the current module’s global names
the outermost scope (searched last) is the namespace containing built-in names
'''
