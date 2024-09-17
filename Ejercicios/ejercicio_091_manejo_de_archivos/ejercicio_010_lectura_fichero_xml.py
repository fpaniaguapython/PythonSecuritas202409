from xml.dom import minidom

documento = minidom.parse('pelicula.xml')
print(type(documento)) #<class 'xml.dom.minidom.Document'>

moviesNodeList = documento.getElementsByTagName("movie") #<class 'xml.dom.minicompat.NodeList'>
for movie in moviesNodeList:
    print(movie.getElementsByTagName("title")[0].firstChild.nodeValue)#Acceso al texto contenido en el elemento
    print(movie.getElementsByTagName("year")[0].getAttribute("info"))#Acceso al atributo