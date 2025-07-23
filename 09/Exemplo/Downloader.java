// Cada tarefa que pode ser executada em uma thread implementa a interface Runnable.
public class Downloader implements Runnable {

    // O método run() contém a lógica que a thread irá executar.
    @Override
    public void run() {
        System.out.println("-> Iniciando o download de arquivos...");
        try {
            for (int i = 0; i < 5; i++) {
                System.out.println("   (Downloader) Baixando arquivo " + (i + 1) + "/5...");
                // Thread.sleep() pausa a execução da thread por um tempo (em milissegundos).
                Thread.sleep(1000); 
            }
        } catch (InterruptedException e) {
            System.out.println("Thread de download foi interrompida.");
        }
    }
}