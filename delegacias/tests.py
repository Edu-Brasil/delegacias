from django.test import TestCase
from .models import Delegacia
from django.utils import timezone

class DelegaciaModelTest(TestCase):

    def setUp(self):
        self.delegacia = Delegacia.objects.create(
            localizacao = "Rua A, 123",
            titulo = "Delegacia Central",
            url = "http://delegacia-central.com",
            criacao=timezone.now()
        )

    def test_delegacia_creation(self):
        self.assertTrue(isinstance(self.delegacia, Delegacia))
        self.assertEqual(self.delegacia.__str__(),"Delegacia Central")

    def test_field_defaults(self):
        delegacia = Delegacia.objects.create(
        titulo = "Delegacia Secundaria",
        url = "http://delegacia-secundaria.com"
        )

        self.assertEqual(delegacia.localizacao,"SOME STRING")











