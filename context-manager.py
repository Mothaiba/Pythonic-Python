# use `with` to open file
with open(file_path, 'r') as f:
    content = f.read()


# use `with` for multi-thread programming

with some_lock:
    # do something

# # is equivalent to:

some_lock.acquire()
try:
    # do something
finally:
    somelock.release()