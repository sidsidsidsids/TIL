package Test04;

public class Test {
	public static void main(String[] args) {
		Animal a1 = new Cat();
		Animal a2 = new Dog();
		Animal a3 = new Human();
		
		a1.eat();
		// instanceof 사용해보기   
		// instanceof: 객체가 해당 클래스로 만든 객체이거나 해당 클래스의 조상 클래스로 만든 객체인 경우 true
		// 자식 클래스나 전혀 상관 없는 클래스로 만든 객체의 경우 false 
		
		System.out.println(a1 instanceof Animal);
		System.out.println(a1 instanceof Cat);
		System.out.println(a1 instanceof Dog);
		
		if(a1 instanceof Cat) {
			Cat c = (Cat) a1;
			c.eat();
		}
		
		if(a2 instanceof Dog) {
			Dog d = (Dog) a2;
			d.eat();
		}
		
		if(a3 instanceof Human) {
			Human h = (Human) a3;
			h.eat();
		}
	}
}
