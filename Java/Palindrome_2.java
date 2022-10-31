import java.util.Scanner;

public class Palindrome_2 {
    public static void main(String[] args) {
        String original, reversed = "";
        try (Scanner sc = new Scanner(System.in)) {
            original = sc.nextLine();
        }
        for (int i = original.length()-1; i>=0; i--) {
            reversed = reversed + original.charAt(i);
        }
        if(original.equals(reversed)) {
            System.out.println("Palindrome");
        }
        else {
            System.out.println("Not a palindrome");
        }
    }
}
 