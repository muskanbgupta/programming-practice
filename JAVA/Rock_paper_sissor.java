import java.util.Scanner;
import java.util.Random;
public class Rock_paper_sissor {
    public static void main(String[] args) {
        boolean play=true;
        System.out.println("***************************");
        System.out.println("Rock,paper,Scissor in Java");
        System.out.println("***************************");
        while(play){
        Scanner s=new Scanner(System.in);
        System.out.print("Enter your choice: ");
        String user=s.nextLine().toLowerCase();
        if(!user.equals("rock") && !user.equals("paper") && !user.equals("scissor")){
            System.out.println("Invalid! ");
            continue;
        }
        String[] choose={"rock","paper","scissor"};
        Random r=new Random();
        String computer=choose[r.nextInt(3)];
        System.out.println("Computer choose: "+computer);
        if(user.equals("rock") && computer.equals("paper")){
            System.out.print("Computer Win!");
        }
        else if(user.equals("scissor") && computer.equals("paper")){
            System.out.print("User Win!");
        }
        else if(user.equals("paper") && computer.equals("scissor")){
            System.out.print("Computer Win!");
        }
        else if(user.equals("rock") && computer.equals("scissor")){
            System.out.print("User Win!");
        }
         else if(user.equals("paper") && computer.equals("rock")){
            System.out.print("User Win!");
        }
         else if(user.equals("scissor") && computer.equals("rock")){
            System.out.print("Computer Win!");
        }
        else{
            System.out.println("Tie!!");
        }
        System.out.print("\nPlay Again(yes/no): ");
        String you=s.nextLine().toLowerCase();
        if(you.equals("no")){
            break;
        }
    }
    }
    
}
