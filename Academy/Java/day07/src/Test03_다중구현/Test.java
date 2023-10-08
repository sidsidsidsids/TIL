package Test03_다중구현;

public class Test {
	public static void main(String[] args) {
		Duck d = new Duck();
		Eagle e = new Eagle();
		
		// 다형성
		AbletoFly f = d;
		// f. -> fly 밖에 없음  
		// d. -> fly, swim, hunt
	}
}
