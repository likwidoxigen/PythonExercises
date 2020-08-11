def make_car(make, model, **carInfo):
    """Make a car object"""
    carInfo['make'] = make
    carInfo['model'] = model
    return carInfo


def print_models(car):
    print(f'The Model is: {car["model"]}')
