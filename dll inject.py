from ctypes import *
PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF )
VIRTUAL_MEM = ( 0x1000 | 0x2000 )
kernel32 = windll.kernel32

try:
    pid = int(input("PID:"))
    dll = input("Dll:")
    #it might be better by doing filedialog

except:
    print("wrong type")

proc = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, pid )

if not proc:
    print("PID is wrong")
else:
    open_process()
    arg = kernel32.VirtualAllocEx(proc, 0, len(dll), VIRTUAL_MEM, PAGE_READWRITE)
    get_alloc()
    written = c_int(0)
    kernel32.WriteProcessMemory(self.h_process, self.arg_adress, self.dll, len(self.dll), byref(self.written))
    tkernel32 = kernel32.GetModuleHandleA("kernel32.dll")
    loadlib = kernel32.GetProcAddress(tkernel32,"LoadLibraryA")
    thid = c_ulong(0)

    if not kernel32.CreateRemoteThread(proc,None,0,loadlib,arg,0,byref(thid)):
        print("Fail!")

    else:
        print("Good job, id=", thid.value)
