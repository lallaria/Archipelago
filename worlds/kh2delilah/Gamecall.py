from pymem import Pymem, logging, ptypes, memory, process
from ctypes import *
#from struct import unpack_from
#from Utils import user_path


class Gamecall(object):

    def __init__(self, kh2: Pymem):
        # anything we don't want dereferenced
        self.kh2pymem = kh2
        self.instructions = []
        self.arg_pts = []
        self.address_pt
        self.jump = False
        self.chain_of_memory
        self.ansem_reports
    
    def jump_me(self, boing: False):
        self.jump = boing

    def inform_me(self, address):
        self.chain_of_memory = memory.virtual_query(self.kh2pymem.process_handle, address + self.kh2pymem.base_address)
        self.ansem_reports = process.base_module(self.kh2pymem.process_handle)

    def call_me(address):
        pass

    def return_me(self, kh2address, *args):
        self.jump = False
        self.arg_pts = []
        for arg in enumerate(*args):
            self.arg_pts.append(POINTER(arg))
        return memory.allocate_memory(self.kh2pymem.process_handle, 0x16)

    def void_me(self, kh2address, *args):
        self.arg_pts = []
        self.address_pt = POINTER(kh2address)
        for arg in enumerate(*args):
            self.arg_pts.append(POINTER(arg))
        newaddr = memory.allocate_memory(self.kh2pymem.process_handle, 0x16)
        self.assemble_me()
        self.kh2pymem.write_bytes(newaddr, self.instructions, len(newaddr))
        thread_handle = self.kh2pymem.start_thread(newaddr)

        self.kh2pymem.inject_python_interpreter
        self.kh2pymem.inject_python_shellcode(self.instructions)

    def assemble_me(self):
        asmstr = []
        extra_params = 0
        if not len(self.arg_pts):
            pass
        else:
            for count, arg in enumerate(self.arg_pts):
                if count < 4:
                    if count == 3: asmstr.insert(0, "mov r9, " + str(arg))
                    if count == 2: asmstr.insert(0, "mov r8, " + str(arg))
                    if count == 1: asmstr.insert(0, "mov rdx, " + str(arg))
                    if count == 0: asmstr.insert(0, "mov rcx, " + str(arg))
                else:
                    asmstr.insert(4, "push " + str(arg))
                    extra_params += 1
        asmstr.append("sub rsp, 32")
        asmstr.append("mov rax, " + str(self.kh2address))
        asmstr.append("call rax")
        asmstr.append("add rsp, " + str(32 + extra_params * 8))
        asmstr.append("ret")

        if self.jump:
            for _ in asmstr:
                if "rsp" in _ and not "mov rsp" in _:
                    _ = "nop"
                if "call rax" in _:
                    _ = "jmp rax"

        logging.info(f"asmstr: {asmstr}\n extra_params {extra_params}")
        #self.instructions = create_string_buffer(asmstr)

    def remind_me(self, kh2address: ptypes.RemotePointer):
        pass




        # logger.info(f"processmodules: {kh2modules}")

        # sorapoint_pt = ptypes.RemotePointer(self.kh2.process_handle, self.game_func_addrs["SoraPointer"] + self.kh2.base_address)#, endianess='big-endian')
        # hitpoint_pt = ptypes.RemotePointer(self.kh2.process_handle, self.game_func_addrs["HitPointFunc"] + self.kh2.base_address)#, endianess='big-endian')
        
        # isthissorafunc = self.kh2.read_ctype(sorapoint_pt.value, ctypes.Structure, get_py_value=False)
        # isthishpfunc = self.kh2.read_ctype(hitpoint_pt.value, ctypes.Structure, get_py_value=False)
        # logger.info(f"Sorapt {isthissorafunc}")
        # logger.info(f"hitpointpt {isthishpfunc}")


        # ctypes.windll.LoadLibrary

        # self.kh2.inject_python_shellcode
        # hpfunc = self.kh2.read_ctype(self.kh2.base_address + self.game_func_addrs["HitPointFunc"], ctypes.Structure)
        # sorapt = self.kh2.read_ctype(self.kh2.base_address + self.game_func_addrs["SoraPointer"], ctypes.Structure)
        # logger.info(f"readctype of funcs hp: {hpfunc} sorapt: {sorapt}")
        # self.kh2.call_function_address()
        
        # @ctypes.PYFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
        # def c_write_int(address, value):
        #     return self.kh2.write_int(self.kh2.base_address + address, value)

        # sorahpfuncpt = ctypes.WINFUNCTYPE(ctypes.c_int)
        # sorahpfunc = sorahpfuncpt(sorapoint_pt.cvalue)

        # hpfuncpt = ctypes.WINFUNCTYPE(None, ctypes.c_longlong, ctypes.c_int)
        # hpfunc = hpfuncpt(hitpoint_pt.cvalue)

        # hpfunc(sorahpfunc, -120)
    


        #write_int = ctypes.cast(c_write_int, ctypes.c_void_p)

        # hpfunc = KH2DelilahContext.kh2_c_call_func(self.game_func_addrs["HitPointFunc"] + self.kh2.base_address)
        # hpfunc(c_write_int(self.Slot1, -120))



# def assemble(src, memorySize=0x10000, passesLimit=100):
#     """Assembles string and returns assembled bytes"""
#     buf = create_string_buffer(memorySize)
#     err = _fasm.fasm_Assemble(c_char_p(src), buf, len(buf), passesLimit, 0)
#     if err == 0:
#         cb, addr = unpack_from('II', buf, 4)
#         ofs = addr - addressof(buf)
#         return buf[ofs:ofs + cb]
#     if err != 2:
#         raise RuntimeError('FASM error: ' + err)
#     cb, addr = unpack_from('II', buf, 4)
#     errCode, errLine = unpack_from('iI', buf, 4)
#     raise RuntimeError('FASM error: ' + errCode + errLine)