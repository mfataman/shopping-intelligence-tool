from flask import Blueprint, request, jsonify

# Initialize Blueprint
search_bp = Blueprint('search', __name__)

@search_bp.route('/api/search', methods=['GET'])
def search_product():
    query = request.args.get('query')
    # Sample implementation - Replace with actual search logic
    if query:
        results = [
            {'id': 1, 'name': 'Sample Product 1', 'description': 'Description 1', 'price': 10.0},
            {'id': 2, 'name': 'Sample Product 2', 'description': 'Description 2', 'price': 20.0}
        ]
        return jsonify(results), 200
    return jsonify({'error': 'Query parameter is required'}), 400


@search_bp.route('/api/search/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Sample implementation - Replace with actual product retrieval logic
    product = {'id': product_id, 'name': f'Sample Product {product_id}', 'description': f'Description {product_id}', 'price': product_id * 10.0}
    return jsonify(product), 200

