/*  Data Structure - Assignment(3) - Programming(1)
ExpressionTree
*/

public class ExpressionTree{
	
	private String postFix;
	private String prefix;
	private String infix;
	private ExpressionNode<String> root;
	

	public static class ExpressionNode<AnyType>{
		AnyType value;

		ExpressionNode<AnyType> left;

		ExpressionNode<AnyType> right;
		
		public ExpressionNode(AnyType value){
			this(value, null, null);
		}

		public ExpressionNode(AnyType value, ExpressionNode<AnyType> left, ExpressionNode<AnyType> right){             // Constructor
			this.value = value;
			this.left  = left ;
			this.right = right;
		}
	}

	public String[] listConvert(String postExpressionInput){
		String[] parts = postExpressionInput.split(" ");                                              // divided the postfix-input into parts by space
	
		return parts;
	}

	public static boolean isNumeric(String s) {                                                     // Check Numeric in splited String
		try { 

	        Integer.parseInt(s); 

	    } catch(NumberFormatException e) { 

	        return false; 

	    } catch(NullPointerException e) {

	        return false;
	    }
	    return true;
	}

	

	public ExpressionTree(String postExpressionInput){
		
		this.postFix = postExpressionInput;
		String[] postFixExp = listConvert(postExpressionInput);                                       // Divide post-input as Strings and Integers
		
		
		MyStack<ExpressionNode<String>> treeStack = new MyStack<ExpressionNode<String>>();

		for (int i = 0; i < (postFixExp.length); i++){
			
			//System.out.println("index is :" + i + ": " + postFixExp[i]);

			if (isNumeric(postFixExp[i])){

				treeStack.push(new ExpressionNode<>(postFixExp[i]));

			} else {

				ExpressionNode<String> right =  treeStack.pop();

				ExpressionNode<String> left  =  treeStack.pop();

				treeStack.push(new ExpressionNode<String>(postFixExp[i], left, right)); 
			}
		}
	
		this.root = treeStack.pop();
	}
	
	
	
	public int calculateNode(ExpressionNode<String> note){                                                         // Calculate one full note, return an int value		
		if (note.value.equals("+")){
			return calculateNode(note.left) + calculateNode(note.right);
			}
		
		else if (note.value.equals("-")){
			return calculateNode(note.left) - calculateNode(note.right);
			}
		
		else if (note.value.equals("*")){
			return calculateNode(note.left) * calculateNode(note.right);
			}
		
		else if (note.value.equals("/")){
			return calculateNode(note.left) / calculateNode(note.right);
			}
		
		else{
			return Integer.valueOf((String) note.value);
			}
		}


	public int eval(){
		return calculateNode(root);
	}
	
	
// ProFix
	public String prefix(){
		this.prefix = "";
		preOrder(root, prefix);
		return prefix;	
	}
	
	public void preOrder(ExpressionNode<String> node, String prefix){
		if (node != null){
			this.prefix = this.prefix + " " + node.value;
			
			preOrder(node.left, prefix);
			
			preOrder(node.right, prefix);	
		}
	}
	
	public String infix(){
		this.infix = "";
		inOrder(root, infix);
		return infix;	
	}
	
	public void inOrder(ExpressionNode<String> node, String infix){
		if (node != null){
			inOrder(node.left, infix);
			
			this.infix = this.infix + " " + node.value;
			
			inOrder(node.right, infix);	
		}
	}
	
	public String postfix(){
		return postFix;
	}
}