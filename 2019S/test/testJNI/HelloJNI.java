public class HelloJNI {
    static {
        System.loadLibrary("hello");
    }

    public native void sayHello();
}
