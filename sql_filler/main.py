from ui.ui import UI
from services.postgresservice import PostgresService
from services.data_service import DataService

pos = PostgresService()
data_service = DataService(pos)
ui = UI(data_service=data_service)
ui.mainloop()

