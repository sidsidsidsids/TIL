package day02;

public class Test08_2차원배열2 {
	public static void main(String[] args) {
		int[][] arr = new int[4][4];
		int cnt = 1;
//		for(int r=0; r<4; r++) {
//			for(int c=0; c<4; c++) {
//				arr[r][c] = cnt++;
//			}
//		}
		
		for(int r=3; r>=0; r--) {
			for(int c=3; c>=0; c--) {
				arr[r][c] = cnt++;
			}
		}
		
		for(int r=0;r<4;r++) {
			for(int c=0;c<4;c++) {
				System.out.printf("%4d", arr[r][c]);
			}
			System.out.println();
		}
	}
}
