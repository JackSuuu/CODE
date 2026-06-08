import java.util.ArrayList;
import java.util.List;

public class list {
    public static void main(String[] args) {
        List<Integer> num = new ArrayList<>();
        
        // 检查是否有足够的参数
        if (args.length >= 3) {
            // 将参数转换为整数并添加到num列表中
            num.add(Integer.valueOf(args[0]));
            num.add(Integer.valueOf(args[1]));
            num.add(Integer.valueOf(args[2]));
        } 
        else {
            System.out.println("请提供三个整数作为参数。");
        }

        for (int each : num) {
            System.out.println(each);
        }
    }
}

