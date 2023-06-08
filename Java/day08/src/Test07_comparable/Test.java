package Test07_comparable;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Test {
	public static void main(String[] args) {
		List<Person> list = new ArrayList<Person>();
		
		list.add(new Person("Park", "990909"));
		list.add(new Person("Paik", "990929"));
		list.add(new Person("Kim", "990919"));
		
		Collections.sort(list);
		System.out.println(list);
	}
}
