package Test06_serialization;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.nio.ReadOnlyBufferException;

public class Test01 {
	public static void main(String[] args) {
		ObjectInputStream in = null;
		ObjectOutputStream out = null;
		
		try {
			out = new ObjectOutputStream(new FileOutputStream(new File("object.dat")));
			out.writeObject(new Person("Hong",21 ));
			System.out.println("output in file");
			
			in = new ObjectInputStream(new FileInputStream(new File("object.dat")));
			Object obj = in.readObject();
			Person p = (Person) obj;
			System.out.println(p);
		} catch(Exception e){
			System.out.println("error");
			e.printStackTrace();
		}	finally {
		try {
			if(out != null)
				out.close();
			if(in != null)
				in.close();
		} catch (Exception e) {
			System.out.println("duplicated try-catch");
			}
		}
	}
}
