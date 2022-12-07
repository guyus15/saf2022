from interests import interests

class Job:
    def __init__(self, name:str, affiliated_interests:list, description:str, qualifications: str, links:list):
        self.name = name
        for interest in affiliated_interests:
            assert(interest in interests)
        self.affiliated_interests = affiliated_interests
        self.description = description
        self.qualifications = qualifications
        self.links = links

        self.match_count = 0

    def get_name(self):
        return self.name

    def get_affiliated_interests(self):
        return self.affiliated_interests

    def get_description(self):
        return self.description

    def get_qualifications(self):
        return self.qualifications
    
    def get_links(self):
        return self.links

    def get_match_count(self):
        return self.match_count

    def has_associated_interest(self, interest: str):
        return interest in self.affiliated_interests

    def increment_match_count(self):
        self.match_count += 1

    def __gt__(self, x):
        return self.get_match_count() < x.get_match_count()

    def __lt__(self, x):
        return self.get_match_count() > x.get_match_count()

jobs = [
    Job("Computer Science",
        ["interest-programming", "interest-team", "interest-solving-problems", "interest-creation"],
        "Computer science focuses on the development and testing of software and software systems. As a computer scientist you might be working on security, algorithms, data analysis and many other sub-topics within the field.",
        "Entry requirements for computer science majors commonly emphasise strong knowledge of mathematics and physics. Some institutions recommend a background of psychology and sociology to compliment your studies.",
        ["https://en.wikipedia.org/wiki/Computer_science", "https://www.topuniversities.com/courses/computer-science-information-systems/guide"]
    ),

    Job("Electrical Engineering",
        ["interest-alone", "interest-solving-problems", "interest-creation", "interest-how-things-work"],
        "Electrical Engineering is a profession concerned with the study, design and application of equipment, devices and systems which use electricity, electronics and electromagnetism. As an electronic engineer you might design, develop, test or supervise the manufacture of electrical equipment.",
        "Strong knowledge of mathematics is almost necessary as an entry requirement for electrical engineering. Other commonly desired skills are sciences such as physics and computer science.",
        ["https://en.wikipedia.org/wiki/Electrical_engineering", "https://www.topuniversities.com/courses/engineering-electrical-electronic/guide"]
    ),

    Job("Healthcare Professional",
        ["interest-helping-others", "interest-team", "interest-people"],
        "Healthcare is the improvement of health via the prevention, diagnosis, treatment and care of a person. Common healthcare roles include, doctors, nurses, healthcare assistants, radiologist and cardiologists",
        "Entry requirements for a healthcare profession are very much dependent on which path you would like to take. For a healthcare assistant, there are no set entry requirements. Employers would expect good literacy and numeracy, and be able to communicate well with patients. Other professions may require more than this, for professions such as doctors and radiologists a degree is required. Common entry requirements are voluntary or work experience related to healthcare, good knowledge of mathematics, biology, chemistry, and physics, and good social skills.",
        ["https://en.wikipedia.org/wiki/Civil_engineering", "https://www.topuniversities.com/courses/engineering-civil-structural/guide"]
    ),

    Job("Law Enforcement",
        ["interest-helping-others", "interest-team", "interest-people", "interest-justice"],
        "Law enforcement is an organised activity to enforce law by discovering, deterring, rehabilitating or punishing people who violates the rules governing a society. Some law enforcement roles include: police, criminal investigators, detectives, and secret service agents.",
        "Basic entry requirements for a major in law enforcent include having a valid driver's license and being at least 18 or 21 years old. Depending on the department's policy, applicants might also need a clean criminal record, although some police departments may allow those with criminal records as long as their offences were very minor.",
        ["https://en.wikipedia.org/wiki/Law_enforcement", "https://www.prospects.ac.uk/jobs-and-work-experience/job-sectors/law-enforcement-and-security/joining-the-police"]
    )
]