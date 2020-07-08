import requests
import time, calendar

# Get timestamp
now = str(time.time()).split('.')[0]

# Date conversion to timestamp
begin_date = calendar.timegm(time.strptime('2017-06-01', '%Y-%m-%d'))
end_date = calendar.timegm(time.strptime('2021-06-01', '%Y-%m-%d'))

# API URL
url = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'

# DATA
data = {
    "full_name": "Messias de Souza Martins",
    "email": "messiasads2017@gmail.com",
    "mobile_phone": "+55 (68) 98110-0124",
    "age": 24,
    "home_address": "Rua Flor da Primavera, 1409 - Rio Branco/AC",
    "start_date": now,
    "opportunity_tag": "dev_intern_200",
    "past_jobs_experience": "I currently work as an intern, performing activities to help the company's systems analyst.",
    "degrees": [{
        "institution_name": "Unimeta Centro Universitário",
        "degree_name": "Bacharelado em Sistemas de Informação",
        "begin_date": begin_date,
        "end_date": end_date
    }],
    "programming_skills": ["python", "javascript", "ec2", "django"],
    "database_skills": ["mysql", "sqlite", "firestore"],
    "hobbies": ["coding", "series", "games", "astronomia", "movies"],
    "why": "I'm already an intern, but I would like to have more challenges, and SciCrop seems like a good place to start my career as a developer. Even though I can't be with you all, I do it for the challenge.",
    "git_url_repositories": "https://github.com/MartinsMessias/"
}

# Request
try:
    response = requests.post(url=url, json=data)
except requests.exceptions.RequestException as error:
    raise SystemExit(error)
finally:
    print(response.status_code)

if __name__ == '__main__':
    pass
