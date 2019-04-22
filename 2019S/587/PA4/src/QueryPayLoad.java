public class QueryPayLoad {
    ByteArray byteArray;

    public QueryPayLoad(String string) {
        byteArray = new ByteArray(string.length());
        byteArray.setBytes(string, 0);
    }

    public QueryPayLoad(byte[] buff, int offset, int length) {
        byteArray = new ByteArray(length);
        byte[] data = new byte[length];
        System.arraycopy(buff, offset, data, 0, length);
        byteArray.setBytes(data);
    }

    public String getString() {
        return new String(byteArray.bytes);
    }
}
