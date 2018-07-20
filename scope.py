def scope_test():
    def do_local():
        spam = "local spam"

    def do_non_local():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "spam test"
    do_local()
    print("after local assignment - " + spam)
    do_non_local()
    print("after nonlocal assignment - " + spam)
    do_global()
    print("after global assignment - " + spam)

scope_test()
print("In global scope:", spam)