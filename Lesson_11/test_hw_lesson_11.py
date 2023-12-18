import time


def test_sleep_1():
    print("I'm going to sleep for 2 seconds")
    time.sleep(2)


def test_uniqe_sleep():
    print("I'm going to UNIQE sleep for 2 seconds")
    time.sleep(2)


def test_sleep_3():
    print("I'm going to sleep for 2 seconds")
    time.sleep(2)


def test_sleep_4():
    print("I'm going to sleep for 2 seconds")
    time.sleep(2)


def test_sleep_5():
    print("I'm going to sleep for 2 seconds")
    time.sleep(2)

# pytest .\test_hw_lesson_11.py -v -k "uniqe"
# pytest .\test_hw_lesson_11.py -v -n=5
# flake8 --ignore=E501 .\test_hw_lesson_11.py
