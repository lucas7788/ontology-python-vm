from src.types.array_item import ArrayItem
from src.types.bool_item import BoolItem
from src.types.map_item import MapItem
from src.types.struct_item import StructItem
from src.utils.push_data import PushData
from src.vm.vm_state import VMState


class FuncArray(object):

    @staticmethod
    def op_array_size(engine):
        item = PushData.pop_stack_item(engine)
        if type(item) is ArrayItem:
            bys = item.get_array()
            PushData.push_data(engine, len(bys))
        else:
            bys = item.get_bytearray()
            PushData.push_data(engine, len(bys))
        return VMState.NONE

    @staticmethod
    def op_pack(engine):
        size = PushData.pop_int(engine)
        items = list()
        for i in range(size):
            x = PushData.pop_stack_item(engine)
            items.append(x)
        PushData.push_data(engine, items)
        return VMState.NONE

    @staticmethod
    def op_unpack(engine):
        items = PushData.pop_array(engine)
        l = len(items)
        for i in range(l - 1, -1, -1):
            PushData.push(engine, items[i])
        PushData.push_data(engine, l)
        return VMState.NONE

    @staticmethod
    def op_pick_item(engine):
        index = PushData.pop_stack_item(engine)
        items = PushData.pop_stack_item(engine)
        if type(items) is ArrayItem:
            i = index.get_biginteger()
            print("i:", i)
            arr = items.get_array()
            PushData.push_data(engine, arr[i])
        elif type(items) is MapItem:
            t = items.try_get_value(index)
            PushData.push_data(engine, t)
        return VMState.NONE

    @staticmethod
    def op_set_item(engine):
        new_item = PushData.pop_stack_item(engine)
        index = PushData.pop_stack_item(engine)
        item = PushData.pop_stack_item(engine)
        if type(item) is ArrayItem:
            i = index.get_biginteger()
            items = item.get_array()
            items[i] = new_item
        elif type(item) is MapItem:
            item.add(index, new_item)
        elif type(item) is StructItem:
            i = index.get_biginteger()
            item.stack_items.set(i, new_item)
        return VMState.NONE

    @staticmethod
    def op_new_array(engine):
        count = PushData.pop_int(engine)
        items = list()
        for i in range(count):
            items.append(BoolItem(False))
        PushData.push_data(engine, ArrayItem(items))
        return VMState.NONE

    @staticmethod
    def op_new_struct(engine):
        return VMState.NONE

    @staticmethod
    def op_new_map(engine):
        PushData.push_data(engine, MapItem())
        return VMState.NONE

    @staticmethod
    def op_append(engine):
        new_item = PushData.pop_stack_item(engine)
        if type(new_item) == StructItem:
            new_item = new_item.clone()
        items = PushData.pop_stack_item(engine)

        return VMState.NONE

    @staticmethod
    def op_reverse(engine):
        items = PushData.pop_array(engine)
        items.reverse()
        return VMState.NONE

    @staticmethod
    def op_remove(engine):
        index = PushData.pop_stack_item(engine)
        item = PushData.pop_stack_item(engine)
        item.remove(index)
        return VMState.NONE
