package Test04;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Test01 {
	public static void main(String[] args) throws IOException {
		// Scanner vs. BufferedReader
		// txt에서 한 줄 씩 읽어와서 문자열로 바꾸기  
		// BufferedReader가 10배 더 빠름  
		
		// FileReader & FileWriter
		test1("    FileReader & FileWriter    ");
		
		// BufferedReader & BufferedWriter
		test2("BufferedReader & BufferedWriter");
	}
	
	public static void test1(String testname) throws IOException {
		try(Scanner sc = new Scanner(new FileInputStream("requirements.txt"))){
			long start = System.nanoTime();
			while(sc.hasNext()) {
				int num = sc.nextByte();
			}
			long end = System.nanoTime();
			System.out.printf("%s - %15d ns. \n", testname, end - start);
		}
	}
	
	public static void test2(String testname) throws IOException {
		try(BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("requirements.txt")))){
			// 표준 입출력 -> 알고리즘 -> 
			// System.in <= InputStream
			// System.out <= OutputStream
			// BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			// Scanner sc = new Scanner(System.in));
			// BufferedInputStream in = new BufferedInputStream(new FileInputStream());
			
			long start = System.nanoTime();
			String l;
//			while((l = br.readLine()) != null) {
//				int num = Integer.parseInt(l);
//			}
			long end = System.nanoTime();
			System.out.printf("%s - %15d ns. \n", testname, end - start);
		}
	}
	
	
}
