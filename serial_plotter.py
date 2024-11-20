import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

numPoints = 100

# Initialize serial connection
ser = serial.Serial("COM22", 9600)
time.sleep(2)  # Wait for the serial connection to initialize

# Initialize lists to store data
x_vals = []
y_vals = []

# Create figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')

# Set up plot to call animate() function periodically
def animate(i):
    global x_vals, y_vals  # Declare x_vals and y_vals as global
    # Read data from serial
    while ser.in_waiting:
        arduinoData_string = ser.readline().decode('utf-8').strip()

    if arduinoData_string:
        try:
            currentTime, value = map(float, arduinoData_string.split())
            x_vals.append(currentTime)
            y_vals.append(value)

            x_vals = x_vals[-numPoints:]
            y_vals = y_vals[-numPoints:]
            
            # Update line data
            line.set_data(x_vals, y_vals)
            ax.relim()
            ax.autoscale_view()
        except ValueError:
            pass

    return line,

ani = animation.FuncAnimation(fig, animate, interval=10, blit=False, save_count=numPoints)
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('Live Plot of Serial Data')
plt.show()