from src.utils.push_data import PushData
from src.vm.vm_state import VMState


class FuncExceptions(object):
    @staticmethod
    def op_throw(engine):
        return VMState.FAULT

    @staticmethod
    def op_throw_if_not(engine):
        b = PushData.pop_bool(engine)
        if not b:
            return VMState.FAULT
        return VMState.NONE