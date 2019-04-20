import sun.security.krb5.internal.crypto.Des;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

public class NeighbourMonitor extends Thread {
    ArrayList<Neighbour> neighbourArrayList;
    int neighbourSize;
    int neighbourSurviveTime;
    UDPSocket udpSocket;

    public void run() {
        System.out.println("Neighbour Monitor Starts ...");
        while (true) {
            try {
                NeighbourOverAllPing();
                NeighbourOverAllCheck();
                sleep(5000);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    NeighbourMonitor(UDPSocket udpSocket) {
        neighbourArrayList = new ArrayList<>();
        neighbourSize = 3;
        neighbourSurviveTime = 60;
        udpSocket = udpSocket;
    }

    void NeighbourOverAllPing() throws IOException {
        for (Neighbour neighbour : neighbourArrayList) {
            ping(neighbour.IP, neighbour.port, 3);
        }
    }

    public void NeighbourOverAllPing(Address address, DescriptorHeader descriptorHeader) throws IOException {
        for (Neighbour neighbour : neighbourArrayList) {
            if (address.IP != neighbour.IP || address.port != neighbour.port)
                ping(neighbour.IP, neighbour.port, descriptorHeader);
        }
    }

    void NeighbourOverAllCheck()
    {
        int currentTime = (int)(System.currentTimeMillis() / 1000);
        Iterator iterator = neighbourArrayList.iterator();
        while (iterator.hasNext()) {
            Neighbour neighbour = (Neighbour) iterator.next();
            if (currentTime - neighbour.latestTime > neighbourSurviveTime) {
                System.out.println("Agent " + neighbour.ID + " ERROR!!! Move it out of the Agent List");
                iterator.remove();
                System.out.println("Now " + neighbourArrayList.size() + " agent(s) in the list. ");
            }
        }
        //System.out.println("list size: " + agentList.size());
    }

    public void add(Neighbour neighbour)
    {
        for (Neighbour item : neighbourArrayList) {
            if (item.ID == neighbour.ID) {
                item.latestTime = neighbour.latestTime;
                return;
            }
        }
        if (neighbourArrayList.size() >= neighbourSize)
            return;
        System.out.println("New agent " + neighbour.ID + " come, add it to the agent list. ");
        System.out.println(" * Port: " + neighbour.port);
        System.out.println(" * IP:   " + neighbour.IP);
        neighbourArrayList.add(neighbour);
        System.out.println("Now " + neighbourArrayList.size() + " agent(s) in the list. ");
    }

    public void ping(String IP, int port, int ttl) throws IOException {
        DescriptorHeader descriptorHeader = new DescriptorHeader();
        descriptorHeader.setTTL((byte) ttl);
        udpSocket.send(descriptorHeader, IP, port);
    }

    public void ping(String IP, int port, DescriptorHeader descriptorHeader) throws IOException {
        udpSocket.send(descriptorHeader, IP, port);
    }

    public void pong(String IP, int port, DescriptorHeader descriptorHeader, PongPayLoad pongPayLoad) throws IOException {
        udpSocket.send(descriptorHeader, IP, port);
        udpSocket.send(pongPayLoad.byteArray.bytes, IP, port);
    }
}
