import java.io.IOException;

public class Util {
    public static void ping(UDPSocket udpSocket, DescriptorHeader descriptorHeader, String IP, int port) throws IOException {
        udpSocket.send(descriptorHeader.byteArray.bytes, IP, port);
    }

    public static void pong(UDPSocket udpSocket, DescriptorHeader descriptorHeader, PongPayLoad pongPayLoad, String IP, int port) throws IOException {
        ByteArray byteArray = descriptorHeader.byteArray.add(pongPayLoad.byteArray);
//        udpSocket.send(descriptorHeader.byteArray.bytes, IP, port);
//        udpSocket.send(pongPayLoad.byteArray.bytes, IP, port);
        udpSocket.send(byteArray.bytes, IP, port);
//        System.out.println("Pong " + IP + ":" + port);
    }

    public static void query(UDPSocket udpSocket, DescriptorHeader descriptorHeader, QueryPayLoad queryPayLoad, String IP, int port) throws IOException {
        ByteArray byteArray = descriptorHeader.byteArray.add(queryPayLoad.byteArray);
        udpSocket.send(byteArray.bytes, IP, port);
    }

    public static void queryHit(UDPSocket udpSocket, DescriptorHeader descriptorHeader, QueryHitPayLoad queryHitPayLoad, String IP, int port) throws IOException {
        ByteArray byteArray = descriptorHeader.byteArray.add(queryHitPayLoad.byteArray);
        udpSocket.send(byteArray.bytes, IP, port);
    }
}
