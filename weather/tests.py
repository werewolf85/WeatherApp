from django.test import TestCase
from .models import City

class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестовый объект City для использования в тестах
        City.objects.create(name='TestCity')

    def test_name_max_length(self):
        city = City.objects.get(id=1)
        max_length = city._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

    def test_name_label(self):
        city = City.objects.get(id=1)
        field_label = city._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_str_method(self):
        city = City.objects.get(id=1)
        expected_object_name = city.name
        self.assertEquals(expected_object_name, str(city))
