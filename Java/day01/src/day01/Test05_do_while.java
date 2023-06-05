package day01;

import java.util.Scanner;

public class Test05_do_while {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 1을 입력 받으면 계속 반복
		// 그 외의 값이면 종료되게
		// 이번에는 초기값과 무관하게 처음에는 무조건 실행
		int num = sc.nextInt();
		do {
			System.out.println("실행행");
			num = sc.nextInt();
		} while(num == 1);
	}
}
