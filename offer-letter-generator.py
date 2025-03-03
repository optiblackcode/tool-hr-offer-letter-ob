import streamlit as st
from fpdf2 import FPDF
import datetime
import os

# Function to generate offer letter PDF
def generate_offer_letter(position, name, email, phone, location, salary_monthly, salary_annual, joining_date):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, f"Offer Letter: {position} with Optiblack", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"Dear {name},\n\n"
                         "Thank you for meeting us to pursue an employment opportunity with Optiblack. "
                         "Based on the information/documents provided by you and the interview you had, "
                         "we are pleased to appoint you as an “{position}” based at {location}. "
                         "The remuneration will be as discussed and mutually agreed upon. "
                         "The Management reserves the right to bifurcate or merge the allowances in the basic salary.\n\n"
                         "This letter does not constitute an employment offer but serves to inform you about essential terms "
                         "and conditions you must be aware of while considering employment with Optiblack. Your services may be utilized "
                         "in any function, within India or abroad.\n\n"
                         f"Your initial place of posting will be at {location}, and your offered CTC will be INR {salary_monthly} Per Month "
                         f"({salary_annual} INR Per Annum).\n\n")
    
    pdf.multi_cell(0, 8, "By signing this letter, you agree that:\n"
                         "(a) The information provided in your CV/job application and during interviews is correct.\n"
                         f"(b) This Letter of Intent is valid only till your joining date, which should not be later than {joining_date}.\n\n")
    
    pdf.multi_cell(0, 8, "A formal appointment letter will be issued upon joining. Kindly confirm acceptance by returning a signed copy of this letter.\n"
                         "Please bring the following documents on the joining date:\n"
                         "- Experience/Relieving Letters & last drawn salary slips (if applicable)\n"
                         "- Four passport-size color photographs\n"
                         "- Photo Identity Card (PAN CARD, Aadhaar Card)\n"
                         "- Proof of Residence (Ration Card, Rent Agreement, Passport, etc.)\n\n")
    
    pdf.cell(0, 8, "Sincerely,", ln=True)
    pdf.cell(0, 8, "Vishal Rewari", ln=True)
    pdf.cell(0, 8, "Partner, Optiblack (297 Designs Firm)", ln=True)
    pdf.ln(10)
    
    pdf.cell(0, 8, "Acknowledged and Agreed By:", ln=True)
    pdf.cell(0, 8, name, ln=True)
    pdf.cell(0, 8, f"Date: {datetime.date.today().strftime('%d %B %Y')}", ln=True)

    # Save the PDF
    pdf_filename = f"Offer_Letter_{name.replace(' ', '_')}.pdf"
    pdf.output(pdf_filename)
    return pdf_filename

# Streamlit App UI
st.title("Optiblack Offer Letter Generator")

# User inputs
position = st.selectbox("Select Position", ["Full-Time", "Internship"])
name = st.text_input("Candidate Name")
email = st.text_input("Candidate Email")
phone = st.text_input("Phone Number")
location = st.text_input("Job Location", "Mumbai, India")
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
