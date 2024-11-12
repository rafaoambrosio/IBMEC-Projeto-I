package com.example.demo_rvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@Controller
public class AdminController {

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
        return "adm/manage"; // Corresponds to adm/manage.html
    }

    @GetMapping("/adm/edit/{id}")
    public String editProduct(@PathVariable("id") Long id, Model model) {
        model.addAttribute("productId", id);
        return "adm/edit";
    }
}
