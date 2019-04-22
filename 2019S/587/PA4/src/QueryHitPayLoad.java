import java.net.InetAddress;

public class QueryHitPayLoad {
    ByteArray byteArray;

    public QueryHitPayLoad() {
        byteArray = new ByteArray(8);
    }

    public QueryHitPayLoad(byte[] buff, int offset) {
        byte[] data = new byte[8];
        System.arraycopy(buff, offset, data, 0, 8);
        byteArray = new ByteArray(data);
    }

    public void setPort(int port) {
        byteArray.setBytes(port, 0);
    }

    public void setIP(String IP) {
        try {
            InetAddress ip = InetAddress.getByName(IP);
            byteArray.setBytes(ip.getAddress(), 4);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public String getIP() {
        try {
            InetAddress ip = InetAddress.getByAddress(byteArray.getBytes(4, 8));
            return ip.getHostAddress();
        } catch (Exception e) {
            System.out.println(e);
        }
        return "";
    }

    public int getPort() {
        return byteArray.getInteger(0);
    }

}
