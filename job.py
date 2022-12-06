from interests import interests

class Job:
    def __init__(self, name:str, affiliated_interests:list, description:str, links:list):
        self.name = name
        for interest in affiliated_interests:
            assert(interest in interests)
        self.affiliated_interests = affiliated_interests
        self.description = description
        self.links = links

        self.match_count = 0

    def get_name(self):
        return self.name

    def get_affiliated_interests(self):
        return self.affiliated_interests

    def get_description(self):
        return self.description
    
    def get_links(self):
        return self.links

    def get_match_count(self):
        return self.match_count

    def has_associated_interest(self, interest: str):
        return interest in self.affiliated_interests

    def increment_match_count(self):
        self.match_count += 1


jobs = [
    Job("Computer Science",
        ["interest-programming", "interest-electronics", "interest-mathematics"],
        "Computer Science is a job",
        ["https://google.com", "https://google.com"]
    ),

    Job("Electrical Engineering",
        ["interest-electronics", "interest-physics"],
        "Electrical Engineering is a job",
        ["https://google.com", "https://google.com"]
    ),

    Job("Civil Engineering",
        ["interest-physics", "interest-architecture"],
        "Civil Engineering is a job",
        ["https://google.com", "https://google.com"]
    )
]