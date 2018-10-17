from src.utils.push_data import PushData
from src.vm.vm_state import VMState


class FuncArithmetic(object):

    @staticmethod
    def op_bigint(engine):
        x = PushData.pop_int(engine)
        if x <0:
            PushData.push_data(engine, -1)
        elif x> 0:
            PushData.push_data(engine, 1)
        else:
            PushData.push_data(engine, 0)

        return VMState.NONE

    @staticmethod
    def op_sign(engine):
        x = PushData.pop_int(engine)
        if x < 0:
            PushData.push_data(engine, -1)
        elif x > 0:
            PushData.push_data(engine, 1)
        else:
            PushData.push_data(engine, 0)
        return VMState.NONE

    @staticmethod
    def op_not(engine):
        x = PushData.pop_bool(engine)
        PushData.push_data(engine, not x)
        return VMState.NONE

    @staticmethod
    def op_nz(engine):
        x = PushData.pop_int(engine)
        PushData.push_data(engine, PushData.bigint_comp(x, engine.op_code))
        return VMState.NONE

    @staticmethod
    def op_bigint_zip(engine):
        x2 = PushData.pop_int(engine)
        x1 = PushData.pop_int(engine)
        b = PushData.bigint_zip(x2, x1, engine.op_code)
        PushData.push_data(engine, b)
        return VMState.NONE

    @staticmethod
    def op_bigint_comp(engine):
        print(engine.evaluation_stack.e[0].value)
        print(engine.evaluation_stack.e[1].value)
        x2 = PushData.pop_int(engine)
        x1 = PushData.pop_int(engine)
        b = PushData.bigint_multi_comp(x1, x2, engine.op_code)
        PushData.push_data(engine, b)
        return VMState.NONE

    @staticmethod
    def op_bool_zip(engine):
        x2 = PushData.pop_bool(engine)
        x1 = PushData.pop_bool(engine)
        b = PushData.bool_zip(x2, x1, engine.op_code)
        PushData.push_data(engine, b)
        return VMState.NONE

    @staticmethod
    def op_within(engine):
        b = PushData.pop_int(engine)
        a = PushData.pop_int(engine)
        c = PushData.pop_int(engine)
        PushData.push_data(engine, PushData.within_op(c, a, b))
        return VMState.NONE