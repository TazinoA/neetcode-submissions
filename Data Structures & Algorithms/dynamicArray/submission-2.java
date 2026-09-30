public class DynamicArray {
    int[] array;
    int capacity;
    int size;
    
    public DynamicArray(int capacity) {
       if(capacity <=0){
        throw new IllegalArgumentException("capacity must be greater than 0");
       }
       this.capacity = capacity;
       array = new int[capacity];
       size = 0;
    }

    
    public int get(int i) {
        return array[i];
    }

    
    public void set(int i, int n) {
        array[i] = n;
        
    }

    public void pushback(int n) {
        if(size == capacity){
            resize();
        }
        array[size] = n;
        size++;
    }

    
    public int popback() {
        int element = array[size-1];
        size--;
        return element;
    }

    
    private void resize() {
        capacity*=2;
        int[] newArr = new int[capacity];
        System.arraycopy(array, 0, newArr, 0, capacity/2);
        array = newArr;
    }

    
    public int getSize() {
        return size;
    }

    
    public int getCapacity() {
      return capacity;
    }
}
