package day01;

import java.util.Scanner;

public class Test04_While {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 1을 입력 받으면 계속 반복
		// 그 외의 값이면 종료되게
		int num = sc.nextInt();
		while(num == 1) {
			System.out.println("실행행");
			num = sc.nextInt();
		}
	}
}
