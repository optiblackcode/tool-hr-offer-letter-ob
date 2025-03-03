import streamlit as st
from fpdf import FPDF
import datetime
import os
from fpdf.enums import XPos, YPos

def generate_offer_letter(position, name, email, phone, location, salary_monthly, salary_annual, joining_date):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Use Unicode font
    pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", "", 12)

    pdf.cell(200, 10, f"Offer Letter: {position} with Optiblack", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(10)

    # Replace curly quotes
    letter_body = f"""Dear {name},

Thank you for meeting us to pursue an employment opportunity with Optiblack.
Based on the information/documents provided by you and the interview you had, 
we are pleased to appoint you as an "{position}" based at {location}. 
The remuneration will be as discussed and mutually agreed upon. 

Your initial place of posting will be at {location}, and your offered CTC will be 
INR {salary_monthly} Per Month ({salary_annual} INR Per Annum).

By signing this letter, you agree that:
(a) The information provided in your CV/job application and during interviews is correct.
(b) This Letter of Intent is valid only till your joining date, which should not be later than {joining_date}.

A formal appointment letter will be issued upon joining. Kindly confirm acceptance 
by returning a signed copy of this letter.
"""

    # Normalize text to avoid Unicode errors
    letter_body = letter_body.replace("“", '"').replace("”", '"')

    pdf.multi_cell(0, 8, letter_body)

    pdf.cell(0, 8, "Sincerely,", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "Acknowledged and Agreed By:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "Vishal Rewari")
    pdf.cell(0, 8, "Partner, Optiblack (297 Designs Firm)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf_filename = f"Offer_Letter_{name.replace(' ', '_')}.pdf"
    pdf.output(pdf_filename)
    return pdf_filename

# Streamlit App UI
st.title("Optiblack Offer Letter Generator")

# User inputs
position = st.text_input("Position")
name = st.text_input("Candidate Name")
email = st.text_input("Candidate Email")
phone = st.text_input("Phone Number")
location = st.text_input("Job Location","India")
salary_monthly = st.text_input("Salary Per Month (INR)")
salary_annual = st.text_input("Salary Per Year (INR)")
joining_date = st.date_input("Joining Date")

# Generate PDF button
if st.button("Generate Offer Letter"):
    if not name or not email or not phone or not salary_monthly or not salary_annual:
        st.error("Please fill all required fields.")
    else:
        pdf_filename = generate_offer_letter(position, name, email, phone, location, salary_monthly, salary_annual, joining_date)
        st.success(f"Offer letter generated successfully!")
        
        # Provide download link
        with open(pdf_filename, "rb") as pdf_file:
            st.download_button(label="Download Offer Letter", data=pdf_file, file_name=pdf_filename, mime="application/pdf")
