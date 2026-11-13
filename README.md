# 🏛️ CidadãoConecta SP — Plataforma CitizenTech (Global Solution 02/2026)

> **Disciplina:** Cloud Solutions & Scalable Infrastructure  
> **Curso / Turma:** Data Science — 2TSCPV (FIAP)

---

## 📌 1. Problema e Proposta da Solução (CitizenTech)
Muitos cidadãos em situação de vulnerabilidade social nas periferias urbanas enfrentam barreiras de informação para compreender a quais benefícios públicos têm direito e onde realizar o atendimento presencial.

O **CidadãoConecta SP** é uma aplicação web e API desenvolvida no contexto **CitizenTech** para simplificar a consulta de elegibilidade a benefícios sociais essenciais — **CadÚnico, Bolsa Família, Tarifa Social de Energia Elétrica e Benefícios de Mobilidade Urbana (SPTrans)** — com base na renda familiar *per capita*, além de listar unidades de referência do **CRAS (Centro de Referência de Assistência Social)** no município de São Paulo.

---

## 👨‍💻 2. Integrantes da Equipe

| Nome Completo | RM | Turma |
| :--- | :--- | :--- |
| Angelo Rabello dos Santos Ferreira | RM 564338 | 2TSCPV |
| Karen Akemi de Oliveira | RM 562733 | 2TSCPV |
| Milena Barbosa de Oliveira | RM 558913 | 2TSCPV |

---

## 🛠️ 3. Origem do Projeto e Tecnologias Utilizadas
* **Origem do Projeto:** Aplicação desenvolvida especificamente para a Global Solution e contextualizada a partir da proposta do grupo voltada à integração social e acesso a benefícios cidadãos.
* **Tecnologias Utilizadas:**
  * **Linguagem & Framework Web:** Python 3.11 + FastAPI + Uvicorn
  * **Testes Automatizados:** Pytest + HTTPX (`TestClient`)
  * **Planejamento & Versionamento:** GitHub Projects, GitHub Issues, Git (Branches e Pull Requests)
  * **Automação de CI/CD:** GitHub Actions (`.github/workflows/ci-cd.yml`)
  * **Provedor de Nuvem (PaaS):** Render Cloud Web Services

### Como executar a aplicação localmente:
```bash
# 1. Clonar o repositório
git clone [https://github.com/AngeloRBLL0/gs-citizentech-cidadaoconecta.git](https://github.com/AngeloRBLL0/gs-citizentech-cidadaoconecta.git)
cd gs-citizentech-cidadaoconecta

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Executar os testes automatizados
pytest -v

# 4. Iniciar o servidor local
uvicorn main:app --reload
