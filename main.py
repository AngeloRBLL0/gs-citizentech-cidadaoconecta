from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="CidadãoConecta SP - CitizenTech",
    description="Plataforma de consulta de elegibilidade para benefícios sociais e CRAS",
    version="2.0.0"
)

def calcular_elegibilidade(renda_per_capita: float, inscrito_cadunico: bool) -> dict:
    beneficios = []
    if renda_per_capita <= 218.0:
        beneficios.append("Bolsa Família")
    if renda_per_capita <= 706.0 and inscrito_cadunico:
        beneficios.append("Tarifa Social de Energia Elétrica")
        beneficios.append(" Isenção / Tarifa Social no Transporte Público (SPTrans)")
    if renda_per_capita <= 706.0 and not inscrito_cadunico:
        beneficios.append("Elegível para inscrição no CadÚnico")
    
    return {
        "versao_regra": "2.0",
        "renda_per_capita": renda_per_capita,
        "inscrito_cadunico": inscrito_cadunico,
        "beneficios_identificados": beneficios,
        "orientacao": "Procure o CRAS mais próximo com CPF, RG e comprovante de residência."
    }

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>CidadãoConecta SP | CitizenTech</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f6f9; color: #333; max-width: 800px; margin: 40px auto; padding: 20px; }
            .card { background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-top: 5px solid #198754; }
            .badge { background: #198754; color: white; padding: 5px 10px; border-radius: 4px; font-size: 12px; font-weight: bold; }
            h1 { color: #198754; margin-top: 10px; }
            .alert { background: #d1e7dd; color: #0f5132; padding: 12px; border-radius: 6px; margin: 15px 0; }
            .endpoint { background: #eef2f7; padding: 12px; border-left: 4px solid #198754; margin: 10px 0; font-family: monospace; }
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">CitizenTech • Global Solution 2TSC • Atualizado via CI/CD</span>
            <h1>CidadãoConecta SP - Versão 2.0 (Deploy Automatizado)</h1>
            <div class="alert">
                <strong>Novidade da Versão 2.0:</strong> Inclusão de consulta para Benefícios de Mobilidade Urbana (SPTrans) e nova unidade CRAS Capão Redondo!
            </div>
            <p>Plataforma digital para orientar cidadãos de São Paulo sobre acesso ao <strong>CadÚnico, Bolsa Família, Tarifa Social e Mobilidade</strong>.</p>
            <h3>Endpoints disponíveis para consulta cidadã:</h3>
            <div class="endpoint">GET /api/elegibilidade?renda_per_capita=200&inscrito_cadunico=true</div>
            <div class="endpoint">GET /api/cras</div>
            <div class="endpoint">GET /docs (Documentação Interativa Swagger)</div>
        </div>
    </body>
    </html>
    """

@app.get("/api/elegibilidade")
def consultar_elegibilidade(renda_per_capita: float = 200.0, inscrito_cadunico: bool = True):
    return calcular_elegibilidade(renda_per_capita, inscrito_cadunico)

@app.get("/api/cras")
def listar_unidades_cras():
    return {
        "cidade": "São Paulo - SP",
        "unidades_referencia": [
            {"unidade": "CRAS Sé", "endereco": "Av. Tiradentes, 749", "horario": "08h às 17h"},
            {"unidade": "CRAS Itaquera", "endereco": "Rua Fontoura Xavier, 577", "horario": "08h às 17h"},
            {"unidade": "CRAS Grajaú", "endereco": "Rua Ezequiel Lopes Cardoso, 333", "horario": "08h às 17h"},
            {"unidade": "CRAS Capão Redondo", "endereco": "Av. Comendador Sant'Anna, 774", "horario": "08h às 17h"}
        ]
    }
