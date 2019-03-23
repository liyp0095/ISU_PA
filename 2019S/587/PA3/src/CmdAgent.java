import java.rmi.RemoteException;

public interface CmdAgent extends java.rmi.Remote {
    Object execute(String CmdID, Object CmdObj) throws RemoteException;
}
