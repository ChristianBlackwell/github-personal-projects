
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import blue


try:
    # Create a PDF document with adjusted margins
    doc = SimpleDocTemplate("resume_template_2023.pdf", pagesize=letter, leftMargin=30, rightMargin=30, topMargin=30, bottomMargin=30)

    # Create a sample stylesheet
    styles = getSampleStyleSheet()

    # Create a hyperlink style
    hyperlink_style = ParagraphStyle('Hyperlink', parent=styles['BodyText'], textColor='blue', underline=True)

    # Create a bold style based on the 'BodyText' style
    bold_style = ParagraphStyle('BoldBodyText', parent=styles['BodyText'])
    bold_style.fontName = 'Helvetica-Bold'

    # Create a title paragraph with your name
    name_text = "<b>Christian Blackwell</b>"
    name_paragraph = Paragraph(name_text, styles['Title'])

    # Create a contact info paragraph
    contact_text1 = "Phone: 479-255-8230 | Email: <a href='mailto:christian.blackwell@outlook.com'><u>christian.blackwell@outlook.com</u></a>"
    contact_text2 = "<br/>LinkedIn Profile: <a href='https://www.linkedin.com/in/christian-blackwell-aa53a0210/'><u>LinkedIn</u></a> | GitHub Portfolio: <a href='https://github.com/ChristianBlackwell/github-personal-projects'><u>GitHub</u></a>"

    contact_text = contact_text1 + contact_text2
    contact_paragraph = Paragraph(contact_text, styles['BodyText'])

    # Create the summary paragraph
    summary_text1 = "<b>Quality Analyst Overview:</b> "
    summary_text2 = "Highly adaptable cross-functional organizational leader with a proven track record of driving business outcomes through effective management. I possess excellent communication, negotiation, problem-solving, and interpersonal skills, enabling me to lead teams to achieve successful project outcomes."

    summary_text = summary_text1 + summary_text2
    summary_paragraph = Paragraph(summary_text, styles['BodyText'])

    # Create a section for work experience
    experience_text = "<u>Professional Experience</u>"
    experience_paragraph = Paragraph(experience_text, styles['Heading1'])
    experience_details = Paragraph("Quality Analyst - Lead | Foundever | April 2022 - Present", bold_style)

    # Job details
    job_details = Paragraph("""
        • Resolved technical, financial, and operational issues through effective collaboration with team members and directors.
        <br/>• Identified and resolved customer problems by communicating requirements to subordinates and delivering appropriate &nbsp;&nbsp;solutions.
        <br/>• Implemented procedural enhancements to enhance the quality of deliverables, surpassing customer expectations.
        <br/>• Facilitated seamless and efficient program development by fostering cross-functional collaboration across departments.
        <br/>• Mentored team members on productivity strategies, policy updates, and performance improvement plans to achieve &nbsp;&nbsp;ambitious objectives.
        <br/>• Monitored program progress by utilizing programming documents, program directives, funding documents, and other &nbsp;&nbsp;program materials.
        <br/>• Oversaw a small test group for an automation project aimed at streamlining a high-risk item.
        <br/>• Conducted software testing for various applications throughout my tenure as Lead QA (Nice, Nexidia, etc.).
    """, styles['BodyText'])

    # Create a section for additional work experience
    experience_text1 = "<u></u>"
    experience_paragraph1 = Paragraph(experience_text1, styles['Heading1'])
    experience_details1 = Paragraph("Lead Quality Analyst | Sykes Enterprises Inc. | October 2016 – May 2021", bold_style)

    # Job details
    job_details1 = Paragraph("""
        • Championed a culture of excellence and achievement by inspiring and motivating employees through positive &nbsp;&nbsp;reinforcement and incentive programs.
        <br/>• Developed comprehensive project plans and timelines, effectively managing workflow and personnel allocation.
        <br/>• Demonstrated exceptional time management skills, consistently meeting or surpassing completion deadlines.
        <br/>• Fostered strong collaboration with Account Managers, Team Managers, Trainers, and other stakeholders, fostering a &nbsp;&nbsp;cohesive and synergistic team-oriented environment.
        <br/>• Served as a mentor to Managers, Quality Analysts, Trainers, and other team members, providing guidance on proper &nbsp;&nbsp;equipment usage and adherence to product procedures.
    """, styles['BodyText'])

    # Create a section for additional work experience
    experience_text2 = "<u></u>"
    experience_paragraph2 = Paragraph(experience_text1, styles['Heading1'])
    experience_details2 = Paragraph("Quality Analyst | Sykes Enterprises Inc. | May 2016 – October 2016", bold_style)

    # Job details
    job_details2 = Paragraph("""
        • Performed regular weekly and monthly audits, meticulously documenting findings and delivering comprehensive reports &nbsp;&nbsp;to Account and Team Managers.
        <br/>• Developed well-structured agendas and crafted effective communication materials for team meetings, ensuring clarity &nbsp;&nbsp;and alignment.
        <br/>• Evaluated agent performance against rigorous quality requirements, proactively identifying areas for improvement and &nbsp;&nbsp;implementing remediation plans to ensure standardized results in compliance with regulatory standards.
        <br/>• Drove customer satisfaction to its highest levels through efficient operational management that strictly adhered to quality &nbsp;&nbsp;standards and fulfilled all customer requirements.
    """, styles['BodyText'])

    # Create a section for work experience
    experience_text3 = "<u>Additional Experience</u>"
    experience_paragraph3 = Paragraph(experience_text3, styles['Heading1'])

    # Job details
    job_details3 = Paragraph("""
        Project Coordinator | SmartSource Inc. | May 2021 – April 2022
        <br/>Customer Support Representative | Sykes Enterprises Inc. | February 2016 – May 2016
    """, styles['BodyText'])

    # Build the PDF document
    content = [
        name_paragraph, Spacer(1, 12), contact_paragraph, Spacer(1, 12),
        summary_paragraph, Spacer(1, 12),
        experience_paragraph, experience_details,
        job_details,
        experience_paragraph1, experience_details1,
        job_details1,
        experience_paragraph2, experience_details2,
        job_details2,
        Spacer(1, 12),
        experience_paragraph3, # Add the updated section and its details
        job_details3 # Add the updated job details for the additional experience
    ]

    doc.build(content)

except Exception as e:
    print("An error occurred:", str(e))
