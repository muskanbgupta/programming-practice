import java.util.Scanner;
public class Simple_Calculator {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int n1=sc.nextInt();
        System.out.print("Enter the Operator(+,-,x,/,%): ");
        String o=sc.next();
        System.out.print("Enter the second number: ");
        int n2=sc.nextInt();
        switch (o){
            case "+"->System.out.printf("Addition of the above number is %d\n",n1+n2);
                    
            case "-"->System.out.printf("Subtraction of the above number is %d\n",n1-n2);
                
            case "x"->System.out.printf("Multiplication of the above number is %d\n",n1*n2);
                     
            case "/"->{
                    if(n2==0){
                        System.out.println("Cannot division by Zero");
                    }
                    else{
                        System.out.printf("Division of the above number is %d\n",n1/n2);
                    }
                    }
                
                        
            case "%"->System.out.printf("Modulus of the above number is %d\n",n1%n2);
                
            default->System.out.println("Invalid");
        
        }           

        sc.close();
        
        
    }
    
}
