from database import Base


class BaseModel(Base):
    """
    Base model
    """
    __abstract__ = True

    def save_to_db(self) -> None:
        pass

    def delete_from_db(self) -> None:
        pass
