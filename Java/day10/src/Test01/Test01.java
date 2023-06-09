package Test01;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileInputStream;

public class Test01 {
	public static void main(String[] args) throws IOException {
		// byte stream
		// => image
		FileInputStream in = null;
		FileOutputStream out = null;
		
		try {
			in = new FileInputStream("parrot.jpeg");
			out = new FileOutputStream("parrot-copy.jpeg");
			
			int b; // byte를 int형으로 저장  
			
			while((b=in.read()) != -1) {
				out.write(b);
			}
			System.out.println("copy complete");
		} finally {
			// close in-output stream
			if(in != null)
				in.close();
			if(out != null)
				out.close();
			
			System.out.println("all resources closed");
		}
	}
}
