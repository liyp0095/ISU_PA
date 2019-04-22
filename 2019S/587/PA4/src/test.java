import java.util.Random;

public class test {
    public static void main(String[] args) {
        try {

            Random random = new Random();
            int port = Integer.parseInt(args[0]);
            String queryCriteria = args[1];
            boolean firstConnect = true;

            UDPSocket sendUdpSocket = new UDPSocket(9091);
            UDPSocket recUdpSocket = new UDPSocket(9090);

            DescriptorHeader descriptorHeader;
            descriptorHeader = new DescriptorHeader();
            descriptorHeader.setPayload((byte)0x60);
            descriptorHeader.setMessageID("Query_"+String.format("%4d", random.nextInt(3000)));
            descriptorHeader.setPayloadLength(queryCriteria.length());

            QueryPayLoad queryPayLoad = new QueryPayLoad(queryCriteria);
            Util.query(sendUdpSocket, descriptorHeader, queryPayLoad, "127.0.0.1", port);
            System.out.println("send query ! ");

            byte[] buff = new byte[1024];
            recUdpSocket.receive(buff);
            descriptorHeader = new DescriptorHeader(buff);
            if (descriptorHeader.getPayload() == 0x61) {
                System.out.println("Query Hit");
                QueryHitPayLoad queryHitPayLoad = new QueryHitPayLoad(buff, 23);
                System.out.println("Hit @ " + queryHitPayLoad.getIP() + " : " + queryHitPayLoad.getPort());
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
