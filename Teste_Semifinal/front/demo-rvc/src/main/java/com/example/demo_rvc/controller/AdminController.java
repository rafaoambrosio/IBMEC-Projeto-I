package com.example.demo_rvc.controller;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.client.RestTemplate;

@Controller
public class AdminController {
    
    private final RestTemplate restTemplate;

    public AdminController(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @GetMapping("/adm")
    public String adminHome(Model model) {
        return "adm/home"; // Corresponds to adm/home.html
    }

    @GetMapping("/adm/add")
    public String addProduct(Model model) {
        return "adm/add"; // Corresponds to adm/add.html
    }

    @GetMapping("/adm/manage")
    public String manageProducts(Model model) {
        String url = "http://localhost:8080/";
        List<?> data = restTemplate.getForObject(url, List.class);
        model.addAttribute("produtos", data);
        return "adm/manage"; // Corresponds to adm/manage.html
    }

    @GetMapping("/adm/edit/{id}")
    public String editProduct(@PathVariable("id") Long id, Model model) {
        String url = "http://localhost:8080/" + id;
        Object data = restTemplate.getForObject(url, Object.class);
        model.addAttribute("produto", data);
        return "adm/edit";
    }
}