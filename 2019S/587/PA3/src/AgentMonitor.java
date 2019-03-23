import java.rmi.Naming;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.Iterator;

public class AgentMonitor extends Thread {
    ArrayList<AgentItem> agentItemArrayList;

    public AgentMonitor() {
        this.agentItemArrayList = new ArrayList<>();
    }

    public void run()
    {
        System.out.println("Agent Monitor Starts");

        while (true)
        {
            try {
                AgentOverAllCheck();
                sleep(1000);
            } catch (InterruptedException e)
            {
                System.out.println(e);
            }
        }
    }

    public void AgentOverAllCheck()
    {
        int currentTime = (int)(System.currentTimeMillis() / 1000);
        Iterator iterator = agentItemArrayList.iterator();
        while (iterator.hasNext()) {
            AgentItem a = (AgentItem) iterator.next();
            if (currentTime - a.latestTime > 10) {
                System.out.println("Agent " + a.ID + " ERROR!!! Move it out of the Agent List");
                iterator.remove();
                System.out.println("Now " + agentItemArrayList.size() + " agent(s) in the list. ");
            }
        }
        //System.out.println("list size: " + agentList.size());
    }

    public void add(Beacon b) {
        int currentTime = (int)(System.currentTimeMillis() / 1000);
        boolean needAdd = true;
        for (AgentItem agentItem : this.agentItemArrayList) {
            if (agentItem.ID == b.ID) {
                if (agentItem.StartUpTime != b.StartUpTime) {
                    System.out.println("Crashed host " + agentItem.ID + " come again. ");
                    agentItem.StartUpTime = b.StartUpTime;
                }
                agentItem.latestTime = currentTime;
                needAdd = false;
                break;
            }
        }
        if (needAdd) {
            System.out.println("new agent " + b.ID + " come!");
            AgentItem agentItem = new AgentItem();
            agentItem.ID = b.ID;
            agentItem.StartUpTime = b.StartUpTime;
            agentItem.latestTime = currentTime;
            agentItemArrayList.add(agentItem);
            // rmi call get local time
            try {
                String registry = "localhost";
                String registration = "rmi://" + registry + "/CmdAgent";
                Remote remoteService = Naming.lookup(registration);
                CmdAgent cmdAgent = (CmdAgent) remoteService;
                int t = (int)cmdAgent.execute("GetLocalTime", 12);
                System.out.println("It's local time is : " + t);
            } catch (Exception e) {
                System.err.println("Error - " + e);
            }
        }
    }
}
