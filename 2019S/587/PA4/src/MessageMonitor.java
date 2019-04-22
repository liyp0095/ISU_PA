import java.util.ArrayList;

public class MessageMonitor extends Thread {
    ArrayList<Message> messageArrayList;

    public void run() {
        while (true) {
            try {
                MessageOverAllCheck();
//                show();
                sleep(6000);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    MessageMonitor() {
        messageArrayList = new ArrayList<>();
    }

    private void MessageOverAllCheck() {
        int curTime = (int)(System.currentTimeMillis() / 1000);
        int index = -1;
        for (Message message : messageArrayList) {
            if (curTime - message.latestTime > 20) {
                index = messageArrayList.indexOf(message);
            }
        }
        if (index >= 0) {
            messageArrayList.remove(index);
        }
    }

    public void add(Message message) {
        for (Message m : messageArrayList) {
            if (message.MessageID.contains(m.MessageID)) {
                m.latestTime = message.latestTime;
                return;
            }
        }
        messageArrayList.add(message);
    }

    public void delete(Message message) {
        messageArrayList.remove(message);
    }

    public void delete(String messageId) {
        int index = 0;
        for (Message message : messageArrayList) {
            if (message.MessageID.equals(messageId)) {
                index = messageArrayList.indexOf(message);
            }
        }
        messageArrayList.remove(index);
    }

    public Message get(String messageID) {
        for (Message message : messageArrayList) {
            if (messageID.contains(message.MessageID)) {
                return message;
            }
        }
        return null;
    }

    public void show() {
        System.out.println("================ Now has Message ===================");
        for (Message message : messageArrayList) {
            System.out.println(message.MessageID + "\t" + message.IP + "\t"
                    + Integer.toString(message.port) + "\t" + message.latestTime);
        }
        System.out.println("======================= end ========================");
    }
}
