
class object_spaceship {
    int weight;
    int length;
    String ship_name;

    public object_spaceship(int weight, int length, String ship) {
        this.weight = weight;
        this.length = length;
        this.ship_name = ship;

    }

    public int get_weight() {
        return this.weight;
    }

}

public class spaceship_oop {
    public static String mix_method() {
        return "This is a method that can be either accessd by creating an object or not";
    }

    public static void main(String[] args) {
        System.out.println("================================");
        // Directly use the method without creating an object
        System.out.println(mix_method());

        // Call the method after creating an instance
        System.err.println("=== After creating an instance ===");
        spaceship_oop main_ship = new spaceship_oop();
        System.err.println(main_ship.mix_method());
    }
}
