
import unittest

from src.utils.script_op import ScriptOp
from src.vm.execution_engine import ExecutionEngine


class TestFuncArithmetic(unittest.TestCase):
    def test_op_bigint(self):
        engine = ExecutionEngine()
        for code in [ScriptOp.OP_INC, ScriptOp.OP_DEC, ScriptOp.OP_NEGATE, ScriptOp.OP_ABS, ScriptOp.OP_PUSH0]:
            engine.evaluation_stack.push()
