public class Scratch // 1
{ // 2
    public static void main(String[] args) // 3
    { // 4
        System.out.println("Manipulating Strings:"); // 5
        final String   INPUT_ORIGINAL = " Some  inTerestING String  "; // 6
        final String[] HEADINGS       = new String[]{"Original String",       // 7: 1st array
                "Manipulated String"};   // 8: 2nd array
        System.out.println("    1st an example statement split over 2 lines:"); // 9
        System.out.printf("%18s: >%s<%n%n",               // 10: 1st 2-line printf
                HEADINGS[0], INPUT_ORIGINAL);   // 11: 2nd 2-line printf
        System.out.println("    2nd an example of one statement over 6 lines with one parameter or chained method per line"); // 12
        System.out.printf("%18s: >%s<%n",         // 13: 1st printf String
                HEADINGS[1],            // 14: 2nd printf String
                INPUT_ORIGINAL.trim()   // 15: 3rd printf String
                        .replaceAll("s", "zzz")    // 16: 4th printf String
                        .toLowerCase()             // 17: 5th printf String
                        .replaceAll("s", "sh"));   // 18: 6th printf String
    } // 19
} // 20
