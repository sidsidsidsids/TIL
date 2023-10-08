package test06;

public class PersonTest {
	public static void main(String[] args) {
		Person p1 = new Person("john",23);
		Person p2 = new Person("joe",123);
		Person p3 = new Person();
		System.out.println(p1.name);
		System.out.println(p2.age);
		System.out.println(p3.name);
	}
}
