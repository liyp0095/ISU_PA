import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;

public class BeaconListenerImpl extends UnicastRemoteObject implements BeaconListener {
    ArrayList<AgentItem> agentItemArrayList;
    AgentMonitor agentMonitor;

    public BeaconListenerImpl() throws RemoteException {
        this.agentItemArrayList = new ArrayList<>();
        this.agentMonitor = new AgentMonitor();
        agentMonitor.start();
    }

    public int deposit(Beacon b) throws RemoteException {
        agentMonitor.add(b);
        return 1;
    }
}
