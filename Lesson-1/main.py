import sys
from platform import python_version


if __name__ == "__main__":
    if 3/2 != 1.5:
        print('You are using Python:', python_version() , ', Your code wont work here!!')
        sys.exit(1)
    else:
        print("You are using Python version:", python_version(), "Welcome!!")
	sys.exit(1)

