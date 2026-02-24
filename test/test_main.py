from fastapi.testclient import TestClient
from main import app

# Creamos un "cliente falso" que simulará ser nuestro navegador o Swagger
client = TestClient(app)

# --- PRUEBA 1: Verificar que el Login funciona ---
def test_login_exitoso():
    # Simulamos llenar el formulario de Swagger con el usuario Mau
    # NOTA: Cambia "tu_contraseña_real" por la contraseña que le pusiste a Mau
    response = client.post(
        "/login/",
        data={"username": "Naruto@oasis.game", "password": "contrasena123"}
    )
    
    # Comprobamos que el servidor responda con un 200 (Éxito)
    assert response.status_code == 200
    
    # Comprobamos que la respuesta contenga el token
    json_response = response.json()
    assert "access_token" in json_response
    assert json_response["token_type"] == "bearer"

# --- PRUEBA 2: Verificar la seguridad (Candado cerrado) ---
def test_obtener_usuarios_sin_token():
    # Intentamos entrar a la ruta de usuarios sin iniciar sesión
    response = client.get("/usuario/")
    
    # Comprobamos que el servidor nos rechace con un 401 (No autorizado)
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

# --- PRUEBA 3: Verificar la seguridad (Candado abierto con Token) ---
def test_obtener_usuarios_con_token():
    # Paso A: Hacemos login para conseguir la "llave"
    login_response = client.post(
        "/login/",
        data={"username": "Naruto@oasis.game", "password": "contrasena123"}
    )
    token = login_response.json()["access_token"]
    
    # Paso B: Preparamos la cabecera de autorización con el token
    headers = {"Authorization": f"Bearer {token}"}
    
    # Paso C: Hacemos la petición enviando la cabecera
    response = client.get("/usuario/", headers=headers)
    
    # Comprobamos que ahora sí nos deje pasar y nos devuelva una lista
    assert response.status_code == 200
    assert isinstance(response.json(), list) # Comprueba que es una lista de usuarios