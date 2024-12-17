from rest_framework import serializers

class Validate():
    
    @staticmethod
    def is_valid_length(expected, received):
        if expected > len(received):
            raise  serializers.ValidationError(f'Longitud del campo insuficiente, logitud minima {expected}')
        
            