package Test07_genericMethod;

public class Test {
	public static void main(String[] args) {
		// Generic Class 변수 선언
		// Generic Class 객체 만듬
		// 선언과 객체 생성 시 타입 지
		GenericBox<String> strBox = new GenericBox<String>();
		strBox.setData("Hello Generic");
		System.out.println(strBox.getData());
		strBox.genericMethod(123);
	}
}
