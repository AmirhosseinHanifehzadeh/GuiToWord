import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout, QScrollArea, QGroupBox

class ContractGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Dictionary to store input values
        self.input_values = {}

        form_layout = QFormLayout()
        subject_group = QGroupBox("اطلاعات مربوط به درس")
        incharge_group = QGroupBox("اطلاعات مسئول درس")
        teacher_group = QGroupBox("اطلاعات مدرس / مدرسین")
        session1 = QGroupBox("جلسه اول")
        session2 = QGroupBox("جلسه دوم")
        session3 = QGroupBox("جلسه سوم")
        session4 = QGroupBox("جلسه چهارم")
        session5 = QGroupBox("جلسه پنجم")
        session6 = QGroupBox("جلسه ششم")
        session7 = QGroupBox("جلسه هفتم")
        session7 = QGroupBox("جلسه هشتم")

        

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
            'purpose2',
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
            'purpose3',
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
            'purpose4',
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
            'purpose5',
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
            'purpose6',
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
            'purpose7',
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
            'purpose7',
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

        labels_keys = [
            "lastUpdate",
            "subjectDescription",
        ]

        for 

        for key in labels_keys:
            label = QLabel(labels_text[key])
            line_edit = QLineEdit()

            # Save the QLineEdit widget in the dictionary with the corresponding label as the key
            self.input_values[key] = line_edit

            form_layout.addRow(label, line_edit)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container.setLayout(form_layout)
        scroll_area.setWidget(container)

        layout.addWidget(scroll_area)

        create_contract_button = QPushButton("Create Contract")
        create_contract_button.clicked.connect(self.create_contract)
        layout.addWidget(create_contract_button)

        self.setLayout(layout)
        self.setWindowTitle("Contract Generator")   

    def create_contract(self):
        # Access the entered values from the dictionary
        for label_text, line_edit in self.input_values.items():
            value = line_edit.text()
            print(f"{label_text}: {value}")

        # Implement the rest of the contract creation logic here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContractGenerator()
    window.show()
    sys.exit(app.exec_())
