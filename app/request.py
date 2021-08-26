
import urllib.request,json
from .models.job import Jobs
from flask_login import current_user
from app import db

job_api_url = None


def configure_request(app):
    global job_api_url
    # job_api_url = app.config['JOB_API_URL']
    job_api_url='https://api.lever.co/v0/postings/leverdemo?mode=json'


def general():
    '''
    fetch all the general jobs
    '''
    get_job_url = job_api_url

    with urllib.request.urlopen(get_job_url) as url:
        get_job_data = url.read()
        get_job_response = json.loads(get_job_data)

        if get_job_response:
            for job in get_job_response:
                job_id  = job.get('id')

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
                descriptionPlain =job.get('descriptionPlain')
                description =job.get('description')
                text = job.get("text")
                applyUrl =job.get('applyUrl')

                if location is None or commitment is None:
                    location = 'Remote'
                    commitment = 'Full time'

                job = Jobs(job_id = job_id,commitment=commitment,department = department,team=team,location=location,descriptionPlain=descriptionPlain,text=text,applyUrl=applyUrl)

                # db.session.add(job)
                # db.session.commit()

        return job

def general_two():
    '''
    fetch all the general jobs
    '''
    get_job_url = job_api_url

    with urllib.request.urlopen(get_job_url) as url:
        get_job_data = url.read()
        get_job_response = json.loads(get_job_data)

        if get_job_response:
            for job in get_job_response:
                job_id  = job.get('id')
                descriptionPlain = job.get("descriptionPlain")
                text = job.get("text")
                applyUrl = job.get("applyUrl")

                job_posting = Jobs(job_id = job_id, commitment = commitment, department = department, 
                                    team = team, location = location, descriptionPlain = descriptionPlain,
                                    text = text, applyUrl = applyUrl)

                db.session.add(job_posting)
                db.session.commit()

    return job_posting    




