from cffi import FFI
import libevt
from evt_data import evt_data
import evt_exception




class evt_public_key:
    def __init__(self,data):
        libevt.init_lib()
        self.lib=libevt.libevt.lib
        self.ffi=libevt.libevt.ffi
        if(isinstance(data,str)):
            self._evt_public_key=self.ffi.new("evt_public_key_t**")
            str_c=bytes(data,encoding='utf-8')
            ret=self.lib.evt_public_key_from_string(str_c,self._evt_public_key)
            evt_exception.evt_exception_raiser(ret)
            self._evt_public_key=self._evt_public_key[0]
        else:
            self._evt_public_key=data

    def __str__(self):
        return self.evt_public_key_string()


    def evt_public_key_string(self):
        str_c=self.ffi.new("char**")
        ret=self.lib.evt_public_key_string(self._evt_public_key,str_c)
        evt_exception.evt_exception_raiser(ret)
        str=self.ffi.string(str_c[0]).decode('utf-8')
        ret=self.lib.evt_free(str_c[0])
        evt_exception.evt_exception_raiser(ret)
        return str



    def __del__(self):
        ret=self.lib.evt_free(self._evt_public_key)
        evt_exception.evt_exception_raiser(ret)


class evt_private_key:
    def __init__(self,data):
        libevt.init_lib()
        self.lib=libevt.libevt.lib
        self.ffi=libevt.libevt.ffi
        if(isinstance(data,str)):
            self._evt_private_key=self.ffi.new("evt_private_key_t**")
            str_c=bytes(data,encoding='utf-8')
            ret=self.lib.evt_private_key_from_string(str_c,self._evt_private_key)
            evt_exception.evt_exception_raiser(ret)
            self._evt_private_key=self._evt_private_key[0]
        else:
            self._evt_private_key=data

    def __str__(self):
        return self.evt_private_key_string()


    def evt_private_key_string(self):
        str_c=self.ffi.new("char**")
        ret=self.lib.evt_private_key_string(self._evt_private_key,str_c)
        evt_exception.evt_exception_raiser(ret)
        str=self.ffi.string(str_c[0]).decode('utf-8')
        ret=self.lib.evt_free(str_c[0])
        evt_exception.evt_exception_raiser(ret)
        return str

    def evt_get_public_key(self):
        public_key_c=self.ffi.new("evt_public_key_t**")
        ret=self.lib.evt_get_public_key(self._evt_private_key,public_key_c)
        evt_exception.evt_exception_raiser(ret)
        return evt_public_key(public_key_c[0])




    def __del__(self):
        ret=self.lib.evt_free(self._evt_private_key)
        evt_exception.evt_exception_raiser(ret)

class evt_signature:
    def __init__(self,data):
        libevt.init_lib()
        self.lib=libevt.libevt.lib
        self.ffi=libevt.libevt.ffi
        if(isinstance(data,str)):
            self._evt_signature=self.ffi.new("evt_signature_t**")
            str_c=bytes(data,encoding='utf-8')
            ret=self.lib.evt_signature_from_string(str_c,self._evt_signature)
            evt_exception.evt_exception_raiser(ret)
            self._evt_signature=self._evt_signature[0]
        else:
            self._evt_signature=data

    def __str__(self):
        return self.evt_signature_string()


    def evt_signature_string(self):
        str_c=self.ffi.new("char**")
        ret=self.lib.evt_signature_string(str_c,self._evt_signature)
        evt_exception.evt_exception_raiser(ret)
        str=self.ffi.string(str_c[0]).decode('utf-8')
        ret=self.lib.evt_free(str_c[0])
        evt_exception.evt_exception_raiser(ret)
        return str

    def __del__(self):
        ret=self.lib.evt_free(self._evt_signature)
        evt_exception.evt_exception_raiser(ret)


class evt_checksum:
    def __init__(self,data):
        libevt.init_lib()
        self.lib=libevt.libevt.lib
        self.ffi=libevt.libevt.ffi
        if(isinstance(data,str)):
            self._evt_checksum=self.ffi.new("evt_checksum_t**")
            str_c=bytes(data,encoding='utf-8')
            ret=self.lib.evt_checksum_from_string(str_c,self._evt_checksum)
            evt_exception.evt_exception_raiser(ret)
            self._evt_checksum=self._evt_checksum[0]
        else:
            self._evt_checksum=data

    def __str__(self):
        return self.evt_checksum_string()


    def evt_checksum_string(self):
        str_c=self.ffi.new("char**")
        ret=self.lib.evt_checksum_string(str_c,self._evt_checksum)
        evt_exception.evt_exception_raiser(ret)
        str=self.ffi.string(str_c[0]).decode('utf-8')
        ret=self.lib.evt_free(str_c[0])
        evt_exception.evt_exception_raiser(ret)
        return str

    def __del__(self):
        ret=elf.lib.evt_free(self._evt_public_key)
        evt_exception.evt_exception_raiser(ret)

class evt_hash:
    def __init__(self,str):
        libevt.init_lib()
        self.lib=libevt.libevt.lib
        self.ffi=libevt.libevt.ffi
        str_c=bytes(str,encoding='utf-8')
        self._evt_hash=self.ffi.new("evt_checksum_t**")
        ret=self.lib.evt_hash(str_c,len(str_c),self._evt_hash)
        evt_exception.evt_exception_raiser(ret)
        self._evt_hash=self._evt_hash[0]

    def __del__(self):
        ret=self.lib.evt_free(self._evt_hash)
        evt_exception.evt_exception_raiser(ret)



def evt_generate_new_pair():
    libevt.init_lib()
    lib=libevt.libevt.lib
    ffi=libevt.libevt.ffi
    evt_public_key_c=ffi.new("evt_public_key_t**")
    evt_private_key_c=ffi.new("evt_private_key_t**")
    ret=lib.evt_generate_new_pair(evt_public_key_c,evt_private_key_c)
    evt_exception.evt_exception_raiser(ret)
    return evt_public_key(evt_public_key_c[0]),evt_private_key(evt_private_key_c[0])

def evt_sign_hash(priv_key,hash):
    libevt.init_lib()
    lib=libevt.libevt.lib
    ffi=libevt.libevt.ffi
    evt_signature_c=ffi.new("evt_signature_t**")
    ret=lib.evt_sign_hash(priv_key._evt_private_key,hash._evt_hash,evt_signature_c)
    evt_exception.evt_exception_raiser(ret)
    return evt_signature(evt_signature_c[0])

def evt_recover(sign,hash):
    libevt.init_lib()
    lib=libevt.libevt.lib
    ffi=libevt.libevt.ffi
    evt_public_key_c=ffi.new("evt_public_key_t**")
    ret=lib.evt_recover(sign._evt_signature,hash._evt_hash,evt_public_key_c)
    evt_exception.evt_exception_raiser(ret)
    return evt_public_key(evt_public_key_c[0])
