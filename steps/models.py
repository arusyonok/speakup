from django.db import models


class Step(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def exercise_count(self):
        exercises = Exercise.objects.filter(step_id = self.id)
        return len(exercises)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=255)

    def choices(self):
        choices = Choice.objects.filter(question_id=self.id)

        return choices

    def __str__(self):
        return self.title

class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

    def question(self):
        return self.question_id.title

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_question = models.BooleanField(default = False)
    question_id = models.ForeignKey(Question, blank = True, null = True)
    step_id = models.ForeignKey(Step)

    def belongs_to(self):
        return self.step_id.name

    def question(self):
        if self.is_question:
            return self.question_id.title