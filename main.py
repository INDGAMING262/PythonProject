from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def create_timetable(data, filename, title=None):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    table_data = []

    if title:
        title_table = Table([[title]])
        table_data.append([title])  # Add title to the data

    for row in data:
        table_data.append(row)


    timetable = Table(table_data)

    # frame = Frame(100, 500, 500, 500)
    # frame.addFromList([timetable], doc)                        #not working see in next update
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('BACKGROUND', (0, 1), (-1, 1), colors.lightblue),
                        ('TEXTCOLOR', (0, 1), (0, -1), colors.black),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 2), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('SPAN', (0, 0), (-1, 0))])
    timetable.setStyle(style)

    doc.build([timetable])

def get_timetable_data():

    num_subjects = int(input("Enter the number of subjects for each day: "))
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    timetable_data = []
    timetable_data = [['Day'] + list(range(1,num_subjects+1))]
    for day in days:
        subjects = [input(f"Enter subject {i+1} for {day}: ") for i in range(num_subjects)]
        timetable_data.append([day] + subjects)

    return timetable_data

title = input("Enter the title for the timetable (leave empty for no title): ")

timetable_data = get_timetable_data()

test=input("Are you Give name of your PDF file Y/N: ")
if test.upper()=="Y":
    output_filename = input("Enter your file name: ")
    output_filename = output_filename + ".pdf"
else:
    output_filename = "timetable.pdf"


create_timetable(timetable_data, output_filename, title)

print(f"Timetable created successfully: {output_filename}")
