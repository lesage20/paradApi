import datetime

def calculate_days(checkIn, checkOut):
        """
        Calcule le nombre de jours selon les règles suivantes :
        - Si le client arrive avant 4h :
          * Sortie avant 13h = 1 jour
          * Sortie après 13h = 2 jours
        - Si le client arrive après 4h :
          * Sortie avant 13h le lendemain = 1 jour
          * Sortie après 13h le lendemain = 2 jours
        """
        # On normalise les dates pour ignorer l'heure d'arrivée
        check_in_date = checkIn
        check_out_date = checkOut
        
        # On vérifie les heures d'arrivée et de départ
        check_in_hour = checkIn.hour
        check_out_hour = checkOut.hour
        
        # Calcul du nombre de jours de base
        days = (check_out_date - check_in_date).days
        
        if check_in_hour < 4:
            # Arrivée avant 4h
            if check_out_hour >= 13:
                days += 1
                
        else:
            # Arrivée après 4h
            # Si c'est le même jour
            if check_in_date == check_out_date:
                days = 1
            # Si c'est le lendemain
            elif (check_out_date - check_in_date).days == 1:
                if check_out_hour >= 13:
                    days = 2
                else:
                    days = 1
            # Si plus d'un jour
            else:
                if check_out_hour >= 13:
                    days += 1
            
        return max(1, days)  # On retourne au minimum 1 jour

if __name__ == "__main__":
    print(calculate_days(datetime.datetime(2025, 6, 13, 3, 0), datetime.datetime(2025, 6, 13, 18, 0)))