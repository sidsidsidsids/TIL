package Test01;

public class Test05 {
	public static void main(String[] args) {
		try {
			int num = 3/0;
		} catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
			System.out.println("그거는 안돼요 ");
		} catch (Exception e) {
			System.out.println("뭐한거에 ");
		}
	}
}
