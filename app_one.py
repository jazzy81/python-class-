import requests
class IRCTC:

    def __init__(self):

        user_input = input("""indian railway welcomes you
                            Enter 1 to check live train status
                            Enter 2  to check PNR
                            Enter 3 to check train schedule""")

        if user_input == "1":
           print("live train status")
        elif user_input == "2":
           print("PNR")
        else:
           self.train_schedule()
    def train_schedule(self):
        train_no=input("Enter the train number")
        self.fetch_data(train_no)

    def fetch_data(self,train_no):

     data =requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/749b97168562f85331bcb8f0716c856e/TrainNumber/{}".format(train_no))
     data=data.json()
     print(data["Route"])


     for i in data["Route"]:
          print(i["StationName"],"||",i["ArrivalTime"],"||",i["Departure433Time"],"||",i["Distance"])

visitor = IRCTC()