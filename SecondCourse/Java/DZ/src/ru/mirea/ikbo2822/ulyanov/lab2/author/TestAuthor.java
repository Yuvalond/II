package ru.mirea.ikbo2822.ulyanov.lab2.author;

public class TestAuthor {
    public static void main(String[] args) {
        Author author = new Author("Arthur Conan Doyle", "arthurconandoyle@example.com", 'M');

        System.out.println(author);

        System.out.println("Name: " + author.getName());
        System.out.println("Email: " + author.getEmail());

        author.setEmail("newemail@example.com");
        System.out.println("Updated Email: " + author.getEmail());
    }
}
