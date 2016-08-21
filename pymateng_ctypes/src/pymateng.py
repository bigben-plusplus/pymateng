# -*- coding:utf-8 -*-

import ctypes


def loadLibEngineDLL(libengname=None):
    if libengname is None:
        import json
        from os.path import dirname, abspath

        matlabinfo = json.load(file(dirname(abspath(__file__)) + "\\matlab.json"))
        libengname = matlabinfo["root"]+ "\\bin\\" + matlabinfo["platform"] + "\\libeng.dll"

    libeng = ctypes.CDLL(libengname)

    return libeng

class mxArray(ctypes.Structure):
    _fields_ = []

class Engine(ctypes.Structure):
	_fields_ = []

libeng = loadLibEngineDLL()

def engOpen(startcmd=""):
    ep = libeng.engOpen(startcmd)
    return ep

def engOpenSingleUse(startcmd=""):
    ep = libeng.engOpenSingleUse(startcmd)
    return ep

def engClose(ep):
    return libeng.engClose(ep)

def engGetVisible(ep):
    r = ctypes.c_bool(False)
    libeng.engGetVisible(ep, ctypes.byref(r))
    return r.value

def engSetVisible(ep, flag=False):
    return libeng.engSetVisible(ep, ctypes.c_bool(flag))

def engGetVariable(ep, name):
    ptr = libeng.engGetVariable(ep, name)
    return ptr

def engPutVariable(ep, name, value):
    return libeng.engPutVariable(ep, name, value)

def engEvalString(ep, stmt):
    return libeng.engEvalString(ep, stmt)

def engOutputBuffer(ep, buffer=None):
    if buffer is None:
        buffer = ctypes.create_string_buffer('/0'*256)
    return libeng.engOutputBuffer(ep, buffer, len(buffer.value))

class MatEngine():
    ep = None

    def __init__(self, buflen=512):
        self.buffer = ctypes.create_string_buffer('/0'*buflen)

    def AttachOutputBuffer(self, buf=None):
        if buf is None:
            buf = self.buffer
        else:
            self.buf = buf

        return engOutputBuffer(self.ep, buf)

    def GetOutputBuffer(self):
        return self.buffer.value

    def Open(self, startcmd=""):
        self.ep = engOpen(startcmd)        

    def OpenSingleUse(self, startcmd=""):
        self.ep = engOpenSingleUse(startcmd)

    def Close(self):
        return engClose(self.ep)

    def GetVisible(self):
        return engGetVisible(self.ep)

    def SetVisible(self, flag=False):
        return engSetVisible(self.ep, ctypes.c_bool(flag))

    def EvalString(self, stmt):
        engEvalString(self.ep, stmt)

    def GetVariable(self, name):
        return engPutVariable(self.ep, name)

    def PuttVariable(self, name, value):
        engPutVariable(self.ep, name, value)


if __name__ == "__main__":
    import sys

    import test_pymateng as p

    level = 2
    if len(sys.argv) >= 2:
        level = int(sys.argv[1])

    if level == 0:
        p.mateng_test0()
    elif level == 1:
        p.mateng_test1()
    elif level == 2:
        p.mateng_test2()
    else:
        print >>sys.stderr, "error: invalid arguments [0|1|2]"

