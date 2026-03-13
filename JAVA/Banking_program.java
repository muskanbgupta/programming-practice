import java.util.Scanner;
public class Banking_program {
     static Scanner s=new Scanner(System.in);
     static double bal=0;
    public static void main(String[] args) {
        boolean isRunning=true;
        while (isRunning) {
            
        
        System.out.println("*******************");
         System.out.println("Banking program");
         System.out.println("*******************");
         System.out.println("1. Show Balance");
         System.out.println("2. Deposite");
         System.out.println("3.Withdraw");
         System.out.println("4. Exit");
        System.out.print("Enter your choice(1-4): ");

        int choice=s.nextInt();
        switch (choice){
            case 1 -> showBalance();
            case 2 -> deposite();
            case 3 -> withdraw();
            case 4 ->{ System.out.print("Thank for coming !");isRunning=false;}
            default -> System.out.println("Invalid!");

        }}
        
    }
    static void showBalance(){
        System.out.printf("The Balance is %.2f\n",bal);

    }
    static void deposite(){
        System.out.print("Enter amount to Deposite: ");
        double de=s.nextDouble();
         bal+=de;
         System.out.printf("Amount deposited %.2f\n",de);
    }
    static void withdraw(){

         System.out.print("Enter amount to withdraw: ");
         double withdraw=s.nextDouble();
         if(withdraw<0 || withdraw>bal){
            System.out.println("Insufficient balance or Amount entered is less than 0");
         }
         else{
         bal-=withdraw;
         System.out.printf("Sum of Rs. %.2f Withdraw\n",withdraw);
         }
        
    }
}



