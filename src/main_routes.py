from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    html_content = """
    <h1>Portal de Pruebas SAST (Inseguro)</h1>
    <ul>
        <li><a href="/login">Ir al Formulario de Login (HTTP)</a></li>
        <li><a href="/register">Ir al Formulario de Registro (HTTP)</a></li>
    </ul>
    """
    return html_content