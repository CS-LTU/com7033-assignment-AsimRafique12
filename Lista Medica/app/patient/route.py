from flask import Blueprint, request, redirect, url_for, render_template, flash
from app.models.patient import create_patient
from app import mongo

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/patients', methods=['GET'])
def list_patients():
    patients = mongo.db.patients.find()
    return render_template('patient/list.html', patients=patients)

@patient_bp.route('/patients/create', methods=['GET', 'POST'])
def create_patient_view():
    if request.method == 'POST':
        patient_data = {
            'patient_id': request.form.get('patient_id'),
            'age': int(request.form.get('age')),
            'gender': request.form.get('gender'),
            'medical_data': request.form.get('medical_data')
        }
        mongo.db.patients.insert_one(patient_data)
        flash('Patient created successfully.')
        return redirect(url_for('patient.list_patients'))
    return render_template('patient/create.html')

# Similar views can be created for update and delete operations.