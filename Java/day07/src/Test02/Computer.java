package Test02;

public class Computer implements HDMI_input{

	private HDMI_output outputDevice;
	
	@Override
	public void setOutput(HDMI_output device) {
		outputDevice = device;
		
	}

	@Override
	public void show() {
		// TODO Auto-generated method stub
		System.out.println("computer display");
		outputDevice.output();
	}

}
