package com.example.demo_rvc.model;

public class ProdutoFaixaPreco {

    private Long id;

    private String faixa;
    private String preco_alta_1p;
    private String preco_alta_2_3p;
    private String preco_alta_4p;
    private String preco_baixa_1p;
    private String preco_baixa_2_3p;
    private String preco_baixa_4p;

    private Produto produto;

    // Getters and Setters

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFaixa() {
        return faixa;
    }

    public void setFaixa(String faixa) {
        this.faixa = faixa;
    }

    public String getPreco_alta_1p() {
        return preco_alta_1p;
    }

    public void setPreco_alta_1p(String preco_alta_1p) {
        this.preco_alta_1p = preco_alta_1p;
    }

    public String getPreco_alta_2_3p() {
        return preco_alta_2_3p;
    }

    public void setPreco_alta_2_3p(String preco_alta_2_3p) {
        this.preco_alta_2_3p = preco_alta_2_3p;
    }

    public String getPreco_alta_4p() {
        return preco_alta_4p;
    }

    public void setPreco_alta_4p(String preco_alta_4p) {
        this.preco_alta_4p = preco_alta_4p;
    }

    public String getPreco_baixa_1p() {
        return preco_baixa_1p;
    }

    public void setPreco_baixa_1p(String preco_baixa_1p) {
        this.preco_baixa_1p = preco_baixa_1p;
    }

    public String getPreco_baixa_2_3p() {
        return preco_baixa_2_3p;
    }

    public void setPreco_baixa_2_3p(String preco_baixa_2_3p) {
        this.preco_baixa_2_3p = preco_baixa_2_3p;
    }

    public String getPreco_baixa_4p() {
        return preco_baixa_4p;
    }

    public void setPreco_baixa_4p(String preco_baixa_4p) {
        this.preco_baixa_4p = preco_baixa_4p;
    }
    
    public Long getProduto() {
        return produto.getId();
    }

    public void setProduto(Produto produto) {
        this.produto = produto;
    }
}
