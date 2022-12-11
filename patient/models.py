from django.db.models import (
    Model,
    CharField,
    IntegerField,
    DateField,
    FloatField,
    ForeignKey,
    DO_NOTHING,
)


class Patient(Model):
    name = CharField(max_length=120)
    age = IntegerField()
    address = CharField(max_length=80)


class Exam(Model):
    name_professional = CharField(max_length=120)
    date = DateField()
    weight = FloatField()
    height = FloatField()
    patient = ForeignKey(Patient, on_delete=DO_NOTHING)
