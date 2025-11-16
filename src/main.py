#!/usr/bin/env python3
import os

from dotenv import load_dotenv
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

# Inicializa console colorido
console = Console()

# Lê a chave da variável de ambiente
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    console.print(
        "[bold red]❌ Erro:[/bold red] variável de ambiente GEMINI_API_KEY não configurada."
    )
    console.print("Use: export GEMINI_API_KEY='SUA_CHAVE_AQUI'")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# Histórico de conversa
chat = model.start_chat(history=[])

console.print(
    "[bold cyan]🤖 Gemini Chat Iniciado![/bold cyan] (digite 'sair' para encerrar)\n"
)

while True:
    user_input = console.input("[bold yellow]👤 Tu:[/bold yellow] ").strip()
    if user_input.lower() in ["sair", "exit", "quit"]:
        console.print("[bold red]👋 Encerrando...[/bold red]")
        break

    if not user_input:
        continue

    try:
        response = chat.send_message(f"responda apenas em português: {user_input}")
        markdown = Markdown(response.text)
        console.print(markdown)
    except Exception as e:
        console.print(f"[bold red]❌ Erro:[/bold red] {e}")
