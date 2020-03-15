from flask import Flask, jsonify


app = Flask(__name__)

# stores = [
#     {
#         'name': 'My Store',
#         'item': [
#             {
#                 'name': 'Item 1',
#                 'price': '15.99'
#             }
#         ]
#     },
# ]

hits = {
    "id"    : 1,
    "name"  : "HR",
    "hits" : [
        {
          "name": "Alex",
          "id": 1,
          "_source": {
              "order_count": 50,
              "event_timestamp": "1",
              "order_type":"OP_BUY"
          }
        },
        {
          "name": "Brian",
          "id": 2,
          "_source": {
              "order_count": 40,
              "event_timestamp": "1",
              "order_type":"OP_SELL"
          }
        },
        {
          "name": "Charles",
          "id": 3,
          "_source": {
              "order_count": 300,
              "event_timestamp": "1",
              "order_type":"EQ_BUY"
          }
        },
        {
          "name": "John",
          "id": 4,
          "_source": {
              "order_count": 200,
              "event_timestamp": "1",
              "order_type":"EQ_SELL"
          }
        }
    ]
}


# POST - used to recieve data
# GET - used to send data


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>')     # 'http://localhost:5000/store/some_name'
def get_store(name):
    pass

# GET /store
@app.route('/store')   
def get_stores():
    return jsonify({"hits":hits})
    # return jsonify({'hits': hits})

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])    # 'http://localhost:5000/store/some_name'
def create_store_item(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')     # 'http://localhost:5000/store/some_name'
def get_store_items(name):
    pass




app.run(port=5000 )
