class FlightData:
    def __init__(self, price, start_city, final_city, start_airport, final_airport, start_date, final_date, stop_overs=0, via_city=""):
        self.price = price
        self.start_city = start_city
        self.final_city = final_city
        self.start_airport = start_airport
        self.final_airport = final_airport
        self.start_date = start_date
        self.final_date = final_date
        self.stop_overs = stop_overs
        self.via_city = via_city
