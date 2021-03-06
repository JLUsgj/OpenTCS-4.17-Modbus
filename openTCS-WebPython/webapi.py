import requests
import json
import uuid

class opentcs:
    def __init__(self, kernel_address="127.0.0.1"):
        self.kernel_address = kernel_address
        self.vehicles = []
        self.orders = []
    def send_request(self, request_url, data1="", method="GET"):
        try:
            if(method == "GET"):
                response = requests.get(
                    url=request_url, data=data1
                    )
                return response
            elif(method == "POST"):
                print(request_url)
                response = requests.post(
                    url=request_url, headers={
                        "Content-Type": "application/json; charset=utf-8",
                    },
                    data=data1
                )
                return response
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
    def get_vehicle(self, vehicle=""):
        # if(vehicle == null):
        rec = self.send_request(request_url="http://{}:55200/v1/vehicles".format(self.kernel_address))
        self.vehicles = json.loads(rec.content)
    def get_orders(self, order=""):
        rec = self.send_request(request_url="http://{}:55200/v1/transportOrders".format(self.kernel_address))
        # print(rec)
        if rec.ok == False:
            return -1
        self.orders = json.loads(rec.content)
        return self.orders
    def get_vehicles_status(self):
        vehicles_status = []
        if(self.vehicles == []):
            return null
        for vehicle in self.vehicles:
            status = []
            status.append(vehicle['name'])
            status.append(vehicle['energyLevel'])
            status.append(vehicle['integrationLevel'])
            # status.append(vehicle['procState'])
            status.append(vehicle['procState'])
            status.append(vehicle['transportOrder'])
            status.append(vehicle['currentPosition'])
            status.append(vehicle['state'])
            vehicles_status.append(status)
        return vehicles_status
    def get_orders_status(self):
        orders_status = []
        if(self.orders == []):
            return null
        for order in orders:
            order_status = []
            order_status.append(order["state"])
            order_status.append(order["processingVehicle"])
            orders_status.append(order_status)
        return orders_status
    def creat_order(self, vehicle="", locations = []):
        locations_json = {"destinations":[]}
        for location in locations:
            location_1 = {"locationName": "{}".format(location[0])}
            location_1.update({"operation": "{}".format(location[1])})
            locations_json["destinations"].append(location_1)
        # print(locations_json)
        data2 = json.dumps(locations_json)
        # print(data2)
        respons = self.send_request(request_url="http://{}:55200/v1/transportOrders/Move-{}".format(self.kernel_address, str(uuid.uuid1())[:13]), data1=data2, method="POST")
        return respons
        # print(respons.text)

if __name__ == "__main__":
    tcs = opentcs("127.0.0.1")
    # tcs.get_vehicle()
    print(tcs.get_orders())
    # print(tcs.vehicles[1])
    # print(tcs.orders)
    # print(tcs.get_vehicles_status())
    tcs.creat_order(locations=[["D", "NOP"]])
    # for a in tcs.vehicles[1]:
    #     print("name: {}, value: {}".format(a, tcs.vehicles[1][a]))