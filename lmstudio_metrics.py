import lmstudio as lms
import time

llm = lms.llm()  # Get the currently loaded LLM

prompt = "In one sentence, what is a Capybara?"
print(f"Prompt: {prompt}\n")

# Iniciar el temporizador
start_time = time.time()

# Realizar inferencia
prediction = llm.respond_stream(prompt)

# Contar tokens
token_count = 0
for token in prediction:
    token_count += 1

# Terminar temporizador
end_time = time.time()

# Calcular métricas
elapsed_time = end_time - start_time
tokens_per_second = token_count / elapsed_time if elapsed_time > 0 else 0

# Mostrar resultados
print(f"\n\n--- Métricas ---")
print(f"Tiempo total de inferencia: {elapsed_time:.2f} segundos")
print(f"Tokens generados: {token_count}")
print(f"Velocidad: {tokens_per_second:.2f} tokens/segundo")
