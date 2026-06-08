

class data {
    int x = 5;
    String name = "Jack";
    int model_year;
    String model_name;

    public data(int year, String name) {
        this.model_year = year;
        this.model_name = name;
    }

    public void set_name(String set_name) {
        this.model_name = set_name;
    }

    public String get_name() {
        return this.model_name;
    }

    public String myMethod() {
        return this.name + " is using method:";
    }

    static void myStaticMethod() {
        System.out.println("Static methods can be called directly");
    }
}

// A second class that can used the methods and attributes of the first
public class oop {
    public static void main(String[] args) {
    data myObj = new data(2003, "Jack");
    System.out.println(myObj.x);
    System.out.println(myObj.name);
    System.err.println(myObj.myMethod());
    System.err.println(myObj.get_name());

    System.err.println("==============================");
    data.myStaticMethod();
    // data.myMethod(); this is not accessable
    }
}
