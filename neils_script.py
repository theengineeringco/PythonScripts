
# Constants
g = 9.81  # m/s
rho = 1.225  # kg/m3

# Variables
ave_wind_speed = 5  # m/s
rpm = 10
power = 8000  # W

# Data
speed_list = [6.8, 6.0, 7.2, 7.3, 8.2, 9.0]
width_list = [0.8, 1.0, 1.2, 1.3, 1.2, 1.0]

# Functions
def forced_convection(speed_list, width_list):
    nussult_no = 0.71  # Constant
    re_no = [speed_list[i] * width_list[i] / nussult_no for i in range(5)]
    return re_no


# Main calculation
re_no = forced_convection(speed_list, width_list)

heat_transfer = []
for i in range(5):
    heat_transfer.append(2 * re_no[i] * rho * ave_wind_speed)


total_heat_transfer = sum(heat_transfer)

print(total_heat_transfer)

