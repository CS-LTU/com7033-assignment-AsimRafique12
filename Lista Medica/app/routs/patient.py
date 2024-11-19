from flask import render_template, redirect, url_for, request
from app import app, mongo
from flask_login import login_required

@app.route('/patients')
@login_required  # Ensure only logged-in users can access this page
def list_patients():
    # Fetch all patients from MongoDB
    patients = mongo.db.patients.find()
    return render_template('patient/list.html', patients=patients)

@app.route('/patients/create', methods=['GET', 'POST'])
@login_required
def create_patient():
    if request.method == 'POST':
        # Get form data
        patient_id = request.form['patient_id']
        age = int(request.form['age'])
        gender = request.form['gender']
        medical_data = request.form['medical_data']
        
        # Insert into MongoDB collection
        mongo.db.patients.insert_one({
            'patient_id': patient_id,
            'age': age,
            'gender': gender,
            'medical_data': medical_data
        })
        return redirect(url_for('patient.list_patients'))
    
    return render_template('patient/create.html')