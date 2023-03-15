from datetime import datetime

def createShortlist(jobApp, length):
    SCORE_DESIRED_PAST_EXPERIENCE = 2

    # Job App fields to determine score
    desiredSkills = dict(jobApp['desiredSkills'])
    minGPA = float(jobApp['minGPA'])
    aptitudeResultsMin = float(jobApp['aptitudeResultsMin'])

    potentialEmployees = jobApp['applicants']
    totalScore = sum(int(val) for _, val in desiredSkills.items())
    shortlist = {}

    # Iterate through potential employees
    for potentialEmployee in potentialEmployees:
        score = 0
        correspondingSkills = []
        # Check if minGPA or minimumAptitudeResults are greater than potential employee results meaning they are not a fit
        if potentialEmployee['GPA'] and minGPA > float(potentialEmployee['GPA']) or aptitudeResultsMin > float(potentialEmployee['aptitudeResults']):
            shortlist[potentialEmployee['id']] = [0, potentialEmployee['name'] ]
            continue
       
        # Check desired skills with potentialemployee skills
        for skill, value in desiredSkills.items():
            
            # If the considered skill in the mockJobApp is in potential employee skills, add value to score
            if skill in potentialEmployee['skills']:
                score += int(value)
                correspondingSkills.append(skill)


        # Check desired previous employements
        # for prevEmployment in desiredPastExperience:
        #     if prevEmployment in potentialEmployee['pastExperiences']:
        #         score += SCORE_DESIRED_PAST_EXPERIENCE
        shortlist[potentialEmployee['id']] = [score, potentialEmployee['name'], correspondingSkills, potentialEmployee['location'], potentialEmployee['email']]

    # Sort and shorten shortlist to the length passed
    shortlist = dict(sorted(shortlist.items(), key=lambda item: item[1][0], reverse=True)[:length])
    print(shortlist)
    response = {
        'shortlist': [],
        'length': len(shortlist),
        'timestamp': datetime.now()
    }

    # Format response
    for id, (score, name, correspondingSkills, location, email) in shortlist.items():
        percentageScore = round(score/totalScore * 100)
        response['shortlist'].append({
            'applicantId': id,
            'name': name,
            'score': percentageScore,
            'correspondingSkills': correspondingSkills,
            'location': location,
            'email': email,
        })
    return response


        
