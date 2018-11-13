import java.util.Arrays;

public class Rectangle implements Comparable <Rectangle> {

	private double Width;
	private double Length;
	private double Perimeter;

	public Rectangle(double LengthInput, double WidthInput){
		this.Width = WidthInput;
		this.Length = LengthInput;
		this.Perimeter = (Width + Length) * 2;
	}
	
	public double getWidth(){
		return Width;
	}
	
	public double getLength(){
		return Length;
	}
	
	public double getPerimeter(){
		return Perimeter;
	}
	
	@Override
	public int compareTo(Rectangle other) {
		return Double.compare(this.Perimeter, other.Perimeter);
	}
	
}
	


