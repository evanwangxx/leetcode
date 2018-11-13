public class Problem1{
	
	public static void main(String [] args){
		
		String y = "6 2 / 1 2 * - 1 2 + *";
		ExpressionTree tree = new ExpressionTree(y);

		int x = tree.eval();
		System.out.println("eval value is : " + x);

		System.out.println("postFix: " + tree.postfix());

		System.out.println("preFix: " + tree.prefix());

		System.out.println("inFix: " + tree.infix());	
	}
}