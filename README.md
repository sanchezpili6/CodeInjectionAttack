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

### Correr programa
- Abre la terminal dentro del proyecto
- make build
- make run
- puedes usar el programa como se supone que funciona, o puedes meter en el parámetro:

```sh
__import__('os').system('mkdir dirPrueba')
```


