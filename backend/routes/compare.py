from flask import Blueprint, jsonify, request
import requests

compare_routes = Blueprint('compare', __name__)

@compare_routes.route('/compare', methods=['GET'])
def compare_prices():
    # Extract query parameters
    item_id = request.args.get('item_id')
    retailers = request.args.getlist('retailers')

    # Dummy data to simulate price comparison
    prices = {
        'retailer1': 10.99,
        'retailer2': 12.49,
        'retailer3': 9.99
    }

    # Filter prices based on requested retailers
    if retailers:
        prices = {k: prices[k] for k in retailers if k in prices}

    return jsonify(prices)

@compare_routes.route('/compare/<item_id>', methods=['GET'])
def compare_prices_item(item_id):
    # Dummy data to simulate price retrieval
    prices = {
        'item1': {'retailer1': 10.99, 'retailer2': 12.49},
        'item2': {'retailer1': 15.49, 'retailer2': 14.99, 'retailer3': 13.99},
    }

    return jsonify(prices.get(item_id, 'Item not found'))