public class Message {
    String MessageID;
    String IP;
    int port;
    int latestTime;

    Message(String messageID, String IP, int port) {
        this.MessageID = messageID;
        this.IP = IP;
        this.port = port;
        this.latestTime = (int)(System.currentTimeMillis() / 1000);
    }
}
