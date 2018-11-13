import java.util.*;
import java.text.*;

public class Problem1 {
	
	public static <AnyType extends Comparable<AnyType>>  AnyType findMax(AnyType[] arr) {
		  int maxIndex = 0;
		  for (int i = 1; i < arr.length; i++)
		    if ( arr[i].compareTo(arr[maxIndex]) > 0 )
		       maxIndex = i;
		    return arr[maxIndex];
		}
	
	public static void main(String [] args){
		
		Rectangle [] recTan = new Rectangle[10];                        // Random length and width generating
		Random rand = new Random();
		DecimalFormat df = new DecimalFormat("#.00");

		int lengthRange = rand.nextInt(20);
		int widthRange = rand.nextInt(10);
		for (int i = 0; i <= recTan.length - 1; i++){
			double lengthPer = lengthRange * rand.nextDouble();
			double widthPer = widthRange * rand.nextDouble();
			recTan[i] = new Rectangle(lengthPer, widthPer);
		}

		for (int i=0; i <= recTan.length - 1; i++){
			System.out.println((i+1) + "-th is " + df.format(recTan[i].getPerimeter()));
		}

		System.out.println("The max perimeter is " + df.format(findMax(recTan).getPerimeter()));

	}

}
