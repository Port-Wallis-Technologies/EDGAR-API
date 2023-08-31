"""
all of the classes that interact with SEC financial Data as seen on the edgar website

key classes are :

EDGAR 
EDGAR_COMPANY


"""

class EDGAR():
    """
    class that encapsulates all of the base data for the EDGAR webset maintained by the SEC 
    """
    cik_table = {}
    def __init__(self,company:str=None,
                 refresh:str=None, db:str=None,schema:str=None ) -> None:
        pass
    def fetch_cik_table():
        
class EDGAR_COMPANY():
    pass

