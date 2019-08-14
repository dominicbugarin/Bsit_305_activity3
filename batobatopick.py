Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import java.util.*;
public class Calculator {

public static void main (String []args){

double result;
Scanner scan = new Scanner(System.in);

System.out.println("Enter the first number:");
int num1 = scan.nextInt();

System.out.println("Enter the Second number:");
int num2 = scan.nextInt(); 

System.out.println("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Divide \n");
int operation = scan.nextInt();

switch (operation){
case 1:
result = num1 + num2;
System.out.println("result is:" + result);
break;

case 2:
result = num1 - num2;
System.out.println("result is:" + result);
break;

case 3:
result = num1 * num2;
System.out.println("result is:" + result);
break;

case 4:
result = num1 / num2;
System.out.println("result is:" + result); 
break;


default:
System.out.println("This is a wrong choice");
break; 


} 


}
}
