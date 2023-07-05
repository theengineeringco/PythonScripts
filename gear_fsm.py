# Get the data from each import
rpm = [
    1000,
    2000,
    3000,
    4000,
    5000,
    6000,
    7000,
    8000,
    7000,
    6000,
    5000,
    6000,
    6000,
    6000,
    5000,
    4000,
]
time_steps = list(range(1, len(rpm)))
t_wait = 0.5
upshift_rpm = 5000
downshift_rpm = 6000

# Component Content
gear = []

# Initialise shift flags
flag_for_change_up = False
flag_for_change_down = False
max_gear = 2
min_gear = 1

# How long is a time step
if len(time_steps) >= 2:
    time_step_difference = time_steps[1] - time_steps[0]
else:
    time_step_difference = 1

# Check t_wait is shorter than a time step
if t_wait > time_step_difference:
    print("T-Wait must be less than or equal to the time difference between time steps")

for i, item in enumerate(time_steps):
    # Values for first time step
    if i == 0:
        prev_gear = 1
        prev_rpm = 0
    else:
        prev_gear = gear[i - 1]
        prev_rpm = rpm[i - 1]

    # Set shift flags
    if t_wait <= 0.5 * time_step_difference:  # Flag for change at current time step
        if rpm[i] > upshift_rpm and prev_rpm <= upshift_rpm:
            flag_for_change_up = True
        elif rpm[i] <= downshift_rpm and prev_rpm > downshift_rpm:
            flag_for_change_down = True

    # This time step will hold the pervious gear unless a flag for change is set
    if flag_for_change_up is False and flag_for_change_down is False:
        gear.append(prev_gear)
    elif flag_for_change_up is True and flag_for_change_down is False:
        if prev_gear == max_gear:
            gear.append(prev_gear)
        else:
            gear.append(prev_gear + 1)
    elif flag_for_change_up is False and flag_for_change_down is True:
        if prev_gear == min_gear:
            gear.append(prev_gear)
        else:
            gear.append(prev_gear - 1)
    else:
        print("You cannot change up and down on the same time step")

    # Reset shift flags
    flag_for_change_up = False
    flag_for_change_down = False

    # Set shift flags
    if t_wait > 0.5 * time_step_difference:  # Flag for change at next time step
        if rpm[i] > upshift_rpm and prev_rpm <= upshift_rpm:
            flag_for_change_up = True
        elif rpm[i] <= downshift_rpm and prev_rpm > downshift_rpm:
            flag_for_change_down = True

output = list(zip(rpm, gear))
print(output)
steps_gear_1 = gear.count(1)
steps_gear_2 = gear.count(2)
print(steps_gear_1)
print(steps_gear_2)
