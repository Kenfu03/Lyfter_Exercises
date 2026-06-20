employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

deparments = {}

for employee in employees:
    deparment = employee.get("department")
    if deparment not in deparments:
        deparments[deparment] = [employee]
    else:
        deparments[deparment].append(employee)

print(deparments)