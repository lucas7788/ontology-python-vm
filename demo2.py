from ontology.account.account import Account
from ontology.common.address import Address
from ontology.ont_sdk import OntologySdk
from ontology.smart_contract.neo_contract.abi.abi_info import AbiInfo
from ontology.smart_contract.neo_contract.abi.build_params import BuildParams
from src.types.bool_item import BoolItem
from src.types.bytearray_item import ByteArrayItem
from src.types.integer_item import IntegerItem
from src.utils.config import Config
from src.utils.script_op import ScriptOp
from src.utils.service_map import ServiceMap
from src.vm.execution_context import ExecutionContext
from src.vm.execution_engine import ExecutionEngine

privatekey1 = "1094e90dd7c4fdfd849c14798d725ac351ae0d924b29a279a9ffa77d5737bd96"
privatekey2 = "bc254cf8d3910bc615ba6bf09d4553846533ce4403bc24f58660ae150a6d64cf"
# nep5abi = {"hash":"0x5bb169f915c916a5e30a3c13a5e0cd228ea26826","entrypoint":"Main","functions":
#     [{"name":"Name","parameters":[],"returntype":"String"},{"name":"Symbol","parameters":[],"returntype":"String"},
#      {"name":"Decimals","parameters":[],"returntype":"Integer"},{"name":"Main","parameters":
#         [{"name":"operation","type":"String"},{"name":"args","type":"Array"}],"returntype":"Any"},
#      {"name":"Init","parameters":[],"returntype":"Boolean"},{"name":"TotalSupply","parameters":[],"returntype":"Integer"},
#      {"name":"Transfer","parameters":[{"name":"from","type":"ByteArray"},{"name":"to","type":"ByteArray"},
#                                       {"name":"value","type":"Integer"}],"returntype":"Boolean"},
#      {"name":"BalanceOf","parameters":[{"name":"address","type":"ByteArray"}],"returntype":"Integer"}],
#            "events":[
#     {"name":"transfer","parameters":[{"name":"arg1","type":"ByteArray"},{"name":"arg2","type":"ByteArray"},
#                                      {"name":"arg3","type":"Integer"}],"returntype":"Void"}]}

nep5abi = {"hash":"0xb80b05b998e017b0b170bc51c52b0f148cb990d3","entrypoint":"Main","functions":[
    {"name":"name","parameters":[],"returntype":"String"},
    {"name":"symbol","parameters":[],"returntype":"String"},
    {"name":"decimals","parameters":[],"returntype":"Integer"},
    {"name":"Main","parameters":[
        {"name":"operation","type":"String"},
        {"name":"args","type":"Array"}],"returntype":"ByteArray"},
    {"name":"deploy","parameters":[],"returntype":"Boolean"},{"name":"totalSupply","parameters":[],"returntype":"Integer"},{"name":"transfer","parameters":[{"name":"from","type":"ByteArray"},{"name":"to","type":"ByteArray"},{"name":"value","type":"Integer"}],"returntype":"Boolean"},{"name":"balanceOf","parameters":[{"name":"address","type":"ByteArray"}],"returntype":"Integer"},{"name":"inflation","parameters":[{"name":"count","type":"Integer"}],"returntype":"Boolean"},{"name":"recycle","parameters":[{"name":"count","type":"Integer"}],"returntype":"Boolean"},{"name":"transferMulti","parameters":[{"name":"args","type":"Array"}],"returntype":"Boolean"}],"events":[]}

# codeStr = "57c56b6c766b00527ac46c766b51527ac4616c766b51c300c36c766b52527ac46c766b51c351c36c766b53527ac46c766b51c352c36c766b54527ac46c766b52c361681b53797374656d2e52756e74696d652e436865636b5769746e657373009c6c766b55527ac46c766b55c3643400610c3d3d3d6661696c3d3d3d3d3d61681253797374656d2e52756e74696d652e4c6f6761026e6f6c766b56527ac46222006c766b52c36c766b53c36c766b54c36152726516006c766b56527ac46203006c766b56c3616c756657c56b6c766b00527ac46c766b51527ac46c766b52527ac461536c766b53527ac461681953797374656d2e53746f726167652e476574436f6e746578746c766b54527ac46c766b54c306726573756c74062d7474657374615272681253797374656d2e53746f726167652e507574616c766b54c306726573756c74617c681253797374656d2e53746f726167652e4765746c766b55527ac40e3d3d737563636573733d3d3d3d3d61681253797374656d2e52756e74696d652e4c6f6761616c766b00c36c766b51c36c766b52c3615272087472616e7366657254c1681553797374656d2e52756e74696d652e4e6f74696679616c766b55c36c766b56527ac46203006c766b56c3616c7566";
codeStr = "0117c56b6c766b00527ac46c766b51527ac4616c766b00c3066465706c6f79876c766b52527ac46c766b52c36411006165f1026c766b53527ac462b7026c766b00c30b746f74616c537570706c79876c766b54527ac46c766b54c3641100616511046c766b53527ac46288026c766b00c3046e616d65876c766b55527ac46c766b55c3641100616573026c766b53527ac46260026c766b00c30673796d626f6c876c766b56527ac46c766b56c364110061655c026c766b53527ac46236026c766b00c308646563696d616c73876c766b57527ac46c766b57c364110061653c026c766b53527ac4620a026c766b00c3087472616e73666572876c766b58527ac46c766b58c3647100616c766b51c3c0539c009c6c766b5c527ac46c766b5cc3640e00006c766b53527ac462c7016c766b51c300c36c766b59527ac46c766b51c351c36c766b5a527ac46c766b51c352c36c766b5b527ac46c766b59c36c766b5ac36c766b5bc3615272655c036c766b53527ac4627e016c766b00c30962616c616e63654f66876c766b5d527ac46c766b5dc3644900616c766b51c3c0519c009c6c766b5f527ac46c766b5fc3640e00006c766b53527ac4623a016c766b51c300c36c766b5e527ac46c766b5ec3616582056c766b53527ac46219016c766b00c309696e666c6174696f6e876c766b60527ac46c766b60c3644d00616c766b51c3c0519c009c6c766b0112527ac46c766b0112c3640e00006c766b53527ac462d3006c766b51c300c36c766b0111527ac46c766b0111c361656e056c766b53527ac462b0006c766b00c30772656379636c65876c766b0113527ac46c766b0113c3644d00616c766b51c3c0519c009c6c766b0115527ac46c766b0115c3640e00006c766b53527ac4626a006c766b51c300c36c766b0114527ac46c766b0114c36165cc066c766b53527ac46247006c766b00c30d7472616e736665724d756c7469876c766b0116527ac46c766b0116c3641700616c766b51c3616598086c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756600c56b0b596f754c6520546f6b656e616c756600c56b04594c5432616c756600c56b51616c756653c56b6161681953797374656d2e53746f726167652e476574436f6e746578740b746f74616c537570706c79617c681253797374656d2e53746f726167652e4765746c766b00527ac46c766b00c3c000a06c766b51527ac46c766b51c3640e00006c766b52527ac462de0061681953797374656d2e53746f726167652e476574436f6e7465787461141320f12cb12625512b7b5e76efc261c222dbfd610400ca9a3b615272681253797374656d2e53746f726167652e5075746153c5765161141320f12cb12625512b7b5e76efc261c222dbfd61c476520400ca9a3bc461681553797374656d2e52756e74696d652e4e6f746966796161681953797374656d2e53746f726167652e476574436f6e746578740b746f74616c537570706c790400ca9a3b615272681253797374656d2e53746f726167652e50757461516c766b52527ac46203006c766b52c3616c756651c56b6161681953797374656d2e53746f726167652e476574436f6e746578740b746f74616c537570706c79617c681253797374656d2e53746f726167652e4765746c766b00527ac46203006c766b00c3616c75665cc56b6c766b00527ac46c766b51527ac46c766b52527ac4616c766b52c300a16c766b55527ac46c766b55c3640e00006c766b56527ac4624b026c766b00c361681b53797374656d2e52756e74696d652e436865636b5769746e657373009c6c766b57527ac46c766b57c3640e00006c766b56527ac4620c026c766b51c3c001149c009c6c766b58527ac46c766b58c3640e00006c766b56527ac462e7016c766b00c36c766b51c39c6c766b59527ac46c766b59c3640e00516c766b56527ac462c20161681953797374656d2e53746f726167652e476574436f6e746578746c766b00c3617c681253797374656d2e53746f726167652e4765746c766b53527ac46c766b53c36c766b52c39f6c766b5a527ac46c766b5ac3640e00006c766b56527ac4625f016c766b53c36c766b52c39c6c766b5b527ac46c766b5bc364410061681953797374656d2e53746f726167652e476574436f6e746578746c766b00c3617c681553797374656d2e53746f726167652e44656c6574656162470061681953797374656d2e53746f726167652e476574436f6e746578746c766b00c36c766b53c36c766b52c394615272681253797374656d2e53746f726167652e5075746161681953797374656d2e53746f726167652e476574436f6e746578746c766b51c3617c681253797374656d2e53746f726167652e4765746c766b54527ac461681953797374656d2e53746f726167652e476574436f6e746578746c766b51c36c766b54c36c766b52c393615272681253797374656d2e53746f726167652e5075746153c576006c766b00c3c476516c766b51c3c476526c766b52c3c461681553797374656d2e52756e74696d652e4e6f7469667961516c766b56527ac46203006c766b56c3616c756652c56b6c766b00527ac46161681953797374656d2e53746f726167652e476574436f6e746578746c766b00c3617c681253797374656d2e53746f726167652e4765746c766b51527ac46203006c766b51c3616c756657c56b6c766b00527ac4616c766b00c3009f6c766b54527ac46c766b54c3640f00006c766b55527ac462950161141320f12cb12625512b7b5e76efc261c222dbfd6161681b53797374656d2e52756e74696d652e436865636b5769746e657373009c6c766b56527ac46c766b56c3640f00006c766b55527ac462450161141320f12cb12625512b7b5e76efc261c222dbfd61616518ff6c766b51527ac461681953797374656d2e53746f726167652e476574436f6e746578746c766b52527ac46c766b52c361141320f12cb12625512b7b5e76efc261c222dbfd616c766b51c36c766b00c393615272681253797374656d2e53746f726167652e5075746161681953797374656d2e53746f726167652e476574436f6e746578740b746f74616c537570706c79617c681253797374656d2e53746f726167652e4765746c766b53527ac46c766b52c30b746f74616c537570706c796c766b53c36c766b00c393615272681253797374656d2e53746f726167652e5075746153c5765161141320f12cb12625512b7b5e76efc261c222dbfd61c476526c766b00c3c461681553797374656d2e52756e74696d652e4e6f7469667961516c766b55527ac46203006c766b55c3616c756658c56b6c766b00527ac4616c766b00c3009f6c766b54527ac46c766b54c3640f00006c766b55527ac462d30161141320f12cb12625512b7b5e76efc261c222dbfd6161681b53797374656d2e52756e74696d652e436865636b5769746e657373009c6c766b56527ac46c766b56c3640f00006c766b55527ac462830161141320f12cb12625512b7b5e76efc261c222dbfd61616551fd6c766b51527ac461681953797374656d2e53746f726167652e476574436f6e746578746c766b52527ac461681953797374656d2e53746f726167652e476574436f6e746578740b746f74616c537570706c79617c681253797374656d2e53746f726167652e4765746c766b53527ac46c766b51c36c766b00c3a06417006c766b53c36c766b00c3940400ca9a3ba2620400006c766b57527ac46c766b57c364bd00616c766b52c361141320f12cb12625512b7b5e76efc261c222dbfd616c766b51c36c766b00c394615272681253797374656d2e53746f726167652e507574616c766b52c30b746f74616c537570706c796c766b53c36c766b00c394615272681253797374656d2e53746f726167652e5075746153c5760061141320f12cb12625512b7b5e76efc261c222dbfd61c476526c766b00c3c461681553797374656d2e52756e74696d652e4e6f7469667961516c766b55527ac4620e00006c766b55527ac46203006c766b55c3616c756656c56b6c766b00527ac461006c766b51527ac4625300616c766b00c36c766b51c3c36c766b52527ac46c766b52c300c36c766b52c351c36c766b52c352c36152726513f9009c6c766b53527ac46c766b53c364050061f0616c766b51c351936c766b51527ac46c766b51c36c766b00c3c09f6c766b54527ac46c766b54c36398ff516c766b55527ac46203006c766b55c3616c7566"
sdk = OntologySdk()

acct1 = Account(privatekey1)
acct2 = Account(privatekey2)


def execute_test():
    code_bytes = bytearray.fromhex(codeStr)
    config = Config('b80b05b998e017b0b170bc51c52b0f148cb990d3')
    params = build_params()
    print("params: ", params.hex())
    config.tx = build_tx()
    # print(config.tx.serialize(True))
    engine = ExecutionEngine()
    engine.push_context(ExecutionContext(engine, params))
    num = 0
    while(True):
        if len(engine.contexts) == 0:
            break
        engine.execute_code()
        if engine.op_code == ScriptOp.OP_RET:
            break
        if engine.op_code is None:
            pass
        elif ScriptOp.OP_PUSHBYTES1.value <= engine.op_code.value <= ScriptOp.OP_PUSHBYTES75.value:
            pass
        elif not engine.validate_op():
            break
        else:
            if engine.op_code is not None:
                print(num, "> " + str(engine.evaluation_stack.count()) + " " + hex(engine.op_code.value) + " " +  engine.op_exec.name + " " + engine.evaluation_stack.info2())
                num += 1
        if ScriptOp.OP_APPCALL == engine.op_code:
            print("####APPCALL####")
            num = 0
            engine2 = ExecutionEngine()
            engine2.push_context(ExecutionContext(engine2, code_bytes))
            engine.evaluation_stack.copy_to(engine2.evaluation_stack)
            engine = engine2
        elif ScriptOp.OP_SYSCALL == engine.op_code:
            bys = engine.context.op_reader.read_var_bytes()
            print("####SYSCALL#### ", bys.decode())
            service = ServiceMap.get_service(bys.decode())
            if service is None:
                print(bys.decode())
                return
            service.exec(config, engine)
        else:
            engine.step_info()
    print("##########end############")
    print("Stack Count:", engine.evaluation_stack.count())
    items = engine.evaluation_stack.peek(0)
    if type(items) is ByteArrayItem:
        print("Result ByteArrayItem:", engine.evaluation_stack.peek(0).get_bytearray().hex() + engine.evaluation_stack.peek(0).get_bytearray().decode())
    elif type(items) is IntegerItem:
        print("Result GetBigInteger:", engine.evaluation_stack.peek(0).get_biginteger())
    elif type(items) is BoolItem:
        print("Result BoolItem:", engine.evaluation_stack.peek(0).get_bool())
    return


def build_params():
    abi = AbiInfo(nep5abi['hash'], nep5abi['entrypoint'], nep5abi["functions"])
    # func = abi.get_function("Transfer")
    # func = abi.get_function("BalanceOf")
    func = abi.get_function("balanceOf")
    # func = abi.get_function("deploy")
    # func.set_params_value((acct1.get_address().to_array(), acct2.get_address().to_array(), 19 * 10000000))
    # add = acct1.get_address().to_reverse_hex_str()
    func.set_params_value((Address.b58decode('AHX1wzvdw9Yipk7E9MuLY4GGX4Ym9tHeDe').to_array(),))
    params = BuildParams.serialize_abi_function(func)
    params += bytearray([0x67])
    return params


def build_tx():
    contract_address = Address.address_from_vm_code(codeStr)
    params = build_params()
    tx = sdk.neo_vm().make_invoke_transaction(contract_address.to_array(), params, None, 0, 0)
    # tx_hash = tx.hash256_bytes()
    # sig_data = acct1.generate_signature(tx_hash, acct1.get_signature_scheme())
    # sig = Sig([acct1.serialize_public_key()], 1, [sig_data])
    # tx.sigs = list()
    # tx.sigs.append(sig)
    return tx


if __name__ == "__main__":
    execute_test()
