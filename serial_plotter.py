import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

numPoints = 100  # Number of data points to display
port = "COM22"

# Initialize serial connection
ser = serial.Serial(port, 9600)  # Replace "COM22" with your actual COM port
time.sleep(2)  # Wait for the serial connection to initialize

# Initialize lists to store data
x_vals = []
y_vals = []

# Create figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')  # Initialize an empty line plot with red color

# Set up plot to call animate() function periodically
def animate(i):
    global x_vals, y_vals  # Declare x_vals and y_vals as global
    
    # Read all available lines from serial
    while ser.in_waiting:
        arduinoData_string = ser.readline().decode('utf-8').strip()
    
    # Process the most recent line
    if arduinoData_string:
        try:
            currentTime, value = map(float, arduinoData_string.split())
            x_vals.append(currentTime)
            y_vals.append(value)

            # Keep only the last 100 data points
            x_vals = x_vals[-numPoints:]
            y_vals = y_vals[-numPoints:]
            
            # Update line data
            line.set_data(x_vals, y_vals)
            ax.relim()  # Recalculate limits
            ax.autoscale_view()  # Autoscale the view
        except ValueError:
            pass

    return line,

# Enable frame caching with a specified save_count
ani = animation.FuncAnimation(fig, animate, interval=10, blit=False, save_count=numPoints)

plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('Live Plot of Serial Data')
plt.show()