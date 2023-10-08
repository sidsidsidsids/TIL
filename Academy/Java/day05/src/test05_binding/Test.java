package test05_binding;

public class Test {
	public static void main(String[] args) {
		Student st = new Student("joe",22,"electric");
		// st.
		st.eat(); // 자식 클래스에서 부모 메서드 재정의 
		
		Person st2 = new Student("kane",30,"striker");
		st2.eat();
	}
}
