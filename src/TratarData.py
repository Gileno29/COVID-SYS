from datetime import datetime


class TratarData:

    def convert_data(self, data):

        if(data == None):
            data = '1999-01-20'
        string = data.split('T')
        print(string)

        nDate = string[0].replace('-', '-')
        print(nDate)
        #date = datetime.strptime(nDate, '%y-%m-%d').date()
        #print(date, type(date))

        return nDate


#data = TratarData()

# data.convert_data('2020-04-01T03:00:00.000Z')
