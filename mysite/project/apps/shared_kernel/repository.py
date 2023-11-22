from apps.database.orm import Base

class RDBRepository:
    @staticmethod
    def add(session, instance: Base):
        return session.add(instance)

    @staticmethod
    def commit(session):
        return session.commit()


class RDBReadRepository:
    pass
