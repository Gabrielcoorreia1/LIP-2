public class Processador implements Runnable {

    @Override
    public void run() {
        System.out.println("<- Iniciando o processamento de dados...");
        try {
            for (int i = 0; i < 5; i++) {
                System.out.println("   (Processador) Analisando dado " + (i + 1) + "/5...");
                Thread.sleep(800); 
            }
        } catch (InterruptedException e) {
            System.out.println("Thread de processamento foi interrompida.");
        }
    }
}