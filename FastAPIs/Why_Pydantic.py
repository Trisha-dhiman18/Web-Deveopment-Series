from pydantic import BaseModel , EmailStr , AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name : Annotated[str, Field(max_length = 50, title = "Patient Name", description = "Give the Name of the patient in less than 50 characters", examples = ["John Doe", "Jane Smith"])]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt = 0 , lt = 120 ) 
    weight : Annotated[float, Field(gt = 0)]
    married : Annotated[bool, Field(default = None ,title = "Marital Status", description = "Indicates if the patient is married")]
    allergies : Annotated[Optional[List[str]], Field(default = None, max_length = 5)]
    contact : Dict[str, str]
def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("Inserted patient data successfully")

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("Updated patient data successfully")
    
patient1 = Patient(name="John Doe", email="john.doe@example.com", linkedin_url="https://www.linkedin.com/in/johndoe", age=30, weight=
                   70.5, married=True, allergies=["pollen", "nuts"], contact={"phone": "123-456-7890"})
update_patient_data(patient1)