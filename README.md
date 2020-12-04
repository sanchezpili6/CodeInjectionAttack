# Ataques mediante inyección de código
### Manual 

- Desarrollada en Python 2


### [Instalar docker](https://snapcraft.io/docker)
Ubuntu: 
```sh
$ sudo apt update
$ sudo apt install snapd
$ sudo snap install docker
```

### [Instalar PyCharm](https://snapcraft.io/pycharm-community)
Ubuntu: 
```sh
$ sudo apt update
$ sudo apt install snapd
$ sudo snap install pycharm-community --classic
```

### [Clonar el repositorio](https://github.com/sanchezpili6/CodeInjectionAttack)
- Da click en el subtítulo de arriba
- Click en el botón verde de clonar
- Copia la liga que aparece ahí
- Abre PyCharm 
- Click en "Check out project from Version Control"
- Selecciona la opción de Git
- Pega el URL que copiaste y elige el directorio donde quieres guardarlo
- Click en clonar

Si ya tenías abierto PyCharm y no apareció el "Check out project from Version Control", entonces puedes poner el el buscador de PyCharm "git", darle click en la opción de clonar y ahí pegar el URL

### Correr programa
- Abre la terminal dentro del proyecto
- make build
- make shell
- puedes usar el programa como se supone que funciona, o puedes meter en el parámetro:

```sh
__import__('os').system('mkdir dirPrueba')
```
- revisa la carpeta donde está el proyecto, se debe haber creado una carpeta llamada dirPrueba. 
- si quieres borrar esa carpeta puedes meter un: 
```sh
__import__('os').system('rmdir dirPrueba')
```

