package Test03;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Test01 {
	public static void main(String[] args) throws IOException {
		
		// FileReader & FileWriter
		test1("    FileReader & FileWriter    ");
		
		// BufferedReader & BufferedWriter
		test2("BufferedReader & BufferedWriter");
	}
	
	public static void test1(String testname) throws IOException {
		try(FileReader reader = new FileReader("requirements.txt");
			FileWriter writer = new FileWriter("requirements-copy2.txt")){
			long start = System.nanoTime();
			int c;
			while((c=reader.read())!= -1) {
				writer.write(c);
			}
			long end = System.nanoTime();
			System.out.printf("%s - %15d ns. \n", testname, end - start);
		}
	}
	// 보조 스트림  
	public static void test2(String testname) throws IOException {
		try(BufferedReader reader = new BufferedReader(new FileReader("requirements.txt"));
			BufferedWriter writer = new BufferedWriter(new FileWriter("requirements-copy2.txt"))){
			long start = System.nanoTime();
			String line;
			while((line = reader.readLine()) != null) {
				writer.write(line);
				writer.newLine();
			}
			long end = System.nanoTime();
			System.out.printf("%s - %15d ns. \n", testname, end - start);
		}
	}
}
