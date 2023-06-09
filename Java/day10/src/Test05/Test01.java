package Test05;

import java.io.File;

public class Test01 {
	public static void main(String[] args) {
		// File Class
		// file 또는 dir의 객체 생성 
		File f = new File("requirements.txt");
		System.out.println("이름 : "+f.getName());
		System.out.println("경로 : "+f.getPath());
		System.out.println("디렉토리니 : "+f.isDirectory());
		System.out.println("파일이니 : "+f.isFile());
		System.out.println(f.toString());
		System.out.println(f);
	}
}
