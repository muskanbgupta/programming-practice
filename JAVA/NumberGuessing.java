import java.util.Scanner;
import java.util.Random;
public class NumberGuessing {
    public static void main(String[] args){
    
    System.out.println("----Number Guessing Game in Java----");
    Random r=new Random();
    int hidden_Num=r.nextInt(1,10);
    Scanner s=new Scanner(System.in);
    String user;
    
    do{
        System.out.print("Guess a number between(1-10): ");
        int n=s.nextInt();
        if(n>hidden_Num)System.out.println("Too big Number!");
        else if(n<hidden_Num)System.out.println("Too small Number!");
        else if(n>hidden_Num && n<hidden_Num)System.out.println("Middle Number!");
        else{
            System.out.println("You guessed!");
            break;
            
        }

        System.out.println("Do u want guess again? ");
        user=s.next().toLowerCase();


    }while(user.equals("yes"));
    

}
}
