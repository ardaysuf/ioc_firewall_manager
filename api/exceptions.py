class APIConnectionError(Exception):
    """API bağlantısı kurulamadı."""
    pass


class APIResponseError(Exception):
    """API beklenmeyen HTTP kodu döndürdü."""
    pass
