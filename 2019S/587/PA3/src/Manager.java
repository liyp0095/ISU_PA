import java.rmi.Naming;
import java.rmi.server.RemoteRef;

public class Manager {

    public static void main(String args[]) {
        // bind beacon listener server
        try {
            BeaconListenerImpl beaconListenerSever = new BeaconListenerImpl();
            RemoteRef location = beaconListenerSever.getRef();
            System.out.println(location.remoteToString());
            String registry = "localhost";
            String registration = "rmi://" + registry + "/BeaconListener";
            Naming.rebind(registration, beaconListenerSever);
        } catch (Exception e) {
            System.err.println("Error - " + e);
        }
    }
}
