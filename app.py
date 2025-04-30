from flask import Flask, render_template, request, send_from_directory
import os
from werkzeug.utils import secure_filename
from utils.timetable_generator import generate_dummy_timetable, extract_pdf_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['GENERATED_FOLDER'] = 'generated_tts'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['GENERATED_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    pdf = request.files['pdf']
    teachers = request.form.getlist('teacher[]')
    subjects = request.form.getlist('subject[]')
    year = request.form.get('year')
    start_time = request.form.get('class_start_time')
    duration = int(request.form.get('class_duration'))
    num_periods = int(request.form.get('num_periods'))

    filename = secure_filename(pdf.filename)
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    pdf.save(pdf_path)

    # Extract text from the PDF and generate a summary
    pdf_text = extract_pdf_text(pdf_path)
    summary = "Summary: " + pdf_text[:500]  # Just a snippet for display
    
    timetable = generate_dummy_timetable(subjects, num_periods, duration, start_time)

    return render_template('timetable.html', timetable=timetable, summary=summary, pdf_path=pdf_path)

@app.route('/regenerate', methods=['POST'])
def regenerate():
    unavailable_teachers = request.form.getlist('unavailable_teachers[]')
    timetable_path = request.form.get('timetable_path')
    
    # Regenerate timetable based on teacher availability
    timetable = generate_dummy_timetable(unavailable_teachers=unavailable_teachers)
    
    return render_template('timetable.html', timetable=timetable, regenerate=True)

if __name__ == '__main__':
    app.run(debug=True)
