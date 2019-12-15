from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class CreateAccountSerializer(serializers.Serializer):
    BLUE = 'blue'
    GREEN = 'green'
    RED = 'red'
    BLACK = 'black'
    BROWN = 'brown'
    COLOUR_CHOICES = (
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (RED, 'Red'),
        (BLACK, 'Black'),
        (BROWN, 'Brown'),
    )

    BEAR = 'bear'
    TIGER = 'tiger'
    SNAKE = 'snake'
    DONKEY = 'donkey'
    ANIMAL_CHOICES = (
        (BEAR, 'Bear'),
        (TIGER, 'Tiger'),
        (SNAKE, 'Snake'),
        (DONKEY, 'Donkey'),
    )

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    colour = serializers.ChoiceField(required=True, choices=COLOUR_CHOICES)
    animal = serializers.MultipleChoiceField(required=True, choices=ANIMAL_CHOICES)
    tiger_type = serializers.CharField(required=True)

    def validate_password(self, value):
        validate_password(value)
        return value
