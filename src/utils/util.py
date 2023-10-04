from datetime import datetime, timedelta, timezone

def formatTime():
        
    # Configuration of the time zone for Brazil (São Paulo)
    timezoneBR = timezone(timedelta(hours=-3))
    
    return datetime.now(timezoneBR).strftime("%d-%m-%Y %H:%M:%S")