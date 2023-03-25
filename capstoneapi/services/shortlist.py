from datetime import datetime

def createShortlistEmployee(jobApp, length):


    # Job App fields to determine score
    desiredSkills = dict(jobApp['desiredSkills'])
    potentialEmployees = jobApp['applicants']
    totalScore = sum(int(val) for _, val in desiredSkills.items())
    totalScorePersonality = len(jobApp['aptitudeTest'])
    shortlist = {}

    # Iterate through potential employees
    for potentialEmployee in potentialEmployees:
        score = 0
        correspondingSkills = []
       
        # Check desired skills with potentialemployee skills
        for skill, value in desiredSkills.items():
            
            # If the considered skill in the mockJobApp is in potential employee skills, add value to score
            if skill in potentialEmployee['skills']:
                score += int(value)
                correspondingSkills.append(skill)

        shortlist[potentialEmployee['id']] = [score, potentialEmployee['name'], correspondingSkills, potentialEmployee['location'], potentialEmployee['email'], potentialEmployee['aptitudeResults']]

    # Sort and shorten shortlist to the length passed
    shortlist = dict(sorted(shortlist.items(), key=lambda item: item[1][0], reverse=True)[:length])
    print(shortlist)
    response = {
        'shortlist': [],
        'length': len(shortlist),
        'timestamp': datetime.now()
    }

    # Format response
    for id, (score, name, correspondingSkills, location, email, aptitudeResults) in shortlist.items():
        percentageScore = round(score/totalScore * 100)
        percentageAptitude = round(aptitudeResults/totalScorePersonality * 100)
        response['shortlist'].append({
            'applicantId': id,
            'name': name,
            'score': percentageScore,
            'correspondingSkills': correspondingSkills,
            'location': location,
            'email': email,
            'aptitudeResults': percentageAptitude
        })
        
    return response


        
def createShortlistJob(potentialEmployee, jobApps, length):
    employeeSkills = [skill.lower().replace(' ', '') for skill in potentialEmployee['skills']]
    shortlist = []

    # Goes through all job applications
    for jobApp in jobApps:
        score = 0
        correspondingSkills = []

        desiredSkills = jobApp.desiredSkills
        
        # Goes through all desired skills in job application
        for skill, value in desiredSkills.items():
            formattedSkill = skill.lower().replace(" ", "")
            if formattedSkill in employeeSkills:
                score += int(value)
                correspondingSkills.append(skill)
        if(score > 0):  
            shortlist.append({'score': score, 'jobId': jobApp.id, 'jobName': jobApp.jobName, 'skills': correspondingSkills})
    print(shortlist)

    # Sort and shorten shortlist to the length passed
    shortlist = sorted(shortlist, key=lambda x: x['score'], reverse=True)[:length]
    response = {
        'shortlist': shortlist,
    }
    return response
