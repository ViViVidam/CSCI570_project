# This is a sample Python script.
import sys
from module import Generator
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

### generator calling
# 1. set filepath
# 2. call parseFile(), on error will return "error" string
if __name__ == '__main__':
    generator = Generator(sys.argv[1])
    stringOne, stringTwo = generator.parseFile()
    print(f'{stringOne}\n{stringTwo}')