import os
if os.path.exists('Demo.txt'):
    os.remove("Demo.txt")
else:
    print("Not Supported")