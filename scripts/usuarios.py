from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crea usuarios personalizados'

    def handle(self, *args, **options):
        users_data = [
    {'username': 'itcelaya', 'email': 'itcelaya@example.com', 'password': 'celaya2023', 'first_name': 'Instituto Tecnológico de Celaya'},
    {'username': 'itmorelia', 'email': 'itmorelia@example.com', 'password': 'morelia2023', 'first_name': 'Instituto Tecnológico de Morelia'},
    {'username': 'ittepic', 'email': 'ittepic@example.com', 'password': 'tepic2023', 'first_name': 'Instituto Tecnológico de Tepic'},
    {'username': 'itmerida', 'email': 'itmerida@example.com', 'password': 'merida2023', 'first_name': 'Instituto Tecnológico de Mérida'},
    {'username': 'itnuevolaredo', 'email': 'itnuevolaredo@example.com', 'password': 'nuevolaredo2023', 'first_name': 'Instituto Tecnológico de Nuevo Laredo'},
    {'username': 'itspurisima', 'email': 'itspurisima@example.com', 'password': 'purisima2023', 'first_name': 'Instituto Tecnológico Superior de Purísima del Rincón'},
    {'username': 'itsguanajuato', 'email': 'itsguanajuato@example.com', 'password': 'guanajuato2023', 'first_name': 'Instituto Tecnológico Superior de Sur de Guanajuato'},
    {'username': 'itpuebla', 'email': 'itpuebla@example.com', 'password': 'puebla2023', 'first_name': 'Instituto Tecnológico de Puebla'},
    {'username': 'ithermosillo', 'email': 'ithermosillo@example.com', 'password': 'hermosillo2023', 'first_name': 'Instituto Tecnológico de Hermosillo'},
    {'username': 'ittijuana', 'email': 'ittijuana@example.com', 'password': 'tijuana2023', 'first_name': 'Instituto Tecnológico de Tijuana'},
    {'username': 'itmochis', 'email': 'itmochis@example.com', 'password': 'mochis2023', 'first_name': 'Instituto Tecnológico de Los Mochis'},
    {'username': 'itssanluispotosi', 'email': 'itssanluispotosi@example.com', 'password': 'sanluispotosi2023', 'first_name': 'Instituto Tecnológico Superior de San Luis Potosí, Capital'},
    {'username': 'itzacatepec', 'email': 'itzacatepec@example.com', 'password': 'zacatepec2023', 'first_name': 'Instituto Tecnológico de Zacatepec'},
    {'username': 'itnogales', 'email': 'itnogales@example.com', 'password': 'nogales2023', 'first_name': 'Instituto Tecnológico de Nogales'},
    {'username': 'itlapaz', 'email': 'itlapaz@example.com', 'password': 'lapaz2023', 'first_name': 'Instituto Tecnológico de La Paz'},
    {'username': 'itmadero', 'email': 'itmadero@example.com', 'password': 'madero2023', 'first_name': 'Instituto Tecnológico de Ciudad Madero'},
    {'username': 'itdurango', 'email': 'itdurango@example.com', 'password': 'durango2023', 'first_name': 'Instituto Tecnológico de Durango'},
    {'username': 'itchihuahua', 'email': 'itchihuahua@example.com', 'password': 'chihuahua2023', 'first_name': 'Instituto Tecnológico de Chihuahua'},
    {'username': 'ittuxtla', 'email': 'ittuxtla@example.com', 'password': 'tuxtla2023', 'first_name': 'Instituto Tecnológico de Tuxtla Gutiérrez'},
    {'username': 'itlaguna', 'email': 'itlaguna@example.com', 'password': 'laguna2023', 'first_name': 'Instituto Tecnológico de La Laguna'},
    {'username': 'itlcardenas', 'email': 'itlcardenas@example.com', 'password': 'lcardenas2023', 'first_name': 'Instituto Tecnológico de Lázaro Cárdenas'},
    {'username': 'itpnegras', 'email': 'itpnegras@example.com', 'password': 'pnegras2023', 'first_name': 'Instituto Tecnológico de Piedras Negras'},
    {'username': 'itvillahermosa', 'email': 'itvillahermosa@example.com', 'password': 'villahermosa2023', 'first_name': 'Instituto Tecnológico de Villahermosa'},
    {'username': 'itcomitan', 'email': 'itcomitan@example.com', 'password': 'comitan2023', 'first_name': 'Instituto Tecnológico de Comitán'},
    {'username': 'itescarbonifera', 'email': 'itescarbonifera@example.com', 'password': 'carbonifera2023', 'first_name': 'Instituto Tecnológico de Estudios Superiores de La Región Carbonífera'},
    {'username': 'ittoluca', 'email': 'ittoluca@example.com', 'password': 'toluca2023', 'first_name': 'Instituto Tecnológico de Toluca'},
    {'username': 'itsteziutlan', 'email': 'itsteziutlan@example.com', 'password': 'teziutlan2023', 'first_name': 'Instituto Tecnológico Superior de Teziutlán'},
    {'username': 'itspuruandiro', 'email': 'itspuruandiro@example.com', 'password': 'puruandiro2023', 'first_name': 'Instituto Tecnológico Superior de Puruándiro'},
    {'username': 'tesecatepec', 'email': 'tesecatepec@example.com', 'password': 'ecatepec2023', 'first_name': 'Tecnológico de Estudios Superiores de Ecatepec'},
    {'username': 'itshuatusco', 'email': 'itshuatusco@example.com', 'password': 'huatusco2023', 'first_name': 'Instituto Tecnológico Superior de Huatusco'},
    {'username': 'ittehuacan', 'email': 'ittehuacan@example.com', 'password': 'tehuacan2023', 'first_name': 'Instituto Tecnológico de Tehuacán'},
    {'username': 'itsmonclova', 'email': 'itsmonclova@example.com', 'password': 'monclova2023', 'first_name': 'Instituto Tecnológico Superior de Monclova'},
    {'username': 'itstexmelucan', 'email': 'itstexmelucan@example.com', 'password': 'texmelucan2023', 'first_name': 'Instituto Tecnológico Superior de San Martín Texmelucan'},
    {'username': 'itistmo', 'email': 'itistmo@example.com', 'password': 'istmo2023', 'first_name': 'Instituto Tecnológico del Istmo'},
    {'username': 'ittlaxiaco', 'email': 'ittlaxiaco@example.com', 'password': 'tlaxiaco2023', 'first_name': 'Instituto Tecnológico de Tlaxiaco'},
    {'username': 'itcuauhtemoc', 'email': 'itcuauhtemoc@example.com', 'password': 'cuauhtemoc2023', 'first_name': 'Instituto Tecnológico de Ciudad Cuauhtémoc'},
    {'username': 'itguzman', 'email': 'itguzman@example.com', 'password': 'guzman2023', 'first_name': 'Instituto Tecnológico de Ciudad Guzmán'},
    {'username': 'itobregon', 'email': 'itobregon@example.com', 'password': 'obregon2023', 'first_name': 'Instituto Tecnológico de Álvaro Obregón'},
    {'username': 'itsvalladolid', 'email': 'itsvalladolid@example.com', 'password': 'valladolid2023', 'first_name': 'Instituto Tecnológico Superior de Valladolid'},
    {'username': 'itsjerez', 'email': 'itsjerez@example.com', 'password': 'jerez2023', 'first_name': 'Instituto Tecnológico Superior de Jerez'},
    {'username': 'itspapasquiaro', 'email': 'itspapasquiaro@example.com', 'password': 'papasquiaro2023', 'first_name': 'Instituto Tecnológico Superior de Santiago Papasquiaro'},
    {'username': 'itsyucatan', 'email': 'itsyucatan@example.com', 'password': 'yucatan2023', 'first_name': 'Instituto Tecnológico Superior de Sur del Estado de Yucatán'},
    {'username': 'itspedrocolonias', 'email': 'itspedrocolonias@example.com', 'password': 'pedrocolonias2023', 'first_name': 'Instituto Tecnológico Superior de San Pedro de las Colonias'},
    {'username': 'itocotlan', 'email': 'itocotlan@example.com', 'password': 'ocotlan2023', 'first_name': 'Instituto Tecnológico de Ocotlán'},
    {'username': 'itzitacuaro', 'email': 'itzitacuaro@example.com', 'password': 'zitacuaro2023', 'first_name': 'Instituto Tecnológico de Zitácuaro'},
    {'username': 'itsabasolo', 'email': 'itsabasolo@example.com', 'password': 'abasolo2023', 'first_name': 'Instituto Tecnológico Superior de Abasolo'},
]


        for data in users_data:
            try:
                user = User.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password=data['password'],
                    first_name=data['first_name']
                )
                self.stdout.write(self.style.SUCCESS(f'Usuario "{data["username"]}" creado exitosamente.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear el usuario "{data["username"]}": {str(e)}'))
