package Test02_set;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;

public class Test01 {
	public static void main(String[] args) {
		// Set<String> set = new HashSet<>();
		Set<String> set = new TreeSet<>();
		
		// HashSet
		// - 해시테이블에 원소를 저장  
		// - 성능면에서 우수하다고 알려져 있음  
		// - 원소들의 순서가 일정하지 않음  
		
		// TreeSet
		// - red-black tree에 원소 저장  
		// - 값에 따라서 순서 결정  
		// - 값을 순서대로 정렬할 필요가 있다면 고려해볼만한 선택지  
		
		
		set.add("Hong");
		set.add("Hong");
		set.add("Jeon");
		set.add("Ko");
		
		System.out.println(set);
		System.out.println("Hong".hashCode());
		System.out.println("Ho".hashCode());
		System.out.println(new String("Hong").hashCode());
		
		System.out.println("Hong".equals("Hong"));
		
		Iterator<String> e = set.iterator();
		while(e.hasNext()) {
			System.out.println(e.next());
		}
	}
}
