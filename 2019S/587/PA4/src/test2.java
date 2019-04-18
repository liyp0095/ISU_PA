import java.util.Arrays;

public class test2 {
    public static void main(String[] args) {
        try {
            UDPSocket socket = new UDPSocket(1300);
            byte[] buf;
            buf = "123".getBytes();
            socket.send(buf, "127.0.0.1", 3000);
            socket.receive(buf);
            System.out.println(new String(buf));
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}