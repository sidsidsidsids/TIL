package Test01;

public class Test02 {
	public static void main(String[] args) {
		int[] nums = {10};
		try {
			System.out.println(nums[1]);
			// 발생한 예외 : arrayindexoutofboundsexception
			// catch()안에 오는 예외클래스는 
			// 그 예외 클래스이거나, 그 클래스의 자식 클래스인 경우 
		} catch(ArrayIndexOutOfBoundsException e) {
			//catch(Exception e) : 어떠한 예외든 처리 
			System.out.println("if outofBounds...");
			System.out.println("error: "+ e.getMessage());
			e.printStackTrace();
		}
		System.out.println("End");
	}
}