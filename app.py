from flask import Flask
from flask import request, render_template

from interests import interests
from job import jobs as jbs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def show_results():
    jobs = get_jobs(request.form)

    for job in jobs:
        print(job.name)

    return render_template('results.html', jobs=jobs, jobs_len=len(jobs), interests=interests, user_interests=request.form)

# Returns the recommended jobs based on the user interests.
def get_jobs(request_form: dict):
    local_jobs = jbs.copy()

    for job in local_jobs:
        for user_selected_interest in request_form:
            if job.has_associated_interest(user_selected_interest):
                job.increment_match_count()

    local_jobs.sort()

    return local_jobs
            
if __name__ == "__main__":
    app.run(debug=True)