package Data_Structures_and_Algorithms.Java;

public class Queue {

    public static int rear, front, capacity;
    public static int[] queue;

    Queue (int size){
        rear = front = 0;
        capacity = size;
        queue = new int[capacity];
    }


    void queueEnqueue(int item) {
        // check if stack is empty
        if(capacity == rear) {
            System.out.println("queue is full");
            return ;
        }
        else {
            // insert elemnt at the rear
            queue[rear] = item;
            rear++;
        }
        return;
    }

    void queueDequeue() {
        // check if stack is empty 
        if(front == rear) {
            System.out.println("Queue is empty");
            return;
        }
        else {
            for(int i = 0; i<rear-1; i++) {
                queue[i] = queue[i+1];
            }
            if(rear < capacity) {
                queue[rear] = 0;
            }
            rear--;
            return;
        }
    }

    void displayQueue() {
    
        // check if queue exist
        if(front == rear) {
            System.out.println("Queue is empty");
            return;
        }
        for(int i = front; i<rear; i++) {
            System.out.println(queue[i]);
        }
        return;
    }


    void peekQueue() {
        if(front == rear) {
            System.out.println("Queue is empty");
            return;
        }
        System.out.printf("Peek element: %d", queue[front]);
        System.out.println();
        return;
    }

}5

class QueueArrayImplemenation {
    public static void main(String[] args) {
        Queue q = new Queue(5);
        System.out.println("Initial queue");
        q.displayQueue();
        
        q.queueEnqueue(1);
        q.queueEnqueue(2);
        q.queueEnqueue(6);
        q.queueEnqueue(7);
        q.queueEnqueue(5);

        System.out.println("After enqueue");

        q.displayQueue();

        q.queueDequeue();
        System.out.println("After dequeue");

        q.displayQueue();

        q.peekQueue();

    }
}
