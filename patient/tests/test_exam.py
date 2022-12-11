import pytest
from django.urls import reverse
from model_bakery import baker


def get_data(patient):
    return {
        "name_professional": "Victória",
        "date": "2022-11-12",
        "weight": 74,
        "height": 1.77,
        "patient": patient,
    }


@pytest.mark.django_db
def test_create_exam(client):
    patient = baker.make('Patient')
    url = reverse("patient:exam-list")
    response = client.post(url, get_data(patient.id))

    json = response.json()
    assert json.get('id')


@pytest.mark.django_db
def test_read_exam(client):
    exam = baker.make('Exam')
    url = reverse("patient:exam-detail", args=[exam.id])
    response = client.get(url)

    json = response.json()
    assert json.get('id')


@pytest.mark.django_db
def test_update_exam(client):
    patient = baker.make('Patient')
    exam = baker.make('Exam')
    url = reverse("patient:exam-detail", args=[exam.id])
    update_data = get_data(patient.id)
    response = client.put(url, data=update_data, content_type='application/json')

    json = response.json()
    assert json.get('id')
    assert json.get('name_professional') == update_data.get('name_professional')
    assert json.get('date') == update_data.get('date')
    assert json.get('weight') == update_data.get('weight')
    assert json.get('height') == update_data.get('height')
    assert json.get('patient') == update_data.get('patient')


@pytest.mark.django_db
def test_delete_patient(client):
    exam = baker.make('Exam')
    url = reverse("patient:exam-detail", args=[exam.id])
    client.delete(url)
    response = client.get(url, content_type='application/json')

    json = response.json()
    assert json.get('detail') == 'Not found.'
