package com.example.demo_rvc.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.client.RestTemplate;

@Controller
public class MainController {

    private final RestTemplate restTemplate;

    @Autowired
    public MainController(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @GetMapping("/")
    public String home(Model model) {
        String url = "http://localhost:8080/";
        List<?> data = restTemplate.getForObject(url, List.class);
        model.addAttribute("data", data);
        return "home"; // Corresponds to home.html
    }

    @GetMapping("/catalogo")
    public String catalogo(Model model) {
        String url = "http://localhost:8080/";
        List<?> data = restTemplate.getForObject(url, List.class);
        model.addAttribute("data", data);
        return "catalogo"; // Corresponds to catalogo.html
    }

    @GetMapping("/produto/{id}")
    public String produto(@PathVariable("id") Long id, Model model) {
        String url = "http://localhost:8080/" + id;
        Object data = restTemplate.getForObject(url, Object.class);
        model.addAttribute("product", data);
        return "produto";
    }

    @GetMapping("/avaliar/{id}")
    public String reviewProduct(@PathVariable("id") Long id, Model model) {
        model.addAttribute("productId", id);
        return "avaliar";
    }

    @GetMapping("/passeios")
    public String passeios(Model model) {
        String url = "http://localhost:8080/passeios";
        List<?> data = restTemplate.getForObject(url, List.class);
        model.addAttribute("data", data);
        return "passeios"; // Corresponds to passeios
    }

    @GetMapping("/pacotes")
    public String pacotes(Model model) {
        String url = "http://localhost:8080/pacotes";
        List<?> data = restTemplate.getForObject(url, List.class);
        model.addAttribute("data", data);
        return "pacotes"; // Corresponds to pacotes
    }

    @GetMapping("/contato")
    public String contato(Model model) {
        String url = "http://localhost:8080/";
        List<?> data = restTemplate.getForObject(url, List.class);
        model.addAttribute("data", data);
        return "contato"; // Corresponds to contato
    }
}
