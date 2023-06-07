package test05_binding;

public class Student extends Person{
	String major;
	
	// 파라미터가 있는 생성자를 만들어야 한다 (부모 클래스에서 그렇게 했으니까 )  
	public Student(String name, int age, String major) {
		super(name, age); // 부모클래스의 생성자 호출  
		this.major = major;
	}
	public void study() {
		System.out.println("studying");
	}
	public void eat() {
		System.out.println("지식을 먹는다.");
	}
}
