import matplotlib.pyplot as plt
import datetime
import os

def plot_results(test_cases, results):
    """Plot the results using matplotlib."""
    plt.bar(test_cases, results)
    plt.xlabel('Test Cases')
    plt.ylabel('Results')
    plt.title('Test Cases Results')
    plt.show()
# calculate
def calculate_area(x, y):
    return x * y

def generate_test_case(x, y, test_type):
    if test_type == 'BVA':
        return [x, y]
    elif test_type == 'Worse case':
        return [x, y]
    elif test_type == 'Robustness':
        return [x - 1, y + 1]
    elif test_type == 'Worse Case Robustness':
        return [x - 1, y + 1]
    else:
        print("Invalid")
# write test case
def write_test_case_to_file(file_name, test_case, expected_result):
    """Write the test case and expected result to a file."""
    now = datetime.datetime.now()
    file_name_with_datetime = f"{file_name}_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(file_name_with_datetime, 'w') as file:
        file.write(f"X,Y,Expected Result\n")
        file.write(f"Test Case: {test_case}\n")
        file.write(f"Expected Result: {expected_result}\n")
        file.write(f"Time: {now}\n")

    print(f"Test case has been written to {file_name}")

def get_user_input():
    """Get user input for X, Y, test type, and file name."""
    x = int(input("Enter X (4 <= X <= 10): "))
    y = int(input("Enter Y (8 <= Y <= 12): "))
    test_type = input("Enter test type (BVA, Worse case, Robustness, Worse Case Robustness): ")
    file_name = input("Enter file name: ")

    return x, y, test_type, file_name

def main():
    x, y, test_type, file_name = get_user_input()

    test_case = generate_test_case(x, y, test_type)
    expected_result = calculate_area(*test_case)

    write_test_case_to_file(file_name, test_case, expected_result)

    test_cases = ['BVA', 'Worse Case', 'Robustness', 'Worse Case Robustness']
    results = [calculate_area(*generate_test_case(x, y, test_case)) for test_case in test_cases]

    plot_results(test_cases, results)

if __name__ == "__main__":
    main()
