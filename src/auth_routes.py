from flask import Blueprint, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f"Intento de login recibido para: {username}"

    return """
    <h2>Iniciar Sesión</h2>
    <form action="http://localhost:8080/login" method="POST">
        <label>Usuario:</label><br>
        <input type="text" name="username"><br>
        <label>Contraseña:</label><br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Ingresar de forma insegura">
    </form>
    """

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        return f"Registro simulado para: {email}"

    return """
    <h2>Registro de Nuevo Usuario</h2>
    <form action="http://localhost:8080/register" method="POST">
        <label>Correo Electrónico:</label><br>
        <input type="email" name="email"><br>
        <label>Contraseña Nueva:</label><br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Registrar cuenta">
    </form>
    """