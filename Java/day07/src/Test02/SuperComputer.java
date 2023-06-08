package Test02;

public class SuperComputer implements HDMI_input{
	
	private HDMI_output device;
	
	@Override
	public void setOutput(HDMI_output device) {
		// TODO Auto-generated method stub
		this.device = device;
	}

	@Override
	public void show() {
		// TODO Auto-generated method stub
		System.out.println("SuperComputer display");
		device.output();
	}

}
