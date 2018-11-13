public class Problem2{
	public static void main(String [] args){

		System.out.println("Test Case 1: --------------------------------");
		TwoStackQueue<Integer> q1 = new TwoStackQueue<>();
		q1.enqueue(1);
		q1.enqueue(2);
		q1.enqueue(3);
		System.out.println("dequeue :  " + q1.dequeue());
		System.out.println("Size:  " + q1.size());
		q1.enqueue(4);
		q1.enqueue(5);
		System.out.println("dequeue :  " + q1.dequeue());
		q1.enqueue(6);

		while(!q1.isEmpty()){
			System.out.println("dequeue :  " +q1.dequeue());
		}

		System.out.println("Test Case 2: --------------------------------");
		TwoStackQueue<String> q2 = new TwoStackQueue<>();
		q2.enqueue("Ippon");
		System.out.println("dequeue :  " + q2.dequeue());
		q2.enqueue("Kokushi");
		q2.enqueue("Budo");
		q2.enqueue("Seoi");
		System.out.println("Size:  " + q2.size());
		q2.enqueue("Yoko");
		System.out.println("dequeue :  " + q2.dequeue());
		q2.enqueue("Takaha");
		q2.enqueue("Hataka Jime");

		while(!q2.isEmpty()){
			System.out.println("dequeue :  " +q2.dequeue());
		}

		System.out.println("Test Case 3: --------------------------------");

		TwoStackQueue<Character> q3 = new TwoStackQueue<>();
		q3.enqueue('A');
		System.out.println("dequeue :  " + q3.dequeue());
		q3.enqueue('B');
		q3.enqueue('C');
		q3.enqueue('D');
		System.out.println("Size:  " + q3.size());
		q3.enqueue('E');
		System.out.println("dequeue :  " + q3.dequeue());
		q3.enqueue('F');
		q3.enqueue('G');

		while(!q3.isEmpty()){
			System.out.println("dequeue :  " +q3.dequeue());
		}






	}
}