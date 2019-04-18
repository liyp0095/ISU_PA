public class test {
    public static void main(String[] args) {
        try {
            UDPSocket socket = new UDPSocket(3000);
            byte[] buf = new byte[1024];
            Address address = new Address();
            socket.receive(buf, address);
            System.out.println(address.port);
            socket.send(buf, address.IP, address.port);
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}
