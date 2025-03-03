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

    pdf.cell(200, 18, f"Offer Letter: {position} with Optiblack", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(10)

    # Replace curly quotes
    letter_body = f"""Dear {name},

Thank you for meeting us to pursue an employment opportunity with Optiblack 
Based on the information /documents provided by you and the interview you had in 
connection with your employment in our Company, we are pleased to appoint you as an “{Position}” based at {location}. 
The remuneration will be as discussed and mutually agreed between us. 
The Management reserves the right to bifurcate or merge the allowances in the basic salary. 
This letter does not constitute an employment offer. This letter is being issued to intimate 
you about certain terms and conditions that are essential which the company believes you must 
be aware of while considering employment opportunities with Optiblack. 
While this appointment is being made the Management reserves the right to utilise your services 
in any function, located elsewhere in India or abroad, either in existence or which may come into existence in future. 
 
Your initial place of posting will be at {location}, and your offered CTC will be 
INR {salary_monthly} Per Month (INR {salary_annual} Per Annum).

Exclusivity and Non-Compete Clause
The Employee/Contractor agrees that during the term of their employment/engagement with the Company, they shall not, directly or indirectly, engage in any other employment, contract work, consulting, or business activities that may conflict with their duties, responsibilities, or obligations to the Company. The Employee/Contractor shall devote their full working hours and best efforts exclusively to the Company’s business and shall not undertake any other work, whether paid or unpaid, without prior written consent from the Company.
Failure to comply with this clause may result in termination of the contract and potential legal action for breach of agreement.


By signing this letter, you agree that:
(a) The information provided in your CV/job application and during interviews is correct.
(b) This Letter of Intent is valid only till your joining date, which should not be later than {joining_date}.

A formal appointment letter will be issued to you. In the meantime, we request your confirmation of acceptance of this offer by returning us a signed copy of this letter. 
Please bring the following documents at the time of your joining: - Original (for verification only) and photocopies of all your documents. 

Experience / Relieving Letters & last drawn salary slips from previous Organizations (not applicable for fresher). 
Four passport size Color photographs. 
Photo Identity Card (PAN CARD) and Aadhaar Card. 
Proof of your Residence/Address Proof (Ration Card, Rent Agreement, Driving License, Passport, Affidavit, Aadhar Card). 

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
