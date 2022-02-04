import inspect
from termcolor import colored
from test_classes.test_palisade import TestPALISADE

test_classes = [TestPALISADE]
n_tests = 0
n_passed = 0
n_failed = 0

for test_class in test_classes:
    test_class_obj = test_class()
    attrs = (getattr(test_class_obj, name) for name in dir(test_class_obj))
    methods = filter(inspect.ismethod, attrs)
    for method in methods:
        if method.__name__ == "__init__":
            continue
        n_tests += 1
        res = method()
        if res is not True:
            print(colored(method.__name__[5:] + " test failed: " + res, 'red'))
            n_failed += 1
            continue
        print(colored(method.__name__[5:] + " test passed", 'green'))
        n_passed += 1

result_color = 'red'
if n_passed == n_tests:
    result_color = 'green'

print(colored('\n==========================', result_color))
print(colored(f"TEST SUMMARY: {n_passed}/{n_tests} ({round(n_passed/n_tests * 100 , 1)}%)", result_color))
print(colored('==========================\n', result_color))

print(colored(f"Number of Tests Passed = {n_passed}", 'green'))
print(colored(f"Number of Tests Failed = {n_failed}", 'red'))


