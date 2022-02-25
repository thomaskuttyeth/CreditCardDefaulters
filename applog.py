

from datetime import datetime

class AppLogger:
    def __init__(self):
        pass
    
    def log(self,file_object,message):
        self.now = datetime.now()
        self.date = datetiem.date()
        self.current_time = self.now.strftime("%H:%M:%s")
        file_object.write(f"{str(self.date)}-{str(self.current_time)}-{message}")
        
        
        