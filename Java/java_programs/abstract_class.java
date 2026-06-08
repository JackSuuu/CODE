// Function makeGreeting gets a greeting string from an object
// greeter of class Hello
// Then sends a greeting to a friend
abstract class greeting {
    public abstract String greet();
}

class Hello extends greeting {
    // must override abstract method
    // to avoid compiler error
    public String greet() {
        return "Hello";
    }
}

class Bonjour extends greeting {
    public String greet() {
        return "Bonjour";
    }
}

public class abstract_class {
    public static void makeGreeting(greeting greeter, String name) {
        System.out.printf(greeter.greet() + "," + name + "!");
        System.out.println();
    }

    public static void main(String[] args) {
        Hello greeter = new Hello();
        makeGreeting(greeter, "James");

        Bonjour f_greeter = new Bonjour();
        makeGreeting(f_greeter, "Jacques");
    }
}
