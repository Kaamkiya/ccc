import java.util.Scanner;

public class J1 {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    
    int appleScore = s.nextInt() * 3;
    appleScore += s.nextInt() * 2;
    appleScore += s.nextInt();
    
    int bananaScore = s.nextInt() * 3;
    bananaScore += s.nextInt() * 2;
    bananaScore += s.nextInt();
    
    if (appleScore > bananaScore) {
      System.out.println("A");
    } else if (appleScore < bananaScore) {
      System.out.println("B");
    } else {
      System.out.println("T");
    }
  }
}
