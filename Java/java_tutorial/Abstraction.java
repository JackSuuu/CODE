// Data *abstratcion* is the process of hiding certain details
// and showing only essential information to the user
// Abstraction can be achieved with either abstract classes / interdaces
abstract class Animal {
    // Abstract method
    public abstract void animalSound();
    // Regular method
    public void sleep() {
        System.out.println("Zzz");
    }
}

// To access the abstract class, it must be inherited from another class
// So we use *extends* keyword to inherit a class

// After we extend the animal class, it can use the inner function of Animal
class Pig extends Animal_T {
    public void animalSound() {
        // The body og animalsound() is provided here
        System.out.println("The pig says: wee wee");
    }
}

public class Abstraction {
    public static void main(String[] args) {
        Pig myPig = new Pig();
        myPig.animalSound();
    }
}
