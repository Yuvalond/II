package ru.mirea.ikbo2822.ulyanov.lab2.ball;

public class TestBall {
    public static void main(String[] args) {
        Ball ball = new Ball();

        System.out.println(ball);

        ball.setXY(2.0, 3.0);
        System.out.println("New Position: " + ball);

        ball.move(1.0, -1.0);
        System.out.println("After Move: " + ball);
    }
}
