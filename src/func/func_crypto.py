from src.utils.push_data import PushData
from src.vm.vm_state import VMState


class FuncCrypto(object):
    @staticmethod
    def op_hash(engine):
        x = PushData.pop_bytearray(engine)
        PushData.push_data(engine, PushData.hash(x, engine))
        return VMState.NONE