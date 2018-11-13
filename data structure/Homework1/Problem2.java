import java.util.*;

public class Problem2 {
	public static <AnyType extends Comparable<AnyType>>
	int binarySearch(AnyType[] a, AnyType x){
		return binarySearch(a, x, 0, a.length-1);
	}

	public static <AnyType extends Comparable<AnyType>>
	int binarySearch(AnyType [] a, AnyType x, int start, int end){
		int mid = (start + end) / 2;
		if (start <= end){
			if (a[mid].compareTo(x) == 0){
				return mid;
				} else if (a[mid].compareTo(x) < 0){
					return binarySearch(a, x, mid+1, end);
					}  else if (a[mid].compareTo(x) > 0){
						return binarySearch(a, x, start, mid-1);
						}
			}
		return -1;
		}

	public static void main(String [] args){

		Rectangle a[] = new Rectangle[10];
		a[0] = new Rectangle(3, 2);
		a[1] = new Rectangle(1, 2);
		a[2] = new Rectangle(7, 3);
		a[3] = new Rectangle(6, 8);
		a[4] = new Rectangle(91, 72);
		a[5] = new Rectangle(2, 14);
		a[6] = new Rectangle(3, 8);
		a[7] = new Rectangle(6, 4);
		a[8] = new Rectangle(71, 52);
		a[9] = new Rectangle(22, 8);
		
		
		Arrays.sort(a);
		System.out.println("After sort, order of the array [a] becomes");
		for (int i = 0; i <= a.length - 1; i++){
			System.out.println( i + ": (" + a[i].getLength() + ", " + a[i].getWidth() + ")");
		}
		int index = binarySearch(a, new Rectangle(3, 8));
		System.out.println("=====================================");
		System.out.println("We are tring to find \"Rectangle(3, 8)\"");
		System.out.println(" Perimeter is " + a[index].getPerimeter());
		System.out.println(" BinarySearch; index is " + index);
		
	}
}