package Problems;

import java.util.*;

public class Q17 {


    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.length() == 0) {
            return result;
        }

        Map<String, List<String>> letters = new HashMap<String, List<String>>() {
            {
                put("2", new ArrayList<>(Arrays.asList("a", "b", "c")));
                put("3", new ArrayList<>(Arrays.asList("d", "e", "f")));
                put("4", new ArrayList<>(Arrays.asList("g", "h", "i")));
                put("5", new ArrayList<>(Arrays.asList("j", "k", "l")));
                put("6", new ArrayList<>(Arrays.asList("m", "n", "o")));
                put("7", new ArrayList<>(Arrays.asList("p", "q", "r", "s")));
                put("8", new ArrayList<>(Arrays.asList("t", "u", "v")));
                put("9", new ArrayList<>(Arrays.asList("w", "x", "y", "z")));
            }
        };
        List<String> digitsSplit = Arrays.asList(digits.split(""));
        return result;
    }
}
