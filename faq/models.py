from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field(config_name="default")

    # Translated Fields
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-translate the question and answer into Hindi
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        super().save(*args, **kwargs)

    def get_translation(self, lang='en'):
        if lang == 'hi':  # Hindi translation
            return {
                "question": self.question_hi or self.question,
                "answer": self.answer_hi or self.answer
            }
        return {"question": self.question, "answer": self.answer}
