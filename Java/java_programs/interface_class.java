interface PetrolCar {
    public static final String FUEL = "Diesel"; 
    public abstract void refillTank();
}

interface ElectricCar {
    public abstract void rechargeBattery();
}

interface Animal {
    public static final String classification = "Kingdom Animalia";
    public void makeNoise();
}

class ChevroletVolt implements PetrolCar, ElectricCar {
    public void refillTank() {
        // refill petrol
    }

    public void rechargeBattery() {
        // recharge power
    }
}

public class interface_class {
    
}
