package Test07_comparable;

// to user Collections.sort(), this class should make Comparable interfacce
public class Person implements Comparable<Person>{
	private String name;
	private String id;
	
	public Person(String name, String id) {
		super();
		this.name = name;
		this.id = id;
	}

	@Override
	public String toString() {
		return "Person [name=" + name + ", id=" + id + "]";
	}

	@Override
	public int hashCode() {
		return this.id.hashCode();
	}

	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Person) {
			Person other = (Person) obj;
			return this.id.equals(other.id);
		} else {
			return false;
		}
	}
	
	// compareTo
	// return value : 양수 -> 자리 바꿈 / 0, 음수 -> 그대
	@Override
	public int compareTo(Person o) {
		// 이름 순으로 (String method 그대로 사용 ) 
		return this.name.compareTo(o.name);
		// return Integer.parseInt(this.id) - Interger.parseInt(o.id);
	}
	
	
}
