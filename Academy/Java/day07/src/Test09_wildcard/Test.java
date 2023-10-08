package Test09_wildcard;

public class Test {
	public static void main(String[] args) {
		GenericBox<Student> studentBox = new GenericBox<>();
		GenericBox<Person> personBox = new GenericBox<>();
		GenericBox<Object> objectBox = new GenericBox<>();
		
		// ? : any types
		GenericBox<?> allBox = objectBox;
		allBox = personBox;
		allBox = studentBox;
		
		// ? extends T : T or T's child
		GenericBox<? extends Person> personAndChild = personBox;
		personAndChild = studentBox;
		// personAndChild = objectBox;
		
		// ? super T : T or T's parent
		GenericBox<? super Person> personAndParent = personBox;
		// personAndParent = studentBox;
		personAndParent = objectBox;
	}
}
