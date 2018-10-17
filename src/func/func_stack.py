from src.utils.push_data import PushData
from src.vm.vm_state import VMState


class FuncStack(object):
    @staticmethod
    def op_to_dup_from_alt_stack(engine):
        PushData.push(engine, engine.alt_stack.peek(0))
        return VMState.NONE

    @staticmethod
    def op_to_alt_stack(engine):
        engine.alt_stack.push(PushData.pop_stack_item(engine))
        return VMState.NONE

    @staticmethod
    def op_from_alt_stack(engine):
        items = engine.alt_stack.pop()
        PushData.push(engine, items)
        return VMState.NONE

    @staticmethod
    def op_x_drop(engine):
        n = PushData.pop_int(engine)
        engine.alt_stack.remove(n)
        return VMState.NONE

    @staticmethod
    def op_x_swap(engine):
        n = PushData.pop_int(engine)
        if n == 0:
            return VMState.NONE
        engine.evaluation_stack.swap(0, n)
        return VMState.NONE

    @staticmethod
    def op_x_tuck(engine):
        n = PushData.pop_int(engine)
        engine.evaluation_stack.insert(n, PushData.peek_stack_item(engine))
        return VMState.NONE

    @staticmethod
    def op_depth(engine):
        PushData.push_data(engine, PushData.count(engine))
        return VMState.NONE

    @staticmethod
    def op_drop(engine):
        PushData.pop_stack_item(engine)
        return VMState.NONE

    @staticmethod
    def op_dup(engine):
        items = PushData.peek_stack_item(engine)
        PushData.push(engine, items)
        return VMState.NONE

    @staticmethod
    def op_nip(engine):
        x2 = PushData.pop_stack_item(engine)
        PushData.peek_stack_item(engine)
        PushData.push(engine, x2)
        return VMState.NONE

    @staticmethod
    def op_over(engine):
        x2 = PushData.pop_stack_item(engine)
        x1 = PushData.peek_stack_item(engine)
        PushData.peek_stack_item(engine)
        PushData.push(engine, x2)
        PushData.push(engine, x1)
        return VMState.NONE



    @staticmethod
    def op_pick(engine):
        n = PushData.pop_int(engine)
        if n == 0:
            return VMState.NONE
        PushData.push(engine, engine.evaluation_stack.peek(n))
        return VMState.NONE

    @staticmethod
    def op_roll(engine):
        n = PushData.pop_int(engine)
        if n == 0:
            return VMState.NONE
        PushData.push(engine, engine.evaluation_stack.remove(n))
        return VMState.NONE

    @staticmethod
    def op_rot(engine):
        x3 = PushData.pop_stack_item(engine)
        x2 = PushData.pop_stack_item(engine)
        x1 = PushData.pop_stack_item(engine)
        PushData.push(engine, x2)
        PushData.push(engine, x3)
        PushData.push(engine, x1)
        return VMState.NONE

    @staticmethod
    def op_swap(engine):
        x2 = PushData.pop_stack_item(engine)
        x1 = PushData.pop_stack_item(engine)
        PushData.push(engine, x2)
        PushData.push(engine, x1)
        return VMState.NONE

    @staticmethod
    def op_tuck(engine):
        x2 = PushData.pop_stack_item(engine)
        x1 = PushData.pop_stack_item(engine)
        PushData.push(engine, x2)
        PushData.push(engine, x1)
        PushData.push(engine, x2)
        return VMState.NONE