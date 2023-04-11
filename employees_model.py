from pydantic import BaseModel
from pydantic.schema import Optional

class Employee(BaseModel):
    name : str
    id : int
    joining_date : Optional[str]
    unit : Optional[str]
    employeed : bool
    joining_month : Optional[str]