package test01;

public class PersonTest {
	public static void main(String[] args) {
		Person p1 = new Person(); // 객체의 생성: new + 생성자 호출 
		p1.name = "승";
		p1.age = 30;
		p1.eat();
		
		Person p2 = new Person();
		p2.name = "jae";
		p2.age = 11;
		p2.eat();
	}
}
