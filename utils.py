from constants import bmi_category, health_risk

def calculate_bmi(mass_kg, height_in_cm):
    converted_height = (int(height_in_cm)/100)**2
    return round(int(mass_kg)/converted_height,2)

def calculate_health_risk(bmi):
    category= None
    risk= None
    if bmi <= 18.4 :
        category = bmi_category.get('UW')
        risk = health_risk.get('MR')
    elif bmi >=18.5 and bmi <= 24.9:
        category = bmi_category.get('NW')
        risk = health_risk.get('LR')
    elif bmi >=25 and bmi <= 29.9:
        category = bmi_category.get("OW")
        risk = health_risk.get('ER')
    elif bmi >=30 and bmi <= 34.9:
        category = bmi_category.get("MO")
        risk = health_risk.get('MRS')
    elif bmi >= 35 and bmi <= 39.9:
        category = bmi_category.get("SO")
        risk = health_risk.get('HR')
    elif bmi > 40:
        category = bmi_category.get("VSO")
        risk = health_risk.get('VHR')
    bmi_list =[category,bmi,risk]
    return bmi_list