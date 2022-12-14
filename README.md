<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>``
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
<span></span>
</div>

<div aling="center">
<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Django - Rest</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>06</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA DE PRESENTACIÓN: </td><td>11-Ago-2022</td><td>HORA DE PRESENTACIÓN: </td><td colspan="3"></td>
</tr>
<tr><td colspan="4">INTEGRANTE(S): 
<ul>
<li>ACO TITO, Anthony Edwin (aacot@unsa.edu.pe)</li>
<li>CALCINA PUMA, Esteven Antonio (ecalcinap@unsa.edu.pe)</li>
<li>CHAMBILLA PERCA, Valentina Milagros (vchambillap@unsa.edu.pe)</li>
<li>GALVEZ QUILLA, Henry Isaias (hgalvezq@unsa.edu.pe)</li>
</ul>
</td>
<td>NOTA: </td>
<td width="150"></td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe (rescobedoq@unsa.edu.pe)</li>
</ul>
</td>
</<tr>
</tdbody>
</table>
</div>


**DJANGO REST FRAMEWORK** 

API GET en formato JSON del API

![api](imagenes/api.jpg)

API GET de los estududiantes, mostrandonos su: Código, Código del tutor, Nombre, Apellido, Dirección, Teléfono, Tipo de Documento, Nro de DOcumento y Fecha de Nacimineto.

![api_alumnos](imagenes/api_alumnos.jpg)

API GET que nos muestra los detalles tanto de Cantidad de Cursos, Cantidad de Alumnos, Cantidad de Padres, Cantidad de Profesores, Monto Total de Cursos y el monto total de honorarios al docente.

![api_detail](imagenes/api_detail.jpg)

Contamos con un único usuario administrador, por medio del GET revizamos los datos que se tienen registrados.

![administradores](imagenes/administradores.jpg)

API GET donde se obtienen los Código de Curso, Codigo de Profesor, Nombre, Precio, Fecha de Inicio y Fecha Fin.

![cursos](imagenes/cursos.jpg)

API GET profesor donde se nos proporcionan los siguientes datos: Codigo Profesor, Nombres, Apellidos, Tipo de DOcumento y Num de Documento.

![docente](imagenes/docente.jpg)

API GET de los registros Donde Principalmente tenemos el Num del Registro, Codigo del Alumno y Código del DOcente que impartira dicho curso.

![matriculas](imagenes/matriculas.jpg)

Prueba del API PUT del Tutor con Código 1

![tutor](imagenes/tutor.jpg)

API GET de Honorarios

![honorarios](imagenes/honorarios.jpg)

API POST del Admin, siendo validado

![login1](imagenes/login1.jpg)

API POST de daots incorrectos, siendo rechazado.

![login2](imagenes/login2.jpg)
