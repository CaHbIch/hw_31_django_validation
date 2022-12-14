from datetime import date

from django.core.exceptions import ValidationError
from rest_framework import serializers


def check_age(date_of_birth: date):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    if age < 9:
        raise ValidationError(f" Ваш возраст должен быть больше 9 лет.")


class EmailDomainValidator:
    def __init__(self, domains):
        if not isinstance(domains, list):
            domains = [domains]

        self.domains = domains

    def __call__(self, email):
        domain = email.split('@')[1]
        if domain in self.domains:
            raise serializers.ValidationError(f"Домен не может быть {domain}")