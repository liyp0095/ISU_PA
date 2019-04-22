import java.io.IOException;
import java.util.Random;

public class HandleCMD extends Thread {
    String cmd;
    Address address;
    DescriptorHeader descriptorHeader;
    UDPSocket udpSocket;
    LocalFileMonitor localFileMonitor;
    byte[] bytes;
    Random rand;
    int port;
    MessageMonitor messageMonitor;
    NeighbourMonitor neighbourMonitor;

    public HandleCMD(String cmd, int port, byte[] buff, UDPSocket udpSocket, Address address, DescriptorHeader descriptorHeader,
                     LocalFileMonitor localFileMonitor, MessageMonitor messageMonitor, NeighbourMonitor neighbourMonitor) throws IOException {
        this.cmd = cmd;
        this.address = address;
        this.descriptorHeader = descriptorHeader;
        this.udpSocket = udpSocket;
        this.localFileMonitor = localFileMonitor;
        this.bytes = buff;
//        this.rand = new Random();
//        this.udpSocket = new UDPSocket(rand.nextInt(4000) + 1000);
        this.port = port;
        this.messageMonitor = messageMonitor;
        this.neighbourMonitor = neighbourMonitor;
    }

    public void run() {
        try {
            switch (cmd) {
                case "Ping":
                    handlePing();
                    break;
                case "Pong":
                    handlePong();
                    break;
                case "Query":
                    handleQuery();
                    break;
                case "QueryHit":
                    handleQueryHit();
                    break;
                case "Push":
                    handlePush();
                    break;
                default:
                    break;
            }
        } catch (Exception e) {
            System.out.println("handle cmd error : " + e);
        }
    }

    private void handlePing() throws IOException {
//        messageMonitor.show();
        // todo pong address
        descriptorHeader.setPayload((byte)0x01);
        PongPayLoad pongPayLoad = new PongPayLoad();
        pongPayLoad.setNumberOfFiles(localFileMonitor.fileNumber);
        pongPayLoad.setNumberOfBytes(localFileMonitor.byteSize);
        pongPayLoad.setIP("127.0.0.1");
        pongPayLoad.setPort(port);
        Util.pong(udpSocket, descriptorHeader, pongPayLoad, address.IP, address.port);
        // todo ping all neighbours except address if ttl > 1
        Message message = messageMonitor.get(descriptorHeader.getMessageID());
        if (message == null) {
//            System.out.println("No this ping, forward!");
            int ttl = descriptorHeader.getTTL();
            int hops = descriptorHeader.getHops();
//            System.out.println(ttl);
            if (ttl - 1 > 0) {
                descriptorHeader.setTTL((byte) (ttl - 1));
                descriptorHeader.setHops((byte) (hops + 1));
                descriptorHeader.setPayload((byte) 0x00);
                neighbourMonitor.NeighbourOverAllPing(address, descriptorHeader);
//                System.out.println("ping add " + address.port);
//                neighbourMonitor.add(new Neighbour(address.IP, address.port));
                // todo add message
                messageMonitor.add(new Message(descriptorHeader.getMessageID(), address.IP, address.port));
            }
//            descriptorHeader.show();
        } else {
//            System.out.println("Get this ping already, drop");
        }
//        System.out.println("add ping into message monitor ... ");
    }

    private void handlePong() throws IOException {
        // todo pong it if message has this ping
//        System.out.println("to pong");
        PongPayLoad pongPayLoad = new PongPayLoad(bytes, 23);
        Message message = messageMonitor.get(descriptorHeader.getMessageID());
        int ttl = descriptorHeader.getTTL();
        int hops = descriptorHeader.getHops();
        if (ttl < 1) return;
        descriptorHeader.setTTL((byte)(ttl - 1));
        descriptorHeader.setHops((byte)(hops + 1));

        if (message == null) {
//            System.out.println("no other node ping this pong.");
        } else {
//            System.out.println("pong forward to " + message.MessageID + "\t" + message.IP + ":" + message.port);
            if (message.port != 0) {
                Util.pong(udpSocket, descriptorHeader, pongPayLoad, message.IP, message.port);
            }
        }

        // todo refresh neighbors
//        System.out.println("pong add " + address.port);
        neighbourMonitor.add(new Neighbour("127.0.0.1", pongPayLoad.getPort()));
    }

    private void handlePush() {
        // todo
    }

    private void handleQuery() throws IOException{
        // todo search self
        int ttl = descriptorHeader.getTTL();
        int hops = descriptorHeader.getHops();
        String MID = descriptorHeader.getMessageID();
        Message message = messageMonitor.get(MID);
        if (message != null)
            return;
        if (ttl < 1)
            return;
        System.out.println("handle query");
        int length = descriptorHeader.getPayloadLength();
        System.out.println("string length : " + length);
        QueryPayLoad queryPayLoad = new QueryPayLoad(bytes, 23, length);
        System.out.println("query : " + queryPayLoad.getString());
        LocalFile localFile = localFileMonitor.serch(queryPayLoad.getString());
        if (localFile == null) {
            // todo forward query
            if (ttl > 1) {
                descriptorHeader.setTTL((byte)(ttl - 1));
                descriptorHeader.setHops((byte)(hops + 1));
                neighbourMonitor.NeighbourOverAllQuery(address, descriptorHeader, queryPayLoad);
                messageMonitor.add(new Message(descriptorHeader.getMessageID(), address.IP, address.port));
            }
        } else {
            // todo back ward query hit
            QueryHitPayLoad queryHitPayLoad = new QueryHitPayLoad();
            queryHitPayLoad.setIP("127.0.0.1");
            queryHitPayLoad.setPort(port);
            descriptorHeader.setPayload((byte)0x61);
            descriptorHeader.setPayloadLength(8);
            Util.queryHit(udpSocket, descriptorHeader, queryHitPayLoad, address.IP, address.port);
            System.out.println("Query hit! sent to " + address.IP + ":" + address.port);
        }
    }

    private void handleQueryHit() throws IOException {
        // todo if memory has this query id forward this
        int ttl = descriptorHeader.getTTL();
        int hops = descriptorHeader.getHops();
        if (ttl < 1)
            return;
        String MID = descriptorHeader.getMessageID();
        Message message = messageMonitor.get(MID);
        QueryHitPayLoad queryHitPayLoad = new QueryHitPayLoad(bytes, 23);
        if (message == null) {
            System.out.println("Query hit @ " + queryHitPayLoad.getIP() + " : " + queryHitPayLoad.getPort());
            return;
        } else {
            descriptorHeader.setTTL((byte)(ttl - 1));
            descriptorHeader.setHops((byte)(hops + 1));
            Util.queryHit(udpSocket, descriptorHeader, queryHitPayLoad, message.IP, message.port);
        }
    }
}
