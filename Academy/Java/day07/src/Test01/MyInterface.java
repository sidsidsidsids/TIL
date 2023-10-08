package Test01;


// 인터페이스의 작성은 interface keyword
public interface MyInterface {
	// 모든 멤버변수는 public static final이며 생략이 가능  
	public static final int MEMBER_1 = 10;
	int MEMBER_2 = 20;
	
	// 모든 메서드는 public abstract이며 생략이 가능  
	public abstract void method1();
	void method2();
}
