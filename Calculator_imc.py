import streamlit as st

st.title('Calculadora de IMC (Índice de Massa Corporal)')

# Criando um subtítulo usando HTML
st.markdown('<h6>IMC é a sigla para Índice de Massa Corpórea, parâmetro adotado pela Organização Mundial de Saúde para calcular o peso ideal de cada pessoa.'
            ' O índice é calculado da seguinte maneira: divide-se o peso do paciente pela sua altura elevada ao quadrado. Diz-se que o indivíduo tem peso normal quando o resultado do IMC está entre 18,5 e 24,9.'
            ' Quer descobrir seu IMC? Insira seu peso e sua altura nos campos abaixo e compare com os índices da tabela. Importante: siga os exemplos e use pontos como separadores..</h6>', unsafe_allow_html=True)

nome = st.text_input('Seu nome: ')
tabela_imc = """
    | IMC         | Classificação            |
    |-------------|--------------------------|
    | Menor que 18.5 | Abaixo do peso          |
    | 18.5 a 24.9   | Peso normal             |
    | 25 a 29.9     | Sobrepeso                |
    | 30 a 34.9     | Obesidade grau I         |
    | 35 a 39.9     | Obesidade grau II        |
    | Maior que 40  | Obesidade grau III       |
    """
st.sidebar.markdown(tabela_imc)

if nome:
    with st.form(key='formulario_imc'):
        st.write(f"Olá, {nome}! Agora insira seus dados abaixo para calcular seu IMC.")
        ano = st.date_input(f'Sua data de nascimento {nome}: ')
        peso = st.number_input(f'Seu peso por favor, {nome} (ex: 77): ', min_value=1.0, step=0.1, format='%1f')
        altura = st.number_input('Sua altura [Metros] (ex: 1.70): ', min_value=0.5, step=0.1, format='%2f')
        botao_calcular = st.form_submit_button(label='Calcular IMC')
    
    if botao_calcular:
        imc = peso / (altura ** 2)
        st.write(f'Seu peso = {peso} kg\nSua altura = {altura} m')
        st.warning(f'Seu IMC é {imc:.2f}')
        
        if imc < 18.5:
            classificacao = 'Abaixo do peso'
        elif 18.5 <= imc < 24.9:
            classificacao = 'Peso Normal'
        elif 25 <= imc < 29.9:
            classificacao = 'Sobrepeso'
        elif 30 <= imc < 34.9:
            classificacao = "Obesidade grau I"
        elif 35 <= imc < 39.9:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"
        
        # Exibir a classificação com cores diferentes
        if classificacao == 'Abaixo do peso':
            st.sidebar.markdown("""
            **Dicas para Abaixo do Peso**:
            - Aumente o consumo calórico com alimentos ricos em nutrientes.
            - Coma refeições frequentes (5-6 por dia).
            - Inclua boas fontes de proteína como ovos, carnes e leguminosas.
            - Realize exercícios de força para ganhar massa muscular.
            - Evite calorias vazias (doces e fast-food).
            """)
            st.warning(f'Classificação: {classificacao}')
        elif classificacao == 'Peso Normal':
            st.sidebar.markdown("""
            **Dicas para Peso Normal**:
            - Mantenha uma alimentação equilibrada com todos os grupos alimentares.
            - Beba bastante água diariamente.
            - Pratique exercícios aeróbicos e de força regularmente.
            - Durma de 7 a 8 horas por noite.
            """)
            st.success(f'Classificação: {classificacao}')
        elif classificacao == 'Sobrepeso':
            st.sidebar.markdown("""
            **Dicas para Sobrepeso**:
            - Controle as porções e prefira alimentos integrais.
            - Pratique exercícios aeróbicos como caminhadas ou corridas leves.
            - Reduza bebidas açucaradas e ultraprocessados.
            - Faça mudanças graduais e sustentáveis na alimentação.
            """)
            st.warning(f'Classificação: {classificacao}')
        elif classificacao == 'Obesidade grau I':
            st.sidebar.markdown("""
            **Dicas para Obesidade Grau I**:
            - Planeje sua alimentação com acompanhamento profissional.
            - Escolha carboidratos de baixo índice glicêmico (ex.: batata-doce, aveia).
            - Inclua atividades físicas leves regularmente.
            - Identifique gatilhos emocionais que levam ao excesso alimentar.
            """)
            st.error(f'Classificação: {classificacao}')
        elif classificacao == 'Obesidade grau II':
            st.sidebar.markdown("""
            **Dicas para Obesidade Grau II**:
            - Consulte médicos e nutricionistas para um plano integrado.
            - Opte por refeições ricas em proteínas magras e vegetais.
            - Foque em exercícios de baixo impacto, como hidroginástica.
            - Trabalhe a relação emocional com a comida.
            """)
            st.error(f'Classificação: {classificacao}')
        elif classificacao == 'Obesidade grau III':
            st.sidebar.markdown("""
            **Dicas para Obesidade Grau III**:
            - Busque tratamento multidisciplinar com médicos, nutricionistas e psicólogos.
            - Considere intervenções médicas, como medicamentos ou cirurgia bariátrica.
            - Priorize exercícios supervisionados para evitar lesões.
            - Mantenha controle rigoroso de doenças associadas, como diabetes e hipertensão.
            """)
            st.error(f'Classificação: {classificacao}')
