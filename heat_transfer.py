"""
in: flow_velocity 5
out: total_heat_transfer
out: injector_plate_dia
out: injector_ports
"""

import math

# Constants
g = 9.81  # m/s
rho = 1.225  # kg/m3

# Variables
# flow_velocity = 5  # m/s
rpm = 10
power = 8000  # W

# Data
speed_list = [6.8, 6.0, 7.2, 7.3, 8.2, 9.0]
width_list = [0.8, 1.0, 1.5, 1.3, 1.2, 1.0]


# Functions
def forced_convection(speed_list, width_list):
    nussult_no = 0.71  # Constant
    re_no = [speed_list[i] * width_list[i] / nussult_no for i in range(5)]
    return re_no


# Main calculation
re_no = forced_convection(speed_list, width_list)

heat_transfer = []
for i in range(5):
    heat_transfer.append(2 * re_no[i] * rho * flow_velocity)


total_heat_transfer = sum(heat_transfer)

heat_transfer_density = 0.0016  # kW/mm2
injector_plate_area = total_heat_transfer / heat_transfer_density
injectior_plate_dia = math.ceil(math.sqrt(injector_plate_area) * 2 / math.pi)
port_diameter = math.ceil(injectior_plate_dia / 100)
port_spacing = 4  # number per 100 mm
injector_ports = math.ceil((injectior_plate_dia / port_spacing) * 6)

print(total_heat_transfer)
