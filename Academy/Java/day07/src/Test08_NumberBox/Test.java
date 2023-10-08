package Test08_NumberBox;

public class Test {
	public static void main(String[] args) {
		// Generic Class 변수 선언
		// Generic Class 객체 만듬
		// 선언과 객체 생성 시 타입 지
		NumberBox<Double> strBox = new NumberBox<>();
		strBox.setData(222.123);
		System.out.println(strBox.getData());
		
		
	}
}
