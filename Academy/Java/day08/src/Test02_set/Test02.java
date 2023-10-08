package Test02_set;

import java.util.HashSet;
import java.util.Set;

public class Test02 {
	public static void main(String[] args) {
		Set<Person> set = new HashSet<>();
		Person p1 = new Person("Yang", "242424");
		Person p2 = new Person("Yang", "242424");
		
		set.add(p1);
		set.add(p2);
		
		// HashSet은 hashCode, equals 두 개 모두 같아야 같은 거로 판단   
		System.out.println(p1.hashCode());
		System.out.println(p2.hashCode());
		
		System.out.println(p1.equals(p2));
	}
}
