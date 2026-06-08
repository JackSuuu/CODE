import java.util.Arrays;

public class practiceTest_1 {
    public static void printBiggest(double num1, double num2, double num3) {
        if (num1 == num2 && num1 == num3 && num2 == num3) {
            System.out.println("Numbers are the same");
        }   else {
            double max = Double.NEGATIVE_INFINITY;
            double[] num_arr = {num1, num2, num3};
            for (double each : num_arr) {
                if (each > max) {
                    max = each;
                }
            }
            System.out.printf("The biggest number is %.1f%n", max);
        }
    }

    public static void bubbleSort(int[] arr) {
        // Before sorting
        System.out.println(Arrays.toString(arr));
        int len = arr.length;
        boolean swaped;

        for (int i=0; i <= len - 1; i++) {
            swaped = false;
            for (int j=1; j < len - i; j++) {
                if (arr[j - 1] > arr[j]) {
                    int temp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = temp;
                    swaped = true;
                }
            }
            // Test if sorted
            if (! swaped) {
                break;
            }
            // One iteration of sort
            System.out.println(Arrays.toString(arr));
        }
    }

    public static void main(String[] args) {
        printBiggest(Double.MAX_VALUE, Double.MIN_VALUE, -1);
        bubbleSort(new int[]{3, 2, 1});
    }
}
