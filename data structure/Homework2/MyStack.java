/// Java Programming - 1


import java.util.LinkedList;

public class MyStack<T>{

	private LinkedList<T> myStack;

	public MyStack(){
		this.myStack = new LinkedList<>();
	}
	

	public void push(T item){
		myStack.add(0, item);
	}
	
	public T pop(){
		T temp = myStack.get(0);
		myStack.remove(0);
		return temp;
	}

	public T get(int index){
		return myStack.get(index);
	}

	public void printMyStack(){
		for (int i = 0; i < myStack.size(); i++){
			System.out.println("for index " + i + " is " + myStack.get(i));
			System.out.println(" -- - - - - - - -- - - - - - - -");
		}

	}

	public int size(){
		return myStack.size();
	}

	public boolean checkExist(T item){
		for(int i = 0; i < myStack.size(); i++){
			if(myStack.get(i) == item){
				return true;
			}
		}
		return false;
	}

	public boolean isEmpty(){
		if (myStack.size() == 0){
			return true;
		}
		else{
			return false;
		}
	}
}