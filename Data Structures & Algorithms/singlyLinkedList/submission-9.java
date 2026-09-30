class LinkedList {
    class Node{
        int val;
        Node next;
    }
    Node head;
    int size;

    public LinkedList() {
        head = null;
        size = 0;
    }

    public int get(int index) {
        if(index < 0 || index >= size){
            return -1;
        }
        int i = 0;
        Node curr = head;
        while(curr != null && i!=index){
            curr = curr.next;
            i++;
        }
        if(curr == null){
            return -1;
        }
        return curr.val;
    }

    public void insertHead(int val) {
        Node newNode = new Node();
        newNode.val = val;
        newNode.next = head;
        head = newNode;
        size++;
    }

    public void insertTail(int val) {
        Node curr = head;
        Node newNode = new Node();
        newNode.val = val;
        newNode.next = null;

        if(head == null){
            head = newNode;
        }

        else{
            while(curr.next!=null){
            curr = curr.next;
        }
        curr.next = newNode;
        }
        size++;
    }

    public boolean remove(int index) {
        if(index < 0 || index >= size){
            return false;
        }

        if(index == 0){
            head = head.next;
            return true;
        }
        
        int i = 0;
        Node curr = head;
        while(i+1!=index){
            curr = curr.next;
            i++;
        }
        
            curr.next = curr.next.next;
        
        size--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> array = new ArrayList<>();
        if(head == null){
            return array;
        }
        Node curr = head;
        int i = 0;
        while(curr.next != null){
            array.add(curr.val);
            curr = curr.next;
            i++;
        }
        array.add(curr.val);
        return array;
    }
}
