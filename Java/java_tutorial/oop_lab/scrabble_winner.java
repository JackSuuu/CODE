package OOP_Lab;

import java.util.HashMap;

public class scrabble_winner {
    public static void main(String[] args) {
        HashMap<String, Integer> character = new HashMap<String, Integer>();

        character.put("AEIUNROSLT", 1);
        character.put("DG", 2);
        character.put("BCMP", 3);
        character.put("FHVWY", 4);
        character.put("K", 5);
        character.put("JX", 8);
        character.put("QZ", 10);

        String word = "QUEEN";
        Integer counter = 0;

        String[] key_arr = character.keySet().toArray(new String[0]);
        // System.out.println(key_arr);

        for (char w : word.toCharArray()) {
            for (String key : key_arr) {
                // System.out.println(key);
                for (char k : key.toCharArray()) {
                    if (k == w) {
                        int score = character.get(key);
                        counter += score;
                    }
                }
            }
        }

        Integer FINAL_SCORE = counter;

        System.out.println(FINAL_SCORE);

        // for (char c : word.toCharArray()) {
        //     String char_score = character.get();
        //     for ()
        //     System.out.println(c);

    }

}

