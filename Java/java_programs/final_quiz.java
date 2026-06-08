import java.util.Arrays;

public class final_quiz{
	public static String[] changeWords(String[]  myArray){
		myArray = Arrays.copyOf(myArray, myArray.length);
		for(int i = 0; i < myArray.length; i++){
			if(myArray[i] == "hello"){
				myArray[i] = "goodbye cruel";
			}
		}
        return myArray;
	}

	public static void main(String[] args){
		String[] s = { "hello", "world" };
		String[] t = changeWords(s);
		System.out.println(Arrays.toString(s));
        System.out.println(Arrays.toString(t));
	}
}
