# Gui-pwm-controller
### Summary
Pwm signal was generated with Stm32F100RB and controlled with the designed interface. The interface design was carried out with Qt Designer. The interface was developed with pyqt5. The HAL library was used for the development of stm32. Keil uVision5 chosen as the IDE. <br/> 
### Interface
The interface was developed with Qt and pyqt5. Developed with user-friendly and error messages in mind. For a quick start, there is an Pwm_Controller_exe extension of the interface in the bist folder inside the exe folder.There are 2 options for setting the duty cycle of the pwm signal. The duty cycle is controlled in seconds or percentiles. <br/>  Specifications:
 - Com port selection 
 - Baud rate selection 
 - Pwm frequency control 
 - Pulse width control(sn or ms)
 - Duty cycle control(Percent)
<img align="center" src="https://user-images.githubusercontent.com/62069736/131516151-5cfb2f01-3823-4955-82db-d35ca1e82822.png" /><br/>

### Stm32F100RB
Communication with the interface was carried out with uart. Data loss is prevented in serial communication with Uart dma. PWM is produced by TIM2. Its initial value is 1 kHz. There are address bytes for classification of incoming data.<br/> 
![VID_20210813_174932](https://user-images.githubusercontent.com/62069736/131518208-54c1a644-11c5-4656-899d-9c40b728ee75.gif)

