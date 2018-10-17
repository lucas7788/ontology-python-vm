
def bigint_from_neo_bytes(ba: bytearray):
    if len(ba) == 0:
        return 0
    ba.reverse()
    return int_from_bytearray(ba)


def int_from_bytearray(ba: bytearray):
    return int.from_bytes(ba, "big", signed=True)