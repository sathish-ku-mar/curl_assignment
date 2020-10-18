import json
from flask import Flask, request, jsonify, Response
from bson import ObjectId, json_util
from mongo import MongoAPI

app = Flask(__name__)

db = MongoAPI({"database": "CurlDB", "collection": "ticker"})


def response_data(response, status=200):
    return Response(response=json.dumps(response, default=str),
                    status=status,
                    mimetype='application/json')


@app.route('/ticker', methods=['GET'])
def get_all_ticker():
    """
    To get the ticker
    :return: Response data
    """
    result = db.read_all()
    return response_data(result)


@app.route('/ticker/<string:ticker_id>', methods=['GET'])
def get_one_ticker(ticker_id):
    """
    To get the ticker by ticker id
    :param ticker_id: Get the ticker id
    :return: Response data
    """
    if not ticker_id:
        return response_data({"Error": "Please provide ticker id"}, 400)

    result = db.read_one({"_id": ObjectId(ticker_id)})
    return response_data(result)


@app.route('/ticker', methods=['POST'])
def create_ticker():
    """
    To create the ticker
    :return: Response data
    """
    data = request.json
    if not data:
        return response_data({"Error": "Please provide data"}, 400)

    result = db.write(data)
    return response_data(result)


@app.route('/ticker/<string:ticker_id>', methods=['PUT'])
def update_ticker(ticker_id):
    """
    To update the ticker by ticker id
    :param ticker_id: Get the ticker id
    :return: Response data
    """
    data = request.json
    if not data or not ticker_id:
        return response_data({"Error": "Please provide data"}, 400)

    data = {
        'Filter': {'_id': ObjectId(ticker_id)},
        'DataToBeUpdated': data
    }
    result = db.update(data)
    return response_data(result)


@app.route('/ticker/<string:ticker_id>', methods=['DELETE'])
def delete_ticker(ticker_id):
    """
    To delete the ticker by ticker id
    :param ticker_id: Get the ticker id
    :return: Response data
    """
    if not ticker_id:
        return response_data({"Error": "Please provide ticker id"}, 400)

    result = db.delete({'_id': ObjectId(ticker_id)})
    return response_data(result)


if __name__ == '__main__':
    app.run(debug=True)
