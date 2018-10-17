from src.func.func_arithmetic import FuncArithmetic
from src.func.func_array import FuncArray
from src.func.func_bitwise import FuncBitwise
from src.func.func_crypto import FuncCrypto
from src.func.func_exceptions import FuncExceptions
from src.func.func_flowcontrol import FuncFlowControl
from src.func.func_splice import FuncSplice
from src.func.func_stack import FuncStack
from src.types.array_item import ArrayItem
from src.types.map_item import MapItem
from src.types.struct_item import StructItem
from src.utils.push_data import PushData
from src.utils.script_op import ScriptOp
from src.vm.op_exec import OpExec


class OpExecList(object):
    op_exec_list = dict()

    @staticmethod
    def get_op_exec(op: ScriptOp):
        if len(OpExecList.op_exec_list) == 0:
            OpExecList.init()
        return OpExecList.op_exec_list[op]

    @staticmethod
    def init():
        opPushData = getattr(PushData(), "op_push_data")
        opNop = getattr(FuncFlowControl(), "op_nop")
        opJmp = getattr(FuncFlowControl(), "op_jmp")
        opCall = getattr(FuncFlowControl(), "op_call")
        opRet = getattr(FuncFlowControl(), "op_ret")
        opToAltStack = getattr(FuncStack(), "op_to_alt_stack")
        opToDupFromAltStack = getattr(FuncStack(), "op_to_dup_from_alt_stack")
        opFromAltStack = getattr(FuncStack(), "op_from_alt_stack")
        opXDrop = getattr(FuncStack(), "op_x_drop")
        opXSwap = getattr(FuncStack(), "op_x_swap")
        opXTuck = getattr(FuncStack(), "op_x_tuck")
        opDepth = getattr(FuncStack(), "op_depth")
        opDrop = getattr(FuncStack(), "op_drop")
        opDup = getattr(FuncStack(), "op_dup")
        opNip = getattr(FuncStack(), "op_nip")
        opOver = getattr(FuncStack(), "op_over")
        opPick = getattr(FuncStack(), "op_pick")
        opRoll = getattr(FuncStack(), "op_roll")
        opRot = getattr(FuncStack(), "op_rot")
        opSwap = getattr(FuncStack(), "op_swap")
        opTuck = getattr(FuncStack(), "op_tuck")
        opCat = getattr(FuncSplice(), "op_cat")
        opSubStr = getattr(FuncSplice(), "op_sub_str")
        opLeft = getattr(FuncSplice(), "op_left")
        opRight = getattr(FuncSplice(), "op_right")
        opSize = getattr(FuncSplice(), "op_size")
        opInvert = getattr(FuncBitwise(), "op_invert")
        opBigIntZip = getattr(FuncArithmetic(), "op_bigint_zip")
        opEqual = getattr(FuncBitwise(), "op_equal")
        opBigInt = getattr(FuncArithmetic(), "op_bigint")
        opSign = getattr(FuncArithmetic(), "op_sign")
        opNot = getattr(FuncArithmetic(), "op_not")
        opNz = getattr(FuncArithmetic(), "op_nz")
        opBoolZip = getattr(FuncArithmetic(), "op_bool_zip")
        opBigIntComp = getattr(FuncArithmetic(), "op_bigint_comp")
        opWithIn = getattr(FuncArithmetic(), "op_within")
        opHash = getattr(FuncCrypto(), "op_hash")
        opArraySize = getattr(FuncArray(), "op_array_size")
        opPack = getattr(FuncArray(), "op_pack")
        opUnpack = getattr(FuncArray(), "op_unpack")
        opPickItem = getattr(FuncArray(), "op_pick_item")
        opSetItem = getattr(FuncArray(), "op_set_item")
        opNewArray = getattr(FuncArray(), "op_new_array")
        opNewMap = getattr(FuncArray(), "op_new_map")
        opNewStruct = getattr(FuncArray(), "op_new_struct")
        opAppend = getattr(FuncArray(), "op_append")
        opReverse = getattr(FuncArray(), "op_reverse")
        opThrow = getattr(FuncExceptions(), "op_throw")
        opThrowIfNot = getattr(FuncExceptions(), "op_throw_if_not")
        validatePickItem = getattr(OpExecList(), "validatePickItem")

        OpExecList.op_exec_list[ScriptOp.OP_PUSH0] = OpExec(ScriptOp.OP_PUSH0, "PUSH0", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSHBYTES1] = OpExec(ScriptOp.OP_PUSHBYTES1, "PUSHBYTES1", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSHBYTES75] = OpExec(ScriptOp.OP_PUSHBYTES75, "PUSHBYTES75", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSHDATA1] = OpExec(ScriptOp.OP_PUSHDATA1, "OP_PUSHDATA1", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSHDATA2] = OpExec(ScriptOp.OP_PUSHDATA2, "PUSH0", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSHDATA4] = OpExec(ScriptOp.OP_PUSHDATA4, "OP_PUSHDATA4", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSHM1] = OpExec(ScriptOp.OP_PUSHM1, "OP_PUSHM1", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH1] = OpExec(ScriptOp.OP_PUSH1, "OP_PUSH1", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH2] = OpExec(ScriptOp.OP_PUSH2, "OP_PUSH2", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH3] = OpExec(ScriptOp.OP_PUSH3, "OP_PUSH3", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH4] = OpExec(ScriptOp.OP_PUSH4, "OP_PUSH4", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH5] = OpExec(ScriptOp.OP_PUSH5, "OP_PUSH5", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH6] = OpExec(ScriptOp.OP_PUSH6, "OP_PUSH6", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH7] = OpExec(ScriptOp.OP_PUSH7, "OP_PUSH7", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH8] = OpExec(ScriptOp.OP_PUSH8, "OP_PUSH8", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH9] = OpExec(ScriptOp.OP_PUSH9, "OP_PUSH9", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH10] = OpExec(ScriptOp.OP_PUSH10, "OP_PUSH10", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH11] = OpExec(ScriptOp.OP_PUSH11, "OP_PUSH11", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH12] = OpExec(ScriptOp.OP_PUSH12, "OP_PUSH12", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH13] = OpExec(ScriptOp.OP_PUSH13, "OP_PUSH13", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH14] = OpExec(ScriptOp.OP_PUSH14, "OP_PUSH14", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH15] = OpExec(ScriptOp.OP_PUSH15, "OP_PUSH15", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_PUSH16] = OpExec(ScriptOp.OP_PUSH16, "OP_PUSH16", opPushData, None)
        OpExecList.op_exec_list[ScriptOp.OP_NOP] = OpExec(ScriptOp.OP_NOP, "OP_NOP", opNop, None)
        OpExecList.op_exec_list[ScriptOp.OP_JMP] = OpExec(ScriptOp.OP_JMP, "OP_JMP", opJmp, None)
        OpExecList.op_exec_list[ScriptOp.OP_JMPIF] = OpExec(ScriptOp.OP_JMPIF, "OP_JMPIF", opJmp, None)
        OpExecList.op_exec_list[ScriptOp.OP_JMPIFNOT] = OpExec(ScriptOp.OP_JMPIFNOT, "OP_JMPIFNOT", opJmp, None)
        OpExecList.op_exec_list[ScriptOp.OP_CALL] = OpExec(ScriptOp.OP_CALL, "OP_CALL", opCall, None)
        OpExecList.op_exec_list[ScriptOp.OP_RET] = OpExec(ScriptOp.OP_RET, "OP_RET", opRet, None)
        OpExecList.op_exec_list[ScriptOp.OP_APPCALL] = OpExec(ScriptOp.OP_APPCALL, "OP_APPCALL", None, None)
        OpExecList.op_exec_list[ScriptOp.OP_SYSCALL] = OpExec(ScriptOp.OP_SYSCALL, "OP_SYSCALL", None, None)
        OpExecList.op_exec_list[ScriptOp.OP_DUPFROMALTSTACK] = OpExec(ScriptOp.OP_DUPFROMALTSTACK, "OP_DUPFROMALTSTACK", opToDupFromAltStack, None)
        OpExecList.op_exec_list[ScriptOp.OP_TOALTSTACK] = OpExec(ScriptOp.OP_TOALTSTACK, "OP_TOALTSTACK", opToAltStack, None)
        OpExecList.op_exec_list[ScriptOp.OP_FROMALTSTACK] = OpExec(ScriptOp.OP_FROMALTSTACK, "OP_FROMALTSTACK", opFromAltStack, None)
        OpExecList.op_exec_list[ScriptOp.OP_XDROP] = OpExec(ScriptOp.OP_XDROP, "OP_XDROP", opXDrop, None)
        OpExecList.op_exec_list[ScriptOp.OP_XSWAP] = OpExec(ScriptOp.OP_XSWAP, "XSWAP", opXSwap, None)
        OpExecList.op_exec_list[ScriptOp.OP_XTUCK] = OpExec(ScriptOp.OP_XTUCK, "XTUCK", opXTuck, None)
        OpExecList.op_exec_list[ScriptOp.OP_DEPTH] = OpExec(ScriptOp.OP_DEPTH, "DEPTH", opDepth, None)
        OpExecList.op_exec_list[ScriptOp.OP_DROP] = OpExec(ScriptOp.OP_DROP, "DROP", opDrop, None)
        OpExecList.op_exec_list[ScriptOp.OP_DUP] = OpExec(ScriptOp.OP_DUP, "DUP", opDup, None)
        OpExecList.op_exec_list[ScriptOp.OP_NIP] = OpExec(ScriptOp.OP_NIP, "NIP", opNip, None)
        OpExecList.op_exec_list[ScriptOp.OP_OVER] = OpExec(ScriptOp.OP_OVER, "OVER", opOver, None)
        OpExecList.op_exec_list[ScriptOp.OP_PICK] = OpExec(ScriptOp.OP_PICK, "PICK", opPick, None)
        OpExecList.op_exec_list[ScriptOp.OP_ROLL] = OpExec(ScriptOp.OP_ROLL, "ROLL", opRoll, None)
        OpExecList.op_exec_list[ScriptOp.OP_ROT] = OpExec(ScriptOp.OP_ROT, "ROT", opRot, None)
        OpExecList.op_exec_list[ScriptOp.OP_SWAP] = OpExec(ScriptOp.OP_SWAP, "SWAP", opSwap, None)
        OpExecList.op_exec_list[ScriptOp.OP_TUCK] = OpExec(ScriptOp.OP_TUCK, "TUCK", opTuck, None)
        OpExecList.op_exec_list[ScriptOp.OP_CAT] = OpExec(ScriptOp.OP_CAT, "CAT", opCat, None)
        OpExecList.op_exec_list[ScriptOp.OP_SUBSTR] = OpExec(ScriptOp.OP_SUBSTR, "SUBSTR", opSubStr, None)
        OpExecList.op_exec_list[ScriptOp.OP_LEFT] = OpExec(ScriptOp.OP_LEFT, "LEFT", opLeft, None)
        OpExecList.op_exec_list[ScriptOp.OP_RIGHT] = OpExec(ScriptOp.OP_RIGHT, "RIGHT", opRight, None)
        OpExecList.op_exec_list[ScriptOp.OP_SIZE] = OpExec(ScriptOp.OP_SIZE, "SIZE", opSize, None)
        OpExecList.op_exec_list[ScriptOp.OP_INVERT] = OpExec(ScriptOp.OP_INVERT, "INVERT", opInvert, None)
        OpExecList.op_exec_list[ScriptOp.OP_AND] = OpExec(ScriptOp.OP_AND, "AND", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_OR] = OpExec(ScriptOp.OP_OR, "OR", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_XOR] = OpExec(ScriptOp.OP_XOR, "XOR", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_EQUAL] = OpExec(ScriptOp.OP_EQUAL, "EQUAL", opEqual, None)
        OpExecList.op_exec_list[ScriptOp.OP_INC] = OpExec(ScriptOp.OP_INC, "INC", opBigInt, None)
        OpExecList.op_exec_list[ScriptOp.OP_DEC] = OpExec(ScriptOp.OP_DEC, "DEC", opBigInt, None)
        OpExecList.op_exec_list[ScriptOp.OP_SIGN] = OpExec(ScriptOp.OP_SIGN, "SIGN", opSign, None)
        OpExecList.op_exec_list[ScriptOp.OP_NEGATE] = OpExec(ScriptOp.OP_NEGATE, "NEGATE", opBigInt, None)
        OpExecList.op_exec_list[ScriptOp.OP_ABS] = OpExec(ScriptOp.OP_ABS, "ABS", opBigInt, None)
        OpExecList.op_exec_list[ScriptOp.OP_NOT] = OpExec(ScriptOp.OP_NOT, "NOT", opNot, None)
        OpExecList.op_exec_list[ScriptOp.OP_NZ] = OpExec(ScriptOp.OP_NZ, "NZ", opNz, None)
        OpExecList.op_exec_list[ScriptOp.OP_ADD] = OpExec(ScriptOp.OP_ADD, "ADD", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_SUB] = OpExec(ScriptOp.OP_SUB, "SUB", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_MUL] = OpExec(ScriptOp.OP_MUL, "MUL", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_DIV] = OpExec(ScriptOp.OP_DIV, "DIV", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_MOD] = OpExec(ScriptOp.OP_MOD, "MOD", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_SHL] = OpExec(ScriptOp.OP_SHL, "SHL", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_SHR] = OpExec(ScriptOp.OP_SHR, "SHR", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_BOOLAND] = OpExec(ScriptOp.OP_BOOLAND, "BOOLAND", opBoolZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_BOOLOR] = OpExec(ScriptOp.OP_BOOLOR, "BOOLOR", opBoolZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_NUMEQUAL] = OpExec(ScriptOp.OP_NUMEQUAL, "NUMEQUAL", opBigIntComp, None)
        OpExecList.op_exec_list[ScriptOp.OP_LT] = OpExec(ScriptOp.OP_LT, "LT", opBigIntComp, None)
        OpExecList.op_exec_list[ScriptOp.OP_GT] = OpExec(ScriptOp.OP_GT, "GT", opBigIntComp, None)
        OpExecList.op_exec_list[ScriptOp.OP_LTE] = OpExec(ScriptOp.OP_LTE, "LTE", opBigIntComp, None)
        OpExecList.op_exec_list[ScriptOp.OP_GTE] = OpExec(ScriptOp.OP_GTE, "GTE", opBigIntComp, None)
        OpExecList.op_exec_list[ScriptOp.OP_MIN] = OpExec(ScriptOp.OP_MIN, "MIN", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_MAX] = OpExec(ScriptOp.OP_MAX, "MAX", opBigIntZip, None)
        OpExecList.op_exec_list[ScriptOp.OP_WITHIN] = OpExec(ScriptOp.OP_WITHIN, "WITHIN", opWithIn, None)
        OpExecList.op_exec_list[ScriptOp.OP_SHA1] = OpExec(ScriptOp.OP_SHA1, "SHA1", opHash, None)
        OpExecList.op_exec_list[ScriptOp.OP_SHA256] = OpExec(ScriptOp.OP_SHA256, "SHA256", opHash, None)
        OpExecList.op_exec_list[ScriptOp.OP_HASH160] = OpExec(ScriptOp.OP_HASH160, "HASH160", opHash, None)
        OpExecList.op_exec_list[ScriptOp.OP_HASH256] = OpExec(ScriptOp.OP_HASH256, "HASH256", opHash, None)
        OpExecList.op_exec_list[ScriptOp.OP_VERIFY] = OpExec(ScriptOp.OP_VERIFY, "OP_VERIFY", None, None)
        OpExecList.op_exec_list[ScriptOp.OP_ARRAYSIZE] = OpExec(ScriptOp.OP_ARRAYSIZE, "OP_ARRAYSIZE", opArraySize, None)
        OpExecList.op_exec_list[ScriptOp.OP_PACK] = OpExec(ScriptOp.OP_PACK, "OP_PACK", opPack, None)
        OpExecList.op_exec_list[ScriptOp.OP_UNPACK] = OpExec(ScriptOp.OP_UNPACK, "OP_UNPACK", opUnpack, None)
        OpExecList.op_exec_list[ScriptOp.OP_PICKITEM] = OpExec(ScriptOp.OP_PICKITEM, "OP_PICKITEM", opPickItem, None)
        OpExecList.op_exec_list[ScriptOp.OP_SETITEM] = OpExec(ScriptOp.OP_SETITEM, "OP_SETITEM", opSetItem, None)
        OpExecList.op_exec_list[ScriptOp.OP_NEWARRAY] = OpExec(ScriptOp.OP_NEWARRAY, "OP_NEWARRAY", opNewArray, None)
        OpExecList.op_exec_list[ScriptOp.OP_NEWMAP] = OpExec(ScriptOp.OP_NEWMAP, "OP_NEWMAP", opNewMap, None)
        OpExecList.op_exec_list[ScriptOp.OP_NEWSTRUCT] = OpExec(ScriptOp.OP_NEWSTRUCT, "OP_NEWSTRUCT", opNewStruct, None)
        OpExecList.op_exec_list[ScriptOp.OP_APPEND] = OpExec(ScriptOp.OP_APPEND, "OP_APPEND", opAppend, None)
        OpExecList.op_exec_list[ScriptOp.OP_REVERSE] = OpExec(ScriptOp.OP_REVERSE, "OP_REVERSE", opReverse, None)
        OpExecList.op_exec_list[ScriptOp.OP_THROW] = OpExec(ScriptOp.OP_THROW, "OP_THROW", opThrow, None)
        OpExecList.op_exec_list[ScriptOp.OP_THROWIFNOT] = OpExec(ScriptOp.OP_THROWIFNOT, "OP_THROWIFNOT", opThrowIfNot, None)

    def validatePickItem(self, engine):
        item = PushData.peek_n_stack_item(1, engine)
        if item is None:
            return False
        elif type(item) == MapItem:
                pass
        elif type(item) == ArrayItem:
            index = PushData.peek_biginteger(engine)
            if index < 0:
                print("ERR_BAD_VALUE")
                return False
            arr = item.get_array()
            if index >= len(arr):
                print("ERR_OVER_MAX_ARRAY_SIZE")
                return False
        elif type(item) == StructItem:
            pass
        return False





