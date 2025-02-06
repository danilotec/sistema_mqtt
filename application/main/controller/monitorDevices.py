from datetime import datetime, timedelta
import pytz
from typing import Dict, List, Optional
from functools import cache
from dataclasses import dataclass, field

@dataclass
class IoTDevice:
    id: str
    expected_interval: timedelta = field(
                                    default_factory=lambda: timedelta(hours=1))
    last_message: Optional[datetime] = None
    status: str = "UNKNOWN"
    received_messages: int = 0

@cache
class IoTMonitoring:
    def __init__(self):
        self.devices: Dict[str, IoTDevice] = {}
        self.timezone = pytz.timezone('America/Sao_Paulo')
    
    def register_device(self, device_id: str) -> IoTDevice:
        if device_id not in self.devices:
            self.devices[device_id] = IoTDevice(id=device_id)
            print(f"Device {device_id} successfully registered")
        return self.devices[device_id]
    
    def register_message(self, device_id: str, 
                         timestamp: datetime = None):#type: ignore
        
        if timestamp is None:
            timestamp = datetime.now(self.timezone)
            
        device = self.register_device(device_id)
        device.last_message = timestamp
        device.status = "ONLINE"
        device.received_messages += 1
        print(f"Message registered for device {device_id} at {timestamp}")
    
    def check_devices_status(self) -> List[Dict]:
        now = datetime.now(self.timezone)
        results = []
        
        for device_id, device in self.devices.items():
            if device.last_message is None:
                status = "NEVER_CONNECTED"
                time_without_message = None
            else:
                time_without_message = now - device.last_message
                
                if time_without_message > device.expected_interval * 2:
                    status = "OFFLINE"
                elif time_without_message > device.expected_interval:
                    status = "DELAYED"
                else:
                    status = "ONLINE"
            
            device.status = status
            
            results.append({
                "device_id": device.id,
                "status": status,
                "last_message": device.last_message,
                "time_without_message": time_without_message,
                "total_messages": device.received_messages
            })
        
        return results
    
    def generate_alerts(self, devices_status: List[Dict]) -> List[Dict]:
        alerts = []
        for device in devices_status:
            if device["status"] in ["OFFLINE", "DELAYED"]:
                alerts.append({
                    "level": "CRITICAL" if device["status"] == "OFFLINE" 
                                                            else "WARNING",
                    "device": device["device_id"],
                    "message": f"Device {device['device_id']} is {device['status']}. "
                              f"Last message received: {device['last_message']}"
                })
        return alerts


if __name__ == "__main__":

    monitor = IoTMonitoring()
    
    monitor.register_message("device_001")
    
    special_device = IoTDevice(
        id="special_device",
        expected_interval=timedelta(minutes=30)
    )
    print(f"\nSpecial device created: {special_device}")
    
    old_time = datetime.now(pytz.timezone('America/Sao_Paulo')) - timedelta(hours=2)
    monitor.register_message("device_002", old_time)
    
    status = monitor.check_devices_status()
    alerts = monitor.generate_alerts(status)
    
    print("\nDevices status:")
    for s in status:
        print(f"Device: {s['device_id']}, Status: {s['status']}, "
              f"Total Messages: {s['total_messages']}")
    
    print("\nGenerated alerts:")
    for alert in alerts:
        print(f"{alert['level']}: {alert['message']}")