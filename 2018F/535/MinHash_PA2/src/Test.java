import java.io.IOException;

public class Test {
    public static void main(String[] args) throws IOException {

        MinHashAccuracy m = new MinHashAccuracy();
        //m.accuracy("data//articles//articles", 800);
        m.myaccuracy("data//space", 400, 0.4);
        m.myaccuracy("data//space", 600, 0.4);
        m.myaccuracy("data//space", 800, 0.4);
        //m.accuracy("data//test", 30);

//        MinHashTime t = new MinHashTime();
//        t.timer("data//space", 600);

/*        MinHashAccuracy m = new MinHashAccuracy();
        m.accuracy("data//space", 600);*/

        System.out.println("End!");
    }
}
