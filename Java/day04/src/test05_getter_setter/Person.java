package test05_getter_setter;

public class Person {
	// 멤버 변수를 private로 선
	private String name;
	private int age;
	private boolean hungry;
	
	// 위 멤버 변수에 접근할 수 있는 통로를
	// public한 메서드로 만들어줌
	// - 값을 변경 -> 설정자(setter)
	// - 값을 조회 -> 접근자(getter)
	
	// 마우스 우클릭 -> Source -> generate getters and setters
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		if(age<0) {
			System.out.println("errorInput");
			return;
		}
		this.age = age;
	}
	public boolean isHungry() {
		return hungry;
	}
	public void setHungry(boolean hungry) {
		this.hungry = hungry;
	}
	
}
