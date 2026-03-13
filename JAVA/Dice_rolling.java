import java.util.Random;
import java.util.Scanner;
public class Dice_rolling {
    public static void main(String[] args) {

    Scanner scanner=new Scanner(System.in);
    System.out.print("Enter number of dice to roll: ");
    int D=scanner.nextInt();

    while (D!=0) {
    Random r=new Random();
    int Dice=r.nextInt(1,7);
    printdie(Dice);
    System.out.printf("You rolled Dice :%d\n",Dice);
    D=D-1;
    }

}
    static void printdie(int Dice){
        String d1="""
                 -------
                |       |
                |   ●   |
                |       |
                 -------
                """;
        String d2="""
                 -------
                |●      |
                |       |
                |      ●|
                 -------
                """;
        String d3="""
                 -------
                |●      |
                |   ●   |
                |      ●|
                 -------
                """;
        String d4="""
                 -------
                |●     ●|
                |       |
                |●     ●|
                 -------
                """;
        String d5="""
                 -------
                |●     ●|
                |   ●   |
                |●     ●|
                 -------
                """;
        String d6="""
                 -------
                |●  ●  ●|
                |       |
                |●  ●  ☻|
                 -------
                """;
        
        switch(Dice){
           case 1 -> System.out.println(d1);
           case 2 -> System.out.println(d2);
           case 3 -> System.out.println(d3);
           case 4 -> System.out.println(d4);
           case 5 -> System.out.println(d5);
           case 6 -> System.out.println(d6);
        }
                
    }
}