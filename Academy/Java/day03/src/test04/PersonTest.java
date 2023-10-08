package test04;

public class PersonTest {
	public static void main(String[] args) {
		Person p1 = new Person();
		int sum = p1.add(9, 16);
		double sum2 = p1.add(41.14, 22.22);
		System.out.println(sum);
		System.out.println(sum2);
		p1.eat();
		p1.eat("탕수육 ");
		p1.eat("ham", 3);
	}
}
