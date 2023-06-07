package test05_getter_setter;

public class PersonTest {
	public static void main(String[] args) {
		Person p1 = new Person();
		p1.setName("nu");
		p1.setAge(1);
		p1.setAge(-421);
		//setter를 이용한 멤버 변수 값 할당  
		System.out.println(p1.getName());
		System.out.println(p1.getAge());
		
	}
}
