public class Factorial {
    public static void main(String[] args) {
        int num = 10;
        System.out.println(factorial(num));
    }

    public static int factorial(int n) {
        if ( n == 0) {
            return 1;
        }
        else {
            return (n*(factorial(n-1)));
        }
    }
}
