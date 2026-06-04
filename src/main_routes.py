from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    html_content = """
    <h1>Pruebas HTTP</h1>
    <ul>
        <li><a href="/login">Ir al Login (HTTP)</a></li>
        <li><a href="/register">Ir al Registro (HTTP)</a></li>
    </ul>
    """
    return html_content