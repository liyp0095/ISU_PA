public class test {
    public static void main(String[] args) {
        Servant servant = new Servant(3000);
        servant.ping("127.0.0.1", 4000);
    }
}
