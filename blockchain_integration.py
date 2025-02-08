import datetime
import hashlib

class BlockchainIntegration:
    def __init__(self):
        self.chain = []

    def record_event(self, data, message):
        timestamp = datetime.datetime.now().isoformat()
        record = f"{timestamp}: {data} - {message}"
        hash_record = hashlib.sha256(record.encode()).hexdigest()
        block = {'timestamp': timestamp, 'data': data, 'message': message, 'hash': hash_record}
        self.chain.append(block)
        print("Blockchain record added:", block)
