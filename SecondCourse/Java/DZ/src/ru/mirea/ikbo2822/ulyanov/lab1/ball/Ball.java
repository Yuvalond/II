package ru.mirea.ikbo2822.ulyanov.lab1.ball;

public class Ball {
    private String color;
    private double radius;

    public Ball(String color, double radius) {
        this.color = color;
        this.radius = radius;
    }
    public Ball(String color) {
        this.color = color;
        this.radius = 68.8;
    }
    public Ball(double radius) {
        this.color = "White";
        this.radius = radius;
    }
    public void setColor(String color) {
        this.color = color;
    }
    public String getColor() {
        return color;
    }
    public void setRadius(double radius) {
        this.radius = radius;
    }
    public double getRadius() {
        return radius;
    }

    public void bounce() {
        System.out.println("The ball is bouncing!");
    }
    public String toString() {
        return "Ball color:" + color + ", radius: " + radius;
    }
}
