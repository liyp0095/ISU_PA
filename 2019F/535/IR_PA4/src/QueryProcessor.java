import java.util.ArrayList;

public class QueryProcessor {

    public static ArrayList<String> topKDocs(String queue, int k) {
        PositionalIndex positionalIndex = new PositionalIndex("data");
        return positionalIndex.getTopK(queue, k);
    }
}
