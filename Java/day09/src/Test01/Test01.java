package Test01;

public class Test01 {
	public static void main(String[] args) {
		int[] nums = {3};
//		System.out.println(nums[1]);
		// Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 1 out of bounds for length 1
		// at Test01.Test01.main(Test01.java:6)
		// System.out.println(nums[-1]); 오버플로우가 발생할 때 음수가 들어가서 에러남  
		
		// int num = 5 / 0 ;
//		Exception in thread "main" java.lang.ArithmeticException: / by zero
//		at Test01.Test01.main(Test01.java:11)
		
//		int nume = Integer.parseInt("rs");
//		Exception in thread "main" java.lang.NumberFormatException: For input string: "rs"
//			at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:67)
//			at java.base/java.lang.Integer.parseInt(Integer.java:668)
//			at java.base/java.lang.Integer.parseInt(Integer.java:786)
//			at Test01.Test01.main(Test01.java:15)
		
		// throw keyword 이용하여 new 예외생성자() => 예외 객체  
		// 예외 객체를 던질 때 발생  
		// 예외가 발생? 내부적으로는 예외 객체가 생성되서 던져진 것  
		// throw new ArrayIndexOutOfBoundsException();
		
		try{
			throw new Exception();
		} catch (Exception e) {
			System.out.println("exception");
		}
		System.out.println("end");
	}
}
