
def employee_serializer(employee) -> dict:
    return {
        "id" : str(employee["_id"]),
        "name" : employee["name"],
        "joining_date" : employee["joining_date"],
        "unit" : employee["unit"],
        "employeed" : employee["employeed"],
        #"joining_month" : employee["joining_month"]
    }

def employees_serializer(employees) -> list:
    return [employee_serializer(employee) for employee in employees]