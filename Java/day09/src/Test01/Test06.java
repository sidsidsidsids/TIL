package Test01;

public class Test06 {
	public static void main(String[] args) {
		// try ~ catch ~ finally
		
		try {
			String str = "9a";
			System.out.println("code 1 - before parse : "+str);
			int num = Integer.parseInt(str);
			System.out.println("code 2 - after parse : "+str);
			return; // code 5 doesn't work as it ends in finally because of return
			// if exception, it doesn't return so code 5 works
		} catch (Exception e) {
			System.out.println("code 3 - exception handling complete");
			
		} finally {
			System.out.println("code 4 - always do");
		}
		
		System.out.println("code 5 - always do?");
	}
}
