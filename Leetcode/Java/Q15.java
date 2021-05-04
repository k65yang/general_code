package Problems;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Q15 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int numsLength = nums.length;
        if (numsLength < 3) {
            return result;
        }

        for (int i = 0; i <= numsLength - 3; i++) {
            for (int j = numsLength - 1; j > i + 1; j--) {
                System.out.println(i + " " + j);
                int required = 0 - nums[i] - nums[j];
                int[] sub = Arrays.copyOfRange(nums, i + 1, j);
                boolean match = Arrays.stream(sub).anyMatch(x -> x == required);
                if (match) {
                    List<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[i]);
                    triplet.add(required);
                    triplet.add(nums[j]);
                    Collections.sort(triplet);
                    if (!result.contains(triplet)) {
                        result.add(triplet);
                    }
                }
            }
        }
        return result;
    }
}
