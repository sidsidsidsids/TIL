package Test01_list;

import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Test01 {
	public static void main(String[] args) {
		// List
		// 순서가 있는 자료 구조 
		// 중복이 허용됨  
		// List<String> names = new ArrayList<>();
		List<String> names = new LinkedList<>();
		
		// add
		names.add("Ahn");
		names.add("Kim");
		names.add("Lee");
		names.add(0,"Lee");
		
		System.out.println(names);
		
		// empty check
		System.out.println(names.isEmpty());
		
		// count elem
		System.out.println(names.size());
		
		// adjust
		names.set(2, "Jung");
		System.out.println(names);
		
		// read
		for(String name : names) {
			System.out.println(name);
		}
		
		// iterator
		Iterator<String> e = names.iterator();
		while(e.hasNext()) {
			System.out.println(e.next());
		}
		// for-each	 도 가능  
		
		// delete(index)
		names.remove(2);
		System.out.println(names);
		
		// delete(value)
		names.remove("Lee");
		System.out.println(names);
		
		// delete all
		names.clear();
		names.add("Park");
		names.add("Park");
		names.add("Seo");
		for(int i = 0; i<names.size(); i++) {
			System.out.println(names.get(i));
		}
		
		// want to delete park
//		for(int i = 0; i<names.size(); i++) {
//			if(names.get(i).equals("Park")) {
//				names.remove(i);
//			}
//		}
		for(int i=names.size()-1; i>=0; i--) {
			if(names.get(i).equals("Park")) {
				names.remove(i);
			}
		}
	}
}
