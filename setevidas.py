
###########AQUI ESTÃO AS IMPORTAÇÕES NECESSÁRIAS PARA ESSE PROJETO!######################
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

#################Sidebar é para constuir o Menu lateral na página...#####################
with st.sidebar:
   
   st.image("https://img.freepik.com/fotos-premium/um-gato-esta-lendo-um-livro-com-uma-folha-verde-na-capa_894855-297.jpg")
   st.write(" :violet[Mr. Bigode]") 
   choose = option_menu("Sete Vidas", ["Iniciar", "Buscador Mr. Bigode", "Novidades", "Portal", "Acervo", "Avaliações", "Sobre Nós"])

#######################TÍTULO DA APLICAÇÃO#####################

st.title("🐾🐾Biblioteca Sete Vidas🐾🐾")
st.image("https://images.alphacoders.com/133/1339726.png")
st.write("---")


######################################################################################################################################################
###############################################################PÁGINAS################################################################################
######################################################################################################################################################

###Página 1  #DESENVOLVENDO...
if choose == ("Iniciar"):
   st.title("A biblioteca é sua!")
   st.subheader("Biblioteca é sinônimo de espaço dinâmico, atrativo, inclusivo e, acima de tudo, repleto de novas ofertas.")
   st.write("Usando a tecnologia a nosso favor, criamos esse site para que você possa se sentir em casa.")
   st.write("Aqui você pode ver as novidades, acessar um portal com suas informações, fazer seu próprio empréstimo de livro, tanto físico quanto digital, sem nenhuma burocrácia. \nPode também dar sua opnião sobre o livro lido para que outros leitores possam saber o que você achou. \nAqui você consegue ver todos os livros disponíveis em nossa biblioteca e encontrá-los com facilidades usando o Buscador Mr. Bigode... Ele te dirá em quais prateleiras encontrará o gênero que deseja ler. ")

###Página 2  ###########DESENVOLVIDO! ------

elif choose == ("Buscador Mr. Bigode"):
   nome=st.text_input("Qual o seu nome? ")
   
   if nome:
 ##Aqui vou criar o buscador de prateleiras de acordo com o gênero de livro que o leitor está procurando.
      st.subheader(f"Bem vindo ao buscador... Meu caro leitor ✨ {nome} ✨")
      st.subheader("Eu sou o Mr.Bigode, e vou te ajudar... 🪄📖")
      st.write("Escolha o gênero desejado, que lhe mostrarei quais prateleiras poderá encontrá-los.")
      if st.button("Infantil"):
        st.write("Os livros do gênero INFANTIL estão nas prateleiras 1 -10!")
      if st.button("Infanto Juvenil"):
        st.write("Os livros INFANTO JUVENIL estão nas prateleiras 11-20!")
      if st.button("Terror"):
        st.write("Os livros de TERROR estão nas prateleiras 21-30!")
      if st.button("Fantasia"):
        st.write("Os livros de FANTASIA estão nas prateleiras 31-40!")
      if st.button("Ficção Científica"):
        st.write("Os livros de FICÇÃO CIENTÍFICA estão nas prateleiras 41-50!")
      if st.button("Espiritualidade(Religioso)"):
        st.write("Os livros de ESPIRITUALIDADE estão nas prateleiras 51-60!")
      if st.button("Auto-Ajuda"):
        st.write("Os livros de AUTO AJUDA estão nas prateleiras 61-70!")
      if st.button("Eróticos"):
        st.write("Os livros ERÓTICOS estão nas prateleiras 71-80!")
      if st.button("Romance"):
         st.write("Os livros de ROMANCE estão nas prateleiras 81-90! ")
      if st.button("Didáticos(Estudos em Geral)"):
        st.write("Os livros DIDÁTICOS de estusos em gerais estão nas prateleiras 91-100!")
      
       
      
     # st.text_input("Me diga pelo número correspondente, qual o genêro de livro que deseja ler? \nVamos encontrar em quais prateleiras ele se encontra...")
      
   
 
###Página 3  #########DESENVOLVIDO! ------
elif choose == ("Novidades"):
   st.subheader("Novidades")
   st.write("Olá, leitor!!! \nQue bom que você está  aqui para sabermos juntinhos sobre as novidades do mundo literário.")
   st.write("Vamos começar falando sobre a saga de livros da maravilhosa Paula Pimenta. \n Já não é novidade pra ninguem que teve gravação do primeiro livro basiado na sequência 'Fazendo Meu filme'.. ")
   st.write("A novidade é que a comédia romântica produzido pela Panorâmica Filmes, Galeria Distribuidora e o Grupo Telefilms, tem estreia prevista para 2024!!!")
   st.write("Isso mesmo, Mr. Bigode me contou que está super ansioso e que vai levar o livro dele para o cinema, para mostrar pra todo mundo que é fã!")
   st.image("https://3.bp.blogspot.com/-Uvqot3wKXs0/Vt4nmNXzJ4I/AAAAAAAAA-M/UoYO6aX5JEY/s1600/o_hobbit.jpg")

   st.write("---")

   genre = st.radio(
    "Qual adaptação dos livros da Carina Rissi, você mais gostou de assistir??",
    [":rainbow[No mundo da Luna]", ":rainbow[Procura-se um Marido]", ":rainbow[Perdida]" ], index=None
    )
   if genre == ":rainbow[No mundo da Luna]":
    st.write("Eu e o mr. Bigode amamos essa adaptação!")
   elif genre == ":rainbow[Procura-se um Marido]":
      st.write("É o meu livro preferido, foi uma honra assistir o filme dele!!")
   elif genre == ":rainbow[Perdida]":
    st.write("Ainda não assisti, está na minha lista")

   st.write("---")

   genre = st.radio(
    "Qual seu livro favorito da Jane Austen?? Mr. Bigode está curioso",
    [":rainbow[Persuasão]", ":rainbow[Orgulho e Preconceito]", ":rainbow[Razão e Sensibilidade]" ], index=None
    )
   if genre == ":rainbow[Persuasão]":
    st.write("Hmm, interessante!!!")
   elif genre == ":rainbow[Orgulho e Preconceito]":
      st.write("É uma mistura de amor e ódio... ahaha")
   elif genre == ":rainbow[Razão e Sensibilidade]":
    st.write("Interessante!!!")

###Página 4 #########DESENVOLVENDO###########

elif choose == ("Portal"):

   choice = st.selectbox("Login/Registro", ["Login", "Registro" ])
   if choice == "Login":

      email=st.text_input("E-mail")
      senha=st.text_input("Senha", type="password")

      if st.button("Login"):
        st.write(":red[PRONTO, ESTÁ LOGADO!]")


   else:

      email=st.text_input("Digite seu E-mail")
      password=st.text_input("Crie uma Senha", type="password")

      username = st.text_input("Digite seu usuário: ")
      st.write("[Ler os termos e condições.](https://policies.google.com/?hl=pt-BR)")
      agree = st.checkbox("Aceito com os termos e condições.")
      if agree:
          st.write("Perfeito!")
          if st.button("Criar minha conta"):
        #username = auth.create_user(email = email, password = password , username=username)
            st.success("Conta criada com Sucesso!")
        #st.markdown("Por favor usuário, entre com seu Login e Senha.")
            st.balloons()
         

###Página 5   ###########DESENVOLVER...
elif choose == ("Acervo"):
  tab1, tab2, tab3 = st.tabs([" Livros Físicos", "Digital(E-book)", "Revistas e HQ's"])

  with tab1:
   st.subheader("Livros Físicos")
   st.write(":red[AINDA NÃO TEMOS NENHUM LIVRO NO ACERVO!]") 
   

  with tab2:
   st.subheader("Digital (E-book)")
   st.write(":red[AINDA NÃO TEMOS NENHUM LIVRO NO ACERVO!]") 
   

  with tab3:
   st.subheader("Revistas e HQ's")
   st.write(":red[AINDA NÃO TEMOS NENHUM LIVRO NO ACERVO!]") 
   

 
  #Perguntar ao professor se consigo conectar ao banco de dados para montar o acervo da biblioteca.


###Página 6  #############DESENVOLVER....
elif choose == ("Avaliações"):
   
   
   st.subheader("Eai, me conta...")
   st.date_input("Data da Avaliação")
   st.text_input("Identificação do Leitor")
   st.text_input("Título do Livro")
   st.text_input("Gênero")
   recomend = st.radio(
    "Recomenda o livro:",
    ["***SIM***", "***NÃO***"]
    )
   
   st.text_input("**Conta pra gente, o que achou do livro... Sem spoiller, viu!**") 
   
   uploaded_files = st.file_uploader("Quer mostrar pra gente uma foto do livro??", accept_multiple_files=True)
   for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)


   if st.button("POSTAR"):
      st.success(":red[Avaliação Postada com Sucesso!]")
      st.balloons()
  

   
   

###Página 7 #########DESENVOLVENDO############
elif choose == ("Sobre Nós"):
  st.subheader("")
  st.write("Sou Nataniely Quiosi, aluna do curso de Programador de Sistemas, ministradas pelo Professor Tiago Dutra Galvão.")
  st.write("A Biblioteca Sete Vidas, é uma biblioteca fictícia na qual o leitor, pode acessar pelo site e ler informações sobre o mundo da cultura.")
  st.write("O usuário pode fazer criar uma conta, fazer login, comentar sobre um livro que leu, ou ler comentários de outros leitores.")
  st.write("Pode fazer o empréstimo de um livro digital direto da sua casa, ou também acessar o sistema e emprestar um livro fisicamente. Pelo buscador, o usuário consegue auxílio para para encontrar em quais prateleiras pode encontrar o livro do gênero desejado e tem acesso ao acervo de livros.")
  st.write("Fiz esse trabalho, usando o programa VsCode, linguagem Python e o Streamlit.")
  st.write("Espero que tenham gostado.")

  st.write("Ainda estou atualizando a página com mais informações e funcionalidades.")

  st.write("[Rede Social](https://instagram.com/nattquiosi?igshid=OGQ5ZDc2ODk2ZA==)")
  st.image("https://img.freepik.com/fotos-premium/um-gato-de-oculos-senta-se-ao-lado-do-monitor-e-ajuda-o-programador-generative-ai_918839-1342.jpg", width=250)
            

################################################
#Comando para colocar foto com link de redirecionamento....
#st.markdown("[![Foo](url da foto)](url do site para onde será direcionado ao clicar na foto)") 
#
#
#
