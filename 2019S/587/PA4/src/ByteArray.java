import java.util.Arrays;

public class ByteArray {
    byte[] bytes;

    ByteArray(int n) {
        bytes = new byte[n];
        for (int i = 0; i < bytes.length; i++ ) {
            bytes[i] = 0;
        }
    }

    ByteArray(byte[] bytes) { this.bytes = bytes; }

    public byte[] getBytes() {
        return bytes;
    }

    public byte getByte(int n) {
        return this.bytes[n];
    }

    public byte[] getBytes(int m, int n) {
        return Arrays.copyOfRange(this.bytes, m, n);
    }

    public String getString() {
        return new String(bytes);
    }

    public String getString(int offset, int length) {
        return new String(Arrays.copyOfRange(this.bytes, offset, offset+length));
    }

    public int getInteger(int offset) {
        return byteArrayToInteger(getBytes(offset, offset + 4));
    }

    public int getTwoByteInteger(int offset) {
        return byteArrayToTwoByteInteger(getBytes(offset, offset + 2));
    }

    public void setBytes(byte[] bytes) {
        this.bytes = bytes;
    }

    public void setByte(byte b, int n) {
        this.bytes[n] = b;
    }

    public void setBytes(byte[] bytes, int offset) {
        for (int i = 0; i < bytes.length; i ++ ) {
            this.bytes[offset + i] = bytes[i];
        }
    }

    public void setBytes(int value, int offset) {
        setBytes(intToByteArray(value), offset);
    }

    public void setTwoBytes(int value, int offset) {
        setBytes(twoByteIntToByteArray(value), offset);
    }

    public void setBytes(String string, int offset) {
        setBytes(string.getBytes(), offset);
    }

    public byte[] intToByteArray(int value) {
        return new byte[] {
                (byte)(value >>> 24),
                (byte)(value >>> 16),
                (byte)(value >>> 8),
                (byte)value};
    }

    public byte[] twoByteIntToByteArray(int value) {
        return new byte[] {
                (byte)(value >>> 8),
                (byte)value};
    }

    public int byteArrayToInteger(byte[] bytes) {
        return bytes[0] << 24 | (bytes[1] & 0xFF) << 16 | (bytes[2] & 0xFF) << 8 | (bytes[3] & 0xFF);
    }

    public int byteArrayToTwoByteInteger(byte[] bytes) {
        return (bytes[0] & 0xFF) << 8 | (bytes[1] & 0xFF);
    }

    public ByteArray add(ByteArray byteArray) {
        ByteArray b = new ByteArray(this.bytes.length + byteArray.bytes.length);
        b.setBytes(this.bytes, 0);
        b.setBytes(byteArray.bytes, this.bytes.length);
        return b;
    }

    public void show() {
        for (int i = 0; i < bytes.length; i ++ ) {
            System.out.print(bytes[i]);
            System.out.println();
        }
    }
}
