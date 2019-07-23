import java.util.ArrayList;

public class WeightedQueue {
    public ArrayList<Node<String>> weightedQueue;

    public WeightedQueue() {
        weightedQueue = new ArrayList<Node<String>>();
    }

    public void add(Node<String> node) {
        int pos = getNodePosition(node);
        if (pos == -1) {
            weightedQueue.add(node);
        } else {
            if (weightedQueue.get(pos).getWeight() < node.getWeight()) {
                weightedQueue.remove(pos);
                weightedQueue.add(node);
            }
        }
    }

    public int getNodePosition(Node<String> node) {
        for (int i = 0; i < weightedQueue.size(); i ++) {
            if (weightedQueue.get(i).getIndex().equals(node.getIndex())) {
                return i;
            }
        }
        return -1;
    }

    public Node<String> extract() {
        return weightedQueue.remove(getMaxWeightPosition());
    }

    public boolean isEmpty() {
        return weightedQueue.isEmpty();
    }

    public void printQueue() {
        for (int i = 0; i < weightedQueue.size(); i++) {
            System.out.print(weightedQueue.get(i).getIndex() + " " + weightedQueue.get(i).getWeight() + "\t");
        }
        System.out.println();
    }

    private int getMaxWeightPosition() {
        int maxWeightPosition = 0;
        for (int i = 0; i < weightedQueue.size(); i++) {
            if (weightedQueue.get(maxWeightPosition).getWeight() < weightedQueue.get(i).getWeight()) {
                maxWeightPosition = i;
            }
            if (weightedQueue.get(maxWeightPosition).getWeight() == 1)
                return maxWeightPosition;
        }
        return maxWeightPosition;
    }

    public int size(){
        return weightedQueue.size();
    }
}
