import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CmdAgentImpl extends UnicastRemoteObject implements CmdAgent {

    static {
        System.loadLibrary("CmdAgentC");
    }

    public CmdAgentImpl() throws RemoteException {}

    private native Object C_GetLocalTime(Object CmdObj);
    private native Object C_GetVersion(Object CmdObj);

    public Object execute(String CmdID, Object CmdObj) throws RemoteException {
        if (CmdID.equals("GetLocalTime")) {
            return C_GetLocalTime((GetLocalTime)CmdObj);
            //return "local time";
        }
        else if (CmdID.equals("GetVersion")) {
            return C_GetVersion((GetVersion)CmdObj);
            //return "version";
        }
        return 1;
    }
}
