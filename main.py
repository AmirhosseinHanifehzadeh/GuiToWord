from pathlib import Path
from docxtpl import DocxTemplate
from base64 import b64decode
from io import BytesIO


def get_embedded_template():
    with open("base64_file.txt", "r") as file:
        encoded_template = file.read()
    return b64decode(encoded_template)


def write_template_file(template_content):
    temp_path = Path(__file__).parent / 'template_temp.docx'
    with open(temp_path, 'wb') as temp_file:
        temp_file.write(template_content)
    return temp_path


def save_doc(inputs, save_path):
    template_content = get_embedded_template()
    # Use io.BytesIO to work with the content as if it were a file
    template_stream = BytesIO(template_content)
    # Use DocxTemplate constructor with the template content
    doc = DocxTemplate(template_stream)
    doc.render(inputs)
    output_path = save_path + ".docx"
    doc.save(output_path)

