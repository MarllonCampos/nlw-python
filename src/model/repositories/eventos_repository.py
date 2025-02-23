from src.model.entities.eventos import Eventos
from src.model.configs.connection import DBConnectionHandler

class EventosRepository:
    def insert(self,event_name:str) -> None:
        with DBConnectionHandler() as DB:
            try:
                new_event = Eventos(nome=event_name)
                DB.session.add(new_event)
                DB.session.commit()
            except Exception as exception:
                DB.session.rolback()
                raise exception
            
    def select_event(self,event_name:str) -> Eventos:
        with DBConnectionHandler() as DB:
            data = (
                DB.session
                .query(Eventos)
                .filter(Eventos.nome == event_name)
                .one_or_none()
            )
            return data