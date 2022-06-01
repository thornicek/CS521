package CS526_Hw;

import java.util.Arrays;

public class Hw1_p1 {

    public static void find(int[] a, int x) {
        // implement this method
        boolean exists = false;
        for(int i=0; i < a.length; i++){
            if(a[i] == x) {
                System.out.println("x is stored at the index: " + i);
                exists = true;
            }
        }
        if(!exists){
            System.out.println("x does not exist");
        }
    }

    public static boolean isPrefix(String s1, String s2) {
        // implement this method
        for(int i=0; i < s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i)){
               return false;
            }
        }
        return true;
    }


    public static void main(String[] args) {

        int[] a = {5, 3, 5, 6, 1, 2, 12, 5, 6, 1};

        find(a, 5);
        find(a, 10);
        System.out.println();

        String s1 = "abc";
        String s2 = "abcde";
        String s3 = "abdef";

        if (isPrefix(s1,s2)) {
            System.out.println(s1 + " is a prefix of " + s2);
        }
        else {
            System.out.println(s1 + " is not a prefix of " + s2);
        }

        if (isPrefix(s1,s3)) {
            System.out.println(s1 + " is a prefix of " + s3);
        }
        else {
            System.out.println(s1 + " is not a prefix of " + s3);
        }
    }
}

