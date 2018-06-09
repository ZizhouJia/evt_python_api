from cffi import FFI
import libevt
from evt_data import evt_data
import evt_exception


class evt_abi:
    def __init__(self):
        libevt.init_lib()
        self.libevt=libevt.libevt.lib
        self.ffi=libevt.libevt.ffi
        self._abi=self.libevt.evt_abi()


    def evt_abi_json_to_bin(self,action,json):
        action_c=bytes(action,encoding='utf-8')
        json_c=bytes(json,encoding='utf-8')
        bin_c=self.ffi.new("evt_bin_t**")
        ret=self.libevt.evt_abi_json_to_bin(self._abi,action_c,json_c,bin_c)
        evt_exception.evt_exception_raiser(ret)
        return evt_data(bin_c[0])

    def evt_abi_bin_to_json(self,action,bin):
        action_c=bytes(action,encoding='utf-8')
        bin_c=bin.data
        json_c=self.ffi.new("char** ")
        ret=self.libevt.evt_abi_bin_to_json(self._abi,action_c,bin_c,json_c)
        evt_exception.evt_exception_raiser(ret)
        json=self.ffi.string(json_c[0]).decode('utf-8')
        ret=self.lib.evt_free(str_c[0])
        evt_exception.evt_exception_raiser(ret)
        return json

    def evt_trx_json_to_digest(self,json,chain_id):
        json_c=bytes(json,encoding='utf-8')
        chain_id_c=chain_id.data
        digest_c=self.ffi.new("evt_checksum_t**")
        ret=self.libevt.evt_trx_json_to_digest(self._abi,json_c,chain_id_c,digest_c)
        evt_exception.evt_exception_raiser(ret)
        return evt_data(digest_c[0])

    def evt_chain_id_from_string(self,str):
        str_c=bytes(str,encoding='utf-8')
        chain_id_c=self.ffi.new("evt_chain_id_t**")
        ret=self.libevt.evt_chain_id_from_string(str_c,chain_id_c)
        evt_exception.evt_exception_raiser(ret)
        return evt_data(chain_id_c[0])

    def __del__(self):
        ret=self.libevt.evt_free_abi(self._abi)
        evt_exception.evt_exception_raiser(ret)
