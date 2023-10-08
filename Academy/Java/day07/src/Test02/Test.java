package Test02;

public class Test {
	public static void main(String[] args) {
		// 인터페이스는 객체를 생성할 수 없지만 
		// 해당 인터페이스를 구현한 클래스로 객체 생성 가능  
		HDMI_output monitor = new Monitor();
		HDMI_output television = new Television();
		
		HDMI_input computer = new Computer();
		computer.setOutput(monitor);
		computer.setOutput(television);
		computer.show();
		
		HDMI_input supercomputer = new SuperComputer();
		supercomputer.setOutput(monitor);
		supercomputer.show();
		
		// 왜 인터페이스를 사용해야 할까 ? 
		// - 클래스(설계도)가 바뀔 때 마다 코드를 다시 고쳐야 하나 ?
		// - 인터페이스를 구현하기만 하면 어떤 클래스의 객체든 사용할 수 있다면 코드를 고칠 필요가 없음 
		
	}
}
