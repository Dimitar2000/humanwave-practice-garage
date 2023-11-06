from flask import Blueprint, abort, jsonify, request, redirect
from shared.model.garage import Garage
from shared.model.car import Car
import logging
import requests

bp = Blueprint(name='garages', import_name=__name__, url_prefix='/garages')

@bp.route('/worker', methods=["GET"])
def redirect_route():
    r = requests.get(url = 'http://localhost:8082/')
    return jsonify(r.json())


# @garages.route('/', defaults={'page': 'index'})
@bp.route('/', methods=["GET"])
def garage_list():
    print(request.args)
    if request.args and 'garage' in request.args:
        garage = Garage.get(key=request.args.get('garage'))
        return jsonify({
            'id': garage.id,
            'name': garage.name,
            'brand': garage.brand,
            'postal_country': garage.postal_country
        })
    return jsonify(
        [
            {
                'id': g.id,
                'name': g.name,
                'brand': g.brand,
                'postal_country': g.postal_country
            } for g in Garage.list()
        ]
    )


@bp.route('/', methods=["POST"])
def garage_add():
    logging.warning(request.json)
    garage = Garage.add(props=request.json)
    new_garage = request.json
    new_garage["id"] = garage.id()

    logging.warning("New garage added: ")
    logging.warning(new_garage)

    return jsonify(new_garage)

@bp.route('/', methods=["PUT"])
def garage_update():
    props = request.json
    garage = Garage.get(key=props.pop('id'))
    # print(garage)
    garage.update(props=props)
    return jsonify({
        'id': garage.id,
        'name': garage.name,
        'brand': garage.brand,
        'postal_country': garage.postal_country
    })

@bp.route('/', methods=["DELETE"])
def garage_delete():

    # Get the garage id
    garage_key = request.json.pop('garage')

    # Delete all cars in the garage
    garage_cars = Car.list(garage_id=garage_key)
    for car in garage_cars:
        car.delete()

    # Delete the garage
    garage = Garage.get(key=garage_key)
    garage.delete()

    return jsonify({'status': 'OK'})

@bp.route('/car', methods=["POST"])
def car_add():
    logging.warning(request.json)
    
    garage_id = request.json.pop('garage_id')
    car_data  = request.json.pop('carData')

    car_data['garage_id'] = garage_id

    new_car_id = Car.add(props=car_data).id()

    response_data = car_data
    response_data['id'] = new_car_id

    return jsonify(response_data)

@bp.route('/car', methods=["GET"])
def car_get():        
    logging.warning(request.args)

    cars = []
    if request.args and "garage_id" in request.args:
        garage_id = request.args.get('garage_id')
        cars = Car.list(garage_id=int(garage_id))
    else:
        cars = Car.list()

    return jsonify(
        [
            {
                'id': car.id,
                'name': car.name,
                'owner': car.owner,
                'price': car.price
            } for car in cars
        ]
    )
 
@bp.route('/car', methods=["DELETE"])
def car_delete():
    car = Car.get(key=request.json.pop('car_id'))
    car.delete()
    return jsonify({'status': 'OK'})

@bp.route('/car', methods=["PUT"])
def car_update():
    props = request.json
    car = Car.get(key=props.pop('car_id'))
    # print(garage)
    car.update(props=props)

    return jsonify({
        'id': car.id,
        'name': car.name,
        'owner': car.owner,
        'price': car.price
    })