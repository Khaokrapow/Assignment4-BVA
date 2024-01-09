import matplotlib.pyplot as plt
import datetime
import os
import random

def calculate_area_index(x, y, num, index, file):
    area = 0
    if num == 1:
        x = x - 1
        y = y + 1
    elif num == 2:
        x = x
        y = y + 1
    elif num == 3:
        x = x + 1
        y = y + 1
    elif num == 4:
        x = x - 1
        y = y
    elif num == 5:
        x = x
        y = y
    elif num == 6:
        x = x + 1
        y = y
    elif num == 7:
        x = x - 1
        y = y - 1
    elif num == 8:
        x = x
        y = y - 1
    elif num == 9:
        x = x + 1
        y = y - 1

    area = x * y
    index += 1
    file.write(f"TC{index}({x}, {y}, {area})\n")
    return index
# x 4-8 y8-12
def generate_test_case(test_type, file): 
    index = 0
    if test_type == 'BVA':  # 4n+1 กลางขอบใน
        #บนกลาง
        index = calculate_area_index(6, 12, 5, index, file)
        index = calculate_area_index(6, 12, 8, index, file)
        #ซ้ายกลาง
        index = calculate_area_index(4, 10, 5, index, file)
        index = calculate_area_index(4, 10, 6, index, file)
        #กลาง
        index = calculate_area_index(6, 10, 5, index, file)
        #ขวากลาง
        index = calculate_area_index(8, 10, 5, index, file)
        index = calculate_area_index(8, 10, 4, index, file)
        #ล่างกลาง
        index = calculate_area_index(6, 8, 5, index, file)
        index = calculate_area_index(6, 8, 2, index, file)
    elif test_type == 'Worse Case':  # 6n+1 กลางขอบนอก
        #บนกลาง
        index = calculate_area_index(6, 12, 2, index, file)
        index = calculate_area_index(6, 12, 5, index, file)
        index = calculate_area_index(6, 12, 8, index, file)
        #ซ้ายกลาง
        index = calculate_area_index(4, 10, 4, index, file)
        index = calculate_area_index(4, 10, 5, index, file)
        index = calculate_area_index(4, 10, 6, index, file)
        #กลาง
        index = calculate_area_index(6, 10, 5, index, file)
        #ขวากลาง
        index = calculate_area_index(8, 10, 6, index, file)
        index = calculate_area_index(8, 10, 5, index, file)
        index = calculate_area_index(8, 10, 4, index, file)
        #ล่างกลาง
        index = calculate_area_index(6, 8, 8, index, file)
        index = calculate_area_index(6, 8, 5, index, file)
        index = calculate_area_index(6, 8, 2, index, file)

    elif test_type == 'Robustness':  # 5^n รอบขอบใน
        #ซ้ายบน
        index = calculate_area_index(4, 12, 5, index, file)
        index = calculate_area_index(4, 12, 6, index, file)
        index = calculate_area_index(4, 12, 8, index, file)
        index = calculate_area_index(4, 12, 9, index, file)
        #บนกลาง
        index = calculate_area_index(6, 12, 5, index, file)
        index = calculate_area_index(6, 12, 8, index, file)
        #ขวาบน
        index = calculate_area_index(8, 12, 4, index, file)
        index = calculate_area_index(8, 12, 5, index, file)
        index = calculate_area_index(8, 12, 7, index, file)
        index = calculate_area_index(8, 12, 8, index, file)
        #ซ้ายกลาง
        index = calculate_area_index(4, 10, 5, index, file)
        index = calculate_area_index(4, 10, 6, index, file)
        #กลาง
        index = calculate_area_index(6, 10, 5, index, file)
        #ขวากลาง
        index = calculate_area_index(8, 10, 5, index, file)
        index = calculate_area_index(8, 10, 4, index, file)
        #ซ้ายล่าง
        index = calculate_area_index(4, 8, 2, index, file)
        index = calculate_area_index(4, 8, 3, index, file)
        index = calculate_area_index(4, 8, 5, index, file)
        index = calculate_area_index(4, 8, 6, index, file)
        #ล่างกลาง
        index = calculate_area_index(6, 8, 5, index, file)
        index = calculate_area_index(6, 8, 2, index, file)
        #ขวาล่าง
        index = calculate_area_index(8, 8, 1, index, file)
        index = calculate_area_index(8, 8, 2, index, file)
        index = calculate_area_index(8, 8, 4, index, file)
        index = calculate_area_index(8, 8, 5, index, file)

    elif test_type == 'Worse Case Robustness':  # 7^n รอบขอบนอก
         #ซ้ายบน
        for i in range(1, 10, 1):
            index = calculate_area_index(4, 12, i, index, file)
        
        #บนกลาง
        index = calculate_area_index(6, 12, 5, index, file)
        index = calculate_area_index(6, 12, 8, index, file)
        #ขวาบน
        for i in range(1, 10, 1):
            index = calculate_area_index(8, 12, i, index, file)
        #ซ้ายกลาง
        index = calculate_area_index(4, 10, 5, index, file)
        index = calculate_area_index(4, 10, 6, index, file)
        #กลาง
        index = calculate_area_index(6, 10, 5, index, file)
        #ขวากลาง
        index = calculate_area_index(8, 10, 5, index, file)
        index = calculate_area_index(8, 10, 4, index, file)
        #ซ้ายล่าง
        for i in range(1, 10, 1):
            index = calculate_area_index(4, 8, i, index, file)
        #ล่างกลาง
        index = calculate_area_index(6, 8, 5, index, file)
        index = calculate_area_index(6, 8, 2, index, file)
        #ขวาล่าง
        for i in range(1, 10, 1):
            index = calculate_area_index(8, 8, i, index, file)

def write_test_case_to_file(file_name,test_type):
    now = datetime.datetime.now()
    file_name_with_datetime = f"{file_name}_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    file_path = os.path.join("TestCase", file_name_with_datetime)

    with open(file_path, 'w') as file:
        file.write(f"Test Cases for {file_name} - {now}\n")

        generate_test_case(test_type,file)


    print(f"---Test cases have been written to {file_path}---")

def get_user_input():
    test_type = input("Enter test type (BVA, Worse Case, Robustness, Worse Case Robustness): ")
    file_name = input("Enter file name: ")

    return test_type, file_name

def main():
    test_type, file_name = get_user_input()

    write_test_case_to_file(file_name,test_type)

if __name__ == "__main__":
    main()
