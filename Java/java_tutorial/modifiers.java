public class modifiers {
    // Static Method
    static void my_static_method() {
        System.out.println("Static Met can be called without creating objects");
    }

    // Public Method
    public void my_pulic_method() {
        System.out.println("Public Met must be called by creating objects");
    }

    // Main Method
    public static void main(String[] args) {
        my_static_method();
        // my_pulic_method();

        modifiers myObj = new modifiers();
        myObj.my_pulic_method();
    }
}
