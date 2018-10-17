from ontology.crypto.digest import Digest
from src.types.array_item import ArrayItem
from src.types.bool_item import BoolItem
from src.types.bytearray_item import ByteArrayItem
from src.types.integer_item import IntegerItem
from src.types.interop_item import InteropItem
from src.types.map_item import MapItem
from src.types.stack_items import StackItems
from src.types.struct_item import StructItem
from src.utils.script_op import ScriptOp
from src.vm.vm_state import VMState


class PushData(object):
    @staticmethod
    def op_push_data(engine):
        data = PushData.get_push_data(engine)
        PushData.push_data(engine, data)
        return VMState.NONE

    @staticmethod
    def get_push_data(e):
        data = None
        if ScriptOp.OP_PUSHBYTES1.value <= e.op_code.value <= ScriptOp.OP_PUSHBYTES75.value:
            data = e.context.op_reader.read_bytes(e.op_code.value)
        if e.op_code == ScriptOp.OP_PUSH0:
            data = 0
        elif e.op_code == ScriptOp.OP_PUSHDATA1:
            b = e.context.op_reader.read_byte()
            data = e.context.op_reader.read_bytes(b)
        elif e.op_code == ScriptOp.OP_PUSHDATA2:
            data = e.context.op_reader.read_bytes(2)
        elif e.op_code == ScriptOp.OP_PUSHDATA4:
            data = e.context.op_reader.read_bytes(4)
        elif e.op_code == ScriptOp.OP_PUSH1 or ScriptOp.OP_PUSH1.value <= e.op_code.value <= ScriptOp.OP_PUSH16.value:
            data = e.op_code.value - ScriptOp.OP_PUSH1.value + 1
        return data

    @staticmethod
    def push_data(engine, data):
        if type(data) is int:
            engine.evaluation_stack.push(IntegerItem(data))
        elif type(data) is bool:
            engine.evaluation_stack.push(BoolItem(data))
        elif type(data) is bytearray or type(data) is bytes:
            engine.evaluation_stack.push(ByteArrayItem(data))
        elif type(data) is ArrayItem:
            engine.evaluation_stack.push(ArrayItem(data.stack_items))
        elif type(data) is IntegerItem:
            engine.evaluation_stack.push(data)
        elif type(data) is BoolItem:
            engine.evaluation_stack.push(data)
        elif type(data) is ByteArrayItem:
            engine.evaluation_stack.push(data)
        elif type(data) is MapItem:
            engine.evaluation_stack.push(data)
        elif type(data) is StructItem:
            engine.evaluation_stack.push(data)
        elif type(data) is StackItems:
            engine.evaluation_stack.push(data)
        elif type(data) is list:
            engine.evaluation_stack.push(ArrayItem(data))
        elif type(data) is InteropItem:
            engine.evaluation_stack.push(data)

    @staticmethod
    def concat(array1: bytearray, array2: bytearray):
        return array1 + array2


    @staticmethod
    def bool_zip(a: bool, b: bool, op: ScriptOp):
        if op == ScriptOp.BOOLAND:
            return a and b
        if op == ScriptOp.BOOLOR:
            return a or b
        return False

    @staticmethod
    def within_op(a: int, b: int, c: int):
        b1 = PushData.bigint_multi_comp(a, b, ScriptOp.GTE)
        b2 = PushData.bigint_multi_comp(a, c, ScriptOp.GTE)
        return PushData.bool_zip(b1, b2, ScriptOp.BOOLOR)

    @staticmethod
    def bigint_multi_comp(a: int, b: int, op: ScriptOp):
        if op == ScriptOp.OP_NUMEQUAL:
            return PushData.compare_to(a, b) == 0
        elif op == ScriptOp.OP_NUMNOTEQUAL:
            return PushData.compare_to(a, b) != 0
        elif op == ScriptOp.OP_LT:
            return PushData.compare_to(a, b) < 0
        elif op == ScriptOp.OP_GT:
            return PushData.compare_to(a, b) > 0
        elif op == ScriptOp.OP_LTE:
            return PushData.compare_to(a, b) <= 0
        elif op == ScriptOp.OP_GTE:
            return PushData.compare_to(a, b) >= 0
        return False

    @staticmethod
    def bigint_zip(a: int, b: int, op: ScriptOp):
        if op == ScriptOp.AND:
            return a and b
        elif op == ScriptOp.OR:
            return a or b
        elif op == ScriptOp.XOR:
            return a ^ b
        elif op == ScriptOp.ADD:
            return a + b
        elif op == ScriptOp.SUB:
            return a - b
        elif op == ScriptOp.MUL:
            return a * b
        elif op == ScriptOp.DIV:
            return a / b
        elif op == ScriptOp.MOD:
            return a % b
        elif op == ScriptOp.SHL:
            return a << b
        elif op == ScriptOp.SHR:
            return a >> b
        elif op == ScriptOp.MIN:
            if a < b:
                return a
            else:
                return b
        elif op == ScriptOp.MAX:
            if a < b:
                return b
            else:
                return a
        return None

    @staticmethod
    def compare_to(a: int, b: int):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    @staticmethod
    def bigint_comp(a: int, op: ScriptOp):
        if op == ScriptOp.NZ:
            return PushData.compare_to(a, 0) != 0
        return False

    @staticmethod
    def bigint_op(a: int, op: ScriptOp):
        if op == ScriptOp.INC:
            return a + 1
        elif op == ScriptOp.DEC:
            return a - 1
        elif op == ScriptOp.NEGATE:
            return -a
        elif op == ScriptOp.ABS:
            return a.__abs__()
        return a

    @staticmethod
    def hash(bs: bytearray, engine):
        if engine.op_code == ScriptOp.SHA1:
            return None
        elif engine.op_code == ScriptOp.SHA256:
            return Digest.sha256(bs)
        elif engine.op_code == ScriptOp.HASH160:
            return Digest.hash160(bs)
        elif engine.op_code == ScriptOp.HASH256:
            return Digest.hash256(bs)
        return None

    @staticmethod
    def pop_array(engine):
        return engine.evaluation_stack.pop().get_array()

    @staticmethod
    def pop_bytearray(engine):
        return engine.evaluation_stack.pop().get_bytearray()

    @staticmethod
    def pop_stack_item(engine):
        return engine.evaluation_stack.pop()

    @staticmethod
    def peek_stack_item(engine):
        return engine.evaluation_stack.peek(0)

    @staticmethod
    def pop_int(engine):
        item = engine.evaluation_stack.pop()
        return item.get_biginteger()

    @staticmethod
    def push(engine, ele: StackItems):
        engine.evaluation_stack.push(ele)

    @staticmethod
    def pop_bool(engine):
        return engine.evaluation_stack.pop().get_bool()

    @staticmethod
    def evaluation_stack_count(engine):
        return engine.evaluation_stack.count()

    @staticmethod
    def pop_interop_interface(engine):
        res = engine.evaluation_stack.pop()
        return res.get_interface()

    @staticmethod
    def peek_biginteger(engine):
        return PushData.peek_stack_item(engine).get_biginteger()

    @staticmethod
    def peek_n_stack_item(i: int, engine):
        return engine.evaluation_stack.peek(i)

    @staticmethod
    def count(engine):
        return engine.evaluation_stack.count()





