import sys

from behave import __main__ as TestRunner

# print(sys.path)

if __name__=='__main__':
        sys.stdout.flush()
        TestRunner.main()


# test_runner()