import java.io.*;
import java.lang.*;

public class SymbolBalanced{
	private String javaFile;

	public boolean SymbolBalanced(String filename){
		fileReader(filename);
		if (!checkSymbol()){
			return false;
		}
		System.out.println("Symbols are balanced! ");
		return true;
	}

	public void fileReader(String filename){
		try {

			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			String fileName = br.readLine();
			BufferedReader file = new BufferedReader( new FileReader(fileName));
			String line = file.readLine();
			String input = "";
			while (line != null){
				input = input + line;
				line = file.readLine();
			}
			this.javaFile = input;
			file.close();
		} catch(Exception e){
			e.printStackTrace();
		}
	}

	public void getFile(){
		System.out.println(javaFile);
	}

	public int getSize(){
		return javaFile.length();
	}

	public boolean checkSymbol(){                                         
		MyStack<Character> myStack = new MyStack<Character>();                // Main check: check {([])}
		MyStack<Character> myStackLiteral = new MyStack<Character>();
		int length = getSize();

		for (int i = 1; i <= length; i++){

			char checker;
			char checker2;
			char temp;

			if (i == length){
				checker = javaFile.charAt(i - 1);
				checker2 = javaFile.charAt(i - 1);
			} else {
				checker = javaFile.charAt(i - 1);
				checker2 = javaFile.charAt(i);
			}

			if (checker == '"' || (checker == '/' && checker2 == '*') || (checker == '*' && checker2 == '/')){
				if (myStackLiteral.size() == 0){
					if (checker == '"'){
						myStackLiteral.push('"');
					} else if (checker == '/' && checker2 == '*'){
						myStackLiteral.push('/');
					}			
				} else if (myStackLiteral.size() == 1){
					if (checker == '"' && myStackLiteral.get(0) == '"'){
						myStackLiteral.pop();
					} else if (checker == '*' && checker2 == '/' && myStackLiteral.get(0) == '/'){
						myStackLiteral.pop();
					}
				}
			} 

			else if ((checker == '{' || checker == '(' || checker == '[') &&  myStackLiteral.size() == 0){
				myStack.push(checker);
			} 

			else if ((checker == '}' || checker == ')' || checker == ']') &&  myStackLiteral.size() == 0){
				if (myStack.size() == 0) {
					System.out.println("Unbalanced Symbol! " + checker + " is mismatched. -");
					return false;
				}

				
				temp = myStack.pop();

				if (checker == '}'){
					if (temp != '{'){
						if (myStack.checkExist('{')){
							System.out.println("Unbalanced! Symbol " + temp + " is mismatched.");
							return false;
						}	

						System.out.println("Unbalanced! Symbol } is mismatched.");
						return false;						
					}
				} else if (checker == ')'){
					if (temp != '('){
						if (myStack.checkExist('(')){
							System.out.println("Unbalanced! Symbol " + temp + " is mismatched.");
							return false;
						}
						System.out.println("Unbalanced! Symbol ) is mismatched.");
						return false;
					}					
				} else if (checker == ']'){
					if (temp != '['){
						System.out.println("Unbalanced! Symbol ] is mismatched.");
						return false;
					}
				}
			}
		}
	

		if (myStack.size() != 0 || myStackLiteral.size() != 0){
			if (myStackLiteral.size() != 0){
				System.out.println("Unbalanced! Symbol "+ myStackLiteral.get(0) + " is mismatched. ++");
			}else {
				System.out.println("Unbalanced! Symbol "+ myStack.get(0) + " is mismatched. ++");
			}	
			return false;
		}
		return true;
	}
}

