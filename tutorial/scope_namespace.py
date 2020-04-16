
def scope_test():
    global t 
    t = "global variable"
    
    def do_local():
        # this spam would not be used outside the function
        spam = "local spam"
        print("Printed inside the do_local:", spam)

    def do_nonlocal():
        # nonlocal variable would be used outside the scope
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        # global variable would be useful outside the module or scope_test
        global spam
        spam = "global spam"

    spam = "test spam"

    do_local()
    print(f"After local assignment {spam}")

    do_nonlocal()
    print(f"After nonlocal assignment {spam}")

    do_global()
    print(f"After global assignment {spam}")

    print("Printed inside the test_scope:", t)

scope_test()
print(f"In global scope: {spam}")
print("Printed outside the test_scope:", t)