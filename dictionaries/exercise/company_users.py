def add_employee_to_company(company_data: dict, name_of_company: str, employee: str) -> dict:
    if name_of_company not in company_data:
        company_data[name_of_company] = []
    if employee not in company_data[name_of_company]:
        company_data[name_of_company].append(employee)
    return company_data


def company_data_view(company_data: dict):
    for company, employee in company_data.items():
        print(f"{company}")
        for employee_id in employee:
            print(f"-- {employee_id}")


def main():
    company = {}
    while True:
        command = input()

        if command == "End":
            break

        company_name, employee_id = command.split(" -> ")
        company = add_employee_to_company(company, company_name, employee_id)

    company_data_view(company)


main()