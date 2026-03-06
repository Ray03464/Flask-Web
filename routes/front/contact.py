from app import app, mail
from flask import render_template, request, redirect
from flask_mail import Message

@app.route('/contact')
def contact():
    return render_template('contact.html', modules='contact')

@app.route('/contact/success')
def contact_success():
    return render_template('contact_success.html')

@app.route('/send_contact', methods=['POST'])
def send_contact():
    try:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form.get('phone', 'N/A')
        subject = request.form['subject']
        message = request.form['message']

        msg = Message(
            subject=f"New Contact Form Message: {subject}",
            recipients=['sinthavry@gmail.com']
        )

        msg.body = f"""
New message from your Contact Form:

Full Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Subject: {subject}

Message:
{message}
"""
        mail.send(msg)

        # Redirect to success page
        return redirect('/contact/success')

    except Exception as e:
        print(f"Error sending email: {e}")
        # Redirect back to contact with error parameter
        return redirect('/contact?error=true')