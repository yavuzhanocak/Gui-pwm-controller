# Gui-pwm-controller
### Summary
Pwm signal was generated with Stm32F100RB and controlled with the designed interface. The interface design was carried out with Qt Designer. The interface was developed with pyqt5. The HAL library was used for the development of stm32. Keil uVision5 chosen as the IDE. <br/> 
### Interface
The interface was developed with Qt and pyqt5. Developed with user-friendly and error messages in mind. For a quick start, there is an Pwm_Controller_exe extension of the interface in the bist folder inside the exe folder.There are 2 options for setting the duty cycle of the pwm signal. The duty cycle is controlled in seconds or percentiles. <br/>  Specifications:
-Com port selection 
-Baud rate selection 
-Pwm frequency control 
-Pulse width control(sn or ms)
-Duty cycle control(Percent)
