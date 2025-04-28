class GoodWeData:
    def __init__(self, status=None, production=None, battery_level=None):
        self.status = status
        self.production = production
        self.battery_level = battery_level

    def to_dict(self):
        return {
            'status': self.status,
            'production': self.production,
            'battery_level': self.battery_level
        }
