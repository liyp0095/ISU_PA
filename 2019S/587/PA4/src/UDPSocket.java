import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPSocket {
    DatagramSocket socket;
    DatagramPacket packet;

    UDPSocket(int port) throws IOException {
        this.socket = new DatagramSocket(port);
    }

    public void send(byte[] buf, String IP, int port) throws IOException {
        InetAddress inetAddress = InetAddress.getByName(IP);
        packet = new DatagramPacket(buf, buf.length, inetAddress, port);
        socket.send(packet);
    }

    public void send(DescriptorHeader descriptorHeader, String IP, int port) throws IOException {
        byte[] buf = descriptorHeader.byteArray.bytes;
        InetAddress inetAddress = InetAddress.getByName(IP);
        packet = new DatagramPacket(buf, buf.length, inetAddress, port);
        socket.send(packet);
    }

    public void receive(byte[] buf) throws IOException {
        packet = new DatagramPacket(buf, buf.length);
        socket.receive(packet);
        System.arraycopy(packet.getData(), 0, buf, 0, buf.length);
    }

    public void receive(byte[] buf, Address address) throws IOException {
        packet = new DatagramPacket(buf, buf.length);
        socket.receive(packet);
        address.IP = packet.getAddress().getHostAddress();
        address.port = packet.getPort();
        System.arraycopy(packet.getData(), 0, buf, 0, buf.length);
    }
}
