from googleapiclient.discovery import build
from database_manager import DatabaseManager
from inventory_manager import FileInventory
from drive_manager import GoogleDriveManager
from notification_manager import NotificationManager

def main():
    # Conectar a la base de datos y crearla si no existe
    db_manager = DatabaseManager()
    connection = db_manager.conexion_a_mysql()
    
    if connection:
        cursor = connection.cursor()
        
        # Crear la base de datos y las tablas si no existen
        db_manager.crear_bd(cursor, db_manager.database_name)
        db_manager.crear_tablas(cursor)
        
        # Inventariar archivos de Google Drive
        inventory_manager = FileInventory(cursor)
        inventory_manager.inventariar_archivos()

        # Cambiar permisos en Google Drive
        drive_manager = GoogleDriveManager()
        drive_manager.cambiar_permisos(cursor)

        # Enviar notificaciones por correo
        notification_manager = NotificationManager()
        notification_manager.enviar_notificaciones(cursor)

        # Cerrar la conexión a la base de datos
        db_manager.cerrar_conexion(cursor)
        connection.close()
    else:
        print("No se pudo conectar a la base de datos.")

if __name__ == "__main__":
    main()


class main:
    def __init__(self):
        self.googleDriveManager = GoogleDriveManager()

    def principal():
        credentials = GoogleDriveManager.authenticate_drive()
        



        #una vez que se encontraron : 
        # 1 - conectarse al servidor local ,
        # 2 - crear el usuario, 
        # 3 - crear la bd y las tablas 

        # 4- cargar los datos si existen se actualiza - SCRIPTS DE ESCRITURA PRIMER TABLA
        # 5 - SCRIPT A SEGUNDA TABLA


        # 6 - SCRIPT DE CAMBIO DE ARCHIVOS PUBLICO A PRIVADO 
        # 7. Script de envio de mails
        # Ejemplo de uso
        # gmail_service = authenticate_mail()
        # if gmail_service:
        #     enviar_notificacion_mail(gmail_service, 'owner_email@example.com', 'archivo_ejemplo.txt')
        #     cerrar_sesion(gmail_service)    


    if __name__ == '__main__':
        main()