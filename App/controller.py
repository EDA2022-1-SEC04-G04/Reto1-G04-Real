"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from gettext import Catalog
from msilib.schema import Control
from ossaudiodev import control_labels
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def nuevoControlador():
    control ={ "model": None}
    control["model"]= model.newCatalog()

return Control

# Inicialización del Catálogo de libros

def CargarDatos(control):

catalog=control["model"]
movies, authors= loadMovies(catalog)

return movies, authors
def loadMovies(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    moviesfile = cf.data_dir + 'streaming/mazon_prime_titles-utf8-small.csv'
    input_file = csv.DictReader(open(moviesfile, encoding='utf8'))
    for movie in input_file:
        model.addMovie(catalog, movie)
    return model.MovieSize(catalog), model.authorSize(catalog)


# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
