package Test03;

public class Test {
	public static void main(String[] args) {
		Animal a1 = new Cat();
		Animal a2 = new Dog();
		Animal a3 = new Human();
		
		a1.eat();
		// 부모클래스에 추상메서드 혹은 일반메서드를 정의해놔야   
		// 부모클래스 타입으로 참조했을 때 메서드 사용 가능   
	}
}
