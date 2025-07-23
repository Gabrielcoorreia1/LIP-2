// Classe base que define os atributos e métodos comuns a todos os veículos.
public class Veiculo {
    // Atributos protegidos para serem acessíveis pelas classes filhas.
    protected String marca;
    protected String modelo;

    // Construtor da classe base.
    public Veiculo(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }

    // Método que será sobrescrito pelas classes filhas.
    public void exibirInfo() {
        System.out.println("Marca: " + this.marca + ", Modelo: " + this.modelo);
    }
}