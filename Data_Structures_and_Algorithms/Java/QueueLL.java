
public class QueueLL {
    private Node front, rear;
    private int queueSize;

    private class Node {
        int data;
        Node next;
    }

    public void LinkedListQueue() {
        front = rear = null;
        queueSize = 0;  
    }

    // check if queue is empty
    public boolean isEmpty() {
        return (queueSize == 0);
    }
    
    // remove item from the front of the queue
    public int deQueue() {
        int data = front.data;
        front = front.next;
        if(isEmpty()) {
            rear = null;
        }
        queueSize--;
        return data;
    }

    public void enqueue(int data) {
        Node oldeRear = rear; 
        rear = new Node();
        rear.data = data;
        rear.next = null;
        if(isEmpty()) {
            front = rear;
        }

        else {
            oldeRear.next = rear; 
        }
        queueSize++;
    }

    public void printFrontRear()  {
        System.out.println("front of the queue: " + front.data + " Rear of the queue: " + rear.data);
    }
}

class QueueLLImplementation  {
    public static void main(String[] args) {
        QueueLL queue = new QueueLL();
        queue.enqueue(12);
        queue.enqueue(13);
        queue.enqueue(14);

        queue.printFrontRear();

    }
}
