def lala(s: str,t : str) -> bool:
        se = sorted(s)
        te = sorted(t)
        if se==te:
            return False
        return True    

lala('ate','eat')        