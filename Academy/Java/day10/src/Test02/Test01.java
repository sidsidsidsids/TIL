package Test02;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Test01 {
	public static void main(String[] args) throws FileNotFoundException, IOException {
		try(FileReader reader = new FileReader("requirements.txt");
				FileWriter writer = new FileWriter("requirements-copy.txt")){
			int c; // char를 int에 담아도 
			while((c = reader.read()) != -1) {
				writer.write(c);
			}
			System.out.println("copy complete");
			System.out.println("use try with resource");
		}
	}
}
