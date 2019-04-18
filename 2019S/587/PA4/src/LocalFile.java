public class LocalFile {
    String fileName;
    String fileContent;

    LocalFile(String name, String content, int num) {
        this.fileName = name + "_" + String.format("%04d", num);
        this.fileContent = content + String.format("%04d", num);
    }

    LocalFile(String name, String content) {
        this.fileName = name;
        this.fileContent = content;
    }
}
