cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    carList = ', '.join(cars['Jeep'])
    print(carList)
    return carList


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    carList = []
    for model in cars.keys():
        carList.append(cars[model][0])
    print(carList)
    return carList


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    carList=[]
    for key in cars.keys():
        for model in cars[key]:
            if grep.capitalize() in model.capitalize():
                carList.append(model)
    return(carList)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    dct = {}
    for key in cars.keys():
        dct[key] = sorted(cars[key])
    return dct


