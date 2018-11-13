README

This project is for the Data Structure, first homework;
Since all testing arrays are hardcoded, you can just compile the code, no need to input any values.

Class Rectangle:

     In this class I have 3 methods: getWidth(), getLength() and getPerimeter(), they will return to Width, Length and Perimeter;

     I also override the function with implements from Comparable, make it is working for compare different rectangle by their perimeter.

Class Problem1:
     Just use the method in the question, which returns to the largest perimeter rectangle.
     In the main function, I used a loop to construct different rectangle objects and then apply the method.
     Since the data type is double, I import java.text.* and set the code only output 2 digits after point, which makes the result much easier to read.



Class Problem2:
     BinarySearch method with a helper method. Since java can share the same signature as long as they have a different parameters, I just call them both BinarySearch;

     The first BinarySearch method will call the helper method, which will return the index of the Rectangle we are looking for based on its perimeter.

     For the helper method, just same as the original binary search method.

Class Problem3:
     For this question, I made each loop becomes a constructor. Then I can construct different object in main function and then compare their running time.

     For the 3rd method, the first output seems unreasonable. I asked TA and she said I can just ignorn the first one. It seems like a lot of students have the same problem.

     The explaination is located in Problem3.txt.
