from flask_cors import CORS

def add_cors(app):
    """Configure CORS for Flask application"""
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    
    # Add CORS headers to all responses
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response