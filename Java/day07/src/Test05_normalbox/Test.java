package Test05_normalbox;

public class Test {
	public static void main(String[] args) {
		NormalBox b = new NormalBox();
		
		b.setData("Hello Worlds");
		// instanceof
		String s = (String) b.getData();
	}
}
