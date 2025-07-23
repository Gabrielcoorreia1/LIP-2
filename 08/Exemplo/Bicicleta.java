// Bicicleta também herda de Veiculo.
public class Bicicleta extends Veiculo {
    private String tipo; // Atributo específico da Bicicleta.

    // Construtor da classe Bicicleta.
    public Bicicleta(String marca, String modelo, String tipo) {
        // Chama o construtor da classe pai (Veiculo).
        super(marca, modelo);
        this.tipo = tipo;
    }

    @Override
    public void exibirInfo() {
        System.out.println("Bicicleta | Marca: " + this.marca + ", Modelo: " + this.modelo + ", Tipo: " + this.tipo);
    }

    // Método específico da classe Bicicleta.
    public void pedalar() {
        System.out.println("A bicicleta " + this.modelo + " está em movimento.");
    }
}