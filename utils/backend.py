import requests
import os

backend_url = os.getenv("BACKEND_URL") or "http://localhost:8080"

def backend_request(method, endpoint, token=None, data=None, params=None, timeout=10):
    """
    Maneja peticiones HTTP al backend de forma centralizada.

    Args:
        method (str): Método HTTP (GET, POST, PUT, DELETE, PATCH)
        endpoint (str): Endpoint del backend (por ejemplo, "/users")
        token (str, opcional): Token JWT para autenticación
        data (dict, opcional): Datos JSON para enviar en la petición
        params (dict, opcional): Parámetros para la query string
        timeout (int, opcional): Tiempo máximo de espera en segundos

    Returns:
        dict | list | None: Respuesta JSON del backend o None si hubo error.
    """
    url = f"{backend_url}{endpoint}"
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f"Bearer {token}"

    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            json=data,
            params=params,
            timeout=timeout
        )
        response.raise_for_status()
        if response.text:
            return response.json()
        return None
    except requests.exceptions.Timeout:
        print(f"[Timeout] La petición a {url} tardó demasiado.")
    except requests.exceptions.ConnectionError:
        print(f"[Conexión fallida] No se pudo conectar al backend en {backend_url}.")
    except requests.exceptions.HTTPError as e:
        print(f"[Error HTTP {response.status_code}] {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[Error inesperado] {e}")

    return None
