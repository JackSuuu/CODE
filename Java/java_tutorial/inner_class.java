// The purpose of nested classes is to group classes that belong together

class OuterClass {
    int x = 10;

    class InnerClass {
        int y = 5;
    }

    // class can be private / protected
    // If you don't want outside objects to access the inner class
    private class InnerPrivateClass {
        int z = 5;
    }
}

public class inner_class {
    public static void main(String[] args) {
        OuterClass myOuter = new OuterClass();
        OuterClass.InnerClass myInner = myOuter.new InnerClass();
        System.out.println(myInner.y + myOuter.x);
    }
}
