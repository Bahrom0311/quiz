import json
from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Import questions from savollar.json'

    def handle(self, *args, **kwargs):
        with open('savollar.json', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                Question.objects.create(
                    text=item['savol'],
                    option1=item['variantlar'][0],
                    option2=item['variantlar'][1],
                    option3=item['variantlar'][2],
                    option4=item['variantlar'][3],
                    correct=item['togri_javob']
                )
        self.stdout.write(self.style.SUCCESS('Savollar import qilindi!')) 