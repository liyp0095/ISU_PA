public class Neighbour {
    String name;
    String IP;
    int port;
    String ID;
    int startUpTime;
    int latestTime;

    Neighbour(String IP, int port) {
        this.IP = IP;
        this.port = port;
        this.ID = IP + "_" + Integer.toString(port);
        this.latestTime = (int)(System.currentTimeMillis() / 1000);
    }
}
