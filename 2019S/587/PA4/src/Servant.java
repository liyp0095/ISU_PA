import java.util.Random;

import static java.lang.Thread.getDefaultUncaughtExceptionHandler;
import static java.lang.Thread.sleep;

public class Servant {
    public static void main(String[] args) {
        Random random = new Random();
        System.out.println(args.length);
        int port = Integer.parseInt(args[0]);
        int recPort = port;
        int sendPort = port + 1;
        int firstConnectPort = 0;
        boolean firstConnect = false;
        boolean queryOrNot = false;
        String queryCriteria = "";
        if (args.length > 1) {
            firstConnectPort = Integer.parseInt(args[1]);
            firstConnect = true;
        }

        if (args.length > 2) {
            queryOrNot = true;
            queryCriteria = args[2];
        }

        LocalFileMonitor localFileMonitor = new LocalFileMonitor();
        localFileMonitor.show();

        MessageMonitor messageMonitor = new MessageMonitor();
        messageMonitor.start();


        try {
            byte[] buff = new byte[1024];
            UDPSocket sendUdpSocket = new UDPSocket(sendPort);
            UDPSocket recUDPSocket = new UDPSocket(recPort);

            Address address = new Address();
            DescriptorHeader descriptorHeader = new DescriptorHeader();

            if (firstConnect)
                Util.ping(sendUdpSocket, descriptorHeader, "127.0.0.1", firstConnectPort);
            descriptorHeader.show();

            NeighbourMonitor neighbourMonitor = new NeighbourMonitor(sendUdpSocket, messageMonitor);
            neighbourMonitor.start();

            while (true) {
                recUDPSocket.receive(buff, address);
                descriptorHeader = new DescriptorHeader(buff);
//                descriptorHeader.show();
                int payLoad = descriptorHeader.getPayload();
//                descriptorHeader.show();
                if (payLoad == 0x00) {
//                    System.out.println("receive ping .. ");
                    new HandleCMD("Ping", recPort, buff, sendUdpSocket, address, descriptorHeader, localFileMonitor, messageMonitor, neighbourMonitor).start();
                } else if (payLoad == 0x01) {
//                    System.out.println("receive pong .. ");
                    new HandleCMD("Pong", recPort, buff, sendUdpSocket, address, descriptorHeader, localFileMonitor, messageMonitor, neighbourMonitor).start();
                } else if (payLoad == 0x60) {
                    System.out.println("receive query .. ");
                    new HandleCMD("Query", recPort, buff, sendUdpSocket, address, descriptorHeader, localFileMonitor, messageMonitor, neighbourMonitor).start();
                } else if (payLoad == 0x61) {
//                    System.out.println("receive pong .. ");
                    new HandleCMD("QueryHit", recPort, buff, sendUdpSocket, address, descriptorHeader, localFileMonitor, messageMonitor, neighbourMonitor).start();
                } else if (payLoad == 0x40) {
//                    System.out.println("receive pong .. ");
                    new HandleCMD("Push", recPort, buff, sendUdpSocket, address, descriptorHeader, localFileMonitor, messageMonitor, neighbourMonitor).start();
                }
            }
        } catch (Exception e) {
            System.out.println("servent error : " + e);
        }
    }
}