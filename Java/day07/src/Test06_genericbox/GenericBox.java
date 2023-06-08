package Test06_genericbox;

// 다양한 타입을 처리할 수 있도록 타입 파라미터가 있어야 함  
public class GenericBox<T> {
	// T는 타입처럼 사용 가능  
	private T data;

	public T getData() {
		return data;
	}

	public void setData(T data) {
		this.data = data;
	}
	

}
