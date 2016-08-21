#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "engine.h"

#include <stdint.h>
typedef uint32_t Handle;

typedef struct {
	char *data;
	int size;
	bool valid;
} Buffer;

static Buffer bufferobj = {NULL, 0, false};

int PyReAllocateBuffer(int bufsize) {
	assert(bufsize > 0);

	if (bufferobj.valid == true) {
		fprintf(stdin, "Buffer object is currently in use, please release it first\n");
		return 1;
	}

	char *pbuf = (char *) calloc(bufsize, sizeof(char));
	if (NULL == pbuf) {
		fprintf(stderr, "Faild to allocate space for buffer\n");
		return -1;
	}

	bufferobj.data = pbuf;
	bufferobj.size = bufsize;
	bufferobj.valid = true;

	return 0;
}

int PyReleaseBuffer(void) {
	if (bufferobj.valid == false) {
		return 0;
	}

	free(bufferobj.data);
	bufferobj.data = NULL;
	bufferobj.size = 0;
	bufferobj.valid = false;

	return 0;
}

char *PyGetBufferData(void) {
	if (bufferobj.valid) {
		return (char *)bufferobj.data;
	} else {
		return (char *)(0);
	}
}

/*
 * Start matlab process
 */
Handle PyEngOpen(const char *startcmdstr) {
	Engine * ep = engOpen(startcmdstr);
	return (Handle) ep;
}

/*
 * Start matlab process for single use.
 * Not currently supported on UNIX.
 */
Handle PyEngOpenSingleUse(const char *startcmdstr) {
	int retstatus;
	return (Handle) engOpenSingleUse(startcmdstr, (void*) 0, &retstatus);
}

/*
 * Close down matlab server
 */
int PyEngClose(Handle ep) {
	return engClose((Engine *) ep);
}

/* 
 * GetVisible, do nothing since this function is only for NT 
 */ 
bool PyEngGetVisible(Handle ep) {
	bool flag = false;
	engGetVisible((Engine *) ep, &flag);

	return flag;
}

/*
 * SetVisible, do nothing since this function is only for NT 
 */ 
int PyEngSetVisible(Handle ep, bool flag) {
	return engSetVisible((Engine *) ep, flag);
}

/*
 * Execute matlab statement
 */
int PyEngEvalString(Handle ep, const char *stmt) {
	return engEvalString((Engine *) ep, stmt);
}

/*
 * Get a variable with the specified name from MATLAB's workspace
 */
Handle PyEngGetVariable(Handle ep, const char *name) {
	return (Handle) engGetVariable((Engine *) ep, name);
}

/*
 * Put a variable into MATLAB's workspace with the specified name
 */
int PyEngPutVariable(Handle ep, const char *name, Handle ap) {
	return engPutVariable((Engine *) ep, name, (const mxArray *) ap);
}

/*
 * register a buffer to hold matlab text output
 */
int PyEngOutputBuffer(Handle ep) {
	assert((false != bufferobj.valid) && (NULL != bufferobj.data) && (0 != bufferobj.size));
	return engOutputBuffer((Engine *) ep, bufferobj.data, bufferobj.size);
}
