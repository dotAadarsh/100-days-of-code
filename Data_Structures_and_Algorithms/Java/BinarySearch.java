package Data_Structures_and_Algorithms.Java;

public class BinarySearch {
    public static void main(String[] args) {
        
        int[] nums = {10, 20, 30, 50, 60, 70};
        int target = 10;

        System.out.println(binarySearch(nums, target));
    }
    public static int binarySearch(int[] nums, int target) {
        int low = 0, high = nums.length;
        do {
            int mid = (low + ((high - low)/2));
            int v = nums[mid];
            if(v == target) {
                return mid;
            }
            else if(v > target) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }while(low < high);
        return -1;
    }
}