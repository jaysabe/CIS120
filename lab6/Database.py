# defines Database Class

class Database:
    @classmethod
    def read_names(cls):
        # stubbed method to begin with
        names_data = [
            {"name": "Lindsay", "year": 1915, "gender": "F", "count": 47877},
            {"name": "Jose", "year": 1906, "gender": "M", "count": 422145},
            {"name": "Casey", "year": 1932, "gender": "F", "count": 489123},
            {"name": "Landon", "year": 1943, "gender": "M", "count": 821132}
        ]
        return names_data
