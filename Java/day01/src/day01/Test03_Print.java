package day01;

public class Test03_Print {
	public static void main(String[] args) {
		// print: "문자열"
		// println: "문자열" + \n
		// printf: %d, %s, %c, ... 형식지정 출력
		System.out.print("Hello SSAF\n");
		System.out.println("Hello GREATGOOGI");
		
		System.out.printf("%d\n", 100);
		System.out.printf("%5d\n", 100); // 5칸을 확보한 다음 출
		System.out.printf("%-5d\n", 100);
		System.out.printf("%05d\n", 100);
		
		System.out.printf("%f\n", 10.1);
		System.out.printf("%f\n", 10.14214);
		System.out.printf("%.2f\n", 10.124214);
	}

}
