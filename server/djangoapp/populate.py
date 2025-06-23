from .models import CarMake, CarModel

def initiate():
    print("Populate not implemented. Add data manually")
    
    # Create car makes
    car_make_data = [
        {"name": "BMW", "description": "German luxury car manufacturer"},
        {"name": "Mercedes-Benz", "description": "German luxury automobile manufacturer"},
        {"name": "Audi", "description": "German automobile manufacturer"},
        {"name": "Toyota", "description": "Japanese multinational automotive manufacturer"},
        {"name": "Honda", "description": "Japanese multinational conglomerate"},
    ]
    
    for make_data in car_make_data:
        car_make, created = CarMake.objects.get_or_create(
            name=make_data["name"],
            defaults={"description": make_data["description"]}
        )
        if created:
            print(f"Created car make: {car_make.name}")
    
    # Create car models
    car_model_data = [
        {"make_name": "BMW", "name": "3 Series", "type": "sedan", "year": 2022},
        {"make_name": "BMW", "name": "X5", "type": "suv", "year": 2023},
        {"make_name": "Mercedes-Benz", "name": "C-Class", "type": "sedan", "year": 2022},
        {"make_name": "Mercedes-Benz", "name": "GLE", "type": "suv", "year": 2023},
        {"make_name": "Audi", "name": "A4", "type": "sedan", "year": 2022},
        {"make_name": "Audi", "name": "Q5", "type": "suv", "year": 2023},
        {"make_name": "Toyota", "name": "Camry", "type": "sedan", "year": 2022},
        {"make_name": "Toyota", "name": "RAV4", "type": "suv", "year": 2023},
        {"make_name": "Honda", "name": "Civic", "type": "sedan", "year": 2022},
        {"make_name": "Honda", "name": "CR-V", "type": "suv", "year": 2023},
    ]
    
    for model_data in car_model_data:
        try:
            car_make = CarMake.objects.get(name=model_data["make_name"])
            car_model, created = CarModel.objects.get_or_create(
                car_make=car_make,
                name=model_data["name"],
                type=model_data["type"],
                year=model_data["year"]
            )
            if created:
                print(f"Created car model: {car_model}")
        except CarMake.DoesNotExist:
            print(f"Car make {model_data['make_name']} not found")
    
    print("Population completed!")
