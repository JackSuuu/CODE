import java.util.Arrays;

public class binary_search {
    public static int rank(int key, int[] arr) {
        int low = 0;
        int high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (key < arr[mid]) {
                high = mid - 1;
            } 
            else if (key > arr[mid]) {
                low = mid + 1;
            }
            else {
                return mid;
            }
        }
        return -1;
    }
}

public static void main(String[] args) {
    System.out.println("Hello World");
}