public class Selection {
    // Basically, 1.find min element 2.exchange with i
    public static int[] sort(int[] arr){
        int N = arr.length; // array length
        for (int i=0; i < N; i++){
            int min = i; // index with minimal entry
            for (int j=i+1; j < N; j++){
                if (arr[j] < min) {
                    min = arr[j];
                }
            }
            // exchange element
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] test = {5, 3, 2, 1, 4};
        System.out.println(sort(test).toString());
    }     
}
