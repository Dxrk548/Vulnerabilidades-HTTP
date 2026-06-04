from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
            }
            .navbar-custom {
                background-color: #495057 !important;
            }
            .btn-neutral {
                background-color: #495057;
                color: #ffffff;
                border: none;
                text-decoration: none;
            }
            .btn-neutral:hover {
                background-color: #3d4550;
                color: #ffffff;
            }
        </style>
    </head>
    <body>
        <nav class="navbar shadow-sm navbar-custom">
            <div class="container">
                <span class="navbar-brand mb-0 h1" style="color: #ffffff;">Testing</span>
            </div>
        </nav>

        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-8 text-center">
                    
                    <div class="row mt-4">
                        <div class="col-md-6 mb-4">
                            <div class="card h-100 shadow-sm border-0">
                                <div class="card-body d-flex flex-column justify-content-between p-4">
                                    <a href="/login" class="btn btn-neutral w-100 mt-4">Login</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-md-6 mb-4">
                            <div class="card h-100 shadow-sm border-0">
                                <div class="card-body d-flex flex-column justify-content-between p-4">
                                    <a href="/register" class="btn btn-neutral w-100 mt-4">Registrarse</a>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </body>
    </html>
    """