from flask import Blueprint, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f"""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .alert-neutral {{
                background-color: #f8f9fa;
                border: 1px solid #495057;
                color: #495057;
            }}
            .btn-neutral {{
                background-color: #495057;
                color: #ffffff;
                border: none;
                text-decoration: none;
            }}
            .btn-neutral:hover {{
                background-color: #3d4550;
                color: #ffffff;
            }}
        </style>
        <div class="container mt-5 text-center">
            <div class="alert-neutral d-inline-block p-4 shadow-sm" role="alert">
                <p>Inicio de sesión recibido.</p>
                <hr>
                <p class="mb-0 text-start"><strong>Usuario:</strong> {username}</p>
                <p class="text-start"><strong>Contraseña:</strong> {password}</p>
                <a href="/" class="btn btn-neutral btn-sm mt-3">Volver al Inicio</a>
            </div>
        </div>
        """

    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Iniciar Sesión</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
            }
            .btn-neutral {
                background-color: #495057;
                color: #ffffff;
                border: none;
                font-weight: 500;
            }
            .btn-neutral:hover {
                background-color: #3d4550;
                color: #ffffff;
            }
            a {
                color: #495057;
            }
            a:hover {
                color: #3d4550;
            }
        </style>
    </head>
    <body>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-4">
                    <div class="card shadow-sm border-0 mt-5">
                        <div class="card-body p-4">
                            <h3 class="card-title text-center fw-bold mb-4" style="color: #495057;">Iniciar Sesión</h3>
                            
                            <form action="http://localhost:8080/login" method="POST">
                                <div class="mb-3">
                                    <label class="form-label fw-semibold">Nombre de Usuario</label>
                                    <input type="text" name="username" class="form-control" placeholder="ejemplo_user" required>
                                </div>
                                <div class="mb-4">
                                    <label class="form-label fw-semibold">Contraseña</label>
                                    <input type="password" name="password" class="form-control" placeholder="••••••••" required>
                                </div>
                                <button type="submit" class="btn btn-neutral w-100 shadow-sm">Ingresar</button>
                            </form>
                            
                            <div class="text-center mt-3">
                                <a href="/" class="small">Volver al Panel Principal</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        return f"""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .alert-neutral {{
                background-color: #f8f9fa;
                border: 1px solid #495057;
                color: #495057;
            }}
            .btn-neutral {{
                background-color: #495057;
                color: #ffffff;
                border: none;
                text-decoration: none;
            }}
            .btn-neutral:hover {{
                background-color: #3d4550;
                color: #ffffff;
            }}
        </style>
        <div class="container mt-5 text-center">
            <div class="alert-neutral d-inline-block p-4 shadow-sm" role="alert">
                <h4 class="fw-bold">Registro</h4>
                <hr>
                <p class="mb-0">El correo <strong>{email}</strong> fue procesado.</p>
                <a href="/" class="btn btn-neutral btn-sm mt-3">Volver al Inicio</a>
            </div>
        </div>
        """

    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Registro de Usuario (Inseguro)</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
            }
            .btn-neutral {
                background-color: #495057;
                color: #ffffff;
                border: none;
                font-weight: 500;
            }
            .btn-neutral:hover {
                background-color: #3d4550;
                color: #ffffff;
            }
            a {
                color: #495057;
            }
            a:hover {
                color: #3d4550;
            }
        </style>
    </head>
    <body>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-4">
                    <div class="card shadow-sm border-0 mt-5">
                        <div class="card-body p-4">
                            <h3 class="card-title text-center fw-bold mb-4" style="color: #495057;">Crear Cuenta</h3>
                            
                            <form action="http://localhost:8080/register" method="POST">
                                <div class="mb-3">
                                    <label class="form-label fw-semibold">Correo Electrónico</label>
                                    <input type="email" name="email" class="form-control" placeholder="correo@ejemplo.com" required>
                                </div>
                                <div class="mb-4">
                                    <label class="form-label fw-semibold">Contraseña Nueva</label>
                                    <input type="password" name="password" class="form-control" placeholder="••••••••" required>
                                </div>
                                <button type="submit" class="btn btn-neutral w-100 shadow-sm">Registrarse</button>
                            </form>
                            
                            <div class="text-center mt-3">
                                <a href="/" class="small">Volver al Panel Principal</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """