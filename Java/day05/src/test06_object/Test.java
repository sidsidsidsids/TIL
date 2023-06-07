package test06_object;

import java.util.HashSet;
import java.util.Set;

public class Test {
	public static void main(String[] args) {
		Student st = new Student("joe",22,"electric");
		// st.
		st.eat(); // 자식 클래스에서 부모 메서드 재정의 
		System.out.println(st.toString());
		// 패키지이름.클래스이름.참조값 
		
		Student st2 = new Student("joe",21,"electric");
		System.out.println(st == st2); // false
		System.out.println(st.equals(st2)); // false
		// 둘다 원래는 해값 비교하는 거 
		// equals을 student에서 이름을 비교하는 것으로 재정의 
		
		Object o = new Object();
		o.equals(st);
		
		Set<Student> set = new HashSet<>();
		set.add(st);
		set.add(st2);
		
		System.out.println(set.size());
		//set에서는 동일성을 판단하기 위해서 equals(),hashcode();
		// hashcode를 재정의 하고 나서야 두 객체가 같은 것으로 봄 
	}
}
