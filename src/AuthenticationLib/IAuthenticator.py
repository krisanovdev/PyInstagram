from abc import ABC, abstractmethod


class IAuthenticator(ABC):
    """Authentication interface"""

    @abstractmethod
    def authenticate(self, username, password):
        """Modify session state so after that call we are authenticated"""
        pass
