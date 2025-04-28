import json
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Replace 'myproject' with your project name
django.setup()

from booking.models import Property  # Adjust if your model is named differently

def import_data():
    with open('mock_properties.json', 'r', encoding='utf-8') as file:
        properties = json.load(file)
        for item in properties:
            Property.objects.create(
                name=item['name'],
                description=item['description'],
                price_per_night=item['price_per_night'],
                location=item['location'],
                image_url=item['image_url']
            )
    print(f"✅ Imported {len(properties)} properties successfully.")

if __name__ == '__main__':
    import_data()