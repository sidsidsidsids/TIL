package test05;

public class Person {
	// static 키워드 -> 클래스 변수 
	// 이 클래스로 생성되는 모든 인스턴스가 공유 
	static String species = "호모 사피엔스 ";
	
	// static이 없으면 인스턴스 변수 
	String name;
	int age;
	
	public Person() {
		this("minsu",33); // Person("minsu", 33);
	}
	// 파라미터가 있는 생성자
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	
	// 메서드 오버로딩: 이름이 같은 메서드 여러 개를 만들 수 있다 
	// 파라미터가 달라야 함 
	public double add(double a, double b) {
		return a+b;
	}
	public int add(int a, int b) {
		return a+b;
	}
	// 메서두 오버로딩의 장점 
	// - 다양한 자료형에 대해 메서드를 만들 때 이름을 똑같이 할 수 있음
	// addInt(), addDouble()
	
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
	
	public void eat(String dish) {
		System.out.println(dish +" 를 먹는 중임 ");
	}
	
	public void eat(String dish, int times) {
		System.out.println(dish + times + "먹는 중 ");
	}
	// 만약 설계도에 생성자가 하나도 없다면
	// JVM이 기본생성자를 추가해줌 
	
}