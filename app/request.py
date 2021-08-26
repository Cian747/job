from .models.job import Jobs, Jobs2, Jobs3
from .models.user import User
import urllib.request, json
from . import db

job_url = None

def configure_request(app):
    global job_url
    # job_url = app.config['JOB_API_URL']
    job_url = 'https://api.lever.co/v0/postings/leverdemo?mode=json'

def job_listings():
    
    with urllib.request.urlopen(job_url) as url:
        jobsRAW = url.read()
        jobsJSON = json.loads(jobsRAW)

        if jobsJSON:
            for job in jobsJSON:
                job_id = job.get("job_id")
                commitment = job.get('categories').get('commitment')
                department = job.get('categories').get('department')
                team = job.get('categories').get('team')
                location = job.get('categories').get('location')
                descriptionPlain = job.get("descriptionPlain")
                text = job.get("text")
                applyUrl = job.get("applyUrl")

                job_posting = Jobs(job_id = job_id, commitment = commitment, department = department, 
                                    team = team, location = location, descriptionPlain = descriptionPlain,
                                    text = text, applyUrl = applyUrl)

                db.session.add(job_posting)
                db.session.commit()

    return job_posting    

def job_listings2():

    results = []

    with urllib.request.urlopen(job_url) as url:
        jobsRAW = url.read()
        jobsJSON = json.loads(jobsRAW)

        if jobsJSON:
            for job in jobsJSON:
                job_id = job.get("job_id")
                commitment = job.get('categories').get('commitment')
                department = job.get('categories').get('department')
                team = job.get('categories').get('team')
                location = job.get('categories').get('location')
                descriptionPlain = job.get("descriptionPlain")
                text = job.get("text")
                applyUrl = job.get("applyUrl")

                job_posting = Jobs2(job_id = job_id, commitment = commitment, department = department, 
                                    team = team, location = location, descriptionPlain = descriptionPlain,
                                    text = text, applyUrl = applyUrl)

                results.append(job_posting)

    return results   
 


