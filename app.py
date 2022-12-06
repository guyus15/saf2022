from flask import Flask
from flask import request, render_template

from interests import interests
from job import jobs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def show_results():
    jobs = get_jobs(request.form)

    for job in jobs:
        print(job.name)

    return request.form

# Returns the recommended jobs based on the user interests.
def get_jobs(request_form: dict):
    current_most_suited_job = jobs[0]

    for job in jobs:
        for user_selected_interest in request_form:
            if job.has_associated_interest(user_selected_interest):
                job.increment_match_count()

        if job.get_match_count() > current_most_suited_job.get_match_count():
            current_most_suited_job = job

    return [current_most_suited_job]
            
if __name__ == "__main__":
    app.run(debug=True)