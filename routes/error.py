from app import app
from flask import render_template, jsonify, abort

@app.errorhandler(404)
def error_404(e):
    return render_template('error/404.html')

# @app.errorhandler(404)
# def not_found_error(e):
#     return jsonify({
#         "error404": "Not Found",
#         "message": "The requested resource could not be found."
#     }), 404

# @app.errorhandler(500)
# def error_500(e):
#     return render_template('error/500.html')

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "error500": "Internal Server Error",
        "message": "An unexpected error occurred on the server."
    }), 500

@app.errorhandler(403)
def forbidden_error(e):
    return jsonify({
        "error403": "Forbidden",
        "message": "You do not have permission to access this resource."
    }), 403

@app.route('/admin')
def admin():
    abort(403)
# @app.errorhandler(403)
# def error_403(e):
#     return render_template('error/403.html')
#
# @app.route("/shop")
# def shop():
#     abort(403)
#     return render_template('shop.html')