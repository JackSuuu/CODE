// Abstract classes in Animal Hierarchy
// Animal -> Feline -> Lion / Cat

public abstract class abstract_animal {
    public void sleep() {
        System.out.println("Sleeping: Zzzzz");
    }

    // abstract methods"
    // - No body
    // - **must** be implemented in any concrete subclass (implemented ~ overriden)
    // - can noly be declared in an abstract class

    public abstract void roam();

    public abstract void makeNoise();
    // if the class is abstract, it does not have a body
    // System.out.println("Noises...");
}

abstract class Feline extends abstract_animal {
    public abstract void roam();

    public abstract void makeNoise();
}

class Lion extends Feline {
    public void roam() {
        System.out.println("Roamin on the plain.");
    }

    public void makeNoise() {
        System.out.println("Buzzz");
    }
}
