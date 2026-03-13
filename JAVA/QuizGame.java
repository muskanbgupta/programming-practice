import java.util.Scanner;
public class QuizGame{
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        String option;
        int score=0;
        System.out.println("*********************");
        System.out.println("JAVA QUIZ GAME");
        System.out.println("*********************");
        String[] question={
            "1. In DBMS, what does SQL stand for?",
            "2. Which data structure works on LIFO (Last In First Out) principle?",
            "3. In Networking, what does IP stand for?",
            "4. Which normal form in DBMS removes partial dependency?"
        };
        
        String[][] op={{"A) Structured Query Language\n",
                        "B) Simple Query Language\n" ,
                        "C) Sequential Query Language\n",
                        "D) Standard Question Language"},
                        {"A) Queue\n",
                         "B) Stack\n",
                         "C) Array\n",
                         "D) Linked List"},
                        {"A) Internet Process\n",
                         "B) Internal Protocol\n",
                         "C) Internet Protocol\n",
                         "D) Information Protocol"},
                        {"A) 1NF\n",
                         "B) BCNF\n",
                         "C) 3NF\n",
                         "D) 2NF"}};
        String[] ans={"a","b","c","d"};

        for(int i=0;i<question.length;i++){
            System.out.println(question[i]);
            for(String options:op[i]){
             System.out.print(options);
            }
            System.out.println(" ");
            System.out.print("Enter Your Choice:");
             option=s.nextLine();
             option=option.toLowerCase();
            if(option.equals(ans[i])){
                System.out.println("________");
                 System.out.println("Correct");
                 System.out.println("________");
                    score++;

                    }
             else{
                System.out.println("________");
                System.out.println("Incorrect");
                System.out.println("________");
                    }
                    
                }
            System.out.println("Your Total Score is: "+score+"/4");
        }


    }

