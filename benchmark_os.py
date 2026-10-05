import time
import csv
import gc

def rodar_benchmark(sistema_operacional):
    nome_arquivo = f'benchmark_resultados_{sistema_operacional}.csv'
    cabecalho = ['bloco_MB', 'teste', 'alloc_ms', 'write_ms', 'read_ms', 'free_ms']
    
    with open(nome_arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho)
        
        for bloco in range(100, 1001, 100):
            tamanho_bytes = bloco * 1024 * 1024
            # Feedback visual no terminal para acompanhamento
            print(f"[{sistema_operacional}] Executando 100 testes no bloco de {bloco} MB...")
            
            for teste in range(1, 101):
                gc.collect()
                
                # 1. Alocação
                start_alloc = time.perf_counter()
                mem_block = bytearray(tamanho_bytes)
                alloc_ms = (time.perf_counter() - start_alloc) * 1000
                
                view = memoryview(mem_block)
                
                # 2. Escrita
                start_write = time.perf_counter()
                for i in range(0, tamanho_bytes, 4096):
                    view[i] = 1
                write_ms = (time.perf_counter() - start_write) * 1000
                
                # 3. Leitura
                start_read = time.perf_counter()
                soma = 0
                for i in range(0, tamanho_bytes, 4096):
                    soma += view[i]
                read_ms = (time.perf_counter() - start_read) * 1000
                
                # 4. Liberação
                start_free = time.perf_counter()
                del mem_block
                del view
                gc.collect()
                free_ms = (time.perf_counter() - start_free) * 1000
                
                writer.writerow([bloco, teste, alloc_ms, write_ms, read_ms, free_ms])
                
    print(f"\nBenchmark finalizado! Dados salvos no arquivo {nome_arquivo}.")

if __name__ == "__main__":
    rodar_benchmark("Windows")