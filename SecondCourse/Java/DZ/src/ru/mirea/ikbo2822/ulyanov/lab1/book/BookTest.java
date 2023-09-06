package ru.mirea.ikbo2822.ulyanov.lab1.book;

public class BookTest {
    public static void main(String[] args) {
        Book book1 = new Book("To Kill a Mockingbird", "Harper Lee", 281);
        Book book2 = new Book("1984", 328);
        Book book3 = new Book("A Study in Scarlet", "Arthur Conan Doyle", 116);

        System.out.println("Book title: " + book1.getTitle()); // "To Kill a Mockingbird"
        System.out.println("Book author: " + book1.getAuthor()); // "Harper Lee"
        System.out.println("Book pageCount: " + book1.getPageCount()); // 281

        book2.setTitle("Nineteen Eighty-Four");
        book2.setAuthor("George Orwell");
        book2.setPageCount(342);

        System.out.println("Book title: " + book2.getTitle()); // "Nineteen Eighty-Four"
        System.out.println("Book author: " + book2.getAuthor()); // "George Orwell"
        System.out.println("Book pageCount: " + book2.getPageCount()); // 342

        System.out.println(book1); // Book title: To Kill a Mockingbird, author: Harper Lee, pageCount: 281"
        System.out.println(book2); // Book title: Nineteen Eighty-Four, author: George Orwell, pageCount: 342"
        System.out.println(book3); // Book title: A Study in Scarlet, author: Arthur Conan Doyle, pageCount: 116"
    }
}
