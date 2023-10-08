package Test01;

public class Test03 {
	public static void main(String[] args) {
		try {
			int num = Integer.parseInt("ss");
		} catch (NumberFormatException e) {
			System.out.println("그거는 안돼요 ");
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("그것도 안돼요 ");
			
		} catch (Exception e) {
			System.out.println("뭐한거에 ");
		}
	}
}
