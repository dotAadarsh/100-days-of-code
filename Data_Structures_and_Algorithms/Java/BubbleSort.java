package Data_Structures_and_Algorithms.Java;

class BubbleSort {
    public static void main(String[] args) {
        int[] nums = {1,5,6,4,8,2};
        for(int i : nums) {
            System.out.print(i);
        }
        System.out.println();
        bubbleSort(nums);
        
        for(int i : nums) {
            System.out.print(i);
        }
        System.out.println();
    }
    public static void bubbleSort(int[] nums) {
        for(int i = 0; i< nums.length; i++) {
            for(int j = 0;j < nums.length-1-i; j++) {
                if(nums[j] > nums[j+1]) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp; 
                }
            }
        }
    }
}