package test08_polymorphism_2;

public class Test {
	public static void main(String[] args) {
		Student st = new Student("park",33,"manu");
		
		Person p = st;
		
		Student st3 = (Student) p;
		st3.study(); // 얘는 잘 됨  
		
		Person p2 = new Person("kim",28);
		
		Student st2 = (Student) p2; //error 
		// st2.study(); // error, 강제 형변환으로 인해 해당 메모리가 없다  
	}
}
