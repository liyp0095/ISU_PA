import sun.security.krb5.internal.crypto.Des;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

public class NeighbourMonitor extends Thread {
    ArrayList<Neighbour> neighbourArrayList;
    int neighbourSize;
    int neighbourSurviveTime;
    UDPSocket udpSocket;
    MessageMonitor messageMonitor;

    public void run() {
        System.out.println("Neighbour Monitor Starts ...");
        while (true) {
            try {
                NeighbourOverAllPing();
                NeighbourOverAllCheck();
                show();
                sleep(5000);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    NeighbourMonitor(UDPSocket udpSocket, MessageMonitor messageMonitor) {
        neighbourArrayList = new ArrayList<>();
        neighbourSize = 5;
        neighbourSurviveTime = 20;
        this.udpSocket = udpSocket;
        this.messageMonitor = messageMonitor;
    }

    public void NeighbourOverAllPing() throws IOException {
//        System.out.println("Ping Neighbour ... ");
        for (Neighbour neighbour : neighbourArrayList) {
//            System.out.println("Ping " + neighbour.ID);
            DescriptorHeader descriptorHeader = new DescriptorHeader();
            messageMonitor.add(new Message(descriptorHeader.getMessageID(), "0", 0));
            Util.ping(udpSocket, descriptorHeader, neighbour.IP, neighbour.port);
        }
    }

    public void NeighbourOverAllPing(Address address, DescriptorHeader descriptorHeader) throws IOException {
//        System.out.println("ping with  out");
        for (Neighbour neighbour : neighbourArrayList) {
            if (address.IP.equals(neighbour.IP) && address.port == neighbour.port) {
                continue;
            }
//            System.out.println("Ping " + neighbour.ID);
//            messageMonitor.add(new Message(descriptorHeader.getMessageID(), "0", 0));
            Util.ping(udpSocket, descriptorHeader, neighbour.IP, neighbour.port);
        }
    }

    public void NeighbourOverAllQuery(Address address, DescriptorHeader descriptorHeader, QueryPayLoad queryPayLoad) throws IOException {
        for (Neighbour neighbour : neighbourArrayList) {
            if (address.IP.equals(neighbour.IP) && address.port == neighbour.port) {
                continue;
            }
            System.out.println("Ping " + neighbour.ID);
//            messageMonitor.add(new Message(descriptorHeader.getMessageID(), "0", 0));
            Util.query(udpSocket, descriptorHeader, queryPayLoad, neighbour.IP, neighbour.port);
        }
    }

    void NeighbourOverAllCheck()
    {
        int currentTime = (int)(System.currentTimeMillis() / 1000);
        Iterator iterator = neighbourArrayList.iterator();
        while (iterator.hasNext()) {
            Neighbour neighbour = (Neighbour) iterator.next();
            if (currentTime - neighbour.latestTime > neighbourSurviveTime) {
                System.out.println("servent " + neighbour.ID + " offline!!! ");
                iterator.remove();
            }
        }
//        show();
        //System.out.println("list size: " + agentList.size());
    }

    public void add(Neighbour neighbour)
    {
        for (Neighbour item : neighbourArrayList) {
            if (item.ID.equals(neighbour.ID)) {
                item.latestTime = neighbour.latestTime;
                return;
            }
        }
        if (neighbourArrayList.size() >= neighbourSize)
            return;
        System.out.println("New servent " + neighbour.ID + " come ");
        neighbourArrayList.add(neighbour);
//        show();
    }

    public void show() {
        System.out.println("------------------ neighbours --------------------");
        for (Neighbour neighbour : neighbourArrayList) {
            System.out.println(neighbour.ID);
        }
        System.out.println("---------------- neighbours end ------------------");
    }
}
