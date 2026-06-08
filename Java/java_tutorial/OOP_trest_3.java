public class OOP_trest_3 {
    public static void printNext5LeapYears(int startYear) {
        int counter = 5;
        int year = startYear;

        while (counter > 0) {
            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                System.out.println(year);
                counter -= 1;
            }
            year += 4;
        }
    }

    public static int[] countFrequencies(int[] input) {
        // input values are always from 0 - 9
        int[] freq_arr = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

        for (int i=0; i < input.length; i++) {
            freq_arr[input[i]] ++;
        }

        return freq_arr;
    }

    public static void printFrequencies(int[] input) {
        for (int i = 0; i < input.length; i++) {
            String index = String.valueOf(i);
            String count = String.valueOf(input[i]);
            String asterisks = "";
            for (int j = 0; j < input[i]; j++) {
                asterisks += '*';
            }
            if (i < 10) {
                System.out.printf("0%s:  %s = <%s>%n", index, count, asterisks);
            }
            else {
                System.out.printf("%s:  %s = <%s>%n", index, count, asterisks);
            }
            
        }
    }

    public static void main(String[] args) {
        // printNext5LeapYears(1900);
        // int [] result = countFrequencies(new int[]{1, 3, 2, 1});
        // for (int element : result) {
        //     System.out.printf("%d, ", element);
        // }
        int[] result = new int[]{4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 8, 9, 10};
        printFrequencies(result);
    }
    
}