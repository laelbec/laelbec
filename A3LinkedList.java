// Name: Lael Bec
// Student number: v01037921

public class A3LinkedList implements A3List {
	private A3Node head;
	private A3Node tail;
	private int length;
	
	public A3LinkedList() {
		head = null;
		tail = null;
		length = 0;
	}
	
	public void addFront(String s) {
		// TODO: implement this
		A3Node n = new A3Node(s);
		if(head!=null){
			n.next = head;
			head.prev = n;
		}
		else{
			tail = n;
		}
		head = n;
		length++;
	}

	public void addBack(String s) {
		// TODO: implement this
		A3Node n = new A3Node(s);
		if(head==null){
			head = n;
		}
		else{
			tail.next = n;
			n.prev = tail;
		}
		tail = n;
		length++;
	}
	
	public int size() {
		return length;
	}
	
	public boolean isEmpty() {
		return length==0;
	}
	
	public void removeFront() {
		// TODO: implement this
		if(length>1) {
			head = head.next;
			head.prev.next = null;
			head.prev = null;
			length--;
		}
		else{
			head = null;
			tail = null;
			length = 0;
		}
		
	}
	
	public void removeBack() {
		// TODO: implement this
		if(length>1) {
			tail = tail.prev;
			tail.next.prev = null;
			tail.next = null;
			length--;
		}
		else{
			head = null;
			tail = null;
			length = 0;
		}
	}
	
	
	
	//////////////////
	/* PART 2 BELOW */
	//////////////////
	/*
	 * Purpose: removes the middle element(s) from this list
	 * Parameters: none
	 * Returns: void - nothing
	 * Note: - if there are an odd number of elements, 
	 *         then the middle element is removed
	 *       - if there are an even number of elements, 
	 *         then the middle TWO elements are removed
	 */
	public void removeMiddle() {
		// TODO: implement this
		if(length>2) {
			if(length%2 == 0){
				int pos = length / 2;
				A3Node cur = head;
				for(int i = 0; i<pos; i++){
					cur = cur.next;
				}
				cur.prev.next = cur.next;
				cur.next.prev = cur.prev;
				
				length--;

				pos = length / 2;
				cur = head;
				for(int i = 0; i<pos; i++){
					cur = cur.next;
				}
				cur.prev.next = cur.next;
				cur.next.prev = cur.prev;
				
				length--;

			}
			else{
				int pos = length/2;
				A3Node cur = head;
				for(int i = 0; i<pos; i++) {
					cur = cur.next;
				}
				cur.prev.next = cur.next;
				cur.next.prev = cur.prev;
				length--;
			}
		}
		else{
			head = null;
			tail = null;
			length = 0;
		}
	}
	
	/* 
	 * Purpose: interleaves the list with another list
	 * Parameters: A3LinkedList other - the list to interleave with
	 * Returns: void - nothing
	 * Example:  If listA: {a1, a2, a3, a4, a5}
	 * 		    and listB: {b1, b2, b3, b4, b5}
	 *          and the two lists were interleaves, the result would
	 *           be listA: {a1, b2, a3, b4, a5}
	 *		    and listB{ {b1, a2, b3, a4, b5}.
	 *
	 * Precondition: the two lists are the same length
	 */
	public void interleave(A3LinkedList other) {
		// TODO: implement this
		if(length != 0) {
			A3Node cur1 = head;
			A3Node cur2 = other.head;
			while(cur1.next != null && cur2.next != null){
				A3Node temp = cur1.next;
				cur1.next = cur2.next;
				cur2.next = temp;
			
				cur1 = cur1.next;
				cur2 = cur2.next;
			}
			cur1 = tail;
			cur2 = other.tail;
			while(cur1.prev!=null && cur2.prev!=null){
				A3Node temp = cur1.prev;
				cur1.prev = cur2.prev;
				cur2.prev = temp;

				cur1 = cur1.prev;
				cur2 = cur2.prev;
			}
		}

	}
	
	
	
	////////////////////////////////////////
	/* METHODS BELOW TO HELP WITH TESTING */
	////////////////////////////////////////
	
	/*
	 * Purpose: return a string representation of the list 
	 *          when traversed from front to back
	 * Parameters: none
	 * Returns: nothing
	 *
	 * USED TO HELP YOU WITH DEBUGGING
	 * DO NOT CHANGE THIS METHOD
	 */
	public String frontToBack() {
		String result = "{";
		A3Node cur = head;
		while (cur != null) {
			result += cur.getData();
			cur = cur.next;
		}
		result += "}";
		return result;
	}
	
	/*
	 * Purpose: return a string representation of the list 
	 *          when traversed from back to front
	 * Parameters: none
	 * Returns: nothing
	 *
	 * USED TO HELP YOU WITH DEBUGGING
	 * DO NOT CHANGE THIS METHOD
	 */
	public String backToFront() {
		String result = "{";
		A3Node cur = tail;
		while (cur != null) {
			result += cur.getData();
			cur = cur.prev;
		}
		result += "}";
		return result;
	}
}
	