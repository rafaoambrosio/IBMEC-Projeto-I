package com.example.demo_rvc.model;

public class ProdutoAvaliacao {

    private Long id;

    private String nome;
    private Long nota;
    private String comentario;
    private Produto produto;

    // Getters and Setters

    public Long getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Long getNota() {
        return nota;
    }

    public void setNota(Long nota) {
        this.nota = nota;
    }

    public String getComentario() {
        return comentario;
    }

    public void setComentario(String comentario) {
        this.comentario = comentario;
    }

    public Long getProduto() {
        return produto.getId();
    }

    public void setProduto(Produto produto) {
        this.produto = produto;
    }
}
