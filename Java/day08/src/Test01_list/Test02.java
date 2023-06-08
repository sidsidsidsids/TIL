package Test01_list;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Vector;

public class Test02 {
	public static void main(String[] args) {
		List<Object> al = new ArrayList<Object>();
		List<Object> ll = new LinkedList<Object>();
		List<Object> v = new Vector<Object>();
		
		test1("순차적 추가 - arraylist - ", al);
		test1("순차적 추가 - linkedlist - ", ll);
		test1("순차적 추가 - vector - ", v);

		test2("중간 추가 - arraylist - ", al);
		test2("중간 추가 - linkedlist - ", ll);
		test2("중간 추가 - vector - ", v);
	

		test3("조회 - arraylist - ", al);
		test3("조회 - linkedlist - ", ll);
		test3("조회 - vector - ", v);
	
	}
	
	public static void test1(String testname, List<Object> list) {
		long start = System.nanoTime(); // start time
		for(int i=0; i<50000; i++) {
			list.add(new String("Hello"));
		}
		long end = System.nanoTime(); // end time
		System.out.printf("%s \t 소요시간: %15d ns. \n", testname, end-start);
	}
	
	public static void test2(String testname, List<Object> list) {
		long start = System.nanoTime(); // start time
		for(int i=0; i<50000; i++) {
			list.add(0, new String("Hello"));
		}
		long end = System.nanoTime(); // end time
		System.out.printf("%s \t 소요시간: %15d ns. \n", testname, end-start);
	}
	
	public static void test3(String testname, List<Object> list) {
		long start = System.nanoTime(); // start time
		for(int i=0; i<50000; i++) {
			list.get(i);
		}
		long end = System.nanoTime(); // end time
		System.out.printf("%s \t 소요시간: %15d ns. \n", testname, end-start);
	}
}
