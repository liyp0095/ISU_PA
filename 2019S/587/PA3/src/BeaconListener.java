import java.rmi.RemoteException;

public interface BeaconListener extends java.rmi.Remote {
    int deposit(Beacon b) throws RemoteException;
}
