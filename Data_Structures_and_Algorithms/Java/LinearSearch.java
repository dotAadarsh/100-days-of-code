package Data_Structures_and_Algorithms.Java;

public class LinearSearch {
    public static void main(String[] args) {
        int[] nums = {10, 20, 30, 40, 50};
        int val = 40;
        System.out.println(linearSearch(nums, val));
    }

    public static int linearSearch(int[] nums, int val) {
        for(int i =0; i<nums.length; i++) {
            if(nums[i] == val) {
                return i;
            }
        }
        return -1;
    }
}
