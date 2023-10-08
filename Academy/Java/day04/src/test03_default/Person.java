package test03_default;

//class는 public or default
public class Person {
	String name;
	int age;
	
	public static void main(String[] args) {
		Person p1 = new Person();
		// 자기 자신은 접근 가능
		p1.name = "srs";
	}
}
