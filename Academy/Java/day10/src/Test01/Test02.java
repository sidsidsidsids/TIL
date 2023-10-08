package Test01;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileInputStream;

public class Test02 {
	public static void main(String[] args) throws IOException {
		// byte stream
		// => image
		
		// try with resource
		// try 다음에 (), ()안에 필요한 리소스 정의 
		// close를 따로할 필요 없이 알아서 close 
		
		try (FileInputStream in = new FileInputStream("parrot.jpeg");
				FileOutputStream out = new FileOutputStream("parrot-copy2.jpeg")){
			
			
			int b; // byte를 int형으로 저장  
			
			while((b=in.read()) != -1) {
				out.write(b);
			}
			System.out.println("copy complete");
		} 
			
		System.out.println("all resources closed");
		
	}
}
