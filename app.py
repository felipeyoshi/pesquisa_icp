import streamlit as st
import streamlit_survey as ss

st.title("Pesquisa de Percepção de Marca")

# Criação do objeto survey
survey = ss.StreamlitSurvey()

# Dicionário com as perguntas e suas respectivas descrições
perguntas_rituais = {
    "ritual_gestual": "Você percebe algum ritual gestual relacionado à marca?",
    "ritual_encantamento": "Você percebe algum ritual de encantamento relacionado à marca?",
    "ritual_venda": "Você percebe algum ritual de venda relacionado à marca?",
    "ritual_pos_venda": "Você percebe algum ritual de pós-venda relacionado à marca?",
    "ritual_utilizacao": "Você percebe algum ritual de utilização relacionado à marca?",
    "ritual_descarte": "Você percebe algum ritual de descarte relacionado à marca?",
    "ritual_producao": "Você percebe algum ritual de produção relacionado à marca?",
    "historias_associados": "Você percebe histórias associados a esta marca?",
}

# Dicionário com as descrições para perguntas detalhadas
descricao_perguntas = {
    "ritual_gestual": "Que ritual gestual associado à marca você percebe? (Ex.: Gesto de abraçar, sinal de O forma de chamar com a mão...)",
    "ritual_encantamento": "Que ritual de encantamento associado à marca você percebe? (Ex.: Uma doação automática de parte do valor de venda para certa associação, atendimento exclusivo, dicas e recomendações, vales-prêmios...)",
    "ritual_venda": "Que ritual de venda associado à marca você percebe? (Ex.: Ir a um determinado local o site, usar determinada senha ou cartão, aguardar determinado período de entrega...)",
    "ritual_pos_venda": "Que ritual de pós-venda associado à marca você percebe? (Ex.: Avaliação de satisfação do cliente, ligação telemarketing para ver se está tudo bem, email para pontuar sistema de atendimento...)",
    "ritual_utilizacao": "Que ritual de utilização associado à marca você percebe? (Ex.: Girar a tampa em determinado sentido, passo 1-2-3, sentar e assistir...)",
    "ritual_descarte": "Que ritual de descarte associado à marca você percebe? (Ex.: Uma certa forma de amassar a embalagem, um certo local para descartar determinado produto, um clique n site para sair do sistema...)",
    "ritual_producao": "Que ritual de produção associado à marca você percebe? (Ex.: Sequência certa de ingredientes, etapas claras de atendimento, passo-a-passo de montagem...)",
    "historias_associados": "Descreva as histórias associadas a esta marca:",
}

with survey.pages(3) as page:
    if page.current == 0:
        st.header("Informações Pessoais")
        survey.text_input("Qual seu email de contato?", id="email")
        survey.text_input("Nome:", id="nome")
        survey.text_input("Empresa:", id="empresa")
        survey.text_input("Cargo", id="cargo")
        survey.radio("Gênero", options=['Feminino', 'Masculino', 'Outro', 'Prefiro não dizer'], horizontal=True, id="genero")
        survey.text_input("Idade", id="idade")

    if page.current == 1:
        st.header("Rituais")
        for key, pergunta in perguntas_rituais.items():
            resposta_ritual = survey.radio(pergunta, options=["Não", "Sim"], horizontal=True, id=key)
            if resposta_ritual == "Sim":
                survey.text_area(descricao_perguntas[key], id=f"desc_{key}")

    if page.current == 2:
        json = survey.to_json()
        st.json(json)