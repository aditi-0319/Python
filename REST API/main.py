from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

url = "http://localhost:5000/"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
db = SQLAlchemy()
db.init_app(app)


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    quote = db.Column(db.String(1000), nullable=False)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


# with app.app_context():
#     db.create_all()
#     new_quote = Quote(id=1, name="Thomas A. Edison",
#                       quote="Many of life’s failures are people who did not realize how close they were to success when they gave up.")
#     db.session.add(new_quote)
#     db.session.commit()
#
#     quotes = Quote.query.all()
#     for quote in quotes:
#         print(f'ID: {quote.id}, Name: {quote.name}, Quote: {quote.quote}')

@app.route('/get', methods=['GET'])
def get_data():
    result = db.session.execute(db.select(Quote).order_by(Quote.id))
    all_quotes = result.scalars().all()
    if all_quotes:
        return jsonify(quote=[quote.to_dict() for quote in all_quotes])
    else:
        return jsonify(error={"Not Found": "Sorry, no quotes are available"}), 404


@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    # new_quote = Quote(
    #     name=request.form.get("name"),
    #     quote=request.form.get("quote"),
    # )

    new_quote = Quote(
        name=data.get("name"),
        quote=data.get("quote"),
    )

    db.session.add(new_quote)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new quote."}), 201


@app.route('/put/<int:quote_id>', methods=['PUT'])
def update(quote_id):
    data = request.get_json()
    quote = Quote.query.get(quote_id)

    # new_name = request.json.get("new_name")
    # new_quote = request.json.get("new_quote")
    # quote = db.get_or_404(Quote, quote_id)
    # if quote:
    #     if new_name is not None:
    #         quote.name = new_name
    #     elif new_quote is not None:
    #         quote.quote = new_quote
    #     else:
    #         return jsonify(error={"Bad Request": "No valid update data provided."}), 400

    if quote:
        if 'name' in data:
            quote.name = data['name']
        if 'quote' in data:
            quote.quote = data['quote']
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the quote."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry, a quote with that id was not found in the database."}), 404


@app.route("/delete/<int:quote_id>", methods=["DELETE"])
def delete_cafe(quote_id):
    quote = db.get_or_404(Quote, quote_id)
    if quote:
        db.session.delete(quote)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the quote from the database."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a quote with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)

# "Life is never easy. There is work to be done and obligations to be met – obligations to truth, to justice, and to liberty." — John F. Kennedy
