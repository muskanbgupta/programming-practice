import java.util.Scanner;
import java.util.Random;
class Slot_Machine{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        int bal=100;
        boolean run=true;
        while(run){
        System.out.println("************************");
        System.out.println("Slot Machine in Java!!!\nSymbols:🍒 🍉 🍊 🔔 🌟");
        System.out.println("************************");
        String[] Slot={"🍒","🍉","🍊","🔔","🌟"};
        System.out.println("Current Balance: Rs."+bal);
        
        System.out.print("Place your Bet Amount: ");
        int bet =s.nextInt();
        if(bet>bal){
            System.out.println("Invalid Amount");
            continue;
        }
        s.nextLine();
        System.out.println("Spining......"); 
        System.out.println("*****************");
        Random r=new Random();
        String s1=Slot[r.nextInt(Slot.length)];
        String s2=Slot[r.nextInt(Slot.length)];
        String s3=Slot[r.nextInt(Slot.length)];
        System.out.println(s1+"|"+s2+"|"+s3);

        if(s1.equals(s2)&&s2.equals(s3)){
            System.out.println("You Won! Rs.50");
            bal=(bal+100)-bet;
        }
        else if(s1.equals(s2) || s2.equals(s3)||s3.equals(s1)){
            System.out.print("JACKPOT 🌟\nYou Won! Rs.100");
            bal=(bal+50)-bet;
        }
        else{
            System.out.println("You lost! ");
            bal=(bal-bet)-20;
        }
        
        System.out.print("Do you want to play again(y/n)? ");
        String choice=s.nextLine().toLowerCase();
        if(choice.equals("no") || choice.equals("n")){
            System.out.println("GAME OVER! Your final balance is Rs."+bal);
            run=false;
        }
    }

    }
}