public class RightTriangleStar {
    public static void main(String[] args) {
        int length = 6;
        for(int i = 0; i<length; i++) {
            for(int j = 0; j<=i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
