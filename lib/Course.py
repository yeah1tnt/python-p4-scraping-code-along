class Course:
    def __init__(self, title = "NULL", schedule = "NULL", description = "NULL"):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        output = ''
        output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n'
        output += '-----------------------'
        return output