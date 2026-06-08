
public class classes {
    public static class Person {
        String name;
        int age;

    // 构造函数
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

        void introduce() {
            System.out.println("My name is " + name + " and I am " + age + " years old.");
        }
    }

    public static void main(String[] args) {
        // 创建对象并调用构造函数
        classes.Person person = new Person("Alice", 25);
        person.introduce();
    }
}

