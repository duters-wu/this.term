import cv2

def test(item: int):
    if item < 10000:
        print(item)
        test(item + 1)

test(1) # maximum recursion depth is 996