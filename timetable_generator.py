import PyPDF2

def extract_pdf_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

def generate_dummy_timetable(subjects, num_periods, duration, start_time, unavailable_teachers=[]):
    # Dummy timetable generation logic with breaks and time slots
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    timetable = {}

    # Breaks
    break_time = 10  # 10-minute break after every 2 classes
    
    for i, day in enumerate(days):
        timetable[day] = []
        class_start_time = start_time
        for j in range(num_periods):
            if j % 2 == 0 and j > 0:
                timetable[day].append(f"Break ({break_time} mins)")
            else:
                subject_index = (i + j) % len(subjects)
                timetable[day].append(subjects[subject_index])

    return timetable
