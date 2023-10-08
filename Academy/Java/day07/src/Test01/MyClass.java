package Test01;

// 클래스는 인터페이스를 구현  
// 인터페이스는 클래스에 의해 구현  
// 클래스가 인터페이스를 구현할 때는 implements 
public class MyClass implements MyInterface{
	
	@Override
	public void method1() {
		// TODO Auto-generated method stub
		System.out.println("method 1");
	}

	@Override
	public void method2() {
		// TODO Auto-generated method stub
		System.out.println("method 2");
	}

}
