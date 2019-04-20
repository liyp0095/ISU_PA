public class Servant {
    public static void main(String[] args) {
        int port = Integer.getInteger(args[0]);
        int firstConnectPort = 0;
        boolean firstConnect = false;
        if (args.length > 1) {
            firstConnectPort = Integer.getInteger(args[1]);
            firstConnect = true;
        }

        LocalFileMonitor localFileMonitor = new LocalFileMonitor();
        localFileMonitor.show();
        MessageMonitor messageMonitor = new MessageMonitor();
        try {
            UDPSocket udpSocket = new UDPSocket(port);
            NeighbourMonitor neighbourMonitor = new NeighbourMonitor(udpSocket);
            neighbourMonitor.run();

            if (firstConnect)
                neighbourMonitor.ping("127.0.0.1", firstConnectPort, 3);

            while (true) {
                byte[] buff = new byte[23];
                Address address = new Address();
                udpSocket.receive(buff, address);
                DescriptorHeader descriptorHeader = new DescriptorHeader(buff);
                int payLoad = descriptorHeader.getPayload();
                if (payLoad == 0x00) {
                    int ttl = descriptorHeader.getTTL() - 1;
                    if (ttl <= 0)
                        continue;
                    descriptorHeader.setTTL((byte)ttl);
                    descriptorHeader.setHops((byte)(descriptorHeader.getHops()+1));
                    neighbourMonitor.NeighbourOverAllPing(address, descriptorHeader);
                    messageMonitor.add(new Message(descriptorHeader.getMessageID(), address));
                    descriptorHeader.setHops((byte)0);
                    descriptorHeader.setTTL((byte)4);
                    descriptorHeader.setPayload((byte)0x01);
                    descriptorHeader.setPayloadLength(16);
                    PongPayLoad pongPayLoad = new PongPayLoad();
                    pongPayLoad.setPort(port);
                    pongPayLoad.setIP("127.0.0.1");
                    pongPayLoad.setNumberOfBytes(localFileMonitor.fileNumber);
                    pongPayLoad.setNumberOfBytes(localFileMonitor.byteSize);
                    neighbourMonitor.pong(address.IP, address.port, descriptorHeader, pongPayLoad);
                } else if (payLoad == 0x01) {
                    PongPayLoad pongPayLoad = new PongPayLoad();
                    udpSocket.receive(pongPayLoad.byteArray.bytes);
                    int MID = descriptorHeader.getMessageID();
                    Message m = messageMonitor.get(MID);
                    neighbourMonitor.add(new Neighbour(address.IP, address.port));
                    if (m == null)
                        continue;
                    neighbourMonitor.pong(m.hostAddress.IP, m.hostAddress.port, descriptorHeader, pongPayLoad);
                }
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}