import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class file {
    public static void main(String[] args) {
        String filePath = "test.txt";

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException error) {
            error.printStackTrace();
        }
    }
}
