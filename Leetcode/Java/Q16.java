package Problems;

public class Q16 {
    public int threeSumClosest(int[] nums, int target) {
        int result = 10^4 + 1;
        int diff = 0;
        int numsLength = nums.length;
        for (int i = 0; i < (numsLength - 2); i++) {
            for (int j = i + 1; j < (numsLength - 1); j++) {
                for (int k = j + 1; k < numsLength; k++) {
                    System.out.println(i + " " + j + " " + k);
                    int sum = nums[i] + nums[j] + nums[k];
                    if (sum == target) {
                        System.out.println(i);
                        System.out.println(j);
                        System.out.println(k);
                        System.out.println(nums[i]);
                        System.out.println(nums[j]);
                        System.out.println(nums[k]);
                        System.out.println("equals");
                        return target;
                    } else {
                        int diffSum = Math.abs(target - sum);
                        if (result == (10 ^ 4 + 1)) {
                            result = sum;
                            diff = diffSum;
                        } else if (diffSum < diff) {
                            result = sum;
                            diff = diffSum;
                        }
                    }
                }
            }
        }
        return result;
    }
}
