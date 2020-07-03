import getpass
from datetime import datetime
def user_date():
    now = datetime.now()
    x = getpass.getuser()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Modified By {} On {}".format(x, dt_string))
user_date()
