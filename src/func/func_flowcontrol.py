from src.utils.push_data import PushData
from src.utils.script_op import ScriptOp
from src.vm.vm_state import VMState


class FuncFlowControl(object):
    @staticmethod
    def op_nop(engine):
        return VMState.NONE

    @staticmethod
    def op_jmp(engine):
        offset = engine.context.op_reader.read_int16()
        offset = engine.context.get_instruction_pointer() + offset - 3
        if offset < 0 or offset > len(engine.context.code):
            return VMState.FAULT
        f_value = True
        if engine.op_code.value > ScriptOp.OP_JMP.value:
            if PushData.evaluation_stack_count(engine) < 1:
                return VMState.FAULT
            f_value = PushData.pop_bool(engine)
            print("pop_bool: ", f_value)
            if engine.op_code == ScriptOp.OP_JMPIFNOT:
                f_value = not f_value
        if f_value:
            engine.context.set_instruction_pointer(offset)
        print("fvalue: ", f_value)
        print("******get_instruction_pointer: ", engine.context.get_instruction_pointer())
        return VMState.NONE

    @staticmethod
    def op_call(engine):
        execution_context = engine.context.clone()
        engine.context.set_instruction_pointer(engine.context.get_instruction_pointer() + 2)
        engine.op_code = ScriptOp.OP_JMP
        engine.push_context(execution_context)
        return FuncFlowControl.op_jmp(engine)

    @staticmethod
    def op_ret(engine):
        engine.pop_context()
        return VMState.NONE