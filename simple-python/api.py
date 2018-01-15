# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Testing(Resource):
    def get(self):
        return {
            'Profile': 
             [ 
               'Dang Thanh Phuc', 
               'Age - 27', 
               'Github: https://github.com/dtphuc'
             ]
        }

# Create routes
api.add_resource(Testing, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
