import java.util.Random;

public class DescriptorHeader {
    ByteArray byteArray;
    Random rand;

    DescriptorHeader() {
        byteArray = new ByteArray(23);
        rand = new Random();
        setMessageID("Ping_" + String.format("%4d", rand.nextInt(10000)));
        setPayload((byte)0x00);
        setTTL((byte)6);
        setHops((byte)0);
        setPayloadLength(0);
    }

    DescriptorHeader(byte[] bytes) {
        byte[] data = new byte[23];
        System.arraycopy(bytes, 0, data, 0, 23);
        this.byteArray = new ByteArray(data);
    }

    public void setMessageID(String messageID) {
        byteArray.setBytes(messageID, 0);
    }

    public void setPayload(byte b) {
        byteArray.setByte(b, 16);
    }

    public void setTTL(byte b) {
        byteArray.setByte(b, 17);
    }

    public void setHops(byte b) {
        byteArray.setByte(b, 18);
    }

    public void setPayloadLength(int payloadLength) {
        byteArray.setBytes(payloadLength, 19);
    }

    public String getMessageID() {
        return byteArray.getString(0, 16);
    }

    public byte getPayload() {
        return byteArray.getByte(16);
    }

    public byte getTTL() {
        return byteArray.getByte(17);
    }

    public byte getHops() {
        return byteArray.getByte(18);
    }

    public int getPayloadLength() {
        return byteArray.getInteger(19);
    }

    public void show() {
        System.out.print(getMessageID() + "\t");
        System.out.print(Integer.toString(getPayload()) + "\t");
        System.out.print(Integer.toString(getTTL()) + "\t");
        System.out.print(Integer.toString(getPayloadLength()) + "\n");
    }
}
