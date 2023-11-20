from pathlib import Path
import PySimpleGUI as sg
from docxtpl import DocxTemplate


def save_doc(inputs): 
    document_path = Path(__file__).parent / "template.docx"
    doc = DocxTemplate(document_path)

    doc.render(inputs)
    output_path = Path(__file__).parent / f"{{ inputs.subject }}.docx"
    doc.save(output_path)

