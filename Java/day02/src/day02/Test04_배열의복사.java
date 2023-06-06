package day02;

import java.util.Arrays;

public class Test04_배열의복사 {
	public static void main(String[] args) {
		int[] scores = new int[] {29, 45, 35, 24, 80};
		
		int[] newScores = new int[10];
		for(int i=0; i<5; i++) {
			newScores[i] = scores[i];
		}
		System.out.println(Arrays.toString(newScores));
		
		int[] newScores2 = Arrays.copyOf(scores, scores.length * 2);
		System.out.println(Arrays.toString(newScores2));
	}
}
