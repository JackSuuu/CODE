public class pqMax {
    private int[] heap;
    private int size;
    private int capacity;

    // Constructor
    public pqMax(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.heap = new int[capacity + 1]; // index 0 will be unused
    }

    // Insert an element into the max priority queue
    public void insert(int value) {
        if (size == capacity) {
            throw new IllegalStateException("Priority queue is full");
        }
        size++;
        heap[size] = value;
        heapifyUp(size);
    }

    // Get the maximum element from the max priority queue
    public int getMax() {
        if (size == 0) {
            throw new IllegalStateException("Priority queue is empty");
        }
        return heap[1];
    }

    // Remove and return the maximum element from the max priority queue
    public int removeMax() {
        if (size == 0) {
            throw new IllegalStateException("Priority queue is empty");
        }
        int max = heap[1];
        heap[1] = heap[size];
        size--;
        heapifyDown(1);
        return max;
    }

    // Heapify up for maintaining the max heap property
    private void heapifyUp(int index) {
        while (index > 1 && heap[index] > heap[index / 2]) {
            swap(index, index / 2);
            index = index / 2;
        }
    }

    // Heapify down for maintaining the max heap property
    private void heapifyDown(int index) {
        while (index <= size / 2) { // Node with no children won't be processed
            int leftChild = 2 * index;
            int rightChild = 2 * index + 1;
            int largerChild = leftChild;

            if (rightChild <= size && heap[rightChild] > heap[leftChild]) {
                largerChild = rightChild;
            }

            if (heap[index] >= heap[largerChild]) {
                break;
            }

            swap(index, largerChild);
            index = largerChild;
        }
    }

    // Swap two elements in the heap
    private void swap(int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    // Check if the priority queue is empty
    public boolean isEmpty() {
        return size == 0;
    }

    // Get the size of the priority queue
    public int size() {
        return size;
    }

    public static void main(String[] args) {
        pqMax pq = new pqMax(10); // Capacity is 10

        pq.insert(10);
        pq.insert(30);
        pq.insert(20);
        pq.insert(5);

        System.out.println("Max Element: " + pq.getMax()); // Should print 30
        System.out.println("Removed Max: " + pq.removeMax()); // Should print 30
        System.out.println("Max Element: " + pq.getMax()); // Should print 20
        System.out.println("Size of queue: " + pq.size()); // Should print 3
        System.out.println("Is queue empty? " + pq.isEmpty()); // Should print false
    }
}
