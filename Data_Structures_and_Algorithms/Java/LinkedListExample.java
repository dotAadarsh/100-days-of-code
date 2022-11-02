package Data_Structures_and_Algorithms.Java;

import java.util.*;
 
public class LinkedListExample {

    public static void main(String[] args) {
        LinkedList<String> ll = new LinkedList<String>();

        ll.add("A");
        ll.add("B");
        ll.add("C");
        ll.add("D");
        ll.add(2, "G");
        System.out.println(ll);

        ll.remove();
        System.out.println(ll);
        ll.remove(2);
        System.out.println(ll);

        Iterator<String> itr = ll.iterator();
        while(itr.hasNext()) {
            System.out.println(itr.next());
        }
        
    }
    


}
