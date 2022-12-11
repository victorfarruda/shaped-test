import pytest
from django.urls import reverse
from model_bakery import baker


def get_data():
    return {
        "name": "Victor",
        "age": 26,
        "address": "Rua XXX, ABC, XXX, Belo Horizonte"
    }


@pytest.mark.django_db
def test_create_patient(client):
    url = reverse("patient:patient-list")
    response = client.post(url, get_data())

    json = response.json()
    assert json.get('id')


@pytest.mark.django_db
def test_read_patient(client):
    patient = baker.make('Patient')
    url = reverse("patient:patient-detail", args=[patient.id])
    response = client.get(url)

    json = response.json()
    assert json.get('id')


@pytest.mark.django_db
def test_update_patient(client):
    patient = baker.make('Patient')
    url = reverse("patient:patient-detail", args=[patient.id])
    update_data = get_data()
    response = client.put(url, data=update_data, content_type='application/json')

    json = response.json()
    assert json.get('id')
    assert update_data.get('name') == json.get('name')
    assert update_data.get('age') == json.get('age')
    assert update_data.get('address') == json.get('address')


@pytest.mark.django_db
def test_delete_patient(client):
    patient = baker.make('Patient')
    url = reverse("patient:patient-detail", args=[patient.id])
    client.delete(url)
    response = client.get(url, content_type='application/json')

    json = response.json()
    assert json.get('detail') == 'Not found.'
