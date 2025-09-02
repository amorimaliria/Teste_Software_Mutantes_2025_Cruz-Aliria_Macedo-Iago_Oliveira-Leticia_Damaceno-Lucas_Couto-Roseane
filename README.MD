# Teste_Software_Mutantes_2025_Cruz-Aliria_Macedo-Iago_Oliveira-Leticia_Damaceno-Lucas_Couto-Roseane

## Atividade 3 - Teste de Software 

### A atividade proposta envolve a execução de testes de mutação em um projeto Python, a análise dos resultados e a criação de um relatório detalhado. O objetivo é identificar e documentar os mutantes gerados, a partir de modificações no código original, e avaliar a eficácia dos testes de mutação. O relatório apresenta os resultados obtidos, incluindo a quantidade de mutantes mortos e vivos, bem como a análise dos testes e a interpretação dos resultados. 

### O documento contendo o turorial das etapas executadas pode ser acessado através do link: [Documento Tutorial](https://drive.google.com/file/d/1ooVcGZtLwScr3-7zxxTOVc80rJH_-XLZ/view?usp=sharing)

### 1- Execução do roteiro do vídeo indicado
#### Etapa 1
Configuração do Ambiente (Windows):
- Instalar o Python 3.7+ e criar um ambiente virtual.

```python
python -m venv venv
``` 
- Ativar o ambiente virtual.

```python
venv\Scripts\activate
```

- Instalar as dependências listadas em requirements.txt

```python
pip install -r requirements.txt
```

#### Etapa 2: Execução dos testes

- run tests normally
``` pytest -vv  cal.py ```

- perform tests with line (node) coverage report
``` pytest -vv  test_cal.py  --cov=cal ``` 

- perform tests with branch coverage report
``` pytest -vv  test_cal.py  --cov=cal  --cov-branch  --cov-report html ```

- run tests with mutmut
``` mutmut run --paths-to-mutate= .. /cal_python/cal.py ```

### 3- Execução dos testes no projeto selecionado

#### Etapa 1
Configuração do Ambiente (Windows WSL):

- Criar ambiente virtual
``` cd django-ecomerce 
```

```python
python -m venv venv
```

- Ativar o ambiente virtual
```python
source venv/bin/activate
```

- Atualizar pip:
```python
python -m pip install --upgrade pip
``` 

- Instalar pytest
```python
sudo apt install python3-pytest
```

#### Etapa 2: Execução dos testes

- Execução padrão ods testes
``` pytest -v ```

- perform tests with line (node) coverage report
``` pytest -vv  test_cal.py  --cov=cal ``` 

- perform tests with branch coverage report
``` python
pytest -vv test_cal.py --cov=cal --cov-branch --cov-report html
```

