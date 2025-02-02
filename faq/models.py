from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from googletrans import Translator

translator = Translator()

# List of supported Indian languages (ISO 639-1 Codes)
INDIAN_LANGUAGES = {
    "hi": "Hindi",
    "bn": "Bengali",
    "gu": "Gujarati",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "pa": "Punjabi",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu"
}

class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field(config_name="default")

    # Dynamically create translation fields for each language
    for lang_code in INDIAN_LANGUAGES.keys():
        locals()[f"question_{lang_code}"] = models.TextField(blank=True, null=True)
        locals()[f"answer_{lang_code}"] = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Auto-translate the question & answer into multiple Indian languages"""
        for lang_code in INDIAN_LANGUAGES.keys():
            question_field = f"question_{lang_code}"
            answer_field = f"answer_{lang_code}"

            # If the translation is missing or null, generate it
            if not getattr(self, question_field):
                setattr(self, question_field, translator.translate(self.question, dest=lang_code).text)
            
            if not getattr(self, answer_field):
                setattr(self, answer_field, translator.translate(self.answer, dest=lang_code).text)

        super().save(*args, **kwargs)

    def get_translation(self, lang="en"):
        """Retrieve translated text dynamically"""
        if lang in INDIAN_LANGUAGES:
            question_field = f"question_{lang}"
            answer_field = f"answer_{lang}"
            return {
                "question": getattr(self, question_field) or self.question,
                "answer": getattr(self, answer_field) or self.answer,
            }
        return {"question": self.question, "answer": self.answer}
