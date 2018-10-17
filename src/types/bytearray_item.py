from src.types.stack_items import StackItems
from src.utils.define import bigint_from_neo_bytes


class ByteArrayItem(StackItems):

    def __init__(self, val: bytearray):
        self.value = val

    def get_bytearray(self):
        return self.value

    def get_biginteger(self):
        return bigint_from_neo_bytes(bytearray(self.value))

    def equals(self, other):
        if self == other:
            return True
        a1 = self.value
        a2 = other.get_bytearray()
        if a1.hex() == a2.hex():
            return True
        return False




