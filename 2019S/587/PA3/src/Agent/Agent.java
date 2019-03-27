import java.rmi.Naming;
import java.rmi.Remote;
import java.rmi.server.RemoteRef;

import static java.lang.Thread.sleep;

public class Agent {
    public static void main(String[] args) {
        int currentTime = (int)(System.currentTimeMillis() / 1000);
        Beacon b = new Beacon();
        b.ID = 10;
        b.StartUpTime = currentTime;

        // bind cmd agent server
        try {
            CmdAgentImpl cmdAgentServer = new CmdAgentImpl();
            String registry = "localhost";
            String registration = "rmi://" + registry + "/CmdAgent";
            Naming.rebind(registration, cmdAgentServer);
        } catch (Exception e) {
            System.err.println("Error - " + e);
        }

        // rmi call deposit beacon
        try {
            if (args.length > 0) {
                b.ID = Integer.parseInt(args[0]);
            }

            String registry = "localhost";
            String registration = "rmi://" + registry + "/BeaconListener";
            Remote remoteService = Naming.lookup(registration);
            BeaconListener beaconListener = (BeaconListener) remoteService;
            while (true) {
                System.out.println("send beacon");
                beaconListener.deposit(b);
                sleep(2000);
            }
        } catch (Exception e) {
            System.err.println("Error - " + e);
        }
    }
}
