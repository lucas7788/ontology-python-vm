import unittest

from src.types.bytearray_item import ByteArrayItem
from src.types.integer_item import IntegerItem
from src.vm.random_access_stack import RandomAccessStack


class TestRandom(unittest.TestCase):
    def test_random(self):
        ras = RandomAccessStack()
        item = IntegerItem(100)
        item2 = ByteArrayItem("sss".encode())
        ras.push(item)
        ras.push(item2)
        print("###########")
        print(ras.e)
        # print(ras.peek(0))
        # print(ras.e)

        # print(ras.pop())
        # print(ras.e)

        # item3 = IntegerItem(200)
        # ras.push(item3, 1)

        print(ras.e)