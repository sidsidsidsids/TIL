package Test02;

import java.io.FileNotFoundException;
import java.io.FileReader;

public class Test01 {
	public static void main(String[] args) {
		method1("1234");
		try {
			method2("input.txt");
		} catch (FileNotFoundException e) {
			System.out.println("should handle");
		}
	}
	public static void method1(String str) {
		// NumberFormatException : UncheckedException
		// 예외 처리 안해도 컴파일은 됨 
		int num = Integer.parseInt(str);
	}
	
	public static void method2(String filename) throws FileNotFoundException{
		// FileNotFoundException : CheckedException
		// 컴파일 되지 않음  -> throw를 통해 해소 
		FileReader reader = new FileReader(filename);
	}
}
