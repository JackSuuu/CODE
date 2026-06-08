public class PriorityQueue {
    private int[] heap;
    private int size;
    private int capacity;

    // Constructor
    public PriorityQueue(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.heap = new int[capacity + 1]; // heap[0] is not used
    }

    // Check if the priority queue is empty
    public boolean isEmpty() {
        return size == 0;
    }

    // Insert an element into the priority queue
    public void insert(int value) {
        if (size >= capacity) {
            throw new RuntimeException("Priority Queue is full");
        }

        // Insert the new element at the end of the heap
        heap[++size] = value;

        // Heapify up to maintain heap property
        heapifyUp(size);
    }

    // Remove and return the element with the highest priority (smallest value)
    public int remove() {
        if (isEmpty()) {
            throw new RuntimeException("Priority Queue is empty");
        }

        // The root of the heap (heap[1]) is the smallest element
        int min = heap[1];

        // Move the last element to the root and heapify down
        heap[1] = heap[size];
        size--;

        heapifyDown(1);

        return min;
    }

    // Heapify up to maintain the heap property after insertion
    private void heapifyUp(int index) {
        while (index > 1 && heap[index] < heap[parent(index)]) {
            swap(index, parent(index));
            index = parent(index);
        }
    }

    // Heapify down to maintain the heap property after removal
    private void heapifyDown(int index) {
        while (leftChild(index) <= size) {
            int smallerChild = leftChild(index);

            if (rightChild(index) <= size && heap[rightChild(index)] < heap[smallerChild]) {
                smallerChild = rightChild(index);
            }

            if (heap[index] <= heap[smallerChild]) {
                break;
            }

            swap(index, smallerChild);
            index = smallerChild;
        }
    }

    // Utility methods
    private int parent(int index) {
        return index / 2;
    }

    private int leftChild(int index) {
        return 2 * index;
    }

    private int rightChild(int index) {
        return 2 * index + 1;
    }

    private void swap(int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    // Return the current size of the priority queue
    public int size() {
        return size;
    }

    // Return the element with the highest priority without removing it
    public int peek() {
        if (isEmpty()) {
            throw new RuntimeException("Priority Queue is empty");
        }
        return heap[1];
    }

    public static void main(String[] args) {
        PriorityQueue pq = new PriorityQueue(10);
        pq.insert(5);
        pq.insert(3);
        pq.insert(8);
        pq.insert(1);

        System.out.println("Top priority element: " + pq.peek()); // Should print 1

        while (!pq.isEmpty()) {
            System.out.println("Removed: " + pq.remove());
        }
    }
}
