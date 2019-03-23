#include <jni.h>
#include <stdio.h>
#include "CmdAgentImpl.h"

#include <time.h>

JNIEXPORT jobject JNICALL Java_CmdAgentImpl_C_1GetLocalTime (JNIEnv * env, jobject obj1, jobject obj2) {
    jclass rstClass;

    rstClass = (*env) -> GetObjectClass(env, obj2);
    int cur_time = time(NULL);
    rstClass.time = cur_time;
    rstClass.valid = 1;
    return rstClass;
}

JNIEXPORT jobject JNICALL Java_CmdAgentImpl_C_1GetVersion (JNIEnv * env, jobject obj1, jobject obj2) {
    char hostname[16];
    int valid = 0;

    if (gethostname(hostname, sizeof(hostname)))
    {
        valid = 1;
    }
    *obj2 = hostname;
    return *obj2;
}
