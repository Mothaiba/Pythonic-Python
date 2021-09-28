class C:
    def foo():
        print("This is before monkey-patched.")


C.foo()  # output: This is before monkey-patched.


def new_foo():
    print("This is after monkey-patched.")


# monkey-patching
C.foo = new_foo

C.foo()  # output: This is after monkey-patched.
