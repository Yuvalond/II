package ru.mirea.ikbo2822.ulyanov.lab1.ball;

public class BallTest {
    public static void main(String[] args) {
        Ball ball1 = new Ball("Red", 5.0);
        Ball ball2 = new Ball("Blue");
        Ball ball3 = new Ball(4.0);

        System.out.println("Ball color: " + ball1.getColor()); // "Red"
        System.out.println("Ball radius: " + ball1.getRadius()); // 5.0

        ball2.setColor("Yellow");
        ball2.setRadius(6.0);

        System.out.println("Ball color: " + ball2.getColor()); //"Yellow"
        System.out.println("Ball radius: " + ball2.getRadius()); // 6.0

        ball3.bounce();

        System.out.println(ball1); // "Ball color: Red, radius: 5.0"
        System.out.println(ball2); // "Ball color: Yellow, radius: 6.0"
        System.out.println(ball3); // "Ball color: Green, radius: 4.0"
    }
}
