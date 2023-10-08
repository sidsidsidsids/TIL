package day02;

public class Test05_min_max {
	public static void main(String[] args) {
		int[] arr = {24, 34, 2, 53, 25, 1, 10, 99};
		
		int min = arr[0]; // 초기 원소를 기준으로 가정
		int max = arr[0];
		for(int i=1; i<arr.length; i++) {
			if(min > arr[i]) min = arr[i];
			if(max < arr[i]) max = arr[i];
		}
		System.out.println(min);
		System.out.println(max);
	}
}
