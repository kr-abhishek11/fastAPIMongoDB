from fastapi import APIRouter
from datetime import datetime
import calendar

from config.database import collection_name
from models.employees_model import Employee
from bson import ObjectId
from schemas.employees_schema import employees_serializer, employee_serializer

employee_api_router = APIRouter()
# creating instance of APIRouter class

#retrive
@employee_api_router.get("/")
async def get_employees():
    employees = employees_serializer(collection_name.find())
    return {"status":"OK", "data": employees}

# searching an employee based on employee name
@employee_api_router.get("/{name}", response_model= Employee)
async def get_employee(name: str):
    result = collection_name.find_one({'name': name})
    return result

#searching an employee based on joining month
@employee_api_router.get("/{joining_month}", response_model= Employee)
async def get_employee(joining_month: str ):
    employees = employees_serializer(collection_name.find())
    emplyee_dict = dict(employees)
    for month in emplyee_dict.values():
        if month == joining_month:
            return {"Status":"Ok", "data":emplyee_dict}
        else:
            return {"Status":"Ok", "data":"No employee had joined this month"}

# post
@employee_api_router.post("/")
async def create_employee(employee: Employee):
    employee_dict = dict(employee)
    date_time_obj = datetime.strptime(employee_dict.get('joining_date'), "%d-%m-%Y")
    month = date_time_obj.month
    joining_month = calendar.month_name[month]
    employee_dict['joining_month'] = joining_month
    _id = collection_name.insert_one(employee_dict)
    return employees_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@employee_api_router.put("/{id}")
async def update_employee(id: str, employee: Employee):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(employee)
    })
    employee_dict = dict(employee)
    date_time_obj = datetime.strptime(employee_dict.get('joining_date'), "%d-%m-%Y")
    month = date_time_obj.month
    joining_month = calendar.month_name[month]
    if joining_month in ["January","February","March"]:
        employee_dict['joining_month'] = joining_month
        _id = collection_name.insert_one(employee_dict)
        employee = employees_serializer(collection_name.find({"_id":ObjectId(id)}))
        return {"Status":"Ok","data": employee}
    else:
        return {"Status":"Ok","Response":"Employee joined apart from Jan-Mar can't be updated"}
    
# delete
@employee_api_router.delete("/{id}")
async def delete_employee(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
