# Constants
M = float(input())
ta = int(input()) # K
cpr = int(input())
ti = int(input()) # K
de = float(input())
ce = float(input())
te = float(input())
ne = float(input())
bspr = float(input())
shc = float(input()) # kJ/kg · K
amw = int(input())

# Calculate airspeed
air_speed = M * ((1.4 * 287 * ta) ** 0.5)
# Calculate diffuser exit temperature
diffuser_exit_temperature = ta + (air_speed ** 2) / (2 * 1005)
# Calculate compressor exit temperature
compressor_exit_temperature = diffuser_exit_temperature + ((cpr ** ((1 - 1 / ce))) - 1) * (ti -
diffuser_exit_temperature)
# Calculate turbine exit temperature
turbine_exit_temperature = ti - ((ti - compressor_exit_temperature) / te)
# Calculate nozzle exit temperature
nozzle_exit_temperature = turbine_exit_temperature - (turbine_exit_temperature / te)
# Calculate the thermal efficiency
thermal_efficiency = (((1 + bspr * de * ce * te * ne) * ti) - ta) / ((shc * 1000) * (ti -
diffuser_exit_temperature))
# Calculate the propulsion efficiency
propulsion_efficiency = (2 * air_speed / (M + 1)) * ((1 - (ta / nozzle_exit_temperature)) **
0.5)
print("Thermal Efficiency:", thermal_efficiency)
print("Propulsion Efficiency:", propulsion_efficiency)