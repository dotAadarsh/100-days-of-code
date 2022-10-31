public class Palindrome {
    public static void main(String[] args) {
        int num = 12121;
        isPalindrome(num);
    }
    public static void isPalindrome(int num) {
        int temp = num;
        int sum = 0;
        while(num > 0) {
            int r = num%10;
            sum = (sum*10) + r;
            num /= 10;
        }
        if(sum == temp) {
            System.out.println("Palindrome");
        }
        else {
            System.out.println("Not a palindrome");
        }
    }
}
