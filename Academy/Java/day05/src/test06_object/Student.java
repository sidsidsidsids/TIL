package test06_object;

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
	@Override // annotation: 컴파일러에게 도움 
	public void eat() {
		System.out.println("지식을 먹는다.");
	}
	// 우클릭 - source - override...
	@Override
	public boolean equals(Object obj) {
		return name.equals(((Student)obj).name);
	}
	@Override
	public String toString() {
		return "Student [name="+super.name+", age="+super.age+"]";
	}
	public int hashCode() {
		return name.hashCode();
	}
}
