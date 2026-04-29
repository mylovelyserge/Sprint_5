import uuid


def generate_email():
    """Генерирует уникальный email для каждого теста регистрации."""
    unique_id = uuid.uuid4().hex[:8]
    return f"testuser_{unique_id}@example.com"
