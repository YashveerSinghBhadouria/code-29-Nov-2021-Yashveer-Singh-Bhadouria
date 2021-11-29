import csv
from utils import calculate_bmi,calculate_health_risk

def read_data():
    data_list = []
    with open('bmi_cal_data.csv') as file:
        raw_data = csv.reader(file)
        for row in raw_data:
            data_list.append(row)
        return data_list

def process_data(data):
    row_count = 0
    valid_data = []
    invalid_data = []
    for row in data:
        if row_count == 0:
            if 'Gender' not in row[0] or 'Height' not in row[1] or 'Weight' not in row[2]:
                return 'Wrong Data Table'
            row_count = 1
        elif row[0].isalpha() == True and row[1].isnumeric() == True and row[2].isnumeric() == True :
            bmi = calculate_bmi(row[2], row[1])
            health_risk = calculate_health_risk(bmi)
            valid_data.append(row+health_risk)
            row_count +=1
        else:
            invalid_data.append(row)
            row_count +=1
    return valid_data

def update_csv(data):
    with open('bmi_calculated_height_weight.csv', 'w',newline='') as file:
        csv_data = csv.writer(file, delimiter=',')
        csv_data.writerow(['Gender', 'Height', 'Weight', 'BMI category', 'BMI range', 'Health risk'])
        for row in data:
            csv_data.writerows([row])
    return 'file updatd successfully'

    
if __name__ == '__main__':
    data = read_data()
    # print(data)
    calculated_bmi_data = process_data(data)
    # print(calculated_bmi_data)
    update_data = update_csv(calculated_bmi_data)
    # print(update_data)
    