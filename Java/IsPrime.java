public class IsPrime {
    public static void main(String[] args) {
        int num = 17;
        isPrimeNum(num);
    }

    public static void isPrimeNum(int n) {
        if (n == 0 || n == 1) {
            System.out.println("Not a prime");
        }
        int m = n/2, flag = 0;
        
        for(int i = 2; i< m; i++) {
            if(n%i == 0) {
                flag = 1;
            }
        }
        if(flag != 0) {
            System.out.println("Not a prime");
        }
        else {
            System.out.println("The number is a prime");
        }
    }
}
