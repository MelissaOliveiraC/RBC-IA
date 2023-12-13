import PySimpleGUI as sg

def janelaInicial():
    sg.theme('DarkGreen4')  # Mudando para um tom de verde mais escuro

    # Definindo cores para os textos e fundos
    cor_texto = '#FFFFFF'  # Branco
    cor_texto_preto = '#000000'  # Preto
    cor_fundo_verde_escuro = '#006400'  # Verde escuro
    cor_botao = ('#FFFFFF', '#5d9666')  # Texto branco, Fundo verde mais escuro
    cor_verde_claro = '#1c6060'
    cor_branco = '#FFFFFF'  # Branco
    cor_fundo_col_verde_claro = '#0e4f4f'  # Fundo verde claro


    coluna1 = [
        [sg.Text('Área Danificada')],
        [sg.Combo(['Baixas Áreas', 'Espalhado', 'Áreas Superiores', 'Campo Inteiro'], key='areaDamaged',
                  enable_events=True, readonly=True, background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Lesão de Cancro')],
        [sg.Combo(['Sem Resposta', 'Marrom', 'dk-marrom-blk', 'Bronzeado'], key='canker-lesion',
                  enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Histórico de Cultura')],
        [sg.Combo(
            ['Diferente do primeiro ano', 'Mesmo do primeiro ano', 'Mesmo do ultimo ano', 'Mesmo do ultimo dois anos'],
            key='crop-hist', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Data')],
        [sg.Combo(
            ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro'], key='date', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Decadência Externa')],
        [sg.Combo(['Ausente', 'Firme e Seco'], key='external decay', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Manchas de Frutas')],
        [sg.Combo(['Não tem resposta', 'Ausente', 'Marrom com manchas pretas', 'Colorido'], key='manchasdeFrutas',
                  enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Corpos de Frutificação')],
        [sg.Combo(['Ausente', 'Presente'], key='corposdeFrutificacao', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Vagens de Frutas')],
        [sg.Combo(['Não tem resposta', 'pouco presente', 'Normal', 'Doente'], key='vagensdeFrutas', enable_events=True,
                  readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Germinação')],
        [sg.Combo(['abaixo de 80%', '80-89 %', '90-100%'], key='germinacao', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)]

    ]
    coluna2 = [
        [sg.Text('Saudação')],
        [sg.Combo(['Não', 'Sim'], key='saudacao', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Descoloração')],
        [sg.Combo(['Nenhum', 'Preto'], key='descoloracao', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Folha-Malf')],
        [sg.Combo(['Ausente', 'Presente'], key='folhaMalf', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Folha-Suave')],
        [sg.Combo(['Ausente', 'Baixo surf', 'Alto surf'], key='folhaSuave', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Folhagem')],
        [sg.Combo(['Ausente', 'Presente'], key='folhagem', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Manchas-Halo')],
        [sg.Combo(['Ausente', 'Sem halo amarelo', 'halo amarelo'], key='manchasHalo', enable_events=True,
                  readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Tamanho da Mancha')],
        [sg.Combo(['Nenhuma das alternativas', 'Abaixo de 1/8', 'Acima de 1/8'], key='tamanhodaMancha',
                  enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Manchas de Folhas-Marg')],
        [sg.Combo(['Nenhuma das alternativas', 'no-w-s-marg', 'w-s-marg'], key='manchasdeFolhasMarg',
                  enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Folhas')],
        [sg.Combo(['Anormal', 'Normal'], key='folhas', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)]

    ]
    coluna3 = [
        [sg.Text('Alojamento')],
        [sg.Combo(['Não', 'Sim'], key='alojamento', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Crescimento de Mofo')],
        [sg.Combo(['Ausente', 'Presente'], key='crescimentodeMofo', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Micélio')],
        [sg.Combo(['Ausente', 'Presente'], key='micelio', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Crescimento da Planta')],
        [sg.Combo(['Anormal', 'Normal'], key='crescimentodaPlanta', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Estande de Plantas')],
        [sg.Combo(['Abaixo do normal', 'Normal'], key='estandedePlantas', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Precipício')],
        [sg.Combo(['Abaixo do normal', 'Normal', 'Acima do Normal'], key='precipício', enable_events=True,
                  readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Raízes')],
        [sg.Combo(['Cistos de Vesícula', 'Normal', 'Apodrecido'], key='raiz', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Sclerotia')],
        [sg.Combo(['Ausente', 'Presente'], key='sclerotia', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Semente')],
        [sg.Combo(['Anormal', 'Normal'], key='semente', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)]

    ]
    coluna4 = [
        [sg.Text('Descoloração da Semente')],
        [sg.Combo(['Ausente ', 'Presente'], key='descoloracaodaSemente', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Tamanho da Semente')],
        [sg.Combo(['Abaixo do normal', 'Normal'], key='tamanhodaSemente', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Semente-Tmt')],
        [sg.Combo(['Nenhum', 'Fungicida', 'Outros'], key='sementeTmt', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Gravidade')],
        [sg.Combo(['Menor', 'Grave', 'Severo'], key='gravidade', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Murchando')],
        [sg.Combo(['Ausente', 'Presente'], key='murchando', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Tronco')],
        [sg.Combo(['Anormal', 'Normal'], key='tronco', enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Cancros do Caule')],
        [sg.Combo(['Ausente', 'Abaixo do Solo', 'Acima do Solo', 'Acima do Segundo'], key='cancrosdoCaule',
                  enable_events=True, readonly=True,  background_color=cor_branco, text_color=cor_texto_preto)],

        [sg.Text('Temperatura')],
        [sg.Combo(['Abaixo do normal', 'Normal', 'Acima do Normal'], key='temperatura',
                  enable_events=True, readonly=True,   background_color=cor_branco, text_color=cor_texto_preto)],
    ]
  
    layout = [
      [sg.Column(coluna1, background_color = cor_fundo_col_verde_claro),
       sg.Column(coluna2, background_color = cor_fundo_col_verde_claro),
       sg.Column(coluna3, background_color = cor_fundo_col_verde_claro),
       sg.Column(coluna4, background_color = cor_fundo_col_verde_claro)],
      [sg.Text('', expand_x=True),
       sg.Button('Continuar', key='botao', button_color=cor_verde_claro),
       sg.Text('', expand_x=True),
       sg.Text('Limite', text_color=cor_texto, background_color=cor_verde_claro),
       sg.Input('0', key='porcentagem', size=(5, 2), text_color=cor_texto, background_color=cor_verde_claro),
       sg.Text('%', text_color=cor_texto, background_color=cor_verde_claro)
       ]
    ]

    return sg.Window('RBC', layout=layout, finalize=True)

def janelaSecundaria(lista, lista2, lista3, cursor):
  # Definindo a lista de problemas
  listaP1 = [
      'area-damaged', 'canker-lesion', 'crop-hist', 'date', 'external decay',
      'fruit spots', 'fruiting-bodies', 'fruit-pods', 'germination', 'hail',
      'int-discolor', 'leaf-malf', 'leaf-mild', 'leaf-shread', 'leafspots-halo',
      'leafspot-size', 'leafspots-marg', 'leaves', 'lodging', 'mold-growth',
      'mycelium', 'plant-growth', 'plant-stand', 'precip', 'roots', 'sclerotia',
      'seed', 'seed-discolor', 'seed-size', 'seed-tmt', 'severity', 'shriveling',
      'stem', 'stem-cankers', 'temp'
  ]

  # Criando uma lista de pares de problema e valor associado
  listaP = [[listaP1[n], lista[n]] for n in range(len(listaP1))]

  # Criando a coluna com a tabela de problemas
  coluna1 = [
      [sg.Table(values=listaP, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'],
                auto_size_columns=False, expand_x=True, key='-TB-')]
  ]

  # Obtendo descrição das doenças para cada caso
  listadoencas = [cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE Caso = ?", (casos[0],)).fetchall()[0] for casos in lista2]

  # Criando uma lista com informações de cada caso (Caso, Doença, Porcentagem)
  listaPP = [
      [lista2[n][0], listadoencas[n], f'{lista3[n]}%'] for n in range(len(lista2))
  ]

  # Criando a coluna com a tabela de informações sobre os casos
  coluna3 = [
      [sg.Table(values=listaPP, select_mode=sg.SELECT_MODE_BROWSE, headings=[' Caso ', 'Doenca', 'Porcentagem'],
                auto_size_columns=False, expand_x=True, key='-TB2-', enable_events=True)]
  ]

  # Criando o layout da janela
  layout = [
      [sg.Column(coluna1), sg.VerticalSeparator(), sg.Column(coluna3)]
  ]

  # Retornando a janela, a lista de informações sobre casos e a lista de pares problema-valor
  return sg.Window('RBC', layout=layout, finalize=True), listaPP, listaP

def janelaFinal(listaP, casoSel, cursor):
  # Criando uma lista com informações sobre cada caso (Caso, Problema)
  lista = [
      [listaP[n][0], resultado[0][3 + n]] for n in range(len(listaP))
  ]

  # Criando a coluna com a tabela de informações sobre os problemas no caso selecionado
  coluna1 = [
      [sg.Table(values=listaP, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'],
                auto_size_columns=False, expand_x=True, key='-TB3-')]
  ]

  # Obtendo as informações completas sobre o caso selecionado
  cursor.execute("SELECT * FROM bancoprincipal WHERE Caso = ?", (casoSel,))
  resultado = cursor.fetchall()

  # Criando a lista com informações sobre o caso (Caso, Valor do Problema)
  coluna2 = [
      [sg.Table(values=lista, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'],
                auto_size_columns=False, expand_x=True, key='-TB4-')]
  ]

  # Criando o layout da janela
  layout = [
      [sg.Text('Solução:' + resultado[0][2])],
      [sg.Column(coluna1), sg.VerticalSeparator(), sg.Column(coluna2)]
  ]

  # Retornando a janela
  return sg.Window('RBC', layout=layout, finalize=True)