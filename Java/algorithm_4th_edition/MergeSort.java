public class MergeSort {
    public static int[] merge(int[] arr, int lo, int mid, int hi){
        int i = lo, j = mid + 1;
        int[] aux = new int[arr.length];

        // Copy arr[lo..hi] to aux[lo..hi]
        for (int k = lo; k <= hi; k++){
            aux[k] = arr[k];
        }

        // Merge back to arr[lo..hi]
        for (int k = lo; k <= hi; k++){
            // The part where i/j over
            if (i > mid){
                arr[k] = aux[j];
                j ++;
            } else if (j > hi){
                arr[k] = aux[i];
                i ++;
            // The main part that merge
            } else if (aux[j] < aux[i]){
                arr[k] = aux[j];
                j ++;
            } else {
                arr[k] = aux[i];
                i ++;
            }
        }

        return arr;
    }

    public static void main(String[] args) {
        int[] test = {5, 4, 2, 1, 3};
        int lo = 0;
        int hi = test.length - 1;
        int mid = (lo + hi) / 2;
        test = MergeSort.merge(test, lo, mid, hi);
        
        // Print out array
        for (int t : test) {
            System.out.print(t + " ");
        }
    }
}
