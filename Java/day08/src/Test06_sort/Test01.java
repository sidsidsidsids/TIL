package Test06_sort;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Test01 {
	public static void main(String[] args) {
		String[] arr = {"Samsung", "SW", "academy", "for", "youth"};
		List<String> list = Arrays.asList(arr);
		System.out.println(list);
		
		Collections.sort(list);
		System.out.println(list);
	}
}
