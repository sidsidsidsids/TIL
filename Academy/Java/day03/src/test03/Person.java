package test03;

public class Person {
	// static 키워드 -> 클래스 변수 
	// 이 클래스로 생성되는 모든 인스턴스가 공유 
	static String species = "호모 사피엔스 ";
	
	// static이 없으면 인스턴스 변수 
	String name;
	int age;
	
	public int add(int a, int b) {
		return a+b;
	}
	
	// 메서드의 종료
	// - 블록의 끝을 만날 때 
	// - return 문을 만날 때 (void에서도 return 가능)
	public void study(String subject) {
		double probability = Math.random();
		
		System.out.println(subject+"를 공부");
		if(probability < 0.3)
			return;
		System.out.println("just playing");
	}
	
	public void eat() {
		String dish = "짜장면";
	}
	
	// 만약 설계도에 생성자가 하나도 없다면
	// JVM이 기본생성자를 추가해
}