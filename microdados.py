import csv
import json

def csv_para_json(csv_file, json_file, colunas_selecionadas, uf_filtro):
    try:
        # Abrir o arquivo CSV com codificação UTF-8
        with open(csv_file, mode='r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)  # Delimitador padrão: vírgula (,)
            
            # Filtrar e processar os dados
            dados = []
            for linha in leitor_csv:
                if linha["SG_UF"] == uf_filtro:  # Filtrar por UF (Paraíba = "PB")
                    linha_filtrada = {coluna: linha[coluna] for coluna in colunas_selecionadas}
                    dados.append(linha_filtrada)
        
        # Salvar os dados em um arquivo JSON
        with open(json_file, mode='w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
        
        print(f"✅ Conversão concluída! Arquivo salvo em: {json_file}")
    
    except FileNotFoundError:
        print(f"❌ Arquivo CSV não encontrado: {csv_file}")
    except Exception as e:
        print(f"❌ Erro: {str(e)}")

# Colunas desejadas (nomes exatos do CSV)
colunas_selecionadas = [
    "NO_REGIAO", 
    "CO_REGIAO",         
    "NO_UF",              
    "SG_UF",
    "CO_UF" ,            
    "NO_MUNICIPIO",
    "CO_MUNICIPIO",       
    "NO_MESORREGIAO",     
    "NO_MICRORREGIAO",    
    "NO_ENTIDADE",
    "QT_MAT_BAS",
    "QT_MAT_INF",
    "QT_MAT_FUND",
    "QT_MAT_MED",
    "QT_MAT_EJA",
    "QT_MAT_EJA_FUND",
    "QT_MAT_ESP",
    "QT_MAT_BAS_EAD",
    "QT_MAT_FUND_INT",
    "QT_MAT_MED_INT",
            
    #"TD_ALUNOS"           
]

# Executar
csv_para_json(
    csv_file='microdados_utf8.csv',
    json_file='dados_paraiba.json',
    colunas_selecionadas=colunas_selecionadas,
    uf_filtro="PB"  # Filtro para a Paraíba
)