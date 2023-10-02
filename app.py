import os
import csv
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Function to validate email format
def is_valid_email(email):
    allowed_domains = ["my.erau.edu", "erau.edu"]
    for domain in allowed_domains:
        if email.endswith(f"@{domain}"):
            return True
    return False

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']

        if is_valid_email(email):
            # Store the email address in a CSV file
            with open('emails.csv', 'a', newline='') as csvfile:
                email_writer = csv.writer(csvfile)
                email_writer.writerow([email])
            flash('Email registered successfully!', 'success')
        else:
            flash('Improper email used, please enter ERAU email', 'danger')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
