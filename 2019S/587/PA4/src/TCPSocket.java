import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class TCPSocket {
    Socket socket;
    DataInputStream inStream;
    DataOutputStream outStream;

    TCPSocket() {}

    TCPSocket(String IP, int port) throws IOException {
        this.socket = new Socket(IP, port);
        this.inStream = new DataInputStream(socket.getInputStream());
        this.outStream = new DataOutputStream(socket.getOutputStream());
    }

    public void write(byte[] buf) throws IOException {
        this.outStream.write(buf, 0, buf.length);
        this.outStream.flush();
    }

    public void read(byte[] buf) throws IOException {
        this.inStream.readFully(buf);
    }
}
