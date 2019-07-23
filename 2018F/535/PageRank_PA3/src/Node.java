public class Node<T>{
    private T index;
    private float weight;

    // constructors
    Node(T index, float weight){
        this.index = index;
        this.weight = weight;
    }

    // methods
    public T getIndex(){
        return this.index;
    }

    public float getWeight(){
        return weight;
    }

    public void setWeight(float weight){
        this.weight = weight;
    }

}