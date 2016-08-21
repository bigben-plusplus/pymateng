# -*- coding:utf-8 -*-

import ctypes
import sys

from pymateng import *

def mateng_test0():
    '''Test DLL Level API'''

    # open a Matlab Engine
    ep = libeng.engOpen("");
    print("Engine handle: {}".format(ep))

    r = ctypes.c_bool(0)
    libeng.engGetVisible(ep, ctypes.byref(r))
    print("Visible: {}".format(r.value))

    libeng.engSetVisible(ep, ctypes.c_bool(0))
    libeng.engSetVisible(ep, ctypes.c_bool(1))

    bufsize = 256
    buf = ctypes.create_string_buffer('/0'*bufsize)
    print("Buffer object: {}".format(buf))

    libeng.engOutputBuffer(ep, buf, len(buf.value))

    libeng.engEvalString(ep, "matlabroot")
    print("Buffer raw: {}".format(buf.raw))
    print("Buffer value: {}".format(buf.value))

    libeng.engEvalString(ep, "format compact;")    

    # 注意以下两条语句的区别，加上分号则不会输出到命令窗口，
    # 此时缓冲区里面也不会有数据
    libeng.engEvalString(ep, "a1=1;")
    print("Buffer value: {}".format(buf.value))
    libeng.engEvalString(ep, "a2=1")
    print("Buffer value: {}".format(buf.value))
    
    libeng.engEvalString(ep, "pwd")
    #libeng.engEvalString(ep, "pwd;")

    ptr_a = libeng.engGetVariable(ep, "a1")
    libeng.engPutVariable(ep, "b", ptr_a)

    raw_input("Hit any key to exit ")

    libeng.engClose(ep)

def mateng_test1():
    '''Test Python Function Level API'''

    # open a Matlab Engine
    ep = engOpen("")
    print("Engine handle: {}".format(ep))

    r = engGetVisible(ep)
    print("Visible: {}".format(r))

    engSetVisible(ep, False)
    engSetVisible(ep, True)

    buf = ctypes.create_string_buffer('/0'*256)
    print("Buffer object: {}".format(buf))

    engOutputBuffer(ep, buf)

    engEvalString(ep, "matlabroot")
    print("Buffer raw: {}".format(buf.raw))
    print("Buffer value: {}".format(buf.value))

    engEvalString(ep, "format compact;")    

    engEvalString(ep, "a1=1;")
    print("Buffer value: {}".format(buf.value))
    engEvalString(ep, "a2=1")
    print("Buffer value: {}".format(buf.value))
    
    engEvalString(ep, "pwd")
    #engEvalString(ep, "pwd;")    

    ptr_a = engGetVariable(ep, "a1")
    engPutVariable(ep, "b", ptr_a)

    raw_input("Hit any key to exit ")

    engClose(ep)

def mateng_test2():
    '''Test Python Class Level API'''

    engine = MatEngine()

    engine.Open("")
    
    r = engine.GetVisible()    
    print("Visible: {}".format(r))

    engine.AttachOutputBuffer()

    engine.EvalString("pwd")

    print("Buffer value: {}".format(engine.GetOutputBuffer()))    

    raw_input("Hit any key to exit ")
    engine.Close()

if __name__ == "__main__":
    import sys
    level = 2
    if len(sys.argv) >= 2:
        level = int(sys.argv[1])

    if level == 0:
        mateng_test0()
    elif level == 1:
        mateng_test1()
    elif level == 2:
        mateng_test2()
    else:
        print >>sys.err, "error: invalid arguments [0|1|2]"

