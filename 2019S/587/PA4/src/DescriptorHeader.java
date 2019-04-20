import java.util.Random;

public class DescriptorHeader {
    ByteArray byteArray;
    Random rand;

    DescriptorHeader() {
        byteArray = new ByteArray(23);
        rand = new Random();
        setMessageID(rand.nextInt(10000));
        setPayload((byte)0x00);
        setTTL((byte)6);
        setHops((byte)0);
        setPayloadLength(0);
    }

    DescriptorHeader(byte[] bytes) {
        this.byteArray = new ByteArray(bytes);
    }

    public void setMessageID(int messageID) {
        byteArray.setTwoBytes(messageID, 0);
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

    public int getMessageID() {
        return byteArray.getTwoByteInteger(0);
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
}
