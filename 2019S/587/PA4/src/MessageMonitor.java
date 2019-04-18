import java.util.ArrayList;

public class MessageMonitor {
    ArrayList<Message> messageArrayList = new ArrayList<>();

    public void add(Message message) {
        messageArrayList.add(message);
    }

    public void delete(Message message) {
        messageArrayList.remove(message);
    }

    public void delete(int messageId) {
        int index = 0;
        for (Message message : messageArrayList) {
            if (message.MessageID == messageId) {
                index = messageArrayList.indexOf(message);
            }
        }
        messageArrayList.remove(index);
    }

    public void show() {
        for (Message message : messageArrayList) {
            System.out.println(message.MessageID + "\t" + message.hostAddress.IP + "\t"
                    + Integer.toString(message.hostAddress.port));
        }
    }
}
