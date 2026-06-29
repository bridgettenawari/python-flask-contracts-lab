#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>')
def contract(id):
    for contract in contracts:
        if contract['id'] == id:
            return make_response(contract["contract_information"], 200)
        else:
            return make_response("Contract not found", 404)

@app.route('/customer/<customer_name>')
def customername(customer_name):
    for customer in customers:
        if customer_name in customer:
            return make_response("", 204)
        else:
            return make_response("Customer not found", 404)
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)

"""
all_students = " ".join([f"<li>{student["name"]} <a href='/students/{id}'> View details </a></li>" for id,student in students.items() ])

country = next((item for item in countries if item )
return f' {country}'

@app.route('/countries/<int:id>')
def countries(id):
    for country in countries:
        if country["id"] == id:
            return country
"""