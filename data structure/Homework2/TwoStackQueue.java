public class TwoStackQueue<AnyType> implements MyQueue<AnyType>{
	private MyStack<AnyType> myStack1 = new MyStack<AnyType>();
	private MyStack<AnyType> myStack2 = new MyStack<AnyType>();
	
	@Override
	public void enqueue(AnyType x){
		myStack1.push(x);
	}
	
	@Override
	public AnyType dequeue(){
		if (myStack1.isEmpty() && myStack2.isEmpty()){
			return null;
		} else if (myStack2.isEmpty()){
			while(!myStack1.isEmpty()){
				myStack2.push(myStack1.pop());
			}
		}
		return myStack2.pop();	
	}
	
	@Override
	public boolean isEmpty(){
		if(myStack1.isEmpty() && myStack2.isEmpty()){
			return true;
		}
		return false;	
	}
	
	@Override
	public int size(){
		return myStack1.size() + myStack2.size();
	}
}