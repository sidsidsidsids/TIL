package Test03;

// 일반 클래스인데 추상 클래스를 상속받는다 
public class Cat extends Animal{
	// 추상클래스를 상속 받은 클래스는
	// 추상메서드를 모두 재정의 해야 한다 
	
	@Override
	public void speak() {
		// TODO Auto-generated method stub
		System.out.println("Meow");
	}
	
	// 자식 클래스에서 독단적으로 eat() 
	public void eat() {
		System.out.println("eat fish");
	}
}
