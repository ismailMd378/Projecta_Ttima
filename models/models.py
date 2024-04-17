from odoo import models, fields

class Cases(models.Model):
    _name = 'rutas_bicicleta.cases'
    _description ='Taula de cases'
    CodiCasa = fields.Char('Codi Casa', size=3)
    NIF = fields.Char('Codi Persona', size=9)
    NomCasa = fields.Char('Nom', size=50)
    NomPersona = fields.Char('Nom de Persona', size=50)
    NomPersona2 = fields.Char('Nom de Persona2', size=50)
    Telefons = fields.Char('Telefons', size=50)
    cc = fields.Integer('cc', size=10)
    Ubicacio = fields.Char('Ubicacio', size=50)
    Adressa = fields.Char('Adressa', size=50)
    Poblacio = fields.Char('Poblacio', size=30)
    CP = fields.Char('C.P', size=5)
    Foto = fields.Object('Foto')



class Habitacions(models.Model):
    _name = 'rutas_bicicleta.habitacions'
    _description ='Taula de Habitacions'
    CodiHabitacio = fields.Char('Codi Habitacio', size=6)
    CodiCasa = fields.Char('Codi Casa', size=3)
    Num_llits = fields.Integer('Num_llits', size=3)
    Bany = fields.Boolean('Bany')
    Observacions = fields.Char('Observacions', size=50)



class Intermediaris (models.Model):
    _name = 'rutas_bicicleta.intermediaris'
    _description ='Taula de Intermediaris'
    CodiIntermidiari = fields.Char('Codi Intermidiari', size=4)
    Nom = fields.Char('Nom', size=50)
    Adressa = fields.Char('Adressa', size=50)
    Poblacio = fields.Char('Poblacio', size=30)
    CP = fields.Char('C.P', size=5)
    Pais = fields.Char('Pais', size=30)
    Telefons = fields.Char('Telefons', size=50)
    PersonaContacte = fields.Char('Persona de Contacte', size=50)


class Grups(models.Model):
    _name = 'rutas_bicicleta.grups'
    _description ='Taula de Grups'
    
    CodiGrup = fields.Char('Codi Grups', size=6,required=True)
    CodiPersonalEnCap = fields.Many2One('Personal.model', string='Personal en Cap')
    Adressa = fields.Char('Adressa', size=50)
    Poblacion = fields.Char('Poblacion', size=30)
    CP = fields.Char('Codi Postal', size=5)
    Pais = fields.Char('Pais', size=30)
    Telefons = fields.Char('Telefons', size=30)
    Num_Persones = fields.Integer('Num_Persones')
    Observacions = fields.Char('Observacions', size=50)


class Persona(models.Model):
    _name = 'rutas_bicicleta.persona'
    _description ='Taula de Persona'
    
    CodiPersona = fields.Char('Codi Persona', size=7)
    Nom = fields.Char('Nom', size=50),
    AnyNaixement = fields.Integer('Any de Naixement')



class Reserves(models.Model):
    _name = 'rutas_bicicleta.reserves'
    _description = 'Taula de Reserves'
     
    CodiReserva = fields.Char('Codi Reserva' , size=7, required=True)
    DataArrivada = fields.Date('Date Arivada')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis')
    DataReserva = fields.Date('Data Reserva')
    CodiIntermidiari = fields.Many2one('Intermidiari.model', string = 'Codi_Intermidiari')
    CodiGrup = fields.Many2one('Codi.grup', string='Code Groupe')
    GrupRuta = fields.Many2one('Codi.Ruta', string = 'Codi Ruta')
    CodiTarifa = fields.Many2one('Codi.Tarifa', string = 'Codi Tarifa')




class rutes(models.Model):
    _name = 'rutas_bicicleta.rutes'
    _description ='Taula de Rutes'
    
    CodiRutes = fields.Integer('Codi Rutes',size=4)
    Nom = fields.Char('Nom', size=40)
    Preu = fields.Integer('Preu', size=7)
