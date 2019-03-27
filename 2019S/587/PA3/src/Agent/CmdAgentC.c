#include <jni.h>
#include <stdio.h>
#include "CmdAgentImpl.h"

#include <time.h>
#include <unistd.h>

JNIEXPORT jobject JNICALL Java_CmdAgentImpl_C_1GetLocalTime (JNIEnv * env, jobject thisObj, jobject obj) {
    jclass rst = (*env) -> FindClass(env, "GetLocalTime");
    jfieldID fidTime = (*env) -> GetFieldID(env, rst, "time", "I");
    jfieldID fidValid = (*env) -> GetFieldID(env, rst, "valid", "C");

    int cur_time = time(NULL);

    (*env) -> SetIntField(env, obj, fidTime, cur_time);
    (*env) -> SetCharField(env, obj, fidValid, 1);

    return obj;
}

JNIEXPORT jobject JNICALL Java_CmdAgentImpl_C_1GetVersion (JNIEnv * env, jobject thisObj, jobject obj) {
    jclass rst = (*env) -> FindClass(env, "GetVersion");
    //jfieldID fidVersion = (*env) -> GetFieldID(env, rst, "version", "Ljava/lang/String;");
    jfieldID fidVersion = (*env) -> GetFieldID(env, rst, "version", "I");

    char hostname[16];
    gethostname(hostname, sizeof(hostname));
    jstring version = (*env) -> NewStringUTF(env, hostname);

    //(*env) -> SetObjectField(env, obj, fidVersion, version);
    (*env) -> SetIntField(env, obj, fidVersion, 12);
    return obj;
}
