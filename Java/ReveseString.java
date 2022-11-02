class ReverseString {
    public static void main(String[] args) {
        String word = "Halloween";
        String reverseWord = "";
        for (int i = word.length()-1; i>=0; i--) {
            reverseWord = reverseWord + word.charAt(i);
        }
        System.out.println(reverseWord);
    }
}