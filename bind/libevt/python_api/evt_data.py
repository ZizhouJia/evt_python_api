from cffi import FFI
import libevt
class evt_data:
    def __init__(self,data):
        self.data=data
        libevt.init_lib()
        self.libevt=libevt.libevt.lib
        self.ffi=libevt.libevt.ffi
    def __del__(self):
        self.libevt.evt_free(self.data)
