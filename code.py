import json
import os

archivo = "psico_db.json"

def guardar_datos():
    datos = {
        "conta_id": conta_id,
        "id_se": id_se,
        "ingres": ingres,
        "users": users,
        "sessions": sessions
    }

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def cargar_datos():
    global conta_id, id_se, ingres, users, sessions

    if not os.path.isfile(archivo):
        return

    with open(archivo, "r", encoding="utf-8") as f:
        datos = json.load(f)

    conta_id = datos.get("conta_id", 1)
    id_se = datos.get("id_se", 1)
    ingres = datos.get("ingres", 0)
    users = datos.get("users", [])
    sessions = datos.get("sessions", [])


ingres = 0
id_se = 1
conta_id = 1

users = [{
  "id": 1,
  "nombre": "Juan Pérez",
  "telefono": "2281234567",
  "correo": "juan@gmail.com",
  "nota": "Ansiedad"
}]




sessions = [
{
  "id": 1,
  "paciente_id": 1,
  "fecha": "2026-05-02",
  "hora": "16:30",
  "duracion_min": 60,
  "costo": 500.0,
  "estado": "completado"   # pendiente / completada / cancelada
}
]




def ver_pacientes():
  if not users:
    print("No hay pacientes")
    return
  for user in users:

    print(f"ID: {user['id']}\nNombre: {user['nombre']}\ntelefono: {user['telefono']}\ncorreo: {user['correo']}\nnota: {user['nota']}")
    for session in sessions:
      print(f"el numero de la sesion es: {session['paciente_id']}")

    print("---------")

def agregar_pacientes():
  global conta_id
  name = input("Dame el nombre del paciente: ")
  if not name:
    print("Nombre invalido")
    return
  number = input("Dame el numero de telefono del paciente: ")
  if not number:
    print("Numero invalido")
    return
  elif len(number) < 10:
    print(f"Numero invalido, el numero cuenta con {len(number)} digitos, lo cual es incorrecto")
    return
  elif len(number) > 10:
    print(f"Numero invalido, el numero cuenta con {len(number)} digitos, lo cual es incorrecto")
    return

  try:
    number = int(number)

  except ValueError:
    print("Numero invalido")
    return


  correo = input("Dame el correo del paciente si es que tiene: ")
  if not correo:
    correo = "No hay correo"


  nota = input("Dame la nota importante del paciente")
  if not nota:
    nota = "No hay nota"


  conta_id += 1
  users.append({
    "id": conta_id,
    "nombre": name,
    "telefono": number,
    "correo": correo,
    "nota": nota
  })



def editar_pacientes():
  global conta_id
  id = input("dame el id del paciente que quieres editar sus datos: ")
  if not id:
    print("Respuesta invalida")
    return
  try:
    id = int(id)
  except ValueError:
    print("respuesta invalida")
    return
  for user in users:
    if user['id'] == id:
      print("Opciones que se pueden cambiar:")
      print("1. Nombre")
      print("2. Telefono")
      print("3. Correo")
      print("4. Nota")
      option_1 = input("Dame el numero que deseas modificar: ")
      if not option_1:
        print("Respuesta invalida")
        return
      try:
        option_1 = int(option_1)
      except ValueError:
        print("Respuesta invalida")

      if option_1 == 1:
        new_name = input("Dame el nombre actualizado: ")
        if not new_name:
          print("Respuesta invalida")
          return
        user['nombre'] = new_name
      elif option_1 == 2:
        new_telefono = input("Dame el telefono actualizado: ")
        if not new_telefono:
          print("Respuesta invalida")
          return
        if len(new_telefono) < 10:
          print("Telefono invalido")
        elif len(new_telefono) > 10:
          print("telefono invalido")
        try:
          new_telefono = int(new_telefono)
        except ValueError:
          print("telefono invalido")
          return
        user['telefono'] = new_telefono

      elif option_1 == 3:
        new_correo = input("Dame el correo actualizado: ")
        if not new_correo:
          print("Respuesta invalida")
          return
        user['correo'] = new_correo
      elif option_1 == 4:
        new_nota = input("Dame la nota actualizada: ")
        if not new_nota:
          print("Respuesta invalida")
          return
        user['nota'] = new_nota



def eliminar_pacientes():
  global conta_id
  global id_se
  id_eliminar = input("Dame el id del paciente a eliminar del registro: ")
  if not id_eliminar:
    print("Respuesta invalida")
    return
  try:
    id_eliminar = int(id_eliminar)
  except ValueError:
    print("Respúesta invalida")
    return
  for user in users:
    if user['id'] == id_eliminar:
      users.remove(user)
      print("Tarea eliminada del registro")

def agendar_session():
    global conta_id
    global id_se

    id_session = input("Dame el id del paciente a agendar: ")
    if not id_session:
      print("Respuesta invalida")
      return

    try:
      id_session = int(id_session)
    except ValueError:
      print("Respuesta invalida")
      return

    # Buscar el paciente
    paciente_encontrado = False
    for user in users:
      if user['id'] == id_session:
        paciente_encontrado = True
        break

    if not paciente_encontrado:
      print("El usuario no existe")
      return

    # Solicitar fecha
    fecha_new = input("Dame la fecha en formato yyyy-mm-dd: ")
    if not fecha_new:
      print("Respuesta invalida")
      return

    # Solicitar hora
    hora_new = input("Dame la hora en formato hh:mm, formato 24 horas: ")
    if not hora_new:
      print("Respuesta invalida")
      return

    # Incrementar ID de sesión
    conta_id += 1
    id_se += 1
    # Agregar sesión
    sessions.append({
      "id": conta_id,
      "paciente_id": id_se,
      "fecha": fecha_new,
      "hora": hora_new,
      "duracion_min": 60,
      "costo": 500.0,
      "estado": "pendiente"
    })

    print(f"✓ Sesión agendada exitosamente con ID: {id_se}")





def ver_sesiones():
  global conta_id
  global id_se
  for sesion in sessions:
    print(f"sesion: {sesion['paciente_id']}\nfecha: {sesion['fecha']}\nhora: {sesion['hora']}")
  for user in users:
    if user['id'] == id_se:
      print(f"Nombre del paciente: {user['nombre']}")
  print("---------")



def ver_sp():
  global conta_id
  global id_se
  user = input("Dame el id del paciente: ")
  if not user:
    print("Respuesta invalida")
    return
  try:
    id_sp = int(user)
  except ValueError:
    print("respuesta invalida")
    return
  for sesion in sessions:
    if sesion['id'] == id_sp:
      if sesion['fecha']:
        print(f"Existe cita para: {sesion['fecha']}, a la hora de:  {sesion['hora']}\n")
        for user in users:
          if user['id'] == id_sp:
            print(f"Nombre del paciente: {user['nombre']}")
            print("---------")


def marcar_completada():
  global conta_id
  global id_se
  id_completada = input("Dame el id de la sesion completada: ")
  if not id_completada:
    print("Respuesta invalida")
    return
  try:
    id_completada = int(id_completada)
  except ValueError:
    print("Respuesta invalida")
    return
  for sesion in sessions:
    if sesion['id'] == id_completada:
      sesion['estado'] = "completado"
      print("Cita completatada")



def cancelar_sesion():
  global conta_id
  global id_se
  cita_eliminada = input("Dame el id de sesion para cancelar: ")
  if not cita_eliminada:
    print("Respuesta invalida")
    return
  try:
    cita_eliminada = int(cita_eliminada)
  except ValueError:
    print("Respuesta invalida")
    return
  for sesion in sessions:
    if sesion['id'] == cita_eliminada:
      sessions.remove(sesion)
      print("Cita cancelada")
      print("----------")


def ingresos():
  global ingres
  for ingreso in sessions:
    if ingreso['estado'] == "completado":
      ingres += 500
      print(f"Los ingresos totales son: {ingres}")


def salir():
  print("Saliendo...")

cargar_datos()
while True:
  print("---opciones---")
  print("1. Ver pacientes")
  print("2. Agregar pacientes")
  print("3. Editar pacientes datos")
  print("4. Eliminar pacientes")
  print("5. Agendar sesion")
  print("6. Ver sesiones")
  print("7. Ver las sesiones de un paciente")
  print("8. Marcar sesion completada")
  print("9. Cancelar o eliminar sesion")
  print("10. Ver ingresos")
  print("11. Salir")



  option = input("Que opcion elige?: ")
  try:
    option = int(option)
    if option < 1 or option > 10:
      print("Respuesta invalida")
      continue

  except ValueError:
    print("Respuesta invalida")
    continue

  if option == 1:
    ver_pacientes()
    guardar_datos()
  elif option == 2:
    agregar_pacientes()
    guardar_datos()
  elif option == 3:
    editar_pacientes()
    guardar_datos()
  elif option == 4:
    eliminar_pacientes()
    guardar_datos()
  elif option == 5:
    agendar_session()
    guardar_datos()
  elif option == 6:
    ver_sesiones()
    guardar_datos()
  elif option == 7:
    ver_sp()
    guardar_datos()
  elif option == 8:
    marcar_completada()
    guardar_datos()
  elif option == 9:
    cancelar_sesion()
    guardar_datos()
  elif option == 10:
    ingresos()
    guardar_datos()
  elif option == 11:
    salir()
    guardar_datos()
    break


