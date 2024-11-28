package com.example.demo_rvc.model;

public class ProdutoImagem {

    private Long id;

    private byte[] bytes;

    private Produto produto;

    // Getters and Setters

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public byte[] getBytes() {
        return bytes;
    }

    public void setBytes(byte[] bytes) {
        this.bytes = bytes;
    }

    public Long getProduto() {
        return produto.getId();
    }

    public void setProduto(Produto produto) {
        this.produto = produto;
    }
}
