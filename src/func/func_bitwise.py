from src.utils.push_data import PushData
from src.vm.vm_state import VMState


class FuncBitwise(object):

    @staticmethod
    def op_invert(engine):
        i = PushData.pop_int()
        PushData.push_data(engine, i)
        return VMState.NONE

    @staticmethod
    def op_equal(engine):
        b1 = PushData.pop_stack_item(engine)
        b2 = PushData.pop_stack_item(engine)
        PushData.push_data(engine, b1.equals(b2))
        return VMState.NONE