import os
import sys
import time
from calendar import calendar, monthrange
from datetime import datetime, timedelta


class DataBackup:
    def __init__(self, num_days, week_day, path):
        self.num_days = num_days
        self.week_day = week_day
        self.path = path

    # ----------------------------------------------------------------------
    def remove(self,path):
        if os.path.isdir(path):
            pass
        else:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except OSError:
                print("Unable to remove file: ", path)

    # ----------------------------------------------------------
    def show_last_date_of_month(self,today):
        return today.replace(day=monthrange(today.year, today.month)[1])

    # ----------------------------------------------------------------------
    def cleanup(self):

        for dir_Name in os.walk(self.path):

            if 'bucket' in dir_Name[0]:
                self.path = dir_Name[0]
                # For time-being new_date=2020-09-18
                new_date = '2020-09-18'
                new_date = datetime.strptime(new_date, '%Y-%m-%d').date()
                new_date1 = new_date - timedelta(days=num_days)

                days_collection = []

                for i in range(self.num_days):
                    day = new_date - timedelta(days=self.week_day + 1, weeks=i)
                    days_collection.append(day)

                for files in os.walk(self.path, topdown=False):

                    for f in (files[2]):
                        date1 = (f[f.index('2020'): f.index('.txt')])
                        date1 = datetime.strptime(date1, '%Y-%m-%d').date()
                        if new_date1 > date1 != self.show_last_date_of_month(date1) and date1 not in days_collection:
                            p_new = (self.path + '\\' + f)
                            self.remove(p_new)

                print("Files removed from ", self.path)


# ----------------------------------------------------------------------
# Driver Code
if __name__ == "__main__":
    
    num_days = int(input("Enter number of days - "))
    week_day = int(input("Enter weekday - ( 0 = Monday and 6 = Sunday ) - "))
    
    # Path = 'C:\Users\Aayushii\Desktop\Python Data Backup Task'
    path = input("Enter Path - ")
    print('--' * 20)
    obj1 = DataBackup(num_days, week_day, path)
    obj1.cleanup()
