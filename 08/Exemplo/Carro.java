// Carro herda de Veiculo usando a palavra-chave "extends".
public class Carro extends Veiculo {
    private int portas; // Atributo específico do Carro.

    // Construtor da classe Carro.
    public Carro(String marca, String modelo, int portas) {
        // "super()" chama o construtor da classe pai (Veiculo).
        super(marca, modelo);
        this.portas = portas;
    }

    // A anotação @Override indica que este método está sobrescrevendo
    // um método da classe pai. Isso é polimorfismo.
    @Override
    public void exibirInfo() {
        System.out.println("Carro | Marca: " + this.marca + ", Modelo: " + this.modelo + ", Portas: " + this.portas);
    }

    // Método específico da classe Carro.
    public void abastecer() {
        System.out.println("O carro " + this.modelo + " está sendo abastecido.");
    }
}