from flask import Flask, render_template
import config
import openai

app = Flask(__name__)
openai.api_key = config.API_KEY

# Define the route for the landing page
@app.route('/')
def landing_page():
    # Serve the index.html file from the templates directory
    return render_template('index.html')

# Route for the Contact Information page (contact_information.html)
@app.route('/contact_information')
def contact_information():
    return render_template('contact_information.html')


# Route for the Objectives page
@app.route('/objective')
def objective():
    return render_template('objective.html')

# Route for the Education page (education.html)
@app.route('/education')
def education():
    return render_template('education.html')

# Route for the Work Experience page (work_experience.html)
@app.route('/work_experience')
def work_experience():
    return render_template('work_experience.html')

# Route for the Skills page (skills.html)
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Route for the Dashboard page (dashboard.html)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)

# flask --app AIResume run --host=0.0.0.0
# Go to Project -> Box Info -> Dynamic Content
# https://julietsugar-helenaatlanta-5000.codio.io/
