from django.test import TestCase, Client
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_availability_gadget(self):
        gadget = Product.objects.create(
          name ="Asus ROG Zephyrus G14",
          price = 2500,
          description = "AMD Ryzen 9 8945 HS, RTX 4060, 32 GB ram",
          stock = 8,
        )
        self.assertTrue(gadget.is_available())