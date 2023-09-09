**Q1: If the Sensor is surrounded by a noisy environment, what type of filter could be used and what is the recommended cutoff frequency depending on the sensor MPU6050 datasheet?**

The MPU6050 datasheet recommends using a low-pass filter to reduce high-frequency noise. The low-pass filter is implemented within the sensor itself and can be configured to attenuate frequencies above a certain cutoff frequency.

According to the MPU6050 datasheet, the recommended cutoff frequency for the low-pass filter can be set to one of the following values: 5 Hz, 10 Hz, 20 Hz, 42 Hz, 98 Hz, or 188 Hz. The specific cutoff frequency to use depends on the requirements of your application.

To select the appropriate cutoff frequency, consider the following factors:
1. The nature and frequency content of the noise in the environment.
2. The desired trade-off between noise reduction and responsiveness to changes in motion.
3. The bandwidth of the motion you are interested in capturing accurately.


**Q2: We need to design a Software Practical Low Pass Filter (LPF) what is the proper cutoff frequency (fc) If WALL-E has Specs:
o Encoder has 540 pulse per revolution
o Track has three wheels only one motorized, with 40cm diameter, (The one that has encoder)
o And Maximum speed of WALL-E 0.5 m/s**

Calculate the maximum rotational speed of the motorized wheel then maximum angular velocity then determine the maximum frequency component in the signal and finally set the cutoff frequency (fc) of the LPF:

Circumference of the wheel: C = π * 40 cm = 125.6 cm = 1.256 m
Maximum rotational speed: ω = 0.5 m/s / 1.256 m = 0.398 Hz
Maximum angular velocity: ω_radians = ω * 2π = 0.398 Hz * 2π = 2.5 radians/s
The maximum frequency component is the same as the maximum angular velocity: 2.5 radians/s
Cutoff frequency (fc) = Maximum frequency component * (1 + 0.1) (10% higher)
fc = 2.5 radians/s * 1.1 ≈ 2.75 radians/s
