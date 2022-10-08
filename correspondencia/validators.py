from django.core.exceptions import ValidationError

def validar_correlativo(value):
     if value < 1:
        raise ValidationError(
            '%(value)s No puede ser Menor a 1',
            params={'value':value}
        )

def validar_gestion(value):
     if value < 2022:
        raise ValidationError(
            '%(value)s La gestion no puede ser Menor a 2022',
            params={'value':value}
        )


def validar_cite(value):
     if value.find("MDPyEP")== -1:
        raise ValidationError(
            '%(value)s no es correcta ej:INF/MDPyEP/001-5421',
            params={'value':value}
        )