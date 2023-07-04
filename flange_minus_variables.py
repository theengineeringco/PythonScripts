"""Variables to initiate in Flow:
fx = 1071 N
fy = 174.4 N
number_of_bolts = 4
"""

import math

# Loads, Dims and Mats

# Forces
# fx = 1071  # N, axial force due to centrepetal
# fy = 174.4  # N, lift force
force_flange = 41  # N, force on a small area of the TE due to twist (approx)

# Dims
bolt_size = 4  # mm
flange_thickness = 6  # mm
weld_thickness = 15  # mm
flange_width = 80  # mm
tearout_length = 16  # mm
# number_of_bolts = 4
length_smt_embed = 39  # mm, dist from Cl to SMT join with PUR
length_pu_embed = 41  # mm
length_weld = 40  # mm
flange_length = length_smt_embed + length_pu_embed + length_weld  # mm
insert_glue_area = 120 * 250 * 0.7 * 2  # mm2

# Mat Props
material_sf = 3  # Material Safety Factor
flange_yield = 145 / material_sf  # MPa, for 7075 with RF on mat props
flange_youngs_mod = 71000  # MPa, 117000 for copper
flange_shear = (
    flange_yield * material_sf * 0.65
)  # MPa, for ally only (www.royalmech.co.uk / Useful_Tables / Matter / shear_tensile.htm)
bolt_uts = 400 / material_sf  # MPa, with RF on mat props for 4.6 carbon steel bolt
insert_yield = 2 / material_sf  # MPa <-- need better number here
glue_shear = 20 / material_sf  # MPa <-- need better number here


# Bolt Bearing, Shear and Tear-out

# Bearing
bearing_area = bolt_size * flange_thickness * number_of_bolts  # mm2
bearing_stress = fx / bearing_area  # MPa
rf_bearing = flange_yield / bearing_stress

# Shear
shear_area = number_of_bolts * math.pi * (bolt_size / 2) ** 2  # mm2
bolt_stress = fx / shear_area  # MPa
rf_shear = bolt_uts / bolt_stress

# Tear-out
tear_out_area = tearout_length * flange_thickness * 2 * 3  # mm2
tear_out_stress = fx / tear_out_area  # MPa
rf_tear_out = flange_yield / tear_out_stress


# Flange BM, Axial and Cantileaver

# Bending
flange_bm = fy * length_smt_embed  # Nmm
flange_second_moment_area = (flange_width * (flange_thickness**3)) / 12  # mm4
flange_bending_stress = (
    flange_bm * (flange_thickness / 2) / flange_second_moment_area
)  # MPa
rf_flange_bending = flange_yield / flange_bending_stress

flange_bending_strain = flange_bending_stress / flange_youngs_mod

# Axial
flange_axial_stress = fx / (flange_width * flange_thickness)  # MPa
rf_flange_axial = flange_yield / flange_axial_stress

flange_axial_strain = flange_axial_stress / flange_youngs_mod
flange_elongation = (flange_axial_strain + flange_bending_strain) * flange_length
elongation_angle = math.degrees(math.atan(flange_elongation / (flange_thickness / 2)))
smt_separation = math.tan(elongation_angle) * 19  # mm, 19 is dist to SMT surface

# Cantileaver
flange_reaction = (flange_length * fy) / (length_pu_embed + length_weld)  # N
area_of_application = (
    flange_width * 2
)  # Width of application - essentially an arbitrary numner...
pu_reation_stress = flange_reaction / area_of_application
rf_pu_reaction = insert_yield / pu_reation_stress

# Pizza Paddle Glue Shear

flange_glue_stress = fx / ((length_pu_embed + length_weld) * flange_width * 2)  # MPa
rf_flange_glue = glue_shear / flange_glue_stress

# SMT Glue Shear

insert_glue_stress = fx / insert_glue_area  # MPa
rf_insert_glue = glue_shear / insert_glue_stress

# Hold In Insert Shear

hold_in_insert_stress = fx / ((weld_thickness - flange_thickness) * flange_width)  # MPa
rf_hold_in_insert = glue_shear / hold_in_insert_stress

# RF Check

rf_dict = {
    "RF Bearing": rf_bearing,
    "RF Shear": rf_shear,
    "RF Tear-out": rf_tear_out,
    "RF Flange Bending": rf_flange_bending,
    "RF Flange Axial": rf_flange_axial,
    "RF PU Reaction": rf_pu_reaction,
    "RF Flange Glue": rf_flange_glue,
    "RF Inseert Glue": rf_insert_glue,
    "RF Hold-In Insert": rf_hold_in_insert,
}

number_of_low_rfs = 0
for rf_key, rf_value in rf_dict.items():
    if rf_value < 1.5:
        print(f"Low RF: {rf_key} at {rf_value}")
        number_of_low_rfs += 1

print(f"Number of Low RFs: {number_of_low_rfs}")
