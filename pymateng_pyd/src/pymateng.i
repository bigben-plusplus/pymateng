%module pymateng
%{
// Put header files here (optional)
#include <stdio.h>
#include "engine.h"

//#include <stddef.h>
#include <stdint.h>
typedef uint32_t Handle;

extern int PyReAllocateBuffer(int bufsize);
extern int PyReleaseBuffer(void);
extern char *PyGetBufferData(void);

extern Handle PyEngOpen(const char *startcmdstr);
extern Handle PyEngOpenSingleUse(const char *startcmdstr);
extern int PyEngClose(Handle ep);
extern bool PyEngGetVisible(Handle ep);
extern int PyEngSetVisible(Handle ep, bool flag);
extern int PyEngEvalString(Handle ep, const char *stmt);
extern Handle PyEngGetVariable(Handle ep, const char *name);
extern int PyEngPutVariable(Handle ep, const char *name, Handle ap);
extern int PyEngOutputBuffer(Handle ep);

%}


extern int PyReAllocateBuffer(int bufsize);
extern int PyReleaseBuffer(void);
extern char *PyGetBufferData(void);

extern Handle PyEngOpen(const char *startcmdstr);
extern Handle PyEngOpenSingleUse(const char *startcmdstr);
extern int PyEngClose(Handle ep);
extern bool PyEngGetVisible(Handle ep);
extern int PyEngSetVisible(Handle ep, bool flag);
extern int PyEngEvalString(Handle ep, const char *stmt);
extern Handle PyEngGetVariable(Handle ep, const char *name);
extern int PyEngPutVariable(Handle ep, const char *name, Handle ap);
extern int PyEngOutputBuffer(Handle ep);

