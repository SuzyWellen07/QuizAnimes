# Gerador de Quiz

``` bash
Implementar uma aplicação do tipo Quiz onde o usuário pode testar seu conhecimento em determinado assunto(s). O app lê de um arquivo ou base de dados no mínimo 10 questões e apresenta ao usuário que poderá escolher uma alternativa por questão. Ao final é apresentado o resultado do quiz (nota, total de acertos).
```

## Tema

### Quiz de animes

- Demon Slayer
- Chaisaw Man
- Dragon Ball Z

---

## Instalação do ambiente python

```bash
# 2. criar ambiente virtual
python3 -m venv env
# 3. ativar ambiente virtual
source env/bin/activate
# 4. instalar dependências
pip install fastapi uvicorn requests
```

### Iniciar servidor fastapi

```bash
uvicorn main:app --reload
```

---