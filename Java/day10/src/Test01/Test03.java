package Test01;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;
import java.io.FileInputStream;

public class Test03 {
	public static void main(String[] args) throws IOException {
		// byte stream
		// => image
		
		// try with resource
		// try 다음에 (), ()안에 필요한 리소스 정의 
		// close를 따로할 필요 없이 알아서 close 
		
		try (FileInputStream in = new FileInputStream("parrot.jpeg");
				FileOutputStream out = new FileOutputStream("parrot-copy3.jpeg")){
			
			// using buffer
			byte[] buffer = new byte[10];
			int read; // byte를 int형으로 저장  
			
			while((read=in.read(buffer)) != -1) {
				// in.read할 때 마다 buffer에 바이트 채워줌 
				// read: 어디까지 읽으면 되는지 
				out.write(buffer, 0, read);
				System.out.println(Arrays.toString(buffer)+", "+read);
			}
			System.out.println("copy complete");
		} 
			
		System.out.println("all resources closed");
		
	}
}
