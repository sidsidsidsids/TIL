package day02;

import java.util.Arrays;

public class Test06_빈도수구하기 {
	public static void main(String[] args) {
		int[] arr = {0, 0, 2, 3, 1, 2, 5, 3, 3, 4};
		
		int[] counter = new int[10];
		
		for(int i=0;i<arr.length;i++) {
			counter[arr[i]]++;
		}
		
		System.out.println(Arrays.toString(counter));
	}
}
