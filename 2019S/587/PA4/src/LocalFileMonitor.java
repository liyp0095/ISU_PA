import java.util.ArrayList;
import java.util.Random;

public class LocalFileMonitor {
    ArrayList<LocalFile> localFileList = new ArrayList<>();
    Random rand = new Random();

    LocalFileMonitor() {
        System.out.println("Generate local file randomly ... ");
        GenerateFiles(rand.nextInt(20));
    }

    private void GenerateFiles(int fileNumber) {
        for (int i = 0; i < fileNumber; i++ ) {
            localFileList.add(new LocalFile("file", "content", rand.nextInt(10000)));
        }
    }

    public void add(LocalFile localFile) {
        for (LocalFile lf : localFileList) {
            if (localFile.fileName == lf.fileName) {
                lf.fileContent = localFile.fileContent;
                return;
            }
        }
        localFileList.add(localFile);
    }

    public void delete(LocalFile localFile) {
//        int index = 0;
//        for (LocalFile lf : localFileList) {
//            if (localFile.fileName == lf.fileName) {
//                index = localFileList.indexOf(lf);
//            }
//        }
//        localFileList.remove(index);
        this.localFileList.remove(localFile);
    }

    public void show() {
        for (LocalFile localFile : localFileList) {
            System.out.println(localFile.fileName + "\t" + localFile.fileContent);
        }
    }
}
