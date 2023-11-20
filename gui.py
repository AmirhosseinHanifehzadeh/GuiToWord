import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout, QScrollArea, QGroupBox
from main import save_doc

class ContractGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Dictionary to store input values
        self.input_values = {}

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Central container to hold all the groups
        container = QWidget()
        container_layout = QVBoxLayout(container)

        subject_group = QGroupBox("اطلاعات مربوط به درس")
        subject_group_layout = QFormLayout(subject_group)
        incharge_group = QGroupBox("اطلاعات مسئول درس")
        incharge_group_layout = QFormLayout(incharge_group)
        teacher_group = QGroupBox("اطلاعات مدرس / مدرسین")
        teacher_group_layout = QFormLayout(teacher_group)
        session1 = QGroupBox("جلسه اول")
        session1_layout = QFormLayout(session1)
        session2 = QGroupBox("جلسه دوم")
        session2_layout = QFormLayout(session2)
        session3 = QGroupBox("جلسه سوم")
        session3_layout = QFormLayout(session3)
        session4 = QGroupBox("جلسه چهارم")
        session4_layout = QFormLayout(session4)
        session5 = QGroupBox("جلسه پنجم")
        session5_layout = QFormLayout(session5)
        session6 = QGroupBox("جلسه ششم")
        session6_layout = QFormLayout(session6)
        session7 = QGroupBox("جلسه هفتم")
        session7_layout = QFormLayout(session7)
        session8 = QGroupBox("جلسه هشتم")
        session8_layout = QFormLayout(session8)

        labels_text = {
            'providedTrainingGroup': 'خدمات گروه آموزشی',
            "subject": 'نام درس',
            "category": "نوع و تعداد واحد",
            "prerequisite": "پیش نیاز / هم نیاز",
            "field": "رشته و مقطع تحصیلی", 
            "courseLocation": "رشته و مقاطع تحصیلی",
            "courseTime": "محل برگزاری دوره",
            "inchargeName": "روز و ساعت کلاس",
            "incharge": "نام و مسئول درس",
            "inchargeField": "رتبه علمی",
            "officeLocation": "رشته تحصیلی",
            "inchargePhone": "محل کار",
            "inchargeEmail": "تلفن تماس",
            "teacherName": "پست الکترونیک",
            "teacherRank": "نام مدرس / مدرسین همکار",
            "teacherEmail": "پست الکترونیک اساتید همکار",
            "teacherField": "رشته تحصیلی",
            "teacherLocation": "محل کار",
            "teacherPhone": "تلفن تماس",
            "lastUpdate": "تاریخ آخرین ویرایش",
            "subjectDescription": "شرح درس",
            'purpose1': "هدف کلی",
            'sp1': "هدف اختصاصی",
            'do1': "پیامد مورد انتظار",
            'a1': "نگرش",
            'k1': "دانش",
            's1': "مهارت",
            'ea1': "رویکرد آموزشی",
            'tm1': "روش یاددهی",
            'lm1': "روش یادگیری",
            'et1': "ابزار آموزشی",
            'em1': "روش ارزیابی",
            't1': "مدرس / مدرسین",
            'purpose2': "هدف کلی",
            'sp2':"هدف اختصاصی",
            'do2': "پیامد های مورد انتظار",
            'k2': "دانش",
            'a2': "نگرش",
            's2': "مهارت",
            'ea2': "رویکرد آموزشی",
            'tm2': "روش یاددهی",
            'lm2': "روش یادگیری",
            'et2': "ابزار آموزشی",
            'em2': "روش ارزیابی",
            't2': "مدرس / مدرسین",
            'purpose3': "هدف کلی",
            'sp3':"هدف اختصاصی",
            'do3': "پیامد های مورد انتظار",
            'k3': "دانش",
            'a3': "نگرش",
            's3': "مهارت",
            'ea3': "رویکرد آموزشی",
            'tm3': "روش یاددهی",
            'lm3': "روش یادگیری",
            'et3': "ابزار آموزشی",
            'em3': "روش ارزیابی",
            't3': "مدرس / مدرسین",
            'purpose4': "هدف کلی",
            'sp4':"هدف اختصاصی",
            'do4': "پیامد های مورد انتظار",
            'k4': "دانش",
            'a4': "نگرش",
            's4': "مهارت",
            'ea4': "رویکرد آموزشی",
            'tm4': "روش یاددهی",
            'lm4': "روش یادگیری",
            'et4': "ابزار آموزشی",
            'em4': "روش ارزیابی",
            't4': "مدرس / مدرسین",
            'purpose5': "هدف کلی",
            'sp5':"هدف اختصاصی",
            'do5': "پیامد های مورد انتظار",
            'k5': "دانش",
            'a5': "نگرش",
            's5': "مهارت",
            'ea5': "رویکرد آموزشی",
            'tm5': "روش یاددهی",
            'lm5': "روش یادگیری",
            'et5': "ابزار آموزشی",
            'em5': "روش ارزیابی",
            't5': "مدرس / مدرسین",
            'purpose6': "هدف کلی",
            'sp6':"هدف اختصاصی",
            'do6': "پیامد های مورد انتظار",
            'k6': "دانش",
            'a6': "نگرش",
            's6': "مهارت",
            'ea6': "رویکرد آموزشی",
            'tm6': "روش یاددهی",
            'lm6': "روش یادگیری",
            'et6': "ابزار آموزشی",
            'em6': "روش ارزیابی",
            't6': "مدرس / مدرسین",
            'purpose7': "هدف کلی",
            'sp7':"هدف اختصاصی",
            'do7': "پیامد های مورد انتظار",
            'k7': "دانش",
            'a7': "نگرش",
            's7': "مهارت",
            'ea7': "رویکرد آموزشی",
            'tm7': "روش یاددهی",
            'lm7': "روش یادگیری",
            'et7': "ابزار آموزشی",
            'em7': "روش ارزیابی",
            't7': "مدرس / مدرسین",
            'purpose8': "هدف کلی",
            'sp8':"هدف اختصاصی",
            'do8': "پیامد های مورد انتظار",
            'k8': "دانش",
            'a8': "نگرش",
            's8': "مهارت",
            'ea8': "رویکرد آموزشی",
            'tm8': "روش یاددهی",
            'lm8': "روش یادگیری",
            'et8': "ابزار آموزشی",
            'em8': "روش ارزیابی",
            't8': "مدرس / مدرسین"
        }

        subject_base_group = [
            "providedTrainingGroup",
            "subject",
            "category",
            "field",
            "prerequisite",
            "courseLocation",
            "courseTime",
        ]

        incharge_info_group = [
            "inchargeName",
            "incharge",
            "inchargeField",
            "officeLocation",
            "inchargePhone",
            "inchargeEmail",
        ]

        teacher_info_group = [
            "teacherName",
            "teacherRank",
            "teacherField",
            "teacherEmail",
            "teacherLocation",
            "teacherPhone"
        ]

        session1_info_group = [
            'purpose1' ,
            'sp1',
            'do1',
            'k1',
            'a1',
            's1',
            'ea1',
            'tm1',
            'lm1',
            'et1',
            'em1',
            't1',
        ]

        session2_info_group = [
            'purpose2' ,
            'sp2',
            'do2',
            'k2',
            'a2',
            's2',
            'ea2',
            'tm2',
            'lm2',
            'et2',
            'em2',
            't2',
        ]

        session3_info_group = [
            'purpose3' ,
            'sp3',
            'do3',
            'k3',
            'a3',
            's3',
            'ea3',
            'tm3',
            'lm3',
            'et3',
            'em3',
            't3',
        ]

        session4_info_group = [
            'purpose4' ,
            'sp4',
            'do4',
            'k4',
            'a4',
            's4',
            'ea4',
            'tm4',
            'lm4',
            'et4',
            'em4',
            't4',
        ]

        session5_info_group = [
            'purpose5' ,
            'sp5',
            'do5',
            'k5',
            'a5',
            's5',
            'ea5',
            'tm5',
            'lm5',
            'et5',
            'em5',
            't5',
        ]

        session6_info_group = [
            'purpose6' ,
            'sp6',
            'do6',
            'k6',
            'a6',
            's6',
            'ea6',
            'tm6',
            'lm6',
            'et6',
            'em6',
            't6',
        ]

        session7_info_group = [
            'purpose7' ,
            'sp7',
            'do7',
            'k7',
            'a7',
            's7',
            'ea7',
            'tm7',
            'lm7',
            'et7',
            'em7',
            't7',
        ]

        session8_info_group = [
            'purpose8' ,
            'sp8',
            'do8',
            'k8',
            'a8',
            's8',
            'ea8',
            'tm8',
            'lm8',
            'et8',
            'em8',
            't8',
        ]
        # ... (session2_info_group, session3_info_group, ..., session8_info_group)

        labels_keys = [
            "lastUpdate",
            "subjectDescription",
        ]

        for key in subject_base_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            subject_group_layout.addRow(label, line_edit)

        container_layout.addWidget(subject_group)

        for key in teacher_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            teacher_group_layout.addRow(label, line_edit)

        container_layout.addWidget(teacher_group)

        for key in incharge_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            incharge_group_layout.addRow(label, line_edit)

        container_layout.addWidget(incharge_group)

        for key in session1_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            session1_layout.addRow(label, line_edit)

        container_layout.addWidget(session1)

        for key in session2_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            session2_layout.addRow(label, line_edit)

        container_layout.addWidget(session2)


        for key in session3_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            session3_layout.addRow(label, line_edit)

        container_layout.addWidget(session3)


        for key in session4_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            session4_layout.addRow(label, line_edit)

        container_layout.addWidget(session4)


        for key in session5_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            session5_layout.addRow(label, line_edit)

        container_layout.addWidget(session5)


        for key in session6_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            session6_layout.addRow(label, line_edit)

        container_layout.addWidget(session6)


        for key in session7_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            session7_layout.addRow(label, line_edit)

        container_layout.addWidget(session7)


        for key in session8_info_group:
            label_text = labels_text[key]
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_values[key] = line_edit
            session8_layout.addRow(label, line_edit)

        container_layout.addWidget(session8)

        # ... (session2, session3, ..., session8)

        scroll_area.setWidget(container)
        layout.addWidget(scroll_area)

        create_contract_button = QPushButton("Create Contract")
        create_contract_button.clicked.connect(self.create_contract)
        layout.addWidget(create_contract_button)

        self.setLayout(layout)
        self.setWindowTitle("")   

    def create_contract(self):
        # Access the entered values from the dictionary
        for label_text, line_edit in self.input_values.items():
            value = line_edit.text()
            print(f"{label_text}: {value}")

        # Implement the rest of the contract creation logic here
        save_doc(self.input_values)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContractGenerator()
    window.show()
    sys.exit(app.exec_())
