# Hackaton ache.io
Projeto desenvolvido para o Hackaton Ache.io - UFPel 2022

O projeto tem como objetivo principal resolver as filas de espera dos ônibus de 
apoio.

#### Solução
Assumimos que temos a relação de quais aulas ocorrem em cada campus e quais alunos estão
matrículados nessas aulas. (Conseguimos através de um requerimento feito para a UFPEL)
Com acesso a esses dados, usamos calculos estatísticos para estimar a quantidade de alunos
em cada parada de ônibus de apoio em dias específicos. Assim, conseguimos estimar depois 
de um determinado tempo funcionando e com a demostração de interesse de cada aluno qual rota 
teria maior demanda.
Cada motorista terá acesso a um smartphone com acesso a uma págia que irá mostrar a rota que ele
deve seguir e no próprio aplicativo ele fará o controle de entrada dos alunos no ônibus, através
de leitura de código de barra fornecido pelo cobalto, funcionando como uma catraca.

#### Tecnologias
- Python
- Django
- Pandas
- Pyplot
- Mapbox
- Bootstrap
- sqlite3

#### Como testar:
Acesse a pasta `app/` pelo terminal
em seguida dê o seguinte comando :
`python3 manage.py runserver`

No navegador, acesse: `http://127.0.0.1:8000/`

#### Páginas
Na página principal, será mostrado os ônibus disponíveis de acordo com a grade 
do aluno no horário atual e a quantidade de lugares disponíveis.

Na página agendamento `http://127.0.0.1:8000/agendamento` o aluno pode sinalizar
quando e qual rota ele usaria (pseudo agendamento).

Na página motorista `http://127.0.0.1:8000/motorista` seria a página a qual o motorista
teria as informações de sua rota e suas informações gerais.

