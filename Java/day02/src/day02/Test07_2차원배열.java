package day02;

public class Test07_2차원배열 {
	public static void main(String[] args) {
		int[][] arr = new int[3][4];
		int[][] raggedArr = new int[3][];
		raggedArr[0] = new int[7];
		raggedArr[1] = new int[3];
		raggedArr[2] = new int[5];
		
		for(int r=0;r<3;r++) {
			for(int c=0;c<4;c++) {
				System.out.printf("%4d", arr[r][c]);
			}
			System.out.println();
		}
	}
}
