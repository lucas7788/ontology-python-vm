from src.utils.push_data import PushData
from src.vm.vm_state import VMState


class FuncSplice(object):
    @staticmethod
    def op_cat(engine):
        bs2 = PushData.pop_bytearray(engine)
        bs1 = PushData.pop_bytearray(engine)
        r = PushData.concat(bs1, bs2)
        PushData.push_data(engine, r)
        return VMState.NONE

    @staticmethod
    def op_sub_str(engine):
        count = PushData.pop_int(engine)
        index = PushData.pop_int(engine)
        arr = PushData.pop_bytearray(engine)
        bs = arr[index:index + count]
        PushData.push_data(engine, bs)
        return VMState.NONE

    @staticmethod
    def op_left(engine):
        count = PushData.pop_int(engine)
        arr = PushData.pop_bytearray(engine)
        bs = arr[0:count]
        PushData.push_data(engine, bs)
        return VMState.NONE

    @staticmethod
    def op_right(engine):
        count = PushData.pop_int(engine)
        arr = PushData.pop_bytearray(engine)
        bs = arr[len(arr) - count:]
        PushData.push_data(engine, bs)
        return VMState.NONE

    @staticmethod
    def op_size(engine):
        arr = PushData.pop_bytearray(engine)
        PushData.push_data(engine, len(arr))
        return VMState.NONE