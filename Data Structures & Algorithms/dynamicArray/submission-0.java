public class DynamicArray {
    int capacity;
    int[] array;
    int size;

    
    public DynamicArray(int capacity) {
        if (capacity <= 0) {
            throw new IllegalArgumentException("Capacity must be greater than 0");
        }
        this.capacity = capacity;
        this.array = new int[capacity];
        this.size = 0;
    }

    
    public int get(int i) {
        return this.array[i];  
    }

    
    public void set(int i, int n) {
        this.array[i] = n;
        
    }

    public void pushback(int n) {
        if (size == capacity) {
            resize(); 
        }
        array[size] = n;
        size++;
    }

    
    public int popback() {
        if (size == 0) {
            throw new IllegalStateException("Array is empty");
        }
        int lastElement = array[size - 1];
        size--;
        return lastElement;
    }

    
    private void resize() {
        capacity *= 2;
        int[] newArray = new int[capacity];
        System.arraycopy(array, 0, newArray, 0, size);
        array = newArray; 
    }

    
    public int getSize() {
        return this.size;
    }

    
    public int getCapacity() {
        return this.capacity;
    }
}
