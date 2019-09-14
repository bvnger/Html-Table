from flask import Flask, render_template
from flask_table import Table, Col
app = Flask(__name__)

@app.route('/')
def index():

# FOR TABLE
    # class ItemTable(Table):
    #     name = Col('Name')
    #     description = Col('Description')

    # class Item(object):
    #     def __init__(self, first_name, last_name):
    #         self.first_name = first_name
    #         self.last_name = last_name
    users= [
        {'first_name' : 'Micha335el', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tone1'},
    ]

    # table = ItemTable(users)

    # print(table.__html__())

    return render_template("index.html", table = users )

if __name__=="__main__":
    app.run(debug=True)