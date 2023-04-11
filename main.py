from fastapi import FastAPI
from routes.employees_routes import employee_api_router

app = FastAPI() #creating instance of FastAPI library

app.include_router(employee_api_router)