from cryptography.fernet import Fernet
import os


class DataDecoder:

    @staticmethod
    def decode_data(data: str) -> str:
        private_key = os.getenv("PRIVATE_KEY")
        fern = Fernet(private_key)
        return fern.decrypt(data).decode()
