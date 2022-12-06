class consulta:
    def __init__(self, nombres, apellidos, dni, edad, celular, correo, razon):
        self.nombres=nombres
        self.apellidos=apellidos
        self.dni=dni
        self.edad=edad
        self.celular=celular
        self.correo=correo
        self.razon=razon
    def __str__(self):
        return "{} {} de {} años, identificado con {}.\nPuede llamarlo al {} a hablarle a su correo {}.\nLa razón de su consulta es:\n{}".format(self.nombres,self.apellidos,self.edad,self.dni,self.celular,self.correo,self.razon)