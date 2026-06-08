
public class spaceship {
    public void shield(String ship, int code) {
        System.out.println(ship + String.valueOf(code) + " Activitate Shield");
    }

    static String gun_attack(String ship) {
        return ship + "Attacking";
    }

    static void nothing() {
        int a = 5;
        int b = 3;
        int c = a + b;
    }
    
    public static void main(String[] args) {

        for (int i=0; i<=3; i++) {
            String attack = gun_attack("ship_1 ") + " Now";

            System.out.println(attack); 
        }

        // 实例化 Build an instance
        spaceship ship_1 = new spaceship();
        ship_1.shield("Voyager", 5);

    }
}
