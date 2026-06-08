import java.util.Arrays;

public class w6_quiz{
	public static String[] changeWords(String[]  myArray){
		for(int i = 0; i < myArray.length; i++){
			if(myArray[i] == "hello"){
				myArray[i] = "goodbye cruel";
			}
		}
    return myArray;
	}
	public static void main(String[] args){
		String[] s = { "hello", "world" };
		s = changeWords(s);
		System.out.println(Arrays.toString(s));
	}
}
