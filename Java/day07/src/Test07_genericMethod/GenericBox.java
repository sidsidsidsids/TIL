package Test07_genericMethod;

// 다양한 타입을 처리할 수 있도록 타입 파라미터가 있어야 함  
public class GenericBox<T> {
	// T는 타입처럼 사용 가능  
	private T data;
	
	// generic method with type param
	public <K> void genericMethod(K k) {
		// use type param as type in method
		// generic method's type param limit in method
		// T : class's type param
		// K : method's type param
		System.out.println("T: "+ data.getClass().getName());
		System.out.println("K: "+ k.getClass().getName());
	}

	public T getData() {
		return data;
	}

	public void setData(T data) {
		this.data = data;
	}
	

}
