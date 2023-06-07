package test06_singleton;

public class PersonTest {
	public static void main(String[] args) {
		// Person p1 = new Person();
		Person p1 = Person.getInstance();
		//setter를 이용한 멤버 변수 값 할당  
		System.out.println(p1.getName());
		System.out.println(p1.getAge());
		
		Person p2 = Person.getInstance();
		System.out.println(p2.getName());
		System.out.println(p2.getAge());
	}
}
