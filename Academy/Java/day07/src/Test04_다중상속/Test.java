package Test04_다중상속;

public class Test {
	public static void main(String[] args) {
		DuckInterface d1 = new Duck();
		DuckInterface d2 = new UglyDuckling();
		DuckInterface d3 = new DonaldDuck();
		
		d1.playInnocent();
		d2.playInnocent();
		d3.playInnocent();
	}
}
