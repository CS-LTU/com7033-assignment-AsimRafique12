from flask_pymongo import PyMongo
mongo = PyMongo()

# Patient schema is not typically created like a model in MongoDB, 
# but we can define a dictionary to structure data.
def create_patient(patient_id, age, gender, medical_data, created_by):
    patient = {
        'patient_id': patient_id,
        'age': age,
        'gender': gender,
        'medical_data': medical_data,
        'created_by': created_by
    }
    return patient